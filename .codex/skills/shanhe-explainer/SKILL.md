---
name: shanhe-explainer
description: World-history, Japan-focused history/society, geopolitics, science, economics, and social-institution short-video explainer scripting distilled from a Shanhe-style Bilibili subtitle corpus, then adapted for Japanese, American, or European audiences. Use when the user asks for 山河有声风格, 日本史/日本社会讲解, 世界史讲解, 外国史, 国际战略杂谈, 科普短视频, 社会制度/经济常识讲解, YouTube/TikTok/Google Trends/新闻/全源热点选题, "为什么/为何/到底/怎么" analytical scripts, or Japanese/English narration optimized for non-Chinese audiences.
metadata: {"openclaw":{"source":"https://github.com/worldwonderer/oh-story-claudecode"}}
---

# Shanhe Explainer

Create sharp analytical explainer scripts for Japan-focused history/society, world history, geopolitics, strategy, science, economics, and social common-sense topics. The target is not textbook chronology; it is a short-video argument: a strong question, a vivid hook, layered causal reasoning, dry humor, and a clean final judgment.

Before topic, hotspot, title, or angle work, read `../story/references/global-topic-history.md`, check the shared project ledger, and register every displayed candidate. A news event or mechanism already used by any fiction or explainer skill is burned across domains by default.

## Source Signal

This skill was distilled from the local subtitle corpus at `C:\Users\Administrator\Desktop\新建文件夹 (3)`:

- 383 subtitle files total.
- 73 Chinese originals.
- 62 each for Japanese, English, Spanish, Portuguese, and Arabic.
- Main reusable signal: question framing, causal-chain explanation, institutional logic, dry punchlines, and strong final judgments.

Use the corpus as a structural benchmark, not as a topic menu. The source channel includes many Chinese-history examples, but this project does **not** need Chinese history by default. For Japanese audiences, include Japan-focused history, society, economy, institutions, and geopolitics as a first-class lane. Otherwise route toward world history, foreign history, geopolitics, science, economics, and social institutions unless the user explicitly asks for Chinese history.

## Workflow

1. Run audience-first intake when the audience is missing:
   - Ask "观众主要在哪里？" before asking output type, topic lane, title, or length.
   - Offer compact choices: Japan, United States, Europe, or Other/international.
   - Treat language and audience as separate fields. "English" does not automatically mean United States; "Japanese" does not automatically mean Japan if the user says otherwise.
   - Skip this question only when the user has already stated the target audience clearly.
2. Ask the new-user state in plain language, not internal workflow terms:
   - **No topic yet**: find video-worthy angles from trends or evergreen topics.
   - **Has keyword/hot event**: convert it into explainer titles.
   - **Has a title/topic**: build a causal-chain outline.
   - **Ready to write**: draft the complete narration in Chinese, Japanese, or English.
   - **Has video/subtitle material**: distill reusable style and topic patterns.
3. Identify the task from that answer:
   - No topic yet -> angle/title batch; ask trend scouting vs evergreen topic design.
   - Has keyword/hot event -> ask for seed keywords, then convert to title options.
   - Has a title/topic -> outline.
   - Ready to write -> full script.
   - Has video/subtitle material -> corpus distillation.
4. If a new corpus path is provided, run `scripts/profile_corpus.py` first and inspect the summary.
5. For any writing task, read:
   - `references/style-patterns.md`
   - `references/structure-template.md`
   - `references/localization.md`
   - `references/anti-homogenization.md`
   - `references/hot-source-router.md` when the user has no topic, wants 热点选题, asks for YouTube/TikTok/Google Trends/news/all-source selection, or rejects the current source as boring.
   - `references/trend-benchmarking.md` when the user wants hot/current/platform-fit topics or selected angle/title generation from trends.
6. Select one topic pack before outlining:
   - Japan-focused history, society, economy, institutions, postwar order, aging, energy, or island geopolitics -> `references/topic-packs/japan-history-society.md`
   - World history, empire, revolution, succession, war turning points -> `references/topic-packs/world-history.md`
   - Geopolitics, sea power, land power, alliances, sanctions, global order -> `references/topic-packs/geopolitics-strategy.md`
   - Institutions, tax, money, state capacity, trade, finance, bureaucracy -> `references/topic-packs/institutions-economy-power.md`
   - Science, technology, civilization, climate, AI, math, infrastructure -> `references/topic-packs/science-technology.md`
   - Social common sense, work, law, public systems, everyday incentives -> `references/topic-packs/social-common-sense.md`
7. Select one audience pack before writing:
   - Japanese audience or Japanese narration -> `references/audience-packs/japan.md`
   - American audience or US-oriented English narration -> `references/audience-packs/united-states.md`
   - European audience or Europe-oriented English narration -> `references/audience-packs/europe.md`
   - If the user specifies language but not audience in an interactive chat, ask the audience question first.
   - If the user explicitly says "你自己决定" or the workflow is noninteractive, use Japan for Japanese and United States for English unless the topic is clearly European.
