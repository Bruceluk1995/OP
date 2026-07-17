# Male-Isekai Progressive Topic Gate

Use this after the user selects presentation mode and viewpoint but has not supplied a concrete premise. Guide the user one decision at a time. Never display the complete topic pool on the first screen.

## Level 1: Creation Entry

Present only this menu:

> 先选故事从哪里出发：
> 1. 搜索实时热点或小说榜单，再转译成原创日式异世界设定
> 2. 从经典热门题材中选择
> 3. 找更冷门、更怪或更新鲜的方向
> 4. 输入自己的题材或关键词
> 0. 由 Codex 按口播传播性自动推荐

Accept legacy controls without displaying them: `40` -> `1`, `39` -> `3`, `38` -> `4`, `37` -> request a two- or three-topic mix after a primary topic is selected.

## Route 1: Live Hot-Topic Conversion

When the user selects `1` or legacy `40`, present this source menu before browsing:

1. Google Trends JP
2. YouTube Japan 热门视频／Shorts
3. TikTok Japan 热门机制／话题
4. 日本离谱新闻／社会新闻
5. 中国男频小说站榜单／分类趋势（只取机制灵感）
6. 生活热点优先的全源综合搜索（日本趋势 + 新闻 + 调查 + 社交平台，可选中国小说站）
7. 用户提供链接或关键词

Then:

- Browse current sources; do not answer from a bundled snapshot alone.
- Collect 6-10 raw items and present 3-5 viable numbered candidates.
- For each candidate, include source market, source, date, raw seed, fantasy conversion, recommended male-isekai lane, Japan cross-check status, and a short risk note.
- Treat source choice and seed choice as separate decisions. Pause for the user's numbered seed choice unless the user explicitly delegates with `你选`, `自动选`, or equivalent.
- Extract only reusable desires, anxieties, objects, rules, competitions, costs, tools, or social mechanisms. Do not copy creators, copyrighted characters, scenes, scandals, victims, or identifiable private facts.
- For option 5, read `chinese-novel-inspiration.md`. Use current public ranking/category/tag/synopsis metadata from at least two Chinese fiction sites when accessible. Treat it as cross-market mechanism inspiration, not Japanese-market validation; cross-check the selected mechanism against a current Japanese signal before making a Japanese-market-fit claim.
- After the seed is selected, propose up to three compact premise variants and route to `$jp-isekai-plan` or `$jp-isekai-oneshot` according to project shape.

### Lifestyle-First Default

Apply this default to source options 1-4 and 6, especially full-source option 6, unless the user requests another trend domain. Apply it to Chinese novel-site option 5 only when the user asks for daily-life or slow-life mechanisms.

- Prioritize ordinary-life pressures in Japan: wages versus living costs, food and daily-goods prices, rent, utilities, subscriptions and automatic billing, commuting and delivery, workload and AI fatigue, saving behavior, convenience retail, household labor, childcare, caregiving, sleep, practical health concerns, hobbies, dining, and 推し活 spending.
- Use current news, official statistics, consumer surveys, Google Trends, and social-platform signals. For a full-source pass, collect 6-10 raw signals from at least three source types before selecting candidates.
- Do not default to sports results, celebrities, entertainment releases, politics, disasters, crimes, individual tragedies, novelty robots, or bizarre animal news. Weather qualifies only when tied directly to household costs, shopping, work, health, or daily adaptation.
- Convert each signal as `recognizable daily pain -> extreme fantasy rule -> repeatable power or conflict engine -> visible payoff`. Do not merely replace a modern noun with an isekai noun.
- Prefer hooks with a concrete bill, salary, price, time burden, cancellation trap, household imbalance, or work consequence when the source supports it. Keep numbers sourced and dated.
- For first-person push narration, favor premises that can establish the narrator, the daily-life contradiction, and the abnormal rule within 3-6 lines.
- If the user rejects a batch as boring or insufficiently life-based, exclude the rejected mechanisms, rescan within the lifestyle categories above, and return a genuinely new batch without defending the previous choices.

## Route 2: Classic Popular Topics

Present only the category menu first:

1. 逆袭与打脸
2. 战斗与升级
3. 开局无敌与势力经营
4. 生产、经营与慢生活
5. 学园、游戏与特殊身份
6. 特殊外挂与高概念

