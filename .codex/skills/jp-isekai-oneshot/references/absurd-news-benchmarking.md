# Absurd News To Isekai Hook

Use when the user wants 逆天新闻, 离谱新闻, 奇葩新闻, 日本社会怪事, bizarre news, or "hot topics with actual story conflict" instead of plain Google Trends terms.

The goal is not to retell real news. Extract the absurd mechanism: unfair rule, ridiculous fee, broken service, strange workplace demand, odd school rule, consumer trap, AI/tool failure, public bureaucracy mistake, or overreaction. Then turn it into a fictional isekai institution that can be punished or outsmarted.

## Source Protocol

Record `searched_at_jst` and `window_start_jst=searched_at_jst-24h`. A news item qualifies only when its publication time is verifiably inside that rolling window. Search-result recency, page crawl time, or an updated index is not enough. Exclude undated or older items and never widen the window. Prefer public, non-paywalled summaries:

- Public odd-news starting points:
  - Excite びっくりニュース: `https://www.excite.co.jp/news/odd/`
  - Livedoor 珍事件・まぬけな事件: `https://news.livedoor.com/topics/keyword/27773/`
  - Yahooリアルタイム検索 for currently discussed phrases, only as a discovery surface.
- Japanese search/news queries:
  - `日本 変なニュース 今日`
  - `日本 びっくりニュース`
  - `日本 珍事件 ニュース`
  - `日本 SNS 話題 ありえない`
  - `日本 炎上 理不尽 ルール`
  - `ブラック企業 ありえない ニュース`
  - `物価高 ありえない 商品 ニュース`
  - `AI 失敗 ニュース 日本`
- Also check Google Trends JP only as a weak signal, not the main source.

Collect 6-10 candidates, then score them. Do not use private-person gossip, violent crime, fatal accidents, child victimization, sexual harm, active doxxing, or ongoing real lawsuits as story fuel.

## Absurd News Score

Score each candidate from 1-5:

- Absurdity: Is there an "are you serious?" rule, cost, mistake, service failure, or social contradiction?
- Conflict engine: Can it produce a clear antagonist, institution, test, or public proof?
- Everyday sting: Can ordinary viewers feel the unfairness quickly?
- Fantasy conversion: Can it become a guild rule, noble contract, dungeon regulation, academy exam, magic item, merchant trap, or skill test?
- Safety distance: Can names, victims, companies, and details be fictionalized cleanly?

Recommended pick:

- Main pick needs absurdity >= 4 and total >= 19/25.
- If the real news involves harm, tragedy, minors, or private people, reject it or abstract only the mechanism with no identifying detail.
- Prefer small absurdity with a clean payoff over huge tragedy with messy ethics.

## Mandatory User Selection Gate

- Collect 6-10 safe news mechanisms verified inside the rolling 24-hour window when available, score them, and present 3-5 viable numbered candidates rather than silently choosing one.
- Show direct source, publication timestamp, `searched_at_jst`, abstracted absurdity, scores, fictional institution, primary/backup route, converted skill, one-shot promise, and safety transform.
- Ask the user to choose a candidate number or request another batch, then stop before title lock, blueprint, drafting, package creation, or ledger mutation.
- Selecting “离谱新闻/逆天新闻” only selects the source lane. It does not select the concrete news seed.
- Bypass the pause only for an exact user-supplied item/link/keyword or explicit `你选/自动选` delegation; state the delegated selection before continuing.

## Conversion Matrix

| Real absurdity | Isekai conversion | Best route |
|---|---|---|
| ridiculous fee, hidden charge, refund trouble | noble contract, guild fee, cursed subscription, merchant trap | `exile-support-reversal` / `craft-commerce-slowlife` |
| black-company rule, unpaid work, impossible quota | adventurer guild quota, party exploitation, dungeon labor rule | `exile-support-reversal` |
| bizarre school/exam rule | academy rank exam, hidden bad-ending route, rigged entrance test | `academy-game-knowledge` |
| AI/tool/customer-service failure | magic bureaucracy, auto-scribe curse, appraisal system bug | `op-dominance` / `earth-commute` |
| food/product shortage, shrinkflation, price shock | storage skill, appraisal logistics, ration fraud, guild supply crisis | `craft-commerce-slowlife` / `exile-support-reversal` |
| delivery/transport chaos | route optimization, transfer gate failure, caravan rescue | `earth-commute` / `dungeon-master-territory` |
| pet/animal oddity | familiar contract, monster behavior rule, tamer proof | `tamer-familiar` |
| sports/contest absurd rule | guild trial, rank match, projectile/trajectory test | `battle-leveling` |

## Output Format

```markdown
1. 中文标题：
   日语标题：
   - News seed:
   - Absurdity score:
   - Total news-hook score:
   - What is absurd:
   - Fictionalized institution:
   - Selected theme route:
   - Backup route:
   - Converted cheat/skill:
   - One-shot promise:
   - Safety transform:
```

## Good Transformations

- Hidden cancellation fee -> cursed guild contract that only a mocked `契約鑑定` skill can expose.
- Black-company overtime rule -> adventurer party forces "free porter hours"; the porter proves his storage skill was carrying the whole raid economy.
- AI customer-service loop -> royal auto-scribe rejects every petition; protagonist's `意図翻訳` skill exposes the cursed instruction.
- Shrinkflation snack news -> guild rations secretly lose mana; mocked cook/appraiser saves a dungeon expedition.
- Bizarre exam rule -> academy exam punishes correct answers unless the student knows the hidden route flag.

## Hard Rule

Never paste a real scandal into the story. Use the shape of the absurdity, not the real names, victims, companies, locations, or legal facts. The final one-shot must feel like original Japanese male-audience isekai, not a disguised news recap.
