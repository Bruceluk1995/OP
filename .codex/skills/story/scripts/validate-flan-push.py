from __future__ import annotations

import argparse
import json
import math
import re
import sys
from pathlib import Path

TURN_RE = re.compile(r"ところが|すると|だが|しかし|しかも|その直後|結果|そこで|一方|にもかかわらず|なぜなら|そして")
FIRST_RE = re.compile(r"俺|僕|私")


def percentile(values: list[int], fraction: float) -> int:
    ordered = sorted(values)
    return ordered[max(0, math.ceil(len(ordered) * fraction) - 1)]


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate Flan-style Japanese push-narration surface metrics.")
    parser.add_argument("--body", required=True)
    parser.add_argument("--person", choices=("first", "third"), required=True)
    args = parser.parse_args()
    for stream in (sys.stdout, sys.stderr):
        reconfigure = getattr(stream, "reconfigure", None)
        if reconfigure:
            reconfigure(encoding="utf-8")
    text = Path(args.body).read_text(encoding="utf-8")
    lines = [line.strip() for line in text.splitlines() if line.strip() and not line.lstrip().startswith("#")]
    if len(lines) < 20:
        print(json.dumps({"status": "fail", "errors": ["need at least 20 spoken lines"]}, ensure_ascii=False))
        return 2
    lengths = [len(line) for line in lines]
    long_ratio = sum(length > 32 for length in lengths) / len(lines)
    comma_ratio = sum(line.count("、") >= 2 for line in lines) / len(lines)
    quote_ratio = sum("「" in line or "」" in line for line in lines) / len(lines)
    turn_ratio = sum(bool(TURN_RE.search(line)) for line in lines) / len(lines)
    metrics = {
        "spoken_lines": len(lines),
        "median_line": percentile(lengths, 0.5),
        "p90_line": percentile(lengths, 0.9),
        "max_line": max(lengths),
        "long_line_ratio": round(long_ratio, 4),
        "multi_comma_ratio": round(comma_ratio, 4),
        "direct_quote_ratio": round(quote_ratio, 4),
        "turn_connector_ratio": round(turn_ratio, 4),
        "first_person_markers": len(FIRST_RE.findall(text)),
    }
    errors: list[str] = []
    if metrics["median_line"] > 20:
        errors.append("median line length exceeds 20")
    if metrics["p90_line"] > 32:
        errors.append("90th-percentile line length exceeds 32")
    if metrics["max_line"] > 60:
        errors.append("maximum line length exceeds 60")
    if long_ratio > 0.12:
        errors.append("more than 12% of lines exceed 32 characters")
    if comma_ratio > 0.15:
        errors.append("too many multi-clause lines")
    if quote_ratio > 0.05:
        errors.append("direct-quote lines exceed 5%")
    if turn_ratio < 1 / 12:
        errors.append("turn/causal connector density is below one per 12 lines")
    if args.person == "first" and metrics["first_person_markers"] == 0:
        errors.append("first-person mode has no first-person marker")
    result = {"status": "fail" if errors else "pass", "person": args.person, "metrics": metrics, "errors": errors}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 2 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
