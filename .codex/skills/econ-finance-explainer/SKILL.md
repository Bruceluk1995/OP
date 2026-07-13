---
name: econ-finance-explainer
description: Economics and finance explainer scripting suite distilled from the local 代数学家89 subtitle corpus, then expanded into longer Shanhe-length analytical videos. Use when the user asks for 经济学讲解, 财经科普, 金融市场/宏观经济/债务/房价/消费/就业/平台经济/行为经济学/投资风险/骗局拆解, YouTube/TikTok/Google Trends/新闻/数据/全源财经热点选题, "普通人为什么赚不到钱", "钱去哪了", "谁在承担成本", or Japanese/English/Chinese economics narration optimized for Japan, US, Europe, or international audiences.
metadata: {"openclaw":{"source":"https://github.com/worldwonderer/oh-story-claudecode"}}
---

# Econ Finance Explainer

## 数字交互契约

- 凡需用户在有限选项中决定，必须在普通对话中列出数字编号，并以“请只回复数字；可多选时用 +，如 1+3”收尾。
- 禁止用开放式问题代替可枚举选项；禁止依赖 AskUserQuestion、request_user_input 或自由文本选项完成有限选择。
- “自定义 / 其他 / 提供素材”也必须编为数字选项。用户选中后，下一轮只索取一个必要内容（如关键词、书名、路径、链接或正文）；这类实际内容不强行数字化。
- 是非确认统一写成 1. 是 / 2. 否，并要求只回复数字。

Create long-form economics and finance explainers that make abstract mechanisms feel concrete. The voice can borrow the source corpus's strength: everyday scenes, fictionalized markets, sharp analogies, and "ordinary people pay the bill" framing. The output length and reasoning depth should follow the Shanhe-style explainer workflow, not the short source subtitles.

Before topic, hotspot, title, or angle work, read `../story/references/global-topic-history.md`, check the shared project ledger, and register every displayed candidate. A news event or mechanism already used by any fiction or explainer skill is burned across domains by default.

## Source Signal

This skill was distilled from the local subtitle corpus at `C:\Users\Administrator\Desktop\36116130_代数学家89`:

- 168 subtitle files total.
- 38 Chinese originals, plus Japanese, English, Spanish, Portuguese, and Arabic translations.
- Main folders: `社会经济学` and `马政经济学`.
- Cleaned Chinese originals average under 1,100 characters, with the longest around 1,300-1,400 characters depending on subtitle cleanup.

Use the corpus as a style and explanation benchmark, not a length benchmark. The reusable signal is:

- translate a financial mechanism into a small-town, workplace, family, platform, or fictional-market scene;
- make the ordinary person's decision pressure visible;
- reveal who captures the upside and who absorbs the downside;
- end with a clean rule, not a generic lecture.

Do not copy recurring names, exact story shells, or source phrasing. Create fresh analogies unless the user explicitly provides a fictional frame.

## Workflow

1. Run audience-first intake when the audience is missing:
   - Before topic, language, or length, display: `1. 日本`、`2. 美国`、`3. 欧洲`、`4. 中国/中文受众`、`5. 其他/国际受众`; require a numeric reply. Option 5 may request the region in the next turn.
   - Treat language and audience as separate fields. English does not automatically mean United States; Japanese does not automatically mean Japan if the user says otherwise.
2. Present the new-user state as a numbered menu:
   - `1. 还没有题目，帮我找财经选题`
   - `2. 已有关键词/热点，帮我转成标题`
   - `3. 已有标题/题目，帮我做因果链大纲`
   - `4. 已准备好，直接写完整讲解稿`
   - `5. 有视频/字幕素材，先拆风格与选题模式`
   Require a numeric reply.
3. For any writing task, read:
   - `references/style-patterns.md`
   - `references/structure-template.md`
   - `references/localization.md`
   - `references/fact-checking.md`
   - `references/anti-homogenization.md`
   - `references/hot-source-router.md` when the user has no topic, wants 热点选题, asks for YouTube/TikTok/Google Trends/news/data/all-source selection, or rejects the current source as boring.
   - `references/trend-benchmarking.md` when the user wants hot/current/platform-fit topics or title generation from trends.
4. Select one topic pack:
   - Household money, consumption, debt traps, education, career choice, sunk cost -> `references/topic-packs/household-money.md`
   - Macro, inflation, interest rates, exchange rates, central banks, recession -> `references/topic-packs/macro-money-policy.md`
   - Stocks, IPOs, funds, real estate finance, securitization, leverage, derivatives -> `references/topic-packs/markets-risk.md`
   - Government debt, local finance, infrastructure, tax, pensions, public services -> `references/topic-packs/public-finance-debt.md`
   - Platform economy, AI, labor, monopoly, pricing power, gig work -> `references/topic-packs/platform-labor-capital.md`
   - Gambling, scams, insurance, consumer finance, behavioral economics -> `references/topic-packs/behavioral-risk-scams.md`
