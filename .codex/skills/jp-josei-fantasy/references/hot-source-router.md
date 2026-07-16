# Josei Fantasy Hot Source Router

Use when the user has no premise, wants 热点选题, asks for Google Trends / YouTube / TikTok / Shorts / ranking / Chinese women-oriented novel sites / news / all-source discovery, or says the current source is boring.

The goal is to choose a source strategy before premise generation. Female-audience fantasy romance needs attention plus emotional convertibility: a hot seed is useful only if it can become heroine dignity, public proof, romance recognition, social reputation repair, contract pressure, family wound, or happy-ending belonging.

## Source Menu

Ask this when the source is missing:

```text
你想从哪个热点入口找女频幻想恋爱选题？

1. YouTube/TikTok 热门视频：适合找短视频钩子、反转证明、公开羞辱、恋爱/婚姻/家庭情绪、生活痛点
2. Google Trends JP：适合看日本正在搜索的生活、天气、健康、工作、价格、考试、活动、关系焦虑
3. 女性向けランキング/タグ页：适合看 Syosetu/Kakuyomu/Narou 当前令嬢、聖女、婚約破棄、溺愛、ざまぁ组合
4. 日本离谱新闻/社会热点：适合找不公平规则、合同坑、学校/职场/家庭荒谬、公共道歉失败
5. 中国女频小说站榜单/分类趋势：适合找情绪伤口、关系拉扯、身份逆转、证据与追妻/救赎机制，只取功能灵感
6. 常青女频类型：不追热点，直接从悪役令嬢、聖女、契約婚、辺境伯溺愛、家族冷遇等题材包选
7. 全选：多源交叉筛，选最适合写成日式女频幻想恋爱的题
```

## All-Source Mode

When the user chooses `全选`, collect small batches from available sources:

- 5-10 Google Trends JP seeds.
- 3-5 YouTube/TikTok video hook mechanics when public access works.
- 3-5 women-oriented ranking/tag signals.
- 5-8 weird/social-news seeds.
- 3-5 Chinese women-oriented ranking/category mechanisms when public pages are accessible; label them as cross-market inspiration.
- 2-4 evergreen lane ideas from `theme-taxonomy.md` or `jp-josei-fantasy-plan/references/type-packs/*`.

Score all candidates together. Do not output one title per source by default; output the best mixed shortlist.

## Mandatory User Selection Gate

1. Collect and score raw candidates from the chosen source mode.
2. Present 3-5 viable numbered candidates. For each, include source market, source/date, source seed, score, selected/backup route, heroine wound, proof or romance mechanism, Japan cross-check status, title hook, payoff, and safety transform.
3. Ask the user to choose a number or request another batch, then stop.
4. A source choice such as `YouTube/TikTok`, `Google Trends JP`, `离谱新闻`, `ランキング`, `中国女频小说站`, or `全选` is not a concrete seed choice. A lane, emotion, or male-lead preference is not a seed choice either.
5. Do not lock a title, create an outline, draft prose, save files, or mutate a ledger before the user confirms the seed.
6. Bypass the pause only if the user gives an exact item/link/keyword or explicitly says `你选/自动选/直接选最好的`; state the selected candidate before continuing.

## Scoring

Score each candidate from 1-5:

- Heroine empathy: can readers immediately feel her humiliation, exhaustion, unfairness, loneliness, fear, or desire to be recognized?
- Romance/zamaa engine: can the seed become public proof, social consequence, contract reversal, legal/church record, male-lead recognition, or earned devotion?
- Japanese female-fantasy fit: can it naturally route to 令嬢, 聖女, 契約結婚, 辺境伯, 悪役令嬢, ループ, 職人, 家族冷遇, or 異類婚姻?
- Safety/copy distance: can it avoid real-person gossip, tragedy, active scandals, copyrighted scenes, creators, songs, and exact news facts?
- Title clickability: can the Japanese title promise the fantasy payoff without requiring knowledge of the original trend?

Recommended pick:

- Main candidate needs total >= 19/25.
- If heroine empathy is below 3, use it only as an opening texture or keep searching.
- Prefer ordinary emotional pressure over remote spectacle.
- If a hot source is attention-rich but romance-poor, transform it into a concrete social rule, ceremony, contract, proof object, or family wound before using it.

## Source-Specific Use

| Source | Best for | Avoid |
|---|---|---|
| YouTube/TikTok | visible before/after proof, POV reversal, apology failure, public reaction, home/food/care, work/school absurdity | copying creators, clips, jokes, exact scenes, songs, anime/game IP |
| Google Trends JP | daily-life anxieties, weather, prices, food, health, exams, travel, apps, shopping, weddings/events | celebrity/sports names with no female-audience mechanism |
| Ranking/tag pages | current tag combinations, title grammar, visible premise promises | copying characters, scene order, or proprietary summaries |
| Chinese women-oriented novel sites | heroine wounds, relationship pressure, identity reversal, proof objects, pursuit/redemption, family and marriage functions | treating Chinese popularity as Japanese proof; copying titles, systems, characters, or plot order |
| Weird/social news | unfair rules, hidden fees, public apology failure, school/workplace/family absurdity | crime/tragedy spectacle, private-person details, ongoing lawsuits |
| Evergreen | durable romance fantasy engines and type-pack safety | stale generic openings with no specific proof object |

## Output Fields

For trend or title batches, include:

```text
- Hot source mode:
- Source seed:
- Source type:
- Source market:
- Japan cross-check status:
- Selected josei route:
- Backup route:
- Heroine empathy score:
- Romance/zamaa engine:
- Converted proof or relationship mechanism:
- Title hook:
- Safety transform:
```

## Hard Rule

Never turn viral material into disguised real-person gossip or copied short-video content. Extract only the public emotion or mechanism, then rebuild it as original Japanese female-audience fantasy romance.

For Chinese women-oriented novel-site sourcing, read `chinese-novel-inspiration.md`. Keep the Chinese signal labeled as cross-market inspiration and require a current Japanese cross-check before claiming Japanese-market fit.
