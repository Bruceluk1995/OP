# Anti-Homogenization

Keep the channel vertical by preserving the promise: mature Japanese family drama, hidden proof, justice, and late-life dignity. Avoid sameness by rotating the lane and story engine.

## Required Preflight

Before generating a new premise, outline, title batch, or full prose:

1. Read recent ledger records from `银发文学知识库/generated-ledger.jsonl` when present.
2. Identify the last 10 used combinations.
3. Avoid repeating more than two of these six fields from any recent record:
   - lane
   - protagonist
   - pressure source
   - proof object
   - reversal venue
   - aftertaste
4. If the user asks for a similar setup, keep only the requested field and vary at least three others.

## Matrix

Pick one from each column:

| Lane | Pressure source | Proof object | Reversal venue | Aftertaste |
|---|---|---|---|---|
| care-labor-reversal | 義母介護の押しつけ | 介護日誌 | 家族会議 | 一人暮らしの再出発 |
| late-life-divorce-retirement-money | 定年退職日の離婚届 | 退職金明細 | 弁護士事務所 | 小さな部屋の鍵 |
| property-inheritance-rights | 家の乗っ取り | 家の名義書 | 不動産会社 | 庭を取り戻す |
| hospital-medical-neglect | 医療放置 | 診断書 | 病院 | 健康回復 |
| funeral-will-posthumous-truth | 葬式での排除 | 遺言書 | 遺言公開 | 故人の約束を守る |
| hidden-identity-old-merit | 会社での侮辱 | 株主名簿 | 取締役会 | 仕事復帰 |
| adult-child-filial-reckoning | 仕送り要求 | 通帳 | 銀行窓口 | 孫との和解 |
| nursing-home-facility | 施設トラブル | 施設請求書 | 介護施設 | 安心できる居場所 |
| pension-fraud-bank-scam | 年金搾取 | 年金通知書 | 警察/銀行 | 朝食の自由 |
| workplace-retirement-reputation | 退職祝いの侮辱 | 社員証/顧客名簿 | 会社受付 | 技術の継承 |
| second-life-romance-remarriage | 再婚相手への支配 | 録音データ | 親族食事会 | 穏やかな再婚 |
| neighbor-community-housing | 近所の見下し | 防犯カメラ映像 | 町内会 | 古い家の灯り |

## Hard Repetition Blocks

Do not generate a new work if it matches a recent record in all of these:

- same lane
- same protagonist role
- same pressure source
- same proof object
- same reversal venue
- same aftertaste

If blocked, change at least three fields. Prefer changing lane, proof object, and venue first, because these most strongly alter scene behavior.

## Variation Levers

Use these to keep episodes fresh without leaving the niche:

- Viewpoint: wife, husband, widower, daughter, son, daughter-in-law, cleaner, retired professional, grandchild, neighbor, facility worker.
- Time span: one night, three days, five years later, after funeral, before surgery, after retirement, before remarriage.
- Moral texture: pure revenge, reconciliation, protective lie, posthumous truth, professional duty, late-life romance, community restoration.
- Power base: law, medicine, property, company, neighborhood trust, old craft, caregiving knowledge, family registry, pension system.
- Ending image: train, key, garden, breakfast, old camera, repaired kimono, clinic appointment, small shop, grandchild's letter, morning radio.

## Ledger Record Schema

Each generated work should append one JSON line:

```json
{"date":"YYYY-MM-DD","title":"...","lane":"care-labor-reversal","protagonist":"67歳の元看護師","pressure":"義母介護の押しつけ","proof":"介護日誌","venue":"家族会議","aftertaste":"一人暮らしの再出発","path":"作品/正文.md","notes":"one-line hook"}
```

Record concepts and title batches too. If no file was saved, use `"path":"chat-only"`.
