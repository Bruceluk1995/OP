---
name: jp-josei-fantasy
description: "Japanese female-audience fantasy romance writing suite router. Use when the user wants 女性向け異世界恋愛, Japanese romantasy, Syosetu/Kakuyomu female-reader fantasy, 悪役令嬢, 婚約破棄, ざまぁ, 溺愛, 聖女, 契約婚, 令嬢, 辺境伯, 宮廷ロマンス, time loop villainess, noble romance, or Chinese-to-Japanese localization for female-oriented fantasy romance."
---

# JP Josei Fantasy

Use this as the router for Japanese female-audience fantasy romance work. Prefer the dedicated sub-skills:

- `$jp-josei-fantasy-plan`: premise, tag cluster, heroine wound, male lead, court/noble rules, revenge/romance arc, chapter beats.
- `$jp-josei-fantasy-write`: Japanese prose drafting or rewriting for 女性向け異世界恋愛 / 令嬢 / 溺愛 / ざまぁ stories.
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
   - New concept, tag strategy, Chinese-to-Japanese localization, or outline -> use `$jp-josei-fantasy-plan`.
   - Write or rewrite Japanese chapters/scenes -> use `$jp-josei-fantasy-write`.
   - Check an existing draft -> use `$jp-josei-fantasy-review`.
2. If the task references an existing project, continuing episode, saved output, or anti-homogenization need, load the project memory protocol before planning or drafting.
3. If the task references current ranking, latest trends, or "now popular", browse current Syosetu/Kakuyomu-style source pages before making market claims.
4. If the task only says "女频" or "幻想恋爱", route to a concrete lane before planning: 婚約破棄ざまぁ, 悪役令嬢, 聖女, 契約結婚, 辺境伯/溺愛, 職人, 王宮/家族/相続, ループ, 異類婚姻, 強いヒロイン, or 手紙すれ違いラブコメ.
5. If adapting from Chinese fantasy, first map institutions, ranks, magic, family roles, marriage customs, and antagonist functions into Japanese female-oriented fantasy equivalents.
6. Keep meta notes in the user's language. Write Japanese prose in Japanese when the user asks for audience-facing text.

## Resources

Read `references/theme-taxonomy.md` when choosing tags, combining formulas, or checking whether a premise fits 女性向け異世界恋愛 expectations.
Read `references/project-memory.md` when routing project-bound work or explaining the suite's engineering model.
