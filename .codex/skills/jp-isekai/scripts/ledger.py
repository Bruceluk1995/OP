#!/usr/bin/env python3
"""Project-local ledgers for Japanese male-audience isekai generation and topic history."""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from datetime import date
from pathlib import Path


LEDGER = Path("男频异世界知识库") / "generated-ledger.jsonl"
TOPIC_LEDGER = Path("男频异世界知识库") / "topic-history.jsonl"
FIELDS = ("protagonist", "cheat", "pressure", "payoff", "venue", "aftertaste")


def extract_root(argv: list[str]) -> tuple[str, list[str]]:
    root = "."
    cleaned: list[str] = []
    i = 0
    while i < len(argv):
        arg = argv[i]
        if arg == "--root":
            if i + 1 >= len(argv):
                raise SystemExit("--root requires a value")
            root = argv[i + 1]
            i += 2
            continue
        if arg.startswith("--root="):
            root = arg.split("=", 1)[1]
            i += 1
            continue
        cleaned.append(arg)
        i += 1
    return root, cleaned


def ledger_path(root: str, topic: bool = False) -> Path:
    return Path(root).resolve() / (TOPIC_LEDGER if topic else LEDGER)


def load_records(path: Path) -> list[dict]:
    if not path.exists():
        return []
    records: list[dict] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            records.append(json.loads(line))
        except json.JSONDecodeError:
            records.append({"_invalid": line})
    return records


def summarize(records: list[dict], limit: int) -> None:
    recent = records[-limit:]
    print(f"ledger_records={len(records)} recent={len(recent)}")
    if not recent:
        print("No prior jp-isekai records found.")
        return
    for field in FIELDS[1:]:
        counts = Counter(str(r.get(field, "")).strip() for r in recent if r.get(field))
        top = ", ".join(f"{k}:{v}" for k, v in counts.most_common(5))
        print(f"{field}: {top or '-'}")
    print("recent_titles:")
    for r in recent[-5:]:
        parts = " / ".join(str(r.get(field, "?")) for field in FIELDS[1:])
        print(f"- {r.get('title', '(untitled)')} | {parts}")


def similarity(record: dict, candidate: dict) -> int:
    return sum(1 for field in FIELDS if candidate.get(field) and candidate.get(field) == record.get(field))


def check(records: list[dict], candidate: dict, limit: int) -> int:
    recent = records[-limit:]
    matches = [(similarity(r, candidate), r) for r in recent]
    matches = [(score, r) for score, r in matches if score > 0]
    matches.sort(key=lambda item: item[0], reverse=True)
    if not matches:
        print("OK: no overlap with recent records.")
        return 0
    score, top = matches[0]
    print(f"top_overlap={score}")
    print(json.dumps(top, ensure_ascii=False))
    if score >= 3:
        print("BLOCK: change at least two of protagonist/cheat/pressure/payoff/venue/aftertaste.")
        return 2
    print("OK: overlap is acceptable, but vary the remaining fields.")
    return 0


def add_record(path: Path, args: argparse.Namespace) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    record = {
        "date": args.date or date.today().isoformat(),
        "title": args.title,
        "protagonist": args.protagonist,
        "cheat": args.cheat,
        "pressure": args.pressure,
        "payoff": args.payoff,
        "venue": args.venue,
        "aftertaste": args.aftertaste,
        "path": args.path,
        "notes": args.notes,
    }
    with path.open("a", encoding="utf-8", newline="\n") as handle:
        handle.write(json.dumps(record, ensure_ascii=False) + "\n")
    print(f"added: {path}")


def split_tags(value: str | list[str]) -> set[str]:
    if isinstance(value, list):
        parts = value
    else:
        parts = re.split(r"[,，|/;；]+", value)
    return {re.sub(r"\s+", "", str(part)).casefold() for part in parts if str(part).strip()}


def topic_summary(records: list[dict], limit: int) -> None:
    recent = records[-limit:]
    print(f"topic_records={len(records)} recent={len(recent)}")
    for record in recent:
        tags = ",".join(sorted(split_tags(record.get("tags", [])))) or "-"
        print(f"- {record.get('date', '?')} [{record.get('status', '?')}] {record.get('seed', '(untitled)')} | {tags}")


