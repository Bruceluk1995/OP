#!/usr/bin/env python3
"""Project-local ledger for econ-finance-explainer generation history."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from datetime import date
from pathlib import Path


LEDGER = Path("财经讲解知识库") / "generated-ledger.jsonl"
FIELDS = (
    "topic_pack",
    "audience_pack",
    "market_region",
    "trend_source",
    "trend_seed",
    "domain",
    "question_type",
    "opening_analogy",
    "mechanism_axis",
    "risk_transfer",
    "thesis_shape",
    "target_language",
)


def ledger_path(root: str) -> Path:
    return Path(root).resolve() / LEDGER


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
        print("No prior econ-finance-explainer records found.")
        return
    for field in FIELDS:
        counts = Counter(str(r.get(field, "")).strip() for r in recent if r.get(field))
        top = ", ".join(f"{k}:{v}" for k, v in counts.most_common(5))
        print(f"{field}: {top or '-'}")
    print("recent_titles:")
    for record in recent[-8:]:
        print(
            f"- {record.get('title', '(untitled)')} | "
            f"{record.get('topic_pack','?')} / {record.get('audience_pack','?')} / "
            f"{record.get('market_region','?')} / {record.get('domain','?')} / "
            f"{record.get('question_type','?')} / {record.get('mechanism_axis','?')} / "
            f"{record.get('risk_transfer','?')} / {record.get('thesis_shape','?')} / "
            f"{record.get('target_language','?')}"
        )


def similarity(record: dict, candidate: dict) -> int:
    return sum(1 for field in FIELDS if candidate.get(field) and candidate.get(field) == record.get(field))


def check(records: list[dict], candidate: dict, limit: int) -> int:
    matches = [(similarity(record, candidate), record) for record in records[-limit:]]
    matches = [(score, record) for score, record in matches if score > 0]
    matches.sort(key=lambda item: item[0], reverse=True)
    if not matches:
        print("OK: no overlap with recent records.")
        return 0
    score, top = matches[0]
    print(f"top_overlap={score}")
    print(json.dumps(top, ensure_ascii=False))
    if score >= 4:
        print("BLOCK: change at least three of topic/audience/market/question/opening/mechanism/risk/thesis/language.")
        return 2
    print("OK: overlap is acceptable, but vary the remaining fields.")
    return 0


def add_record(path: Path, args: argparse.Namespace) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    record = {"date": args.date or date.today().isoformat(), "title": args.title}
    for field in FIELDS:
        record[field] = getattr(args, field)
    record["path"] = args.path
    record["notes"] = args.notes
    with path.open("a", encoding="utf-8", newline="\n") as handle:
        handle.write(json.dumps(record, ensure_ascii=False) + "\n")
    print(f"added: {path}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Manage econ-finance-explainer generated-content ledger.")
    parser.add_argument("--root", default=".", help="Project root containing the ledger.")
    sub = parser.add_subparsers(dest="command", required=True)

    p_summary = sub.add_parser("summary")
    p_summary.add_argument("--limit", type=int, default=20)

    p_check = sub.add_parser("check")
    p_check.add_argument("--limit", type=int, default=20)
    for field in ("title", *FIELDS):
        p_check.add_argument(f"--{field}", default="")

    p_add = sub.add_parser("add")
    p_add.add_argument("--date", default="")
    for field in ("title", *FIELDS, "path", "notes"):
        p_add.add_argument(f"--{field}", default="")

    args = parser.parse_args()
    path = ledger_path(args.root)
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
    raise AssertionError(args.command)


if __name__ == "__main__":
    raise SystemExit(main())