8. For trend-driven angle/title batches:
   - If the user has not selected a source, ask the hotspot source menu from `references/hot-source-router.md`.
   - If the user chooses 全选, collect from multiple source types and score candidates together before applying the selected topic lane.
   - Prefer YouTube/TikTok when the user wants short-video hooks, public reactions, or a stronger first 30 seconds. Prefer official/data/report sources when the topic is policy, demographics, energy, economics, health, public systems, or geopolitics.
   - Use Google Trends JP for Japanese audiences unless the user provides another market.
   - Treat trend source scope and topic lane as separate gates. "All categories" only broadens trend collection; it must not broaden the already selected topic lane.
   - Apply the selected topic pack as a hard filter before converting trends into titles.
   - If the user selected Japan-focused history/society/institutions, keep only trends that can directly become Japan-local history, society, economy, institutions, public systems, work/education, disaster governance, energy, demographics, local finance, or island-state questions.
   - Reject overseas sports, foreign celebrity, match schedule, and transfer-news trends unless the user selected a sports/media/social-common-sense lane or explicitly asks to broaden.
   - If not enough trend seeds pass the selected-lane filter, report the shortage and ask whether to broaden the lane, switch to evergreen topics, or output fewer titles.
   - Convert search trends into durable explanatory questions. Do not simply restate celebrity, sports, or breaking-news queries.
   - Prefer trend seeds that can be reframed through Japan-focused society, world history, geopolitics, institutions/economy, science/technology, or social common sense.
9. If the topic involves current politics, finance, public health, or fast-changing facts, verify with current reliable sources before writing. Do not invent numbers, dates, laws, quotes, or market claims.
   - Build a compact claim ledger before prose: `claim | fact/inference | source/date/jurisdiction | confidence | strongest counterexample`. Every major causal link needs either direct evidence or an explicit inference label.
   - Stress-test the thesis with the strongest plausible rival explanation. Keep it in the final script when it materially changes the conclusion; otherwise note why the chosen mechanism explains more of the evidence.
10. Before proposing a new angle or full script, check the project ledger if present:
   - `python .codex/skills/shanhe-explainer/scripts/ledger.py --root . summary`
   - `python .codex/skills/shanhe-explainer/scripts/ledger.py --root . check ...`
11. After delivering a concept, outline, or script, append a ledger record unless the user says not to.

## Output Defaults

- Default language: follow the user's request. If not specified, use Japanese for this project.
- Default audience: ask the user first in interactive use. Only default to Japanese for Japanese scripts or American for English scripts when the user asks the agent to decide or when the task is noninteractive.
- Default title-batch display for Japanese-audience projects: Chinese + Japanese bilingual. The operator is usually Chinese and needs a Chinese working title/meaning to judge direction; the Japanese title is the publish-facing version.
- Default full-script length:
  - Japanese: target at least 15,000 characters for a complete episode; 12,000-16,000 is acceptable only when the user explicitly asks for a tighter version.
  - English: target 3,500-5,000 words for a complete episode; 1,800-2,800 words only when the user asks for a short version.
  - Chinese: target at least 15,000 Chinese characters for a complete episode; 5,000-9,000 characters only when the user asks for a short version.
- Treat the 15,000-character target as functional density, not padding permission. Add mechanisms, comparisons, scenes, evidence, consequences, and reversals; do not add generic background or repeated adjectives.
- For complete episodes, follow the 15,000-character rhythm in `references/structure-template.md`: 14-18 meaningful beats, with a new mechanism, proof, comparison, cost-transfer point, or consequence every 700-1,000 Japanese/Chinese characters.
- Keep line breaks TTS-friendly: one idea or one punchline per line.
- Do not include visible section headings inside the final narration unless the user asks for an outline or production script.

## Hard Rules

- Do not write an encyclopedia entry. Every segment must answer the central question.
- Do not make a bland balanced essay. Use a defensible thesis and then test it.
- Do not imitate exact recurring phrasing or copy source subtitles. Preserve structure and rhetorical function only.
- Do not default to Chinese dynastic history. Treat Chinese-history corpus material as style training only unless the user explicitly asks for that subject.
- If the audience is Japan, do not hide Japan inside "world history" only. Offer Japan-focused topics as a dedicated lane.
- Never override a previously selected topic lane because the trend feed is noisy. The selected lane is the contract.
- Do not use jokes that obscure the argument. Humor should sharpen the logic.
- Do not pad with generic background. If a paragraph can be removed without weakening the causal chain, delete it.
- If writing in Japanese or English, localize the rhetoric instead of translating Chinese idioms literally.

## Deliverable Shape

For a full script, provide:

1. Title options. For Japanese-audience projects, provide Chinese + Japanese bilingual title pairs unless the user explicitly asks for Japanese-only.
2. One-line thesis.
3. Selected topic pack and audience pack.
4. Beat outline.
5. Final narration script.
6. Character/word count.
7. Fact-check sources, date scope, inference/risk note, and unresolved uncertainty.
8. Ledger status: checked/recorded or why skipped.

For only title/angle work, provide:

1. Chinese working title.
2. Japanese publish title.
3. Trend seed or evergreen seed.
4. Hot source mode and source type when trend-driven.
5. Short Chinese note on the promised argument.
6. Risk/fact-check note if needed.
