#!/usr/bin/env python3
"""Company-wide creative dedup client with local SQLite offline fallback."""

from __future__ import annotations

import hashlib
import json
import os
import sqlite3
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
import uuid
from contextlib import closing
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


TIMEOUT_SECONDS = 8.0
SNAPSHOT_MAX_AGE_SECONDS = 60
_network_failed = False


class BridgeRequestError(ConnectionError):
    """A bridge request failed with a classified HTTP or transport error."""

    def __init__(self, message: str, *, status_code: int = 0, retryable: bool = True) -> None:
        super().__init__(message)
        self.status_code = status_code
        self.retryable = retryable


def _codex_home() -> Path:
    return Path(os.environ.get("CODEX_HOME", Path.home() / ".codex"))


def _cache_path() -> Path:
    override = os.environ.get("STORY_DEDUP_CACHE", "").strip()
    return Path(override) if override else _codex_home() / "story-company-cache.sqlite3"


def _bridge_paths() -> list[Path]:
    paths: list[Path] = []
    if override := os.environ.get("STORY_DEDUP_BRIDGE", "").strip():
        return [Path(override)]
    if appdata := os.environ.get("APPDATA", "").strip():
        paths.append(Path(appdata) / "sggoi-studio" / "story-dedup-bridge.json")
    paths.extend([
        Path.home() / ".config" / "sggoi-studio" / "story-dedup-bridge.json",
        Path.home() / "Library" / "Application Support" / "sggoi-studio" / "story-dedup-bridge.json",
    ])
    return paths


def canonical_key(fingerprint: str) -> str:
    normalized = unicodedata.normalize("NFKC", fingerprint).strip().lower()
    normalized = "".join(
        ch for ch in normalized
        if not ch.isspace() and not unicodedata.category(ch).startswith("P")
    )
    return hashlib.sha256(normalized.encode("utf-8")).hexdigest()


def work_id_for(root: Path, hint: str = "") -> str:
    """Return a stable local project id without relying on a common folder name."""
    resolved = root.resolve()
    marker = resolved / ".story-work-id"
    try:
        project_id = marker.read_text(encoding="utf-8").strip()
    except OSError:
        project_id = ""
    if not project_id:
        meta_key = "project_id:" + hashlib.sha256(str(resolved).casefold().encode("utf-8")).hexdigest()
        with closing(_connect()) as db, db:
            row = db.execute("SELECT value FROM meta WHERE key=?", (meta_key,)).fetchone()
            if row:
                project_id = str(row["value"])
            else:
                project_id = uuid.uuid4().hex
                db.execute("INSERT INTO meta(key,value) VALUES(?,?)", (meta_key, project_id))
    work_part = hashlib.sha256(hint.strip().casefold().encode("utf-8")).hexdigest()[:16] if hint.strip() else "root"
    return f"{project_id}:{work_part}"


def _now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _connect() -> sqlite3.Connection:
    path = _cache_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    db = sqlite3.connect(path, timeout=2)
    db.row_factory = sqlite3.Row
    db.executescript(
        """
        PRAGMA journal_mode=WAL;
        CREATE TABLE IF NOT EXISTS records (
          kind TEXT NOT NULL,
          canonical_key TEXT NOT NULL,
          fingerprint TEXT NOT NULL,
          work_id TEXT NOT NULL DEFAULT '',
          label TEXT NOT NULL DEFAULT '',
          status TEXT NOT NULL DEFAULT 'presented',
          server_state TEXT NOT NULL DEFAULT 'synced',
          updated_at TEXT NOT NULL,
          PRIMARY KEY (kind, canonical_key)
        );
        CREATE TABLE IF NOT EXISTS outbox (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          action TEXT NOT NULL,
          payload TEXT NOT NULL,
          created_at TEXT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS dead_letter (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          outbox_id INTEGER NOT NULL,
          action TEXT NOT NULL,
          payload TEXT NOT NULL,
          error TEXT NOT NULL,
          failed_at TEXT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS meta (
          key TEXT PRIMARY KEY,
          value TEXT NOT NULL
        );
        """
    )
    return db


