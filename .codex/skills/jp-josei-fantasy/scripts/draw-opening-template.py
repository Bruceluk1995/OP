import argparse
import json
import secrets


CARDS = {
    "J01": ("公开婚约破弃反转", {"engagement", "villainess", "proof"}),
    "J02": ("反向服从撤回付出", {"engagement", "saint", "family", "craft"}),
    "J03": ("假圣女上位后连续失效", {"saint", "proof"}),
    "J04": ("恶役千金避死触发新路线", {"villainess", "loop"}),
    "J05": ("契约到期主动离婚反转", {"contract", "beloved"}),
    "J06": ("继承权让出后债务反转", {"family", "proof"}),
    "J07": ("女主离开前后崩坏", {"family", "saint", "craft", "beloved"}),
    "J08": ("被嫌弃与被具体珍视", {"beloved", "saint", "villainess"}),
    "J09": ("重生后让出前世选择", {"loop", "family"}),
    "J10": ("双重生抢走表面幸福", {"loop", "villainess", "family"}),
    "J11": ("文件最后一条翻案", {"engagement", "saint", "family", "proof"}),
    "J12": ("被夺功劳的二次实证", {"saint", "craft", "proof"}),
    "J13": ("小谎证据连锁崩塌", {"engagement", "family", "proof", "mystery"}),
    "J14": ("耻辱印记其实是功勋", {"saint", "villainess", "beloved", "proof"}),
    "J15": ("不公平规则漏洞反杀", {"saint", "engagement", "family", "proof"}),
    "J16": ("先还名誉再公开选择", {"beloved", "engagement", "saint", "proof"}),
    "J17": ("小愿望滚成王国事件", {"contract", "craft", "beloved"}),
    "J18": ("错投信件／契约对象掉马", {"contract", "beloved", "mystery"}),
}


def main():
    parser = argparse.ArgumentParser(description="Draw a compatible josei push-opening template.")
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
