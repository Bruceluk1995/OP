#!/usr/bin/env python3
"""Preview exported trend CSV rows for finance/economics topic conversion."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description="Preview trend CSV seeds for econ-finance-explainer.")
    parser.add_argument("csv_path")
    parser.add_argument("--limit", type=int, default=30)
    args = parser.parse_args()

    path = Path(args.csv_path)
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        print("columns=" + ", ".join(reader.fieldnames or []))
        for idx, row in enumerate(reader, start=1):
            if idx > args.limit:
                break
            parts = [f"{key}={value}" for key, value in row.items() if value]
            print(f"{idx}. " + " | ".join(parts))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