def _load_bridge() -> dict[str, str]:
    for path in _bridge_paths():
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
            if data.get("url") and data.get("token"):
                return {"url": str(data["url"]).rstrip("/"), "token": str(data["token"])}
        except (OSError, ValueError, TypeError):
            continue
    raise ConnectionError("SGGOI Studio bridge unavailable")


def _request(method: str, path: str, payload: dict[str, Any] | None = None) -> dict[str, Any]:
    global _network_failed
    if _network_failed:
        raise BridgeRequestError("SGGOI Studio bridge unavailable in this process", retryable=True)
    try:
        bridge = _load_bridge()
    except ConnectionError as exc:
        _network_failed = True
        raise BridgeRequestError(str(exc), retryable=True) from exc
    data = None if payload is None else json.dumps(payload, ensure_ascii=False).encode("utf-8")
    req = urllib.request.Request(bridge["url"] + path, data=data, method=method)
    req.add_header("Authorization", "Bearer " + bridge["token"])
    if data is not None:
        req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT_SECONDS) as resp:
            body = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        try:
            message = json.loads(exc.read().decode("utf-8")).get("error", str(exc))
        except Exception:
            message = str(exc)
        retryable = exc.code in (401, 403, 408, 425, 429) or exc.code >= 500
        if retryable:
            _network_failed = True
        raise BridgeRequestError(message, status_code=exc.code, retryable=retryable) from exc
    except (OSError, ValueError) as exc:
        _network_failed = True
        raise BridgeRequestError(str(exc), retryable=True) from exc
    if body.get("error"):
        raise BridgeRequestError(str(body["error"]), retryable=False)
    return body


def _save_record(db: sqlite3.Connection, item: dict[str, Any], server_state: str) -> None:
    key = canonical_key(item["fingerprint"])
    db.execute(
        """INSERT INTO records
           (kind, canonical_key, fingerprint, work_id, label, status, server_state, updated_at)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?)
           ON CONFLICT(kind, canonical_key) DO UPDATE SET
             work_id=excluded.work_id, label=excluded.label, status=excluded.status,
             server_state=excluded.server_state, updated_at=excluded.updated_at""",
        (
            item["kind"], key, item["fingerprint"], item.get("work_id", ""),
            item.get("label", ""), item.get("status", "presented"), server_state, _now(),
        ),
    )


def _enqueue(db: sqlite3.Connection, action: str, payload: dict[str, Any]) -> None:
    db.execute(
        "INSERT INTO outbox(action, payload, created_at) VALUES (?, ?, ?)",
        (action, json.dumps(payload, ensure_ascii=False), _now()),
    )


def _dead_letter(db: sqlite3.Connection, row: sqlite3.Row, error: Exception) -> None:
    db.execute(
        "INSERT INTO dead_letter(outbox_id, action, payload, error, failed_at) VALUES (?, ?, ?, ?, ?)",
        (row["id"], row["action"], row["payload"], str(error), _now()),
    )
    db.execute("DELETE FROM outbox WHERE id=?", (row["id"],))


def _apply_reserve_result(
    db: sqlite3.Connection, item: dict[str, Any], result: dict[str, Any], conflicts: list[str],
) -> None:
    key = canonical_key(item["fingerprint"])
    if result.get("reserved"):
        db.execute(
            "UPDATE records SET server_state='synced', updated_at=? WHERE kind=? AND canonical_key=?",
            (_now(), item["kind"], key),
        )
        return
    db.execute(
        """UPDATE records SET work_id=?, status=?, server_state='conflict', updated_at=?
           WHERE kind=? AND canonical_key=?""",
        (
            result.get("existing_work_id", ""), result.get("existing_status", "presented"),
            _now(), item["kind"], key,
        ),
    )
    conflicts.append(item.get("label") or item["fingerprint"])


