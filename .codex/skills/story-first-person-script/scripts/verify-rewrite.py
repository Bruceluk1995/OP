#!/usr/bin/env python3
"""Detect append-only or copy-heavy rewrites.

This is an integrity check, not a literary-quality validator.
"""

from __future__ import annotations

import argparse
import json
import re
from difflib import SequenceMatcher
from pathlib import Path


def normalize(text: str) -> str:
    return re.sub(r"\s+", "", text)


def meaningful_lines(text: str) -> list[str]:
    result = []
    for line in text.splitlines():
        line = re.sub(r"\s+", "", line)
        if len(line) >= 12:
            result.append(line)
    return result


def common_prefix_length(a: str, b: str) -> int:
    limit = min(len(a), len(b))
    index = 0
    while index < limit and a[index] == b[index]:
        index += 1
    return index


def assess(old_text: str, new_text: str) -> dict[str, object]:
    old = normalize(old_text)
    new = normalize(new_text)
    if not old or not new:
        return {"verdict": "fail", "reasons": ["old or new body is empty"]}

    similarity = SequenceMatcher(None, old, new, autojunk=False).ratio()
    prefix_coverage = common_prefix_length(old, new) / len(old)

    old_lines = meaningful_lines(old_text)
    new_line_set = set(meaningful_lines(new_text))
    reused_lines = sum(1 for line in old_lines if line in new_line_set)
    line_reuse = reused_lines / len(old_lines) if old_lines else 0.0

    reasons: list[str] = []
    if new.startswith(old) and len(new) > len(old):
        reasons.append("new body contains the complete old body followed by appended text")
    if prefix_coverage >= 0.80:
        reasons.append(f"{prefix_coverage:.1%} of the old body survives as an unchanged prefix")
    if similarity >= 0.82:
        reasons.append(f"whole-body similarity is {similarity:.1%}")
    if len(old_lines) >= 8 and line_reuse >= 0.70:
        reasons.append(f"exact reuse covers {line_reuse:.1%} of meaningful old lines")

    return {
        "verdict": "fail" if reasons else "pass",
        "check_scope": "rewrite_integrity_only",
        "literary_quality": "not_evaluated",
        "old_characters": len(old),
        "new_characters": len(new),
        "similarity": round(similarity, 4),
        "unchanged_prefix_old_coverage": round(prefix_coverage, 4),
        "exact_meaningful_line_reuse": round(line_reuse, 4),
        "reasons": reasons,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Check whether a claimed rewrite is copy-heavy or append-only.")
    parser.add_argument("--old", required=True, type=Path)
    parser.add_argument("--new", required=True, type=Path)
    args = parser.parse_args()

    result = assess(
        args.old.read_text(encoding="utf-8"),
        args.new.read_text(encoding="utf-8"),
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 1 if result["verdict"] == "fail" else 0


if __name__ == "__main__":
    raise SystemExit(main())
