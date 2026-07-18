# Male-Isekai Progressive Topic Gate

Use this immediately after the user selects the Japanese male-isekai lane but has not supplied a concrete premise. Lock one broad story category, then one Japanese-site subgenre from `japanese-classic-subgenre-map.md`, and only then ask where the story should come from. Run all three layers before asking presentation mode, viewpoint, operation, or length. Guide the user one decision at a time.

## Level 1: Broad Story Category

Present only this menu first:

1. 逆袭与打脸
2. 战斗与升级
3. 开局无敌与势力经营
4. 生产、经营与慢生活
5. 学园、游戏与特殊身份
6. 特殊外挂与高概念

Pause for one category choice. Do not browse, show the creation-entry menu, or generate premises yet.

## Level 2: Story Subgenre

After the broad category is locked, read `japanese-classic-subgenre-map.md` and present only that category's numbered subgenre menu. Ask for one primary subgenre and allow at most two secondary flavors. Do not browse or generate premises yet.

After the subgenre is locked, return here with normalized `broad_category` and `subgenre` state.

## Level 3: Creation Entry

Only after both category and subgenre are locked, present this menu exactly:

> 先选故事从哪里出发：
> 1. 搜索过去24小时热点或小说榜单，再转译成原创日式异世界设定
> 2. 从经典热门题材中选择
> 3. 找更冷门、更怪或更新鲜的方向
> 4. 输入自己的题材或关键词
> 5. 由 Codex 按口播传播性自动推荐
>
> 请回复数字。

Accept legacy controls without displaying them: `0` -> `5`, `40` -> `1`, `39` -> `3`, `38` -> `4`, `37` -> request a two- or three-topic mix after a primary topic is selected.

## Route 1: Rolling-24-Hour Hot-Topic Conversion

When the user selects `1` or legacy `40`, present this source menu before browsing:

1. Google Trends JP（过去24小时）
2. YouTube Japan 热门视频／Shorts（过去24小时）
3. TikTok Japan 热门机制／话题（过去24小时）
4. 日本离谱新闻／社会新闻（过去24小时）
5. 中国男频小说站24小时榜／实时分类趋势（只取机制灵感）
6. 生活热点优先的24小时全源综合搜索（日本趋势 + 新闻 + 社交平台，可选中国小说站）
7. 用户提供链接或关键词

Then:

- Search and convert signals only inside the locked broad category and subgenre. For example, selected `生产、经营与慢生活 -> 農園・開拓・自給自足` cannot return restaurant management or battle leveling merely because that signal is louder.
- At search start, record `searched_at_jst` and `window_start_jst=searched_at_jst-24h`. A source item qualifies only when its publication/upload time, active-trend time, or ranking snapshot is verifiably inside that rolling window.
- Use Google Trends `Past 24 hours`; news must be published inside the window; YouTube/TikTok items must be uploaded or explicitly active/trending inside it; novel sites must use realtime/daily/24-hour ranking snapshots captured inside it. Weekly/monthly/all-time charts, old surveys/reports, undated items, and search pages merely crawled today do not qualify.
- Browse live sources; do not answer from a bundled snapshot alone. If a source cannot expose a qualifying timestamp or 24-hour view, exclude it rather than widening the window.
- Collect 6-10 verified raw items when available and present 3-5 viable numbered candidates. If the strict window produces fewer, return fewer and state the shortage; never pad with older material.
- For each candidate, include source market, direct source, publication/activity time, `searched_at_jst`, raw seed, locked category/subgenre, fantasy conversion, Japan cross-check status, and a short risk note.
- Treat source choice and seed choice as separate decisions. Pause for the user's numbered seed choice unless the user explicitly delegates with `你选`, `自动选`, or equivalent.
- Extract only reusable desires, anxieties, objects, rules, competitions, costs, tools, or social mechanisms. Do not copy creators, copyrighted characters, scenes, scandals, victims, or identifiable private facts.
- For option 5, read `chinese-novel-inspiration.md`. Use only public realtime/daily/24-hour ranking/category/tag signals verified inside the same window. Treat them as cross-market mechanism inspiration, not Japanese-market validation; cross-check the selected mechanism against a same-window Japanese signal before making a Japanese-market-fit claim.
- After the seed is selected, propose up to three compact premise variants and route to `$jp-isekai-plan` or `$jp-isekai-oneshot` according to project shape.

### Lifestyle-First Default

Apply this default to source options 1-4 and 6, especially full-source option 6, unless the user requests another trend domain. Apply it to Chinese novel-site option 5 only when the user asks for daily-life or slow-life mechanisms.

