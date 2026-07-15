#!/usr/bin/env python3
"""Detect append-only or copy-heavy rewrites; never judge literary quality."""

from __future__ import annotations

import argparse
import json
import re
import sys
from difflib import SequenceMatcher
from pathlib import Path


def normalize(text: str) -> str:
    return re.sub(r"\s+", "", text)


def meaningful_lines(text: str) -> list[str]:
    return [line for raw in text.splitlines() if len(line := re.sub(r"\s+", "", raw)) >= 12]


def common_prefix_length(a: str, b: str) -> int:
    index = 0
    while index < min(len(a), len(b)) and a[index] == b[index]:
        index += 1
    return index


def assess(old_text: str, new_text: str) -> dict[str, object]:
    old, new = normalize(old_text), normalize(new_text)
    if not old or not new:
        return {"verdict": "fail", "scope": "rewrite_integrity_only", "reasons": ["empty body"]}
    similarity = SequenceMatcher(None, old, new, autojunk=False).ratio()
    prefix = common_prefix_length(old, new) / len(old)
    old_lines, new_lines = meaningful_lines(old_text), set(meaningful_lines(new_text))
    line_reuse = sum(line in new_lines for line in old_lines) / len(old_lines) if old_lines else 0.0
    reasons: list[str] = []
    if new.startswith(old) and len(new) > len(old):
        reasons.append("complete old body survives with appended text")
    if prefix >= 0.80:
        reasons.append(f"unchanged prefix covers {prefix:.1%} of old body")
    if similarity >= 0.82:
        reasons.append(f"whole-body similarity is {similarity:.1%}")
    if len(old_lines) >= 8 and line_reuse >= 0.70:
        reasons.append(f"exact reuse covers {line_reuse:.1%} of meaningful old lines")
    return {
        "verdict": "fail" if reasons else "pass",
        "scope": "rewrite_integrity_only",
        "literary_quality": "not_evaluated",
        "old_characters": len(old), "new_characters": len(new),
        "similarity": round(similarity, 4),
        "unchanged_prefix_old_coverage": round(prefix, 4),
        "exact_meaningful_line_reuse": round(line_reuse, 4),
        "reasons": reasons,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Check claimed rewrite for append-only or copy-heavy reuse.")
    parser.add_argument("--old", type=Path, required=True)
    parser.add_argument("--new", type=Path, required=True)
    args = parser.parse_args()
    for stream in (sys.stdout, sys.stderr):
        if reconfigure := getattr(stream, "reconfigure", None):
            reconfigure(encoding="utf-8")
    result = assess(args.old.read_text(encoding="utf-8"), args.new.read_text(encoding="utf-8"))
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 1 if result["verdict"] == "fail" else 0


if __name__ == "__main__":
    raise SystemExit(main())
