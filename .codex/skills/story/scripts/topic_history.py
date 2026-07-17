#!/usr/bin/env python3
"""Project-wide topic history shared by all story and explainer skills."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from datetime import date
from pathlib import Path

import company_dedup


LEDGER = Path("选题历史") / "global-topic-history.jsonl"
STATUSES = ("presented", "selected", "generated", "rejected")
SEED_FIELDS = (
    "trend_seed", "news_seed", "video_seed", "seed", "title",
    "chinese_title", "japanese_title", "engine", "protagonist_engine",
)
TAG_FIELDS = ("tags", "domain", "topic_pack", "theme_route", "subtype", "route", "hotness_angle")


def extract_root(argv: list[str]) -> tuple[Path, list[str]]:
    root = Path(".")
    cleaned: list[str] = []
    i = 0
    while i < len(argv):
        arg = argv[i]
        if arg == "--root":
            if i + 1 >= len(argv):
                raise SystemExit("--root requires a value")
            root = Path(argv[i + 1])
            i += 2
        elif arg.startswith("--root="):
            root = Path(arg.split("=", 1)[1])
            i += 1
        else:
            cleaned.append(arg)
            i += 1
    return root.resolve(), cleaned


def split_tags(value: object) -> set[str]:
    values = value if isinstance(value, list) else re.split(r"[,，|/;；]+", str(value or ""))
    return {re.sub(r"\s+", "", str(item)).casefold() for item in values if str(item).strip()}


def load(path: Path) -> list[dict]:
    if not path.exists():
        return []
    records = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        try:
            records.append(json.loads(line))
        except json.JSONDecodeError:
            records.append({"_invalid": line})
    return records


def append(path: Path, record: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8", newline="\n") as handle:
        handle.write(json.dumps(record, ensure_ascii=False) + "\n")


def choose_seed(record: dict) -> str:
    return next((str(record.get(field, "")).strip() for field in SEED_FIELDS if record.get(field)), "(untitled)")


def derived_tags(record: dict) -> list[str]:
    tags: set[str] = set()
    for field in TAG_FIELDS:
        tags.update(split_tags(record.get(field, "")))
    return sorted(tags)


def topic_fingerprint(seed: str, tags: object) -> str:
    normalized_tags = sorted(split_tags(tags))
    return "topic|" + seed.strip() + "|" + "|".join(normalized_tags)


def import_existing(root: Path, path: Path) -> None:
    records = load(path)
    known = {r.get("record_id") for r in records if r.get("record_id")}
    added = 0
    sources = list(root.rglob("generated-ledger.jsonl")) + [
        p for p in root.rglob("topic-history.jsonl") if p.resolve() != path.resolve()
    ]
    for source in sources:
        if ".codex" in source.parts or "选题历史" in source.parts:
            continue
        for line in source.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            record_id = hashlib.sha1((str(source.relative_to(root)) + "\n" + line).encode("utf-8")).hexdigest()[:16]
            if record_id in known:
                continue
            try:
                original = json.loads(line)
            except json.JSONDecodeError:
                continue
            append(path, {
                "record_id": record_id,
                "date": original.get("date", date.today().isoformat()),
                "domain": source.parent.name,
                "source": original.get("source", source.name),
                "seed": choose_seed(original),
                "tags": derived_tags(original),
                "status": original.get("status", "generated"),
                "origin": str(source.relative_to(root)),
                "details": {k: original[k] for k in SEED_FIELDS + TAG_FIELDS if original.get(k)},
            })
            known.add(record_id)
            added += 1
    print(f"imported={added} total={len(load(path))}")


def summary(records: list[dict], limit: int) -> None:
    recent = records[-limit:]
    print(f"global_topic_records={len(records)} recent={len(recent)}")
    for record in recent:
        tags = ",".join(sorted(split_tags(record.get("tags", [])))) or "-"
        print(f"- {record.get('date', '?')} [{record.get('status', '?')}] {record.get('domain', '?')} | {record.get('seed', '(untitled)')} | {tags}")


def check(records: list[dict], seed: str, tags: str, limit: int, root: Path) -> int:
    candidate_seed = re.sub(r"\s+", "", seed).casefold()
    candidate_tags = split_tags(tags)
    hits = []
    for record in records[-limit:]:
        prior_seed = re.sub(r"\s+", "", str(record.get("seed", ""))).casefold()
        common = candidate_tags & split_tags(record.get("tags", []))
        same_seed = bool(candidate_seed and prior_seed and (
            candidate_seed == prior_seed or candidate_seed in prior_seed or prior_seed in candidate_seed
        ))
        if same_seed or common:
            hits.append((len(common) + (2 if same_seed else 0), common, record))
    if not hits:
        result = company_dedup.reserve(
            kind="topic",
            fingerprint=topic_fingerprint(seed, tags),
            work_id=company_dedup.work_id_for(root),
            label=seed,
            tags=sorted(split_tags(tags)),
            source="story-topic-history",
            status="presented",
        )
        if not result.get("reserved"):
            print(
                "BLOCK: company-wide topic already used; "
                f"work={result.get('existing_work_id', '?')} status={result.get('existing_status', '?')}"
            )
            return 2
        if result.get("provisional"):
            print("BLOCK: company server unavailable; provisional outbox entry does not authorize this topic.")
            return 3
        print("OK: company-wide online reservation confirmed.")
        return 0
    score, common, record = sorted(hits, key=lambda item: item[0], reverse=True)[0]
    print(f"BLOCK: global overlap score={score}; common_tags={','.join(sorted(common)) or '-'}")
    print(json.dumps(record, ensure_ascii=False))
    return 2


def add(path: Path, args: argparse.Namespace, root: Path) -> None:
    append(path, {
        "date": args.date or date.today().isoformat(),
        "domain": args.domain,
        "source": args.source,
        "seed": args.seed,
        "tags": sorted(split_tags(args.tags)),
        "status": args.status,
        "notes": args.notes,
    })
    sync_result = company_dedup.commit(
        kind="topic",
        fingerprint=topic_fingerprint(args.seed, args.tags),
        work_id=company_dedup.work_id_for(root),
        status=args.status,
    )
    print(f"added: {path}")
    if not sync_result.get("synced"):
        print("WARN: company status update queued for later sync.")


def sync_company(records: list[dict], root: Path) -> int:
    synced = 0
    blocked = 0
    for record in records:
        if record.get("_invalid"):
            continue
        seed = str(record.get("seed", "")).strip()
        if not seed:
            continue
        result = company_dedup.reserve(
            kind="topic",
            fingerprint=topic_fingerprint(seed, record.get("tags", [])),
            work_id=company_dedup.work_id_for(root, str(record.get("origin", ""))),
            label=seed,
            tags=sorted(split_tags(record.get("tags", []))),
            source=str(record.get("source", "history-import")),
            status=str(record.get("status", "generated")),
        )
        if result.get("reserved"):
            synced += 1
        else:
            blocked += 1
    print(f"company_sync={synced} conflicts={blocked}")
    return 2 if blocked else 0


def parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Manage project-wide creative topic history.")
    sub = p.add_subparsers(dest="command", required=True)
    sub.add_parser("import-existing")
    sub.add_parser("sync-company")
    s = sub.add_parser("summary"); s.add_argument("--limit", type=int, default=100)
    c = sub.add_parser("check"); c.add_argument("--limit", type=int, default=500); c.add_argument("--seed", default=""); c.add_argument("--tags", default="")
    a = sub.add_parser("add"); a.add_argument("--date", default=""); a.add_argument("--domain", required=True); a.add_argument("--source", default=""); a.add_argument("--seed", required=True); a.add_argument("--tags", required=True); a.add_argument("--status", choices=STATUSES, default="presented"); a.add_argument("--notes", default="")
    return p


def main(argv: list[str] | None = None) -> int:
    root, cleaned = extract_root(list(sys.argv[1:] if argv is None else argv))
    args = parser().parse_args(cleaned)
    path = root / LEDGER
    records = load(path)
    if args.command == "import-existing": import_existing(root, path); return 0
    if args.command == "summary": summary(records, args.limit); return 0
    if args.command == "check": return check(records, args.seed, args.tags, args.limit, root)
    if args.command == "add": add(path, args, root); return 0
    if args.command == "sync-company": return sync_company(records, root)
    raise AssertionError(args.command)


if __name__ == "__main__":
    raise SystemExit(main())
