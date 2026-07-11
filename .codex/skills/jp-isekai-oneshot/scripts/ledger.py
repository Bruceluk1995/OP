#!/usr/bin/env python3
"""Ledger for standalone Japanese male-audience isekai one-shots."""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from datetime import date
from pathlib import Path


LEDGER = Path("男频异世界短篇知识库") / "generated-ledger.jsonl"
FIELDS = (
    "seed_source",
    "trend_source",
    "trend_seed",
    "news_seed",
    "video_seed",
    "hook_mechanic",
    "absurdity_score",
    "video_hook_score",
    "everyday_resonance",
    "hotness_angle",
    "opening_card",
    "opening_chain",
    "structure_fingerprint",
    "theme_route",
    "subtype",
    "protagonist_engine",
    "cheat",
    "opening_bomb",
    "payoff_engine",
    "progression_axis",
    "antagonist_pressure",
    "ending_type",
    "target_language",
)

FIELD_WEIGHTS = {
    "opening_card": 1,
    "opening_chain": 2,
    "structure_fingerprint": 3,
}


def configure_stdio() -> None:
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="replace")


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


def opening_card(record: dict) -> str:
    card = str(record.get("opening_card", "")).strip().upper()
    if card:
        return card
    legacy = re.search(r"(?:opening card|开场模板卡|开场卡)\s*[:：]?\s*([A-Z]\d)", str(record.get("notes", "")), re.IGNORECASE)
    return legacy.group(1).upper() if legacy else ""


def summarize(records: list[dict], limit: int) -> None:
    recent = records[-limit:]
    print(f"ledger_records={len(records)} recent={len(recent)}")
    if not recent:
        print("No prior isekai one-shot records found.")
        return
    for field in FIELDS:
        values = [opening_card(record) for record in recent] if field == "opening_card" else [str(record.get(field, "")).strip() for record in recent]
        counts = Counter(value for value in values if value)
        print(f"{field}: " + (", ".join(f"{k}:{v}" for k, v in counts.most_common(5)) or "-"))
    print("recent_titles:")
    for record in recent[-8:]:
        print(
            f"- {record.get('title', '(untitled)')} | "
            f"{record.get('trend_source','?')}:{record.get('trend_seed','?')} / "
            f"{record.get('subtype','?')} / {record.get('cheat','?')} / "
            f"{record.get('payoff_engine','?')} / {record.get('ending_type','?')} / "
            f"{record.get('target_language','?')}"
        )


def similarity(record: dict, candidate: dict) -> tuple[int, list[str]]:
    matched: list[str] = []
    for field in FIELDS:
        candidate_value = candidate.get(field)
        record_value = opening_card(record) if field == "opening_card" else record.get(field)
        if candidate_value and candidate_value == record_value:
            matched.append(field)
    score = sum(FIELD_WEIGHTS.get(field, 1) for field in matched)
    return score, matched


def check(records: list[dict], candidate: dict, limit: int) -> int:
    matches = [(*similarity(record, candidate), record) for record in records[-limit:]]
    matches = [(score, fields, record) for score, fields, record in matches if score > 0]
    matches.sort(key=lambda item: item[0], reverse=True)
    if not matches:
        print("OK: no overlap with recent records.")
        return 0
    score, matched_fields, top = matches[0]
    print(f"top_overlap_score={score}")
    print("matched_fields=" + ",".join(matched_fields))
    print(json.dumps(top, ensure_ascii=False))
    if score >= 4:
        print("BLOCK: vary the opening chain or macro structure, then change at least two story-engine fields.")
        return 2
    print("OK: overlap acceptable.")
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
    configure_stdio()
    parser = argparse.ArgumentParser(description="Manage isekai one-shot ledger.")
    parser.add_argument("--root", default=".")
    sub = parser.add_subparsers(dest="command", required=True)

    p_summary = sub.add_parser("summary")
    p_summary.add_argument("--limit", type=int, default=20)

    p_cards = sub.add_parser("recent-cards")
    p_cards.add_argument("--limit", type=int, default=3)

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
    if args.command == "recent-cards":
        cards = [opening_card(record) for record in records]
        cards = [card for card in cards if card]
        print(json.dumps({"recent_cards": cards[-args.limit :] if args.limit > 0 else []}, ensure_ascii=False))
        return 0
    if args.command == "check":
        return check(records, {field: getattr(args, field) for field in FIELDS}, args.limit)
    if args.command == "add":
        add_record(path, args)
        return 0
    raise AssertionError(args.command)


if __name__ == "__main__":
    raise SystemExit(main())