5. Select one audience pack:
   - Japanese audience or Japanese narration -> `references/audience-packs/japan.md`
   - American audience or US-oriented English narration -> `references/audience-packs/united-states.md`
   - European audience or EU/UK-oriented English narration -> `references/audience-packs/europe.md`
   - Chinese-speaking audience -> use `references/localization.md` and keep examples domestic or generic unless the user says otherwise.
6. If the topic involves current prices, interest rates, jobs, inflation, stocks, funds, crypto, real estate, regulation, tax, pensions, or public finance, verify with current reliable sources before writing. Do not invent figures, rankings, rates, dates, or policy details.
   - Build a compact claim ledger before prose: `claim | fact/inference | source/date/market | confidence | strongest counterexample`. Separate nominal from real values, stock from flow, correlation from mechanism, and household examples from population claims.
   - Stress-test the thesis against the strongest rival explanation and identify who would falsify the story: a different time window, country, income group, policy regime, or denominator. Do not hide material uncertainty for a cleaner ending.
7. For trend-driven angle/title batches:
   - If the source is missing, ask the source menu from `references/hot-source-router.md`.
   - If the user chooses 全选, collect from multiple source types and score candidates together.
   - Prefer YouTube/TikTok when the user wants ordinary-life hooks, scams, platform work, creator economy, or consumer traps. Prefer official data and finance news when the topic needs current rates, prices, policy, market, or regulatory facts.
8. Before proposing a new angle or full script, check the ledger if present:
   - `python .codex/skills/econ-finance-explainer/scripts/ledger.py --root . summary`
   - `python .codex/skills/econ-finance-explainer/scripts/ledger.py --root . check ...`
9. After delivering a concept, outline, or script, append a ledger record unless the user says not to.

## Output Defaults

- Default language: follow the user's request. If not specified in this project, ask once; if the user says "你决定", use Japanese for Japan, English for US/Europe, and Chinese for Chinese-speaking audiences.
- Default full-script length:
  - Japanese: target at least 15,000 characters for a complete episode; 12,000-16,000 is acceptable only when the user explicitly asks for a tighter version.
  - English: target 3,500-5,000 words for a complete episode; 1,800-2,800 words only when the user asks for a short version.
  - Chinese: target at least 15,000 Chinese characters for a complete episode; 5,000-9,000 characters only when the user asks for a short version.
- The 代数学家89 corpus is short; do not let it shrink the output. Expand by adding real mechanisms, comparisons, scenes, counterarguments, and verified evidence, not filler.
- Treat the 15,000-character target as functional density, not padding permission. Add cash-flow turns, contract details, household choices, institutional tradeoffs, comparisons, and consequences; do not add empty adjectives or repeated moral commentary.
- Keep line breaks TTS-friendly: one idea, beat, or punchline per line.
- For Japanese-audience title batches, default to Chinese + Japanese bilingual titles. The operator is usually Chinese and needs a Chinese working title to judge direction.
- For finance topics, include a short note distinguishing educational explanation from investment advice when the output could be read as advice.

## Hard Rules

- Do not give personalized investment, tax, legal, medical, or debt advice. Explain mechanisms and risks; tell the user to consult qualified professionals for decisions.
- Do not fabricate current data, asset prices, yields, policy rates, inflation rates, stock performance, or regulations.
- Do not recommend buying, selling, holding, shorting, leveraging, or timing a specific asset unless the user explicitly asks for a general educational framework; even then, avoid actionable trade calls.
- Do not default to China-specific finance unless the user asks for it. Match the audience's market and institutions.
- Do not copy SpongeBob/Bikini Bottom style names or exact source setups by default. Use original fictional shells such as a coastal town, shopping street, school, factory, platform, or family budget.
- Do not pad with generic "background." Every segment must reveal a mechanism, contradiction, incentive, cost transfer, or reader-useful rule.
- Do not make all episodes about "the rich harvest the poor." Keep the critique specific: pricing power, information asymmetry, leverage, regulation, market cycle, labor bargaining, or behavioral bias.

## Deliverable Shape

For a full script, provide:

1. Title options. For Japanese-audience projects, provide Chinese + Japanese bilingual title pairs unless the user asks for Japanese-only.
2. One-line thesis.
3. Selected topic pack and audience pack.
4. Beat outline.
5. Final narration script.
6. Character/word count.
7. Fact-check sources and risk note.
8. Ledger status: checked/recorded or why skipped.

For title/angle work, provide:

1. Chinese working title.
2. Target-language publish title.
3. Trend seed, evergreen seed, or user keyword.
4. Hot source mode and source type when trend-driven.
5. Promised economic mechanism.
6. Audience-specific hook.
7. Risk/fact-check note.
