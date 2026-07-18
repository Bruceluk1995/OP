from __future__ import annotations

import json
import os
import sqlite3
import sys
import tempfile
import threading
import unittest
from contextlib import closing
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from unittest.mock import patch


SCRIPTS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SCRIPTS))
import company_dedup  # noqa: E402
import topic_history  # noqa: E402


class _BridgeHandler(BaseHTTPRequestHandler):
    requests: list[tuple[str, str, str, dict]] = []
    snapshot_records: list[dict] = []
    reserve_result = {
        "kind": "topic",
        "canonical_key": "server-key",
        "reserved": True,
        "same_work": False,
    }
    commit_status = 200
    commit_body: dict = {"status": "generated"}

    def _reply(self, body: dict, status: int = 200) -> None:
        encoded = json.dumps(body).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(encoded)))
        self.end_headers()
        self.wfile.write(encoded)

    def do_POST(self) -> None:  # noqa: N802
        length = int(self.headers.get("Content-Length", "0"))
        payload = json.loads(self.rfile.read(length) or b"{}")
        self.requests.append(("POST", self.path, self.headers.get("Authorization", ""), payload))
        if self.path.endswith("/reserve"):
            self._reply({"results": [dict(self.reserve_result) for _ in payload.get("items", [])]})
        else:
            self._reply(self.commit_body, self.commit_status)

    def do_GET(self) -> None:  # noqa: N802
        self.requests.append(("GET", self.path, self.headers.get("Authorization", ""), {}))
        self._reply({"records": self.snapshot_records, "server_time": "2026-01-01T00:00:00Z"})

    def log_message(self, *_args: object) -> None:
        return