After the user chooses one category, present only that category's six candidates. Allow multi-select inside the category. If the user wants cross-category mixing, first lock one primary engine, then offer at most two secondary flavors.

### Ability Economy Rule

- Do not rewrite every classic candidate as `strong ability + mandatory personal price`. Ability cost is optional, not a quality requirement.
- For `生产、经营与慢生活`, default to benefit-first powers that create better products, money, comfort, safety, reputation, territory, or useful scale. Build conflict from demand, rivals, supply, protection, identity, politics, or the next opportunity created by success.
- Across any generated batch, vary power design: free/OP, conditional, skill-based, information-limited, and cost-driven may coexist. A whole batch using backlash, memory/lifespan loss, debt, future repayment, or loss of control is a failed batch and must be rebuilt before display.

### Topic Pool

#### 逆袭与打脸

1. 被勇者队伍驱逐，隐藏辅助能力曝光
2. 最弱职业／E级技能被严重误判
3. 遭贵族、家族或公会背叛后反击
4. 路人角色掌握原作剧情，避开死亡结局
5. 无能领主接手废土，反超王都
6. 被当成普通人，实际一句话改变战争

#### 战斗与升级

1. 迷宫打怪、掉落装备、连续升级
2. 吞噬魔物获得技能与进化路线
3. 荒野求生，从零打造战斗体系
4. 魔物使／驯兽师组建异种小队
5. 死灵术师、召唤师或军团流
6. 肉盾、防御或辅助职业开发攻击玩法

#### 开局无敌与势力经营

1. 满级角色穿越，隐藏实力游戏人间
2. 转生魔王／不死王，统治地下城
3. 地下城主布置陷阱、经营领地
4. 建立秘密组织，部下不断脑补
5. 收服敌对种族，发展多种族王国
6. 无敌者只想低调，行动却持续改变国家格局

#### 生产、经营与慢生活

1. 炼金术、锻造或附魔垄断高端装备
2. 异世界料理、美食店或流放者食堂
3. 农业、牧场、建村与领地基建
4. 商会、物流、拍卖与现代经营知识
5. 日本与异世界往返，倒卖现代物资
6. 素材采集、鉴定与魔物生态旅行

#### 学园、游戏与特殊身份

1. 魔法学院吊车尾逆袭首席
2. 转生反派贵族，修改必死剧情
3. VRMMO能力带入真实异世界
4. 转生成史莱姆、哥布林、龙或魔剑
5. 时间循环，反复攻略同一场灾难
6. 勇者召唤出错，获得乱码／隐藏职业

#### 特殊外挂与高概念

1. 鉴定眼看穿技能、谎言或价值
2. 无限收纳、复制、合成或分解
3. 每日签到、抽卡或随机奖励系统
4. 诅咒技能反向利用，越受伤越强
5. 现代职业知识变成异世界外挂
6. 治疗术、净化术或生活魔法战斗化

Use `宠物、幼龙或神兽养成进化` as an optional secondary flavor when it fits the chosen primary engine.

## Route 3: Fresh or Strange Directions

Generate exactly five compact candidates. Favor underused combinations, unfamiliar practical occupations, unusual rules or optional costs, inverted skill logic, nonstandard monsters, or contemporary Japanese anxieties. Give each candidate one-line appeal and one-line risk. Do not show the classic topic pool unless the user asks.

## Route 4: User Keywords

Ask for one sentence or several keywords. Convert them into up to three compact premise variants. Ask only for missing information that would materially change the premise.

## Route 0: Automatic Recommendation

Recommend exactly three candidates optimized for the selected presentation mode. State one short reason for each, then ask the user to choose one. Do not expose the complete topic pool.

## Interaction Rules

- Keep each screen to at most seven numbered choices.
- Ask for one decision layer at a time: entry -> source/category -> candidate -> premise variant.
- Do not repeat choices already fixed in the conversation.
- Use local numbering within each screen; do not require users to remember global topic IDs.
- Accept free-form keywords at every layer.
- If more than three topics are selected, warn that the premise may become crowded and reduce them to one primary engine plus at most two secondary flavors.
- For multiple presentation modes and multiple topics, confirm which versions share the same premise before drafting full-length outputs.
