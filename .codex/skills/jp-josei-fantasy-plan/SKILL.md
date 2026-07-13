---
name: jp-josei-fantasy-plan
description: "Plan Japanese female-audience fantasy romance in traditional web-novel or anime-recap/push narration form, with first-person or third-person. Use for 女性向け異世界恋愛, 女频推文, 悪役令嬢, 婚約破棄, ざまぁ, 溺愛, 聖女, 契約婚, family inheritance, loops, court romance, hot-topic conversion, and localization."
metadata: {"openclaw":{"source":"https://github.com/worldwonderer/oh-story-claudecode"}}
---

# JP Josei Fantasy Plan

## 数字交互契约

- 凡需用户在有限选项中决定，必须在普通对话中列出数字编号，并以“请只回复数字；可多选时用 +，如 1+3”收尾。
- 禁止用开放式问题代替可枚举选项；禁止依赖 AskUserQuestion、request_user_input 或自由文本选项完成有限选择。
- “自定义 / 其他 / 提供素材”也必须编为数字选项。用户选中后，下一轮只索取一个必要内容（如关键词、书名、路径、链接或正文）；这类实际内容不强行数字化。
- 是非确认统一写成 1. 是 / 2. 否，并要求只回复数字。

Build Japanese-style female-audience fantasy romance plans. This skill is for concept, market fit, emotional structure, and chapter beats, not final prose.

Before premise or title work, read `../story/references/global-topic-history.md`, check the shared project ledger, and record every displayed candidate before output. Cross-domain re-skins of burned topics are blocked by default.

When planning prose beats, design colloquial, direct scene movement: action, dialogue, choices, evidence, romance movement, and social consequence. Do not plan long scenery passages, long psychology passages, or literary mood filler as a way to carry the story.

## Required Reads

- Read `../jp-josei-fantasy/references/presentation-modes.md` before planning any long or short project. Present its numbered 1-4 menu unless already explicit.
- Read `../story/references/flan-push-strict-mode.md` for either push option and plan short narrated evidence/romance beats rather than scene prose, regardless of person.
- Read `../jp-josei-fantasy/references/push-opening-template-deck.md` when push narration is selected. Filter by lane, randomly draw one compatible card, and record the card ID in the plan.
- Read `references/market-patterns.md` when the user asks for hot themes, Syosetu/Kakuyomu fit, or tag combinations.
- Read `references/planning-template.md` before producing a full concept package.
- Read `references/terminology.md` whenever adapting from Chinese fantasy or when the user says not to use Chinese elements.
- Read `references/dynamic-benchmarking.md` when the user wants current market fit, website-based拆书, hottest works, or when no strong project benchmark exists for the chosen subtype.
- Read `../jp-josei-fantasy/references/hot-source-router.md` when the user has no premise, wants 热点选题, asks for YouTube/TikTok/Google Trends/news/all-source selection, or rejects the current source as boring.
- Read `../jp-josei-fantasy/references/trend-benchmarking.md` when the user wants Google Trends JP or hot/current topic conversion.
- Read `../jp-josei-fantasy/references/social-video-trends.md` when the user wants YouTube/TikTok/Shorts/video hooks.
- Read `../jp-josei-fantasy/references/absurd-news-benchmarking.md` when the user wants 离谱新闻, 逆天新闻, or Japanese social-news hooks.
- Read `../jp-josei-fantasy/references/trend-theme-router.md` after selecting any hot seed, before choosing the final tag cluster, heroine wound, proof object, male-lead recognition mode, or outline.
- Read `../jp-josei-fantasy/references/project-memory.md` before opening a project, continuing a serial, creating chapter outlines, or trying to avoid repeated premises.
- Read `../story/references/character-name-policy.md` before naming the cast. Run `import-existing`, check heroine/male-lead/supporting-cast names, enforce `jp-female-fantasy`, and record the selected names after saving.
- Before planning any subtype, resolve its benchmark priority: project拆文 or live website benchmark first, project subtype notes second, bundled type pack only as fallback. Do not rely on the generic josei fantasy rules alone.

Type pack routing:

- 婚約破棄 / public accusation / ざまぁ -> `references/type-packs/engagement-annulment-zamaa.md`
- 悪役令嬢 / 乙女ゲーム / manga or novel reincarnation / death flags -> `references/type-packs/villainess-otome-game.md`
- 聖女 / 偽聖女 / church proof / healing or purification -> `references/type-packs/saint-replacement-church.md`
- 契約結婚 / 白い結婚 / political marriage / forced proximity -> `references/type-packs/contract-marriage-white-marriage.md`
- 溺愛公爵 / 辺境伯 / cursed duke or prince / new home -> `references/type-packs/beloved-duke-frontier.md`
- 職人 / shop / craft / magic tool / job competence -> `references/type-packs/craft-job-competence.md`
- 王宮 / family coldness / inheritance / stepfamily / divorce or remarriage -> `references/type-packs/palace-family-inheritance.md`
- ループ / やり直し / foreknowledge / tragedy prevention -> `references/type-packs/time-loop-foreknowledge.md`
- 魔王 / 勇者 / 竜人 / interspecies marriage / culture-gap romance -> `references/type-packs/monster-demon-interspecies-romance.md`
- 強いヒロイン / status gap / exile action romance -> `references/type-packs/strong-heroine-status-gap.md`
- 手紙 / すれ違い / misunderstanding romantic comedy -> `references/type-packs/letter-misunderstanding-comedy.md`