class CompanyDedupTest(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.cache = self.root / "cache.sqlite3"
        self.bridge = self.root / "bridge.json"
        self.env = patch.dict(os.environ, {
            "STORY_DEDUP_CACHE": str(self.cache),
            "STORY_DEDUP_BRIDGE": str(self.bridge),
        }, clear=False)
        self.env.start()
        company_dedup._network_failed = False
        _BridgeHandler.requests = []
        _BridgeHandler.snapshot_records = []
        _BridgeHandler.reserve_result = {
            "kind": "topic",
            "canonical_key": "server-key",
            "reserved": True,
            "same_work": False,
        }
        _BridgeHandler.commit_status = 200
        _BridgeHandler.commit_body = {"status": "generated"}

    def tearDown(self) -> None:
        self.env.stop()
        self.temp.cleanup()

    def _start_bridge(self) -> tuple[ThreadingHTTPServer, threading.Thread]:
        server = ThreadingHTTPServer(("127.0.0.1", 0), _BridgeHandler)
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        self.bridge.write_text(json.dumps({
            "url": f"http://127.0.0.1:{server.server_port}",
            "token": "local-secret",
        }), encoding="utf-8")
        return server, thread

    def test_offline_reservation_is_queued_and_blocks_another_work(self) -> None:
        first = company_dedup.reserve(
            kind="topic", fingerprint="topic|追放令嬢", work_id="work-a", label="追放令嬢",
        )
        second = company_dedup.reserve(
            kind="topic", fingerprint="topic|追放令嬢", work_id="work-b", label="追放令嬢",
        )
        self.assertTrue(first["reserved"])
        self.assertTrue(first["provisional"])
        self.assertFalse(second["reserved"])
        with closing(sqlite3.connect(self.cache)) as db:
            self.assertEqual(db.execute("SELECT COUNT(*) FROM outbox").fetchone()[0], 1)

    def test_repeated_offline_check_does_not_duplicate_outbox(self) -> None:
        for _ in range(3):
            result = company_dedup.reserve(
                kind="character", fingerprint="character|リナ", work_id="work-a", label="リナ",
            )
            self.assertTrue(result["reserved"])
            self.assertTrue(result["provisional"])
        with closing(sqlite3.connect(self.cache)) as db:
            self.assertEqual(db.execute("SELECT COUNT(*) FROM outbox").fetchone()[0], 1)

    def test_topic_gate_fails_closed_without_online_confirmation(self) -> None:
        result = topic_history.check(
            [],
            "role=porter|engine=weight conversion|pressure=collapse|payoff=rescue|venue=dungeon|aftertaste=respect",
            "",
            500,
            self.root,
        )
        self.assertEqual(result, 3)

    def test_work_ids_are_stable_but_do_not_trust_common_folder_names(self) -> None:
        project_a = self.root / "machine-a" / "劇本"
        project_b = self.root / "machine-b" / "劇本"
        project_a.mkdir(parents=True)
        project_b.mkdir(parents=True)
        first = company_dedup.work_id_for(project_a, "book-one")
        repeated = company_dedup.work_id_for(project_a, "book-one")
        other_path = company_dedup.work_id_for(project_b, "book-one")
        other_book = company_dedup.work_id_for(project_a, "book-two")
        self.assertEqual(first, repeated)
        self.assertNotEqual(first, other_path)
        self.assertNotEqual(first, other_book)

    def test_online_reservation_uses_local_bridge_token(self) -> None:
        server, thread = self._start_bridge()
        try:
            result = company_dedup.reserve(
                kind="topic", fingerprint="topic|聖女", work_id="work-a", label="聖女",
            )
        finally:
            server.shutdown()
            server.server_close()
            thread.join(timeout=2)
        self.assertTrue(result["reserved"])
        self.assertFalse(result["provisional"])
        self.assertEqual(_BridgeHandler.requests[-1][1], "/api/story-dedup/reserve")
        self.assertEqual(_BridgeHandler.requests[-1][2], "Bearer local-secret")

    def test_flushing_offline_reservation_marks_cache_synced(self) -> None:
        company_dedup.reserve(
            kind="character", fingerprint="character|アリス", work_id="work-a", label="アリス",
        )
        server, thread = self._start_bridge()
        try:
            conflicts = company_dedup.flush_outbox()
        finally:
            server.shutdown()
            server.server_close()
            thread.join(timeout=2)
        self.assertEqual(conflicts, [])
        with closing(sqlite3.connect(self.cache)) as db:
            state = db.execute("SELECT server_state FROM records").fetchone()[0]
            queued = db.execute("SELECT COUNT(*) FROM outbox").fetchone()[0]
        self.assertEqual(state, "synced")
        self.assertEqual(queued, 0)

    def test_current_reservation_does_not_wait_for_stale_outbox(self) -> None:
        with closing(company_dedup._connect()) as db, db:
            company_dedup._enqueue(db, "commit", {
                "kind": "topic", "fingerprint": "missing-old-topic",
                "work_id": "old-work", "status": "generated",
            })
        _BridgeHandler.commit_status = 404
        _BridgeHandler.commit_body = {"error": "reservation not found"}
        server, thread = self._start_bridge()
        try:
            result = company_dedup.reserve(
                kind="topic", fingerprint="new-topic", work_id="new-work", label="new topic",
            )
        finally:
            server.shutdown()
            server.server_close()
            thread.join(timeout=2)
        self.assertTrue(result["reserved"])
        self.assertFalse(result["provisional"])
        paths = [request[1] for request in _BridgeHandler.requests]
        self.assertNotIn("/api/story-dedup/commit", paths)
        with closing(sqlite3.connect(self.cache)) as db:
            self.assertEqual(db.execute("SELECT COUNT(*) FROM outbox").fetchone()[0], 1)

    def test_permanent_poison_entry_moves_to_dead_letter_and_queue_continues(self) -> None:
        with closing(company_dedup._connect()) as db, db:
            company_dedup._enqueue(db, "commit", {
                "kind": "topic", "fingerprint": "missing-old-topic",
                "work_id": "old-work", "status": "generated",
            })
            item = {
                "kind": "topic", "fingerprint": "queued-topic", "work_id": "queued-work",
                "label": "queued", "tags": [], "source": "test", "metadata": {},
                "status": "presented",
            }
            company_dedup._save_record(db, item, "pending")
            company_dedup._enqueue(db, "reserve", {"items": [item]})
        _BridgeHandler.commit_status = 404
        _BridgeHandler.commit_body = {"error": "reservation not found"}
        server, thread = self._start_bridge()
        try:
            conflicts = company_dedup.flush_outbox()
        finally:
            server.shutdown()
            server.server_close()
            thread.join(timeout=2)
        self.assertEqual(conflicts, [])
        with closing(sqlite3.connect(self.cache)) as db:
            self.assertEqual(db.execute("SELECT COUNT(*) FROM outbox").fetchone()[0], 0)
            self.assertEqual(db.execute("SELECT COUNT(*) FROM dead_letter").fetchone()[0], 1)
            self.assertEqual(
                db.execute("SELECT server_state FROM records WHERE fingerprint='queued-topic'").fetchone()[0],
                "synced",
            )

    def test_reserve_outbox_is_sent_in_one_batch(self) -> None:
        with closing(company_dedup._connect()) as db, db:
            for suffix in ("a", "b"):
                item = {
                    "kind": "topic", "fingerprint": f"queued-{suffix}",
                    "work_id": f"work-{suffix}", "label": suffix, "tags": [],
                    "source": "test", "metadata": {}, "status": "presented",
                }
                company_dedup._save_record(db, item, "pending")
                company_dedup._enqueue(db, "reserve", {"items": [item]})
        server, thread = self._start_bridge()
        try:
            company_dedup.flush_outbox()
        finally:
            server.shutdown()
            server.server_close()
            thread.join(timeout=2)
        reserve_requests = [request for request in _BridgeHandler.requests if request[1].endswith("/reserve")]
        self.assertEqual(len(reserve_requests), 1)
        self.assertEqual(len(reserve_requests[0][3]["items"]), 2)

    def test_server_conflict_is_cached_for_offline_checks(self) -> None:
        _BridgeHandler.reserve_result = {
            "kind": "topic",
            "canonical_key": "server-key",
            "reserved": False,
            "same_work": False,
            "existing_work_id": "old-work",
            "existing_status": "generated",
        }
        server, thread = self._start_bridge()
        try:
            online = company_dedup.reserve(
                kind="topic", fingerprint="topic|年金危機", work_id="new-work", label="年金危機",
            )
        finally:
            server.shutdown()
            server.server_close()
            thread.join(timeout=2)
        self.bridge.unlink()
        offline = company_dedup.reserve(
            kind="topic", fingerprint="topic|年金危機", work_id="third-work", label="年金危機",
        )
        self.assertFalse(online["reserved"])
        self.assertFalse(offline["reserved"])
        self.assertEqual(offline["existing_work_id"], "old-work")

    def test_company_snapshot_protects_later_offline_check(self) -> None:
        fingerprint = "topic|介護離職"
        _BridgeHandler.snapshot_records = [{
            "kind": "topic",
            "canonical_key": company_dedup.canonical_key(fingerprint),
            "work_id": "company-work",
            "label": "介護離職",
            "status": "generated",
            "updated_at": "2025-12-31T00:00:00Z",
        }]
        server, thread = self._start_bridge()
        try:
            first = company_dedup.reserve(
                kind="topic", fingerprint=fingerprint, work_id="new-work", label="介護離職",
            )
        finally:
            server.shutdown()
            server.server_close()
            thread.join(timeout=2)
        self.bridge.unlink()
        offline = company_dedup.reserve(
            kind="topic", fingerprint=fingerprint, work_id="offline-work", label="介護離職",
        )
        self.assertFalse(first["reserved"])
        self.assertEqual(first["existing_work_id"], "company-work")
        self.assertFalse(offline["reserved"])


if __name__ == "__main__":
    unittest.main()
