import argparse
import json
import re
import secrets
import sys
from pathlib import Path

from opening_cards import CARDS, CARD_SURFACES, REQUIRED_CHAINS

DEFAULT_LEDGER = Path("男频异世界短篇知识库") / "generated-ledger.jsonl"


def configure_stdio() -> None:
    for stream in (sys.stdout, sys.stderr):
        reconfigure = getattr(stream, "reconfigure", None)
        if reconfigure:
            reconfigure(encoding="utf-8")


def recent_cards(path: Path, limit: int) -> list[str]:
    if not path.exists():
        return []
    cards: list[str] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        try:
            record = json.loads(line)
        except json.JSONDecodeError:
            continue
        card = str(record.get("opening_card", "")).strip().upper()
        if not card:
            legacy = re.search(r"(?:opening card|开场模板卡|开场卡)\s*[:：]?\s*([A-Z]\d)", str(record.get("notes", "")), re.IGNORECASE)
            card = legacy.group(1).upper() if legacy else ""
        if card in CARDS:
            cards.append(card)
    return cards[-limit:] if limit > 0 else []


def main():
    configure_stdio()
    parser = argparse.ArgumentParser(description="Draw a compatible male-isekai push-opening template.")
    parser.add_argument("--lane", default="any")
    parser.add_argument("--recent", default="")
    parser.add_argument("--root", default=".")
    parser.add_argument("--ledger", default="")
    parser.add_argument("--recent-limit", type=int, default=3)
    args = parser.parse_args()

    ledger_path = Path(args.ledger).resolve() if args.ledger else Path(args.root).resolve() / DEFAULT_LEDGER
    ledger_recent = recent_cards(ledger_path, max(args.recent_limit, 0))
    explicit_recent = [x.strip().upper() for x in args.recent.split(",") if x.strip()]
    recent = set(ledger_recent + explicit_recent)
    compatible = [cid for cid, (_, lanes) in CARDS.items() if args.lane == "any" or args.lane in lanes]
    if args.lane != "any" and not compatible:
        raise SystemExit(f"Unknown or unsupported lane: {args.lane}")
    eligible = [cid for cid in compatible if cid not in recent]
    if not eligible:
        eligible = compatible or list(CARDS)

    card_id = secrets.choice(eligible)
    name, lanes = CARDS[card_id]
    print(
        json.dumps(
            {
                "card_id": card_id,
                "name": name,
                "lanes": sorted(lanes),
                "required_chain": REQUIRED_CHAINS[card_id],
                "surface_beats": CARD_SURFACES[card_id],
                "excluded_recent": sorted(recent),
                "ledger_path": str(ledger_path),
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