- Prioritize ordinary-life pressures in Japan: wages versus living costs, food and daily-goods prices, rent, utilities, subscriptions and automatic billing, commuting and delivery, workload and AI fatigue, saving behavior, convenience retail, household labor, childcare, caregiving, sleep, practical health concerns, hobbies, dining, and 推し活 spending.
- Use news, official releases, surveys, Google Trends, and social-platform signals only when the individual item is published or active inside the strict 24-hour window. For a full-source pass, prefer 6-10 verified raw signals from at least three source types, but never expand the window to satisfy the quota.
- Do not default to sports results, celebrities, entertainment releases, politics, disasters, crimes, individual tragedies, novelty robots, or bizarre animal news. Weather qualifies only when tied directly to household costs, shopping, work, health, or daily adaptation.
- Convert each signal as `recognizable daily pain -> extreme fantasy rule -> repeatable power or conflict engine -> visible payoff`. Do not merely replace a modern noun with an isekai noun.
- Prefer hooks with a concrete bill, salary, price, time burden, cancellation trap, household imbalance, or work consequence when the source supports it. Keep numbers sourced and dated.
- For first-person push narration, favor premises that can establish the narrator, the daily-life contradiction, and the abnormal rule within 3-6 lines.
- If the user rejects a batch as boring or insufficiently life-based, exclude the rejected mechanisms, rescan within the lifestyle categories above, and return a genuinely new batch without defending the previous choices.

## Route 2: Classic Popular Topics

Use the already locked subgenre; do not repeat either the broad-category or subgenre screen. Generate exactly three original premise candidates within it. Make their protagonist role, repeatable engine, and core payoff meaningfully different. Give each candidate a one-line hook and one-line payoff, obtain the company-wide reservation, add each displayed candidate to presented-topic history, then pause for a numbered choice.

### Ability Economy Rule

- Do not rewrite every classic candidate as `strong ability + mandatory personal price`. Ability cost is optional, not a quality requirement.
- For `生产、经营与慢生活`, default to benefit-first powers that create better products, money, comfort, safety, reputation, territory, or useful scale. Build conflict from demand, rivals, supply, protection, identity, politics, or the next opportunity created by success.
- Across any generated batch, vary power design: free/OP, conditional, skill-based, information-limited, and cost-driven may coexist. A whole batch using backlash, memory/lifespan loss, debt, future repayment, or loss of control is a failed batch and must be rebuilt before display.

### Japanese Novel-Site Subgenre Gate

- The canonical subgenre menus and their maintenance evidence live in `japanese-classic-subgenre-map.md`; do not recreate a smaller improvised list in this file or in chat.
- Treat those labels as recurring premise clusters found on Japanese web-novel sites, not as official platform genres or proof of current popularity.
- Keep classic taxonomy selection offline. Browse only when the user asks for current heat, rankings, dates, market validation, or fresh examples.
- Never use a representative work in the evidence index as an adaptation target. Generate original premises only after the subgenre is fixed.

## Route 3: Fresh or Strange Directions

Generate exactly five compact candidates inside the locked broad category and subgenre. Favor underused combinations, unfamiliar practical occupations, unusual rules or optional costs, inverted skill logic, nonstandard monsters, or contemporary Japanese anxieties. Give each candidate one-line appeal and one-line risk. Do not drift into another subgenre merely to appear novel, and do not repeat the subgenre menu.

## Route 4: User Keywords

Ask for one sentence or several keywords. Combine them with the locked broad category and subgenre and convert them into up to three compact premise variants. If the keyword conflicts with either field, ask whether to keep the locked route or switch it instead of silently switching. Ask only for missing information that would materially change the premise.

## Route 5: Automatic Recommendation

Recommend exactly three candidates inside the locked broad category and subgenre, optimized for oral传播性. State one short reason for each, then ask the user to choose one. This choice optimizes the premise but does not silently set `presentation=push`; ask presentation and viewpoint after the premise is fixed. Do not expose the complete subgenre pool.

## Interaction Rules

- Keep each screen to at most seven numbered choices.
- Ask for one decision layer at a time. Every route begins `broad category -> Japanese-site subgenre -> creation entry`. Classic continues `original premise candidate`; live continues `24-hour source -> verified seed -> premise variant`.
- Do not repeat choices already fixed in the conversation.
- Use local numbering within each screen; do not require users to remember global topic IDs.
- Accept free-form keywords at every layer.
- If more than three topics are selected, warn that the premise may become crowded and reduce them to one primary engine plus at most two secondary flavors.
- After a concrete premise is selected, return to the upstream intake and ask any still-missing presentation, viewpoint, operation, and length fields in that order.
- For multiple presentation modes and multiple topics, confirm which versions share the same premise before drafting full-length outputs.
