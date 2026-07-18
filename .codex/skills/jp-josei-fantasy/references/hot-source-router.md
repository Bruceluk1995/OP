# Josei Fantasy Progressive Topic Gate

Use this immediately after the user selects the Japanese female-fantasy romance lane but has not supplied a concrete premise. Lock one broad story category, then one Japanese-site subgenre from `theme-taxonomy.md`, and only then ask where the story should come from. Run all three layers before asking presentation mode, viewpoint, operation, or length.

## Level 1: Broad Story Category

Present only this menu first:

1. 婚约破弃、追放与ざまぁ
2. 恶役令嬢、乙女游戏与重新来过
3. 圣女、魔女与职业女主
4. 契约结婚、溺爱与身份差恋爱
5. 边境、领地经营与慢生活
6. 王宫、家庭与异类／特殊关系

Pause for one category choice. Do not browse, show the creation-entry menu, or generate premises yet.

## Level 2: Story Subgenre

After the broad category is locked, read `theme-taxonomy.md` and present only that category's numbered subgenre menu. Ask for one primary subgenre and allow at most two secondary flavors. Do not browse or generate premises yet.

After the subgenre is locked, return here with normalized `broad_category` and `subgenre` state.

## Level 3: Creation Entry

Only after both category and subgenre are locked, present this menu exactly:

> 先选故事从哪里出发：
> 1. 搜索过去24小时热点或日本小说榜单，再转译成原创日式女频幻想恋爱设定
> 2. 从经典热门题材中选择
> 3. 找更冷门、更怪或更新鲜的方向
> 4. 输入自己的题材或关键词
> 5. 由 Codex 按口播传播性自动推荐
>
> 请回复数字。

At this third layer only, accept legacy `6` as `2` for users continuing from the former evergreen menu. Do not display the legacy mapping.

## Route 1: Live Hot-Topic or Novel-Ranking Conversion

Present this source menu before browsing:

1. Google Trends JP（过去24小时）
2. YouTube／TikTok Japan 热门视频与机制（过去24小时）
3. 日本女性向け小说24小时榜／实时标签页
4. 日本离谱新闻／社会热点（过去24小时）
5. 中国女频小说站24小时榜／实时分类趋势（只取情绪与关系机制）
6. 过去24小时全源综合搜索
7. 用户提供链接或关键词

Then:

- Search and convert signals only inside the locked broad category and subgenre. A selected `边境、领地经营与慢生活 -> 領地経営・村づくり・農園` cannot return a palace-trial or shop-only premise merely because that signal ranks higher.
- At search start, record `searched_at_jst` and `window_start_jst=searched_at_jst-24h`. A source item qualifies only when its publication/upload time, active-trend time, or ranking snapshot is verifiably inside that rolling window.
- Use Google Trends `Past 24 hours`; news must be published inside the window; YouTube/TikTok items must be uploaded or explicitly active/trending inside it; novel sites must use realtime/daily/24-hour ranking snapshots captured inside it. Weekly/monthly/all-time charts, old surveys/reports, undated items, and pages merely crawled today do not qualify.
- Browse live sources; do not answer from a bundled snapshot alone. If a source cannot expose a qualifying timestamp or 24-hour view, exclude it rather than widening the window.
- Collect 6-10 verified raw items when available and present 3-5 viable numbered candidates. If the strict window produces fewer, return fewer and state the shortage; never pad with older material.
- For each candidate, include source market, direct source, publication/activity time, `searched_at_jst`, source seed, locked category/subgenre, heroine wound or desire, proof/romance mechanism, Japan cross-check status, title hook, payoff, and safety transform.
- Treat source choice and seed choice as separate decisions. Pause for the user's numbered seed choice unless the user explicitly delegates with `你选`, `自动选`, or equivalent.
- For source option 5, read `chinese-novel-inspiration.md`. Keep it labeled as cross-market inspiration and require a same-window Japanese cross-check before claiming Japanese-market fit.
- After the seed is selected, propose up to three original premise variants inside the locked category.

### All-Source Mode

For source option 6, collect small batches from available sources:

- 5-10 Google Trends JP seeds verified in its past-24-hours view.
- 3-5 YouTube/TikTok hook mechanics with qualifying upload/activity times.
- 3-5 women-oriented Japanese realtime/daily/24-hour ranking/tag signals.
- 5-8 weird/social-news seeds published inside the window.
- 3-5 Chinese women-oriented realtime/daily/24-hour ranking/category mechanisms when public pages are accessible, labeled as cross-market inspiration.