Benchmark priority:

1. If `对标/{lane}/{work}/拆文报告.md` or `拆文库/{work}/` exists, read it before bundled type packs.
2. If the user asks for current/hot/platform-fit or there is no project benchmark, browse the relevant public ranking/tag pages and create a Dynamic Benchmark Card from `references/dynamic-benchmarking.md`. If the user asks for Google Trends, YouTube, TikTok, weird news, or all-source discovery, use the hot-source references above and then convert the selected seed with `trend-theme-router.md`.
3. Read any project-local `女频幻想恋爱知识库/type-packs/{lane}.md`.
4. Read the bundled `references/type-packs/{lane}.md` only as fallback scaffolding.

## Planning Workflow

1. Resolve the numbered format choice and, for push mode, draw the compatible opening card before locking opening beats.
2. Choose the central promise:
   - `婚約破棄 -> ざまぁ -> higher-status love`
   - `悪役令嬢 -> fate avoidance -> sincere romance`
   - `family coldness -> public proof -> rescue and self-worth`
   - `聖女 replacement -> hidden power -> reversal`
   - `契約婚 -> daily care -> mutual devotion`
   - `追放 / frontier -> slow life -> competence and beloved place`
   - `loop -> tragedy prevention -> chosen happiness`
   - `craft/job false evaluation -> product proof -> respected work and love`
   - `palace/family/inheritance wound -> record proof -> chosen family`
   - `monster/demon/dragon marriage -> culture rule -> accepted bond`
   - `strong heroine/status gap -> action proof -> honored love`
   - `hot trend / video / news seed -> emotion or social rule -> josei fantasy proof and romance route`
   - After choosing a subtype, follow the benchmark priority above. Use the bundled type pack only to fill gaps after dynamic/project benchmarks are loaded.
3. Design the heroine's wound and agency:
   - Give her a 2-6 character everyday name. If rank requires a house name, keep the two-part full name at 10 characters or fewer and use the short given name in narration.
   - What was taken from her: reputation, fiance, inheritance, magic credit, family love, public trust.
   - What she can do: knowledge, etiquette, healing, territory work, magic, negotiation, cooking, record keeping, courage.
   - What she refuses to lose again.
4. Design the male lead as a romance engine:
   - Rank or social force: prince, duke, frontier count, knight captain, cursed emperor, mage, black knight.
   - First value to the heroine: safety, fair evaluation, legal shelter, practical partnership, emotional respect.
   - Private vulnerability and public choosing scene.
5. Build a clean antagonist system:
   - Antagonists should expose themselves through greed, lies, abuse, class arrogance, stolen credit, or political overreach.
   - Ensure the punishment follows social/legal logic, not author fiat.
   - For every planned episode, record `romance/social promise -> pressure -> heroine choice -> proof/recognition -> cost -> state delta -> next pressure`. The state delta must change evidence, reputation, safety, legal/family position, resources, relationship trust, or the heroine's available choices. Do not let two adjacent episodes repeat the same humiliation without a new consequence or counter-move.
6. Set the project scale before making outlines:
   - Default for YouTube/push/episode-like serials: short-season novel, fixed 6 episodes/chapters.
   - Keep short-season outlines at exactly 6 episodes/chapters.
   - Keep the prose and files novel-style (`细纲_第XXX章.md`, episode folders, tracking files); do not switch to screenplay format.
   - Do not plan a hundred-chapter roadmap unless the user explicitly asks for a long webnovel.
7. If the task is project-bound, materialize the plan into the common project files:
   - Create or update `设定/题材定位.md`, heroine/male-lead/antagonist `设定/角色/` files, faction/house files, and reusable court/church/world files.
   - Create `大纲/大纲.md`, `大纲/卷纲_第X卷.md`, and the first rolling batch of `大纲/细纲_第XXX章.md`.
   - Create or update `追踪/伏笔.md`, `追踪/时间线.md`, `追踪/角色状态.md`, and `追踪/上下文.md`.
   - Run the `女频幻想恋爱知识库` ledger check before finalizing a wound-romance-reversal engine, then add a compact record after generation.
8. Output a usable package:
   - Japanese title candidates, tag cluster, one-line hook, heroine, male lead, antagonists, world rules, romance progression, zamaa progression, first 5-10 chapter beats, terminology map, banned leakage list.

## Output Rules

- Keep the structure readable in Chinese unless the user requests Japanese planning notes.
- Use Japanese genre labels and terms for titles/tags.
- For trend-driven concept batches, include source mode, seed, selected josei route, backup route, heroine-empathy score, converted proof/romance mechanism, safety transform, and why the seed works for Japanese female-audience fantasy romance.
- Do not stack all 30 themes into one story. Pick 3-5 primary tags and 1-2 secondary flavors.
- Do not leave a project-bound plan only in chat when the user expects a reusable writing project; write the corresponding `设定/`, `大纲/`, and `追踪/` artifacts.
- If the user asks to write next, hand off to `$jp-josei-fantasy-write` with the tag cluster, heroine wound, romance ladder, and chapter beats.
