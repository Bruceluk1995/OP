---
name: jp-josei-fantasy
description: "Japanese female-audience fantasy romance suite for traditional web-novel prose or anime-recap/push narration, each supporting first-person or third-person. Use for 女性向け異世界恋愛, 女频幻想恋爱推文, 悪役令嬢, 婚約破棄, ざまぁ, 溺愛, 聖女, 契約婚, 令嬢, 辺境伯, 宮廷ロマンス, loops, noble romance, localization, or hot-topic conversion."
metadata: {"openclaw":{"source":"https://github.com/worldwonderer/oh-story-claudecode"}}
---

# JP Josei Fantasy

## 数字交互契约

- 凡需用户在有限选项中决定，必须在普通对话中列出数字编号，并以“请只回复数字；可多选时用 +，如 1+3”收尾。
- 禁止用开放式问题代替可枚举选项；禁止依赖 AskUserQuestion、request_user_input 或自由文本选项完成有限选择。
- “自定义 / 其他 / 提供素材”也必须编为数字选项。用户选中后，下一轮只索取一个必要内容（如关键词、书名、路径、链接或正文）；这类实际内容不强行数字化。
- 是非确认统一写成 1. 是 / 2. 否，并要求只回复数字。

Use this as the router for Japanese female-audience fantasy romance work. Prefer the dedicated sub-skills:

Before proposing any premise, hotspot, title, or angle, read `../story/references/global-topic-history.md` and enforce the project-wide burned-topic ledger. A topic used or merely displayed by any other story or explainer skill must not be shown again unless the user explicitly requests reuse.

Before character naming, read `../story/references/character-name-policy.md`, import and check the shared name ledger, and record every selected name. New works may not recycle a prior heroine or male-lead given name. Heroines and core women use short daily names: 2-6 characters; two-part fantasy full names max 10 characters; no three-part aristocratic names by default.

- `$jp-josei-fantasy-plan`: premise, tag cluster, hot-topic conversion, heroine wound, male lead, court/noble rules, revenge/romance arc, chapter beats.
- `$jp-josei-fantasy-write`: Japanese prose drafting or rewriting for 女性向け異世界恋愛 / 令嬢 / 溺愛 / ざまぁ stories.
- `$jp-josei-fantasy-oneshot`: standalone 14,500-16,500 character Japanese female-audience fantasy romance short stories, including Google Trends JP / YouTube / TikTok / weird-news seeds converted into one-file romance payoffs.
- `$jp-josei-fantasy-review`: genre fit, Japanese readability, romance payoff, zamaa logic, and Chinese-term leakage checks.

## Core Contract

- Before long or short female-fantasy planning or drafting, read `references/presentation-modes.md` and present its numbered 1-4 menu unless already explicit. Allow multiple selections as separate versions.
- For either push option, read `../story/references/flan-push-strict-mode.md`; first/third person share the same recap surface and saved bodies must pass its validator.
- Female push requires retention, emotional movement, proof, relationship movement, and payoff; it does not require jokes or comedy unless the chosen lane benefits from them.
- When push narration is selected, read `references/push-opening-template-deck.md`, filter by the chosen female lane, run its random draw script, fill only the selected card, and record the ID.
- Reject literary prose in drafted or rewritten fiction: avoid long environment description and long psychology description; use colloquial, direct everyday language to advance plot through action, dialogue, choices, proof, and consequences.

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

1. Resolve presentation mode and viewpoint from `references/presentation-modes.md`.
2. Determine the task:
   - Standalone short story, one-shot, 一发完结, 15000字短篇, or "不是连续剧" -> use `$jp-josei-fantasy-oneshot`.
   - Explicit one-shot/一发完结 wins even when the prompt also mentions YouTube, thumbnail, 15,000 characters, or a hot topic. Explicit 6-episode/serial/第N話 wins over one-shot and routes through plan/write.
   - New concept, tag strategy, Chinese-to-Japanese localization, or outline -> use `$jp-josei-fantasy-plan`.
   - Write or rewrite Japanese chapters/scenes -> use `$jp-josei-fantasy-write`.
   - Check an existing draft -> use `$jp-josei-fantasy-review`.
3. If the task references an existing project, continuing episode, saved output, or anti-homogenization need, load the project memory protocol before planning or drafting.
4. If the task references current ranking, latest trends, Google Trends, YouTube, TikTok, Shorts, viral videos, 热点, or "现在日本什么火", read `references/hot-source-router.md`, browse/fetch current source pages before making market claims, then route:
   - One-file story / 15000字 / 一发完结 -> `$jp-josei-fantasy-oneshot`.
   - Book concept, serialized project, tag strategy, or outline -> `$jp-josei-fantasy-plan`.
5. If the task only says "女频" or "幻想恋爱", display a numbered lane menu before planning: `1 婚約破棄ざまぁ`、`2 悪役令嬢`、`3 聖女`、`4 契約結婚`、`5 辺境伯/溺愛`、`6 職人`、`7 王宮/家族/相続`、`8 ループ`、`9 異類婚姻`、`10 強いヒロイン`、`11 手紙すれ違いラブコメ`、`12 热点发现`、`13 自定义`; require a numeric reply. If 12 is selected, display source menu: `1 YouTube/TikTok`、`2 Google Trends JP`、`3 小说榜/标签页`、`4 离谱/社会新闻`、`5 常青题材`、`6 全选`; require a numeric reply. Option 13 may request one keyword in the next turn.
6. If push narration is selected, map the chosen lane to the template deck, draw one compatible card, and lock it before outlining the opening.
7. If adapting from Chinese fantasy or a real-world trend, first map institutions, ranks, magic, family roles, marriage customs, public proof, and antagonist functions into Japanese female-oriented fantasy equivalents.
8. Keep meta notes in the user's language. Write Japanese prose in Japanese when the user asks for audience-facing text.

## Resources

Read `references/theme-taxonomy.md` when choosing tags, combining formulas, or checking whether a premise fits 女性向け異世界恋愛 expectations.
Read `references/hot-source-router.md` when the user has no premise, asks for 热点选题, or wants Google Trends / YouTube / TikTok / all-source discovery.
Read `references/project-memory.md` when routing project-bound work or explaining the suite's engineering model.
Read `references/presentation-modes.md` before all planning or drafting.
Read `references/push-opening-template-deck.md` whenever push narration is selected.
