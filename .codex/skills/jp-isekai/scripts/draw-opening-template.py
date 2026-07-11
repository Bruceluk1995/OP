import argparse
import json
import secrets


CARDS = {
    "R1": ("反转・身份受辱型", {"exile", "academy", "craft"}),
    "R2": ("反转・世界常识错误型", {"battle", "op", "system", "academy", "craft"}),
    "R3": ("反转・转生结果型", {"rebirth"}),
    "N1": ("无脑・证明离谱设定型", {"battle", "op", "system", "craft", "tamer"}),
    "N2": ("无脑・第一次就失控型", {"battle", "system", "academy", "craft", "tamer"}),
    "N3": ("无脑・全民错误认知型", {"system", "op", "mystery", "academy"}),
    "C1": ("对比・被嫌弃与被争抢型", {"exile", "craft", "academy"}),
    "C2": ("对比・离开前后型", {"exile", "craft"}),
    "P1": ("铺垫・异常行为合理借口型", {"battle", "op", "craft", "survival", "earth"}),
    "P2": ("铺垫・小目标滚成大灾难型", {"craft", "survival", "territory", "earth"}),
    "D1": ("直接上・世界规则清单型", {"system", "academy", "op", "tamer"}),
    "D2": ("直接上・主角设定连爆型", {"battle", "op", "rebirth", "system"}),
    "E1": ("经验共识・偏偏反着做型", {"battle", "craft", "academy", "earth", "survival"}),
    "A1": ("意外・误操作滚大型", {"system", "academy", "earth", "mystery"}),
    "B1": ("吹牛／谎话字面成真型", {"system", "op", "mystery"}),
    "C3": ("对比・明明有功却受罚型", {"exile", "battle", "craft", "academy"}),
    "F1": ("反常备灾／囤积型", {"survival", "territory", "rebirth", "earth"}),
    "D3": ("单一规则连续兑现型", {"system", "craft", "op", "battle"}),
}


def main():
    parser = argparse.ArgumentParser(description="Draw a compatible male-isekai push-opening template.")
    parser.add_argument("--lane", default="any")
    parser.add_argument("--recent", default="")
    args = parser.parse_args()

    recent = {x.strip().upper() for x in args.recent.split(",") if x.strip()}
    compatible = [cid for cid, (_, lanes) in CARDS.items() if args.lane == "any" or args.lane in lanes]
    if args.lane != "any" and not compatible:
        raise SystemExit(f"Unknown or unsupported lane: {args.lane}")
    eligible = [cid for cid in compatible if cid not in recent]
    if not eligible:
        eligible = compatible or list(CARDS)

    card_id = secrets.choice(eligible)
    name, lanes = CARDS[card_id]
    print(json.dumps({"card_id": card_id, "name": name, "lanes": sorted(lanes)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