Score all candidates together and return only candidates that still belong to the locked category.

## Route 2: Classic Popular Subgenres

Use the already locked subgenre; do not repeat either the broad-category or subgenre screen. Generate exactly three original premise candidates inside it. Make them different in heroine position, relationship pressure, proof or recognition mechanism, and emotional payoff. Add every displayed premise to presented-topic history, then pause for a numbered choice.

This stable taxonomy does not require live browsing. Switch to Route 1 only when the user asks for current rankings, current tag heat, dates, or live market proof.

## Route 3: Fresh or Strange Directions

Generate exactly five compact candidates inside the locked broad category and subgenre. Favor underused relationship structures, unfamiliar practical roles, inverted heroine positions, unusual social rules, or contemporary Japanese anxieties. Give each candidate a one-line appeal and one-line risk. Do not drift into another subgenre merely to appear novel.

## Route 4: User Keywords

Ask for one sentence or several keywords. Combine them with the locked broad category and subgenre and convert them into up to three compact premise variants. If the keyword conflicts with either field, ask whether to keep the locked route or switch it instead of silently switching.

## Route 5: Automatic Recommendation

Recommend exactly three candidates inside the locked broad category and subgenre, optimized for oral传播性. State one short reason for each, then ask the user to choose one. This does not silently set `presentation=push`; ask presentation and viewpoint after the premise is fixed.

## Candidate Scoring

For live, fresh, or automatic batches, treat category fidelity as a hard gate, then score the other five dimensions from 1-5:

- Category fidelity (hard gate): the core loop and payoff remain inside the user's locked category.
- Heroine empathy: immediate humiliation, exhaustion, unfairness, loneliness, fear, or desire.
- Romance/zamaa engine: public proof, social consequence, contract reversal, recognition, or earned devotion.
- Japanese female-fantasy fit: institutions and relationship logic feel native to the target market.
- Safety/copy distance: no real-person gossip, tragedy exploitation, copyrighted scenes, creators, songs, or copied plots.
- Title clickability: the Japanese title promises the payoff without knowledge of the source trend.

For scored live candidates, prefer totals of at least 19/25 and heroine empathy of at least 3/5. A category-fidelity failure cannot be compensated by a high score.

## Source-Specific Use

| Source | Best for | Avoid |
|---|---|---|
| YouTube/TikTok | visible before/after proof, POV reversal, apology failure, care, work/family emotion | copying creators, clips, jokes, exact scenes, songs, anime/game IP |
| Google Trends JP | daily-life anxieties, weather, prices, food, health, exams, travel, weddings/events | celebrity/sports names with no female-audience mechanism |
| Japanese ranking/tag pages | current tag combinations, title grammar, visible premise promises | copying characters, scene order, or proprietary summaries |
| Chinese women-oriented novel sites | heroine wounds, relationship pressure, identity reversal, proof objects, pursuit/redemption | treating Chinese popularity as Japanese proof; copying titles, systems, characters, or plot order |
| Weird/social news | unfair rules, hidden fees, public apology failure, school/workplace/family absurdity | crime/tragedy spectacle, private-person details, ongoing lawsuits |

## Interaction Rules

- Keep each screen to at most seven numbered choices.
- Ask for one decision layer at a time. Every route begins `broad category -> Japanese-site subgenre -> creation entry`. Classic continues `original premise candidate`; live continues `24-hour source -> verified seed -> premise variant`.
- Do not repeat choices already fixed in the conversation.
- Use local numbering within each screen and accept free-form keywords at every layer.
- Keep one primary category and one primary subgenre. Allow at most two secondary flavors.
- After a concrete premise is selected, return to upstream intake and ask any still-missing presentation, viewpoint, operation, and length fields in that order.
- Do not lock a title, create an outline, draft prose, save files, or mutate a ledger before the user confirms the concrete premise.

## Hard Rules

- Never turn viral material into disguised real-person gossip or copied short-video content.
- Never use a representative Japanese work as an adaptation target; extract only a category or mechanism signal.
- Never let a louder live signal override the broad category the user selected.
- Never treat `ざまぁ`, `溺愛`, `ハッピーエンド`, or a noble title as a complete premise by itself.
