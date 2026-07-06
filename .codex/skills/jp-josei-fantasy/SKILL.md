---
name: jp-josei-fantasy
description: "Japanese female-audience fantasy romance writing suite router. Use when the user wants 女性向け異世界恋愛, Japanese romantasy, Syosetu/Kakuyomu female-reader fantasy, 悪役令嬢, 婚約破棄, ざまぁ, 溺愛, 聖女, 契約婚, 令嬢, 辺境伯, 宮廷ロマンス, time loop villainess, noble romance, Chinese-to-Japanese localization for female-oriented fantasy romance, or YouTube/TikTok/Google Trends JP hot-topic selection converted into josei fantasy romance."
---

# JP Josei Fantasy

Use this as the router for Japanese female-audience fantasy romance work. Prefer the dedicated sub-skills:

- `$jp-josei-fantasy-plan`: premise, tag cluster, hot-topic conversion, heroine wound, male lead, court/noble rules, revenge/romance arc, chapter beats.
- `$jp-josei-fantasy-write`: Japanese prose drafting or rewriting for 女性向け異世界恋愛 / 令嬢 / 溺愛 / ざまぁ stories.
- `$jp-josei-fantasy-oneshot`: standalone 14,500-16,500 character Japanese female-audience fantasy romance short stories, including Google Trends JP / YouTube / TikTok / weird-news seeds converted into one-file romance payoffs.
- `$jp-josei-fantasy-review`: genre fit, Japanese readability, romance payoff, zamaa logic, and Chinese-term leakage checks.

## Core Contract

Always localize toward Japanese female-reader web novel expectations:

- Center the heroine's dignity, emotional recovery, social reputation, and happy ending.
- Treat romance as the main engine or a co-main engine, not a side reward after power progression.
- Use court, noble-house, church, academy, frontier, salon, ball, contract-marriage, saint, curse, and family-inheritance pressures as plot fuel.
- Make `ざまぁ` emotionally earned: the public proof, social consequence, or legal reversal should expose the antagonist's own actions.
- Make `溺愛` feel protective, respectful, and specific. Avoid possessive flattening unless the user wants darker yandere-adjacent tones.
- Avoid male-audience RPG optimization, harem framing, xianxia/wuxia terms, and Chinese court fantasy defaults unless the user explicitly asks for them.

## Project Memory Contract

When the task is project-bound, treat this suite as a genre layer on top of the common story project architecture:

- Use `设定/`, `大纲/`, `追踪/`, `episodes/`, `对标/`, and `拆文库/` as long-term memory.
- Use `女频幻想恋爱知识库/generated-ledger.jsonl` to remember generated concepts, outlines, titles, and episodes so future work does not repeat the same wound-romance-reversal engine.
- Use project拆文, live benchmark cards, project-local subtype notes, and bundled type packs in that order when a female-fantasy subtype is selected.
- `$jp-josei-fantasy-plan` owns settings, outlines, first rolling chapter blueprints, and initial tracking files.
- `$jp-josei-fantasy-write` must read the current outline and tracking files before prose, then update tracking and ledger after saving.
- `$jp-josei-fantasy-review` should flag project-bound drafts that bypass the outline/tracking/ledger loop.

Detailed protocol: `references/project-memory.md`.

## Workflow

1. Determine the task:
   - Standalone short story, one-shot, 一发完结, 15000字短篇, or "不是连续剧" -> use `$jp-josei-fantasy-oneshot`.
   - New concept, tag strategy, Chinese-to-Japanese localization, or outline -> use `$jp-josei-fantasy-plan`.
   - Write or rewrite Japanese chapters/scenes -> use `$jp-josei-fantasy-write`.
   - Check an existing draft -> use `$jp-josei-fantasy-review`.
2. If the task references an existing project, continuing episode, saved output, or anti-homogenization need, load the project memory protocol before planning or drafting.
3. If the task references current ranking, latest trends, Google Trends, YouTube, TikTok, Shorts, viral videos, 热点, or "现在日本什么火", read `references/hot-source-router.md`, browse/fetch current source pages before making market claims, then route:
   - One-file story / 15000字 / 一发完结 -> `$jp-josei-fantasy-oneshot`.
   - Book concept, serialized project, tag strategy, or outline -> `$jp-josei-fantasy-plan`.
4. If the task only says "女频" or "幻想恋爱", ask or infer a compact lane before planning: 婚約破棄ざまぁ, 悪役令嬢, 聖女, 契約結婚, 辺境伯/溺愛, 職人, 王宮/家族/相続, ループ, 異類婚姻, 強いヒロイン, or 手紙すれ違いラブコメ. If the user wants discovery, offer source first: YouTube/TikTok, Google Trends JP, ranking/tag pages, weird/social news, evergreen lane, or 全选.
5. If adapting from Chinese fantasy or a real-world trend, first map institutions, ranks, magic, family roles, marriage customs, public proof, and antagonist functions into Japanese female-oriented fantasy equivalents.
6. Keep meta notes in the user's language. Write Japanese prose in Japanese when the user asks for audience-facing text.

## Resources

Read `references/theme-taxonomy.md` when choosing tags, combining formulas, or checking whether a premise fits 女性向け異世界恋愛 expectations.
Read `references/hot-source-router.md` when the user has no premise, asks for 热点选题, or wants Google Trends / YouTube / TikTok / all-source discovery.
Read `references/project-memory.md` when routing project-bound work or explaining the suite's engineering model.
