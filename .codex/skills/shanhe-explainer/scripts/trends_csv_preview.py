#!/usr/bin/env python3
"""Preview Google Trends CSV exports for shanhe-explainer topic selection."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path


PREFERRED_COLUMNS = (
    "Trends",
    "Trend",
    "Search term",
    "Title",
    "Search volume",
    "Started",
    "Status",
    "Breakdown",
)


def read_rows(path: Path) -> list[dict[str, str]]:
    text = path.read_text(encoding="utf-8-sig")
    sample = text[:4096]
    try:
        dialect = csv.Sniffer().sniff(sample) if sample.strip() else csv.excel
    except csv.Error:
        dialect = csv.excel
    reader = csv.DictReader(text.splitlines(), dialect=dialect)
    return [{str(k): (v or "").strip() for k, v in row.items()} for row in reader]


def compact_row(row: dict[str, str]) -> dict[str, str]:
    if not row:
        return {}
    picked = {key: row.get(key, "") for key in PREFERRED_COLUMNS if row.get(key)}
    if picked:
        return picked
    return {key: value for key, value in row.items() if value}


def main() -> int:
    parser = argparse.ArgumentParser(description="Preview Google Trends CSV rows.")
    parser.add_argument("csv_path", help="CSV exported from Google Trends.")
    parser.add_argument("--limit", type=int, default=20)
    args = parser.parse_args()

    rows = read_rows(Path(args.csv_path))
    print(f"rows={len(rows)}")
    for index, row in enumerate(rows[: args.limit], start=1):
        compact = compact_row(row)
        joined = " | ".join(f"{k}: {v}" for k, v in compact.items())
        print(f"{index}. {joined}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