def _flush_reserve_rows(
    db: sqlite3.Connection, rows: list[sqlite3.Row], conflicts: list[str],
) -> bool:
    """Flush reserve rows in batches. Return False only for a retryable outage."""
    valid: list[tuple[sqlite3.Row, dict[str, Any]]] = []
    for row in rows:
        try:
            payload = json.loads(row["payload"])
            items = payload.get("items", [])
            if len(items) != 1 or not isinstance(items[0], dict):
                raise ValueError("reserve outbox payload must contain exactly one item")
            valid.append((row, items[0]))
        except (ValueError, TypeError, json.JSONDecodeError) as exc:
            _dead_letter(db, row, exc)
    if not valid:
        return True

    try:
        response = _request("POST", "/api/story-dedup/reserve", {"items": [item for _, item in valid]})
        results = response.get("results", [])
        if len(results) != len(valid):
            raise BridgeRequestError("reserve response count mismatch", retryable=True)
        for (row, item), result in zip(valid, results):
            _apply_reserve_result(db, item, result, conflicts)
            db.execute("DELETE FROM outbox WHERE id=?", (row["id"],))
        return True
    except BridgeRequestError as exc:
        if exc.retryable:
            return False

    # A permanent batch error may belong to only one item. Isolate it so one
    # poison record cannot block the rest of the queue.
    for row, item in valid:
        try:
            response = _request("POST", "/api/story-dedup/reserve", {"items": [item]})
            results = response.get("results", [])
            if len(results) != 1:
                raise BridgeRequestError("reserve response count mismatch", retryable=True)
            _apply_reserve_result(db, item, results[0], conflicts)
            db.execute("DELETE FROM outbox WHERE id=?", (row["id"],))
        except BridgeRequestError as exc:
            if exc.retryable:
                return False
            _dead_letter(db, row, exc)
    return True


def flush_outbox(limit: int = 100) -> list[str]:
    global _network_failed
    _network_failed = False
    conflicts: list[str] = []
    with closing(_connect()) as db, db:
        rows = db.execute(
            "SELECT id, action, payload FROM outbox ORDER BY id LIMIT ?", (limit,)
        ).fetchall()
        index = 0
        while index < len(rows):
            row = rows[index]
            if row["action"] == "reserve":
                batch: list[sqlite3.Row] = []
                while index < len(rows) and rows[index]["action"] == "reserve" and len(batch) < 50:
                    batch.append(rows[index])
                    index += 1
                if not _flush_reserve_rows(db, batch, conflicts):
                    break
                continue
            try:
                payload = json.loads(row["payload"])
                _request("POST", "/api/story-dedup/commit", payload)
                db.execute("DELETE FROM outbox WHERE id=?", (row["id"],))
            except (ValueError, TypeError, json.JSONDecodeError) as exc:
                _dead_letter(db, row, exc)
            except BridgeRequestError as exc:
                if exc.retryable:
                    break
                _dead_letter(db, row, exc)
            index += 1
    return conflicts


