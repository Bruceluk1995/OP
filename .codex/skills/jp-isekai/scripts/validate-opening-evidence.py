#!/usr/bin/env python3
"""Validate that a drawn opening card is evidenced in the saved opening text."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

from opening_cards import REQUIRED_CHAINS


def compact(text: str) -> str:
    return re.sub(r"\s+", "", text)


def fail(messages: list[str]) -> int:
    print(json.dumps({"status": "fail", "errors": messages}, ensure_ascii=False, indent=2))
    return 2


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate opening-card evidence against a saved body.")
    parser.add_argument("--body", type=Path, required=True)
    parser.add_argument("--evidence", type=Path, required=True)
    parser.add_argument("--opening-chars", type=int, default=2000)
    args = parser.parse_args()

    if not args.body.exists():
        return fail([f"body not found: {args.body}"])
    if not args.evidence.exists():
        return fail([f"evidence not found: {args.evidence}"])

    try:
        payload = json.loads(args.evidence.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return fail([f"invalid evidence JSON: {exc}"])

    card_id = str(payload.get("card_id", "")).strip().upper()
    if card_id not in REQUIRED_CHAINS:
        return fail([f"unknown card_id: {card_id or '(empty)'}"])

    evidence = payload.get("evidence")
    if not isinstance(evidence, dict):
        return fail(["evidence must be an object keyed by required-chain slot"])

    opening = compact(args.body.read_text(encoding="utf-8"))[: max(args.opening_chars, 1)]
    required = REQUIRED_CHAINS[card_id]
    errors: list[str] = []
    positions: dict[str, int] = {}
    seen_quotes: set[str] = set()

    for slot in required:
        quote = evidence.get(slot)
        if not isinstance(quote, str) or not compact(quote):
            errors.append(f"missing evidence slot: {slot}")
            continue
        normalized = compact(quote)
        if len(normalized) < 4:
            errors.append(f"evidence too short for {slot}: use an exact quote of at least 4 characters")
            continue
        if normalized in seen_quotes:
            errors.append(f"duplicate evidence reused for slot: {slot}")
            continue
        seen_quotes.add(normalized)
        position = opening.find(normalized)
        if position < 0:
            errors.append(f"evidence for {slot} is not present in the first {args.opening_chars} non-whitespace characters")
            continue
        positions[slot] = position

    ordered_positions = [positions[slot] for slot in required if slot in positions]
    if len(ordered_positions) == len(required) and ordered_positions != sorted(ordered_positions):
        errors.append("evidence slots do not appear in the card's required order")

    if errors:
        return fail(errors)

    print(
        json.dumps(
            {
                "status": "pass",
                "card_id": card_id,
                "opening_chars_checked": args.opening_chars,
                "required_chain": required,
                "evidence_positions": positions,
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