def topic_check(records: list[dict], seed: str, tags: str, limit: int) -> int:
    candidate_seed = re.sub(r"\s+", "", seed).casefold()
    candidate_tags = split_tags(tags)
    hits: list[tuple[int, dict, set[str]]] = []
    for record in records[-limit:]:
        prior_seed = re.sub(r"\s+", "", str(record.get("seed", ""))).casefold()
        common = candidate_tags & split_tags(record.get("tags", []))
        same_seed = bool(candidate_seed and prior_seed and (
            candidate_seed == prior_seed or candidate_seed in prior_seed or prior_seed in candidate_seed
        ))
        if same_seed or common:
            hits.append((len(common) + (2 if same_seed else 0), record, common))
    if not hits:
        print("OK: topic and tags are new within the checked history.")
        return 0
    hits.sort(key=lambda item: item[0], reverse=True)
    score, record, common = hits[0]
    print(f"BLOCK: prior topic overlap score={score}; common_tags={','.join(sorted(common)) or '-'}")
    print(json.dumps(record, ensure_ascii=False))
    return 2


def topic_add(path: Path, args: argparse.Namespace) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    record = {
        "date": args.date or date.today().isoformat(),
        "source": args.source,
        "seed": args.seed,
        "tags": sorted(split_tags(args.tags)),
        "status": args.status,
        "notes": args.notes,
    }
    with path.open("a", encoding="utf-8", newline="\n") as handle:
        handle.write(json.dumps(record, ensure_ascii=False) + "\n")
    print(f"added: {path}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Manage jp-isekai generated-content ledger.")
    sub = parser.add_subparsers(dest="command", required=True)

    p_summary = sub.add_parser("summary")
    p_summary.add_argument("--limit", type=int, default=20)

    p_check = sub.add_parser("check")
    p_check.add_argument("--limit", type=int, default=10)
    for field in ("title", *FIELDS):
        p_check.add_argument(f"--{field}", default="")

    p_add = sub.add_parser("add")
    p_add.add_argument("--date", default="")
    for field in ("title", *FIELDS, "path", "notes"):
        p_add.add_argument(f"--{field}", default="")

    p_topic_summary = sub.add_parser("topic-summary")
    p_topic_summary.add_argument("--limit", type=int, default=50)

    p_topic_check = sub.add_parser("topic-check")
    p_topic_check.add_argument("--limit", type=int, default=100)
    p_topic_check.add_argument("--seed", default="")
    p_topic_check.add_argument("--tags", default="")

    p_topic_add = sub.add_parser("topic-add")
    p_topic_add.add_argument("--date", default="")
    p_topic_add.add_argument("--source", default="")
    p_topic_add.add_argument("--seed", required=True)
    p_topic_add.add_argument("--tags", required=True)
    p_topic_add.add_argument(
        "--status", choices=("presented", "selected", "generated", "rejected"), default="presented"
    )
    p_topic_add.add_argument("--notes", default="")

    return parser


def main(argv: list[str] | None = None) -> int:
    root, cleaned = extract_root(list(sys.argv[1:] if argv is None else argv))
    parser = build_parser()
    args = parser.parse_args(cleaned)
    is_topic = args.command.startswith("topic-")
    path = ledger_path(root, topic=is_topic)
    records = load_records(path)

    if args.command == "summary":
        summarize(records, args.limit)
        return 0
    if args.command == "check":
        candidate = {field: getattr(args, field) for field in FIELDS}
        return check(records, candidate, args.limit)
    if args.command == "add":
        add_record(path, args)
        return 0
    if args.command == "topic-summary":
        topic_summary(records, args.limit)
        return 0
    if args.command == "topic-check":
        return topic_check(records, args.seed, args.tags, args.limit)
    if args.command == "topic-add":
        topic_add(path, args)
        return 0
    raise AssertionError(args.command)


if __name__ == "__main__":
    raise SystemExit(main())