def reserve(
    *, kind: str, fingerprint: str, work_id: str, label: str = "",
    tags: list[str] | None = None, source: str = "codex", metadata: dict[str, Any] | None = None,
    status: str = "presented",
) -> dict[str, Any]:
    global _network_failed
    item = {
        "kind": kind,
        "fingerprint": fingerprint,
        "work_id": work_id,
        "label": label,
        "tags": tags or [],
        "source": source,
        "metadata": metadata or {},
        "status": status,
    }
    key = canonical_key(fingerprint)
    _network_failed = False
    try:
        sync_snapshot()
    except ConnectionError:
        # Snapshot freshness must not prevent an independent current reserve
        # attempt. A stale outbox or a transient GET failure cannot veto it.
        _network_failed = False
    with closing(_connect()) as db, db:
        existing = db.execute(
            "SELECT work_id, status, server_state FROM records WHERE kind=? AND canonical_key=?",
            (kind, key),
        ).fetchone()
        if existing and existing["work_id"] and existing["work_id"] != work_id:
            return {
                "reserved": False,
                "provisional": existing["server_state"] != "synced",
                "existing_work_id": existing["work_id"],
                "existing_status": existing["status"],
            }

        try:
            response = _request("POST", "/api/story-dedup/reserve", {"items": [item]})
            result = response["results"][0]
            if result.get("reserved"):
                _save_record(db, item, "synced")
            else:
                conflict_item = {
                    **item,
                    "work_id": result.get("existing_work_id", ""),
                    "status": result.get("existing_status", "presented"),
                }
                _save_record(db, conflict_item, "synced")
            return {**result, "provisional": False}
        except (ConnectionError, KeyError, IndexError):
            _save_record(db, item, "pending")
            if not existing or existing["work_id"] != work_id or existing["server_state"] != "pending":
                _enqueue(db, "reserve", {"items": [item]})
            return {"reserved": True, "provisional": True, "canonical_key": key}


def commit(*, kind: str, fingerprint: str, work_id: str, status: str) -> dict[str, Any]:
    payload = {"kind": kind, "fingerprint": fingerprint, "work_id": work_id, "status": status}
    with closing(_connect()) as db, db:
        key = canonical_key(fingerprint)
        db.execute(
            "UPDATE records SET status=?, updated_at=? WHERE kind=? AND canonical_key=?",
            (status, _now(), kind, key),
        )
        try:
            response = _request("POST", "/api/story-dedup/commit", payload)
            db.execute(
                "UPDATE records SET server_state='synced' WHERE kind=? AND canonical_key=?",
                (kind, key),
            )
            return {"synced": True, "response": response}
        except ConnectionError:
            _enqueue(db, "commit", payload)
            return {"synced": False, "provisional": True}


def sync_snapshot(*, force: bool = False) -> int:
    since = ""
    with closing(_connect()) as db:
        checked = db.execute("SELECT value FROM meta WHERE key='snapshot_checked_at'").fetchone()
        if not force and checked:
            try:
                if time.time() - float(checked["value"]) < SNAPSHOT_MAX_AGE_SECONDS:
                    return 0
            except (TypeError, ValueError):
                pass
        last = db.execute("SELECT value FROM meta WHERE key='last_snapshot'").fetchone()
        if last:
            since = str(last["value"])
    path = "/api/story-dedup/snapshot"
    if since:
        path += "?since=" + urllib.parse.quote(since)
    response = _request("GET", path)
    records = response.get("records", [])
    with closing(_connect()) as db, db:
        for record in records:
            fingerprint = "server:" + record["canonical_key"]
            db.execute(
                """INSERT INTO records
                   (kind, canonical_key, fingerprint, work_id, label, status, server_state, updated_at)
                   VALUES (?, ?, ?, ?, ?, ?, 'synced', ?)
                   ON CONFLICT(kind, canonical_key) DO UPDATE SET
                     work_id=excluded.work_id, label=excluded.label, status=excluded.status,
                     server_state='synced', updated_at=excluded.updated_at""",
                (
                    record["kind"], record["canonical_key"], fingerprint,
                    record.get("work_id", ""), record.get("label", ""),
                    record.get("status", "presented"), record.get("updated_at", _now()),
                ),
            )
        db.execute(
            "INSERT INTO meta(key,value) VALUES('last_snapshot',?) ON CONFLICT(key) DO UPDATE SET value=excluded.value",
            (response.get("server_time", _now()),),
        )
        db.execute(
            "INSERT INTO meta(key,value) VALUES('snapshot_checked_at',?) ON CONFLICT(key) DO UPDATE SET value=excluded.value",
            (str(time.time()),),
        )
    return len(records)
