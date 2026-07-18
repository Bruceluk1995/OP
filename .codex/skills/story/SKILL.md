---
name: story
description: "内容创作工具箱总入口。根据用户需求自动路由到对应 skill；当用户是新用户、刚装 skills、不知道用哪个 skill、意图不明确，或要检查/优化整个技能包时触发。分发到网文长短篇、日式男频异世界、女频幻想恋爱、银发文学、山河式讲解、财经讲解、扫榜/拆文/去AI味/封面/导入/审查/环境部署/技能包体检。触发方式：/story、$story、/网文、「我想写小说」「做讲解视频」「刚装好怎么用」「检查更新」「优化 skills」「技能包体检」。"
metadata: {"openclaw":{"source":"https://github.com/worldwonderer/oh-story-claudecode"}}
---
# story：内容创作工具箱路由

Mandatory topic gate: whenever this router or a downstream route may invent,
show, select, or generate a new topic, premise, title, hotspot, evergreen idea,
or episode angle, read `references/global-topic-history.md` and complete its
company-wide online reservation before the candidate may proceed. Local recent
history is never a substitute. If online confirmation is unavailable, stop the
new-topic path instead of silently continuing.

Global content rule: read `references/audience-comprehension-floor.md` before routing or auditing audience-facing creation. Every downstream writing/review skill must prefer ordinary action, visible change, and human consequence over lore, jargon, inventories, titles, or template filling.

Global push rule: every anime-recap/push-narration branch must read `references/push-prompt-architecture.md`, `references/push-entertainment-gate.md`, and `references/push-retention-chain.md`; lock the speaker/listener and audience emotional contracts before prose; complete the adversarial entertainment read and saved-body evidence map before release; and treat surface lint as subtitle-shape evidence only. A strong first line followed by setup, chronology, technical flowchart, function-only characters, or a long post-payoff tail is a blocking failure, even when every line is short.

你是整个内容创作工具箱的路由入口。用户的请求模糊时由你分发到具体 skill。不要在用户选择前预设他要写男频异世界、女频、银发、讲解稿或传统网文。

## 单一工位路由合同

- 一次请求只指定一个主工位；其他 skill 只能作为明确的前置资料或后续交接，不能同时成为最高规则。
- 请求已经给出题材、载体、视角、篇幅和动作时直接路由，不展示菜单，不重复确认。
- 正常创作走快速档：选题/故事核 -> 结构 -> 正文 -> 盲读修改。只有用户要求实时市场、完整工程、拆文、封面或多版本时才加载对应能力。
- “写”“审”“拆”“扫”“去 AI 味”“导入”是不同动作。审稿不擅自改写，扫榜不擅自开写，去 AI 味不掩盖结构失败。
- 路由输出只传递下游真正需要的决定：受众承诺、题材、载体、视角、长度预算、必须保留事实。不要把整个技能包规则塞进一个 prompt。
- 若两项规则冲突，以用户明确目标、读者继续阅读欲望、人物因果和核心兑现优先；格式、文件、计数和自动校验靠后。

菜单回答完成后，必须把本地编号归一化为显式交接状态，再进入下游：

```text
content_form=<long|season|oneshot|...>
lane=<jp_isekai|jp_josei|...>
presentation=<traditional|push>
viewpoint=<first|third>
operation=<new|continue|rewrite|review>
length_budget=<explicit value or skill default>
```

`2a`、`1a`、`3` 等 raw menu code 只在当次菜单中有效，禁止原样传给下游。确认 `presentation=push` 后它是 sticky state：除非用户明确改选，否则任何下游不得重新询问、重新推断、把第一人称解释成传统小说，或让写手再次选择表现分支。上下文丢失且无法恢复时，只补问表现形式，不得默认 traditional。

## 冻结入口链路 v1

这是用户所有的固定产品合同，不是可自由优化的示例。除非用户在当前请求中明确说“修改冻结入口链路”，否则任何 skill 更新、重构、同步或路由优化都不得增删选项、改名、换序、合并或提前进入题材/项目。新增能力只能挂在七个入口之后。

当用户只说“使用剧本 skills”“我要做内容/写作品/写视频/写小说”或没有给出足够形态时，必须原样展示以下一级菜单：

<!-- FIXED_STORY_ROUTER_V1_START -->
```text
你想做哪种内容？

1. 长篇网文／持续连载
2. 短季分集小说／连续剧（默认首季6集）
3. 单篇短篇／一发完结
4. 视频讲解稿／知识科普
5. 已有作品处理：续写、改写、审查、去AI味、封面
6. 拆文／对标／扫榜／热点选题
7. 不确定，帮我选择

请回复数字。
```
<!-- FIXED_STORY_ROUTER_V1_END -->

固定后续顺序：

1. **内容形态**：只能先走上面的七项入口。
2. **题材**：选择 `1/2/3` 后，再问 `1 日式男频异世界`、`2 日本女频幻想恋爱`、`3 银发文学/熟年逆转`、`4 通用网文`、`5 还不确定，帮我推荐`。
3. **表现形式与视角**：题材确定后，再确认传统小说正文或动漫解说/推文口播，以及第一人称或第三人称；用户已经说清时不重复问。
4. **具体动作与长度**：最后确认开新作、续写/改写、审查，以及长度预算；一发完结不得被改成六集连续剧，短季分集不得被改成长篇规划。

分支规则：

- 选 `4 视频讲解稿/知识科普`：继续问 `1 山河式历史/社会/制度/国际杂谈`、`2 财经/经济学/金融/普通人钱的问题`。
- 选 `5 已有作品处理`：按用户动作路由到续写、改写、审查、去 AI 味或封面；没有用户明确的续写/现有作品意图时，不得读取 `.active-book`、追踪文件或旧项目状态。
- 选 `6 拆文/对标/扫榜/热点选题`：继续问长篇、短篇、男频异世界、女频幻想恋爱、银发文学或讲解稿。
- 选 `7 不确定`：只帮助选择内容形态，不得直接生成题材或擅自接入旧项目。
- 用户直接给足内容形态、题材、表现形式、视角和动作时可跳过已回答的问题，但不得改变未回答问题的固定顺序。

只在内容形态与题材都明确后，才进入 `$jp-isekai`、`$jp-isekai-oneshot`、`$jp-josei-fantasy`、`$silver-literature`、`$story-long-write`、`$story-short-write`、`$shanhe-explainer` 或 `$econ-finance-explainer` 等具体 skill。

## 路由表

> Codex CLI 中优先使用 `$story-*` 或 `/skills` 触发；Claude Code / OpenCode 继续使用 `/story-*`；OpenClaw 可用 `/skill story-*` 或自然语言点名 skill。下表以 slash command 展示，Codex 可将 `/story-long-write` 等价替换为 `$story-long-write`，OpenClaw 可将其等价替换为 `/skill story-long-write`。

| 用户意图 | 关键词示例 | 路由到 |
|---|---|---|
| 写长篇 | 开书、写大纲、长篇、连载 | `/story-long-write` |
| 短季分集小说 | 短季、分集、每集、6集、油管朗读连载 | `/story-long-write`（短季模式：固定首季 6 集） |
| 写短篇 | 短篇、盐言、一万字 | `/story-short-write` |
| 日式男频异世界 | 男频异世界、なろう系、RPG、打怪升级、龙傲天 | `$jp-isekai` |
| 男频异世界短篇 | 男频异世界短篇、一发完结、12000字单篇、不是6集 | `$jp-isekai-oneshot` |
| 日本女频幻想恋爱 | 女频幻想恋爱、悪役令嬢、婚約破棄、溺愛、ざまぁ | `$jp-josei-fantasy` |
| 女频幻想恋爱短篇 | 女频幻想恋爱短篇、一发完结、12000字单篇、不是6集 | `$jp-josei-fantasy-oneshot` |
| 日本商业短篇总编辑/救稿 | 男频女频都废了、整条链路重构、作品不好看、留存差、真重写 | `$jp-short-fiction-studio`（再选男频或女频题材包） |
| 银发文学 | 银发、熟年、介护、遗产、退休金、老后逆转 | `$silver-literature` |
| 山河式讲解 | 山河有声、世界史、日本社会、制度、国际战略、科学杂谈 | `$shanhe-explainer` |
| 财经经济学讲解 | 财经、经济学、金融、房价、债务、就业、普通人赚钱 | `$econ-finance-explainer` |
| 长篇拆文 | 长篇拆文、分析这部长篇、黄金三章、多章连载拆解 | `/story-long-analyze` |
| 短篇拆文 | 拆短篇、分析这个故事 | `/story-short-analyze` |
| 长篇扫榜 | 长篇排行、什么火、起点/番茄/晋江 | `/story-long-scan` |
| 选题决策 | 写什么能爆、帮我选题、选题方向 | 先确定长篇/短篇/日式男频/女频/银发/讲解，再进对应 scan/router |
| 短篇扫榜 | 短篇排行、知乎盐言排行 | `/story-short-scan` |
| 去 AI 味 | 去 AI 味、太 AI、去味 | `/story-deslop` |
| 封面 | 封面、封面图 | `/story-cover` |
| 环境部署 | 准备写书、搭环境、初始化 | `/story-setup` |
| Chrome CDP | CDP、复用 Chrome 登录态、提取 token、agent-browser | `/browser-cdp`；普通网页读取优先当前运行时原生浏览器/检索能力 |
| 导入小说 | 导入、反向解析、导入小说、把我的书导进来 | `/story-import` |
| 检查/更新版本 | 检查更新、有新版本吗、升级、更新工具箱 | 见下方「版本更新检查」 |
| 技能包体检/优化 | 优化 skills、检查技能包、skill 健康检查、断链检查 | 见下方「技能包体检」 |
| 切换/列出书目 | 切书、换书、列出我的书、我在写哪几本、切换项目 | 见下方「多书切换」 |
| 查故事资料 | 查角色、查伏笔、查进度、查设定、什么状态、写到哪了 | spawn `story-explorer` agent（结构化 prompt：`项目目录：{dir}\n查询类型：{根据意图选择}\n查询参数：{用户查询}`）；agent 不可用时见下方「查询降级」 |
| 查资料 | 查资料、帮我查资料、调研、搜索一下、搜一下 | spawn `story-researcher` agent；agent 不可用时见下方「查询降级」 |

## 路由流程

1. 分析用户请求，提取意图关键词
2. 按优先级匹配：用户显式点名 skill > 一发完结/非连续剧 > 专门题材路由 > 通用长短篇 > 总入口。不能因为出现“短篇/12000字”就盖掉“男频异世界/女性向幻想恋爱”等更具体题材。
3. 如果能明确匹配，直接调用对应 skill（Claude/OpenCode 可用 `Skill("skill-name")` 或 slash command；Codex 用 `$skill-name` / `/skills`；OpenClaw 用 `/skill skill-name` 或自然语言点名）
4. 如果无法匹配，询问用户想做什么（从上表中选择）
5. 如果用户说“使用剧本 skills”“我想写小说”但未指定形态，原样展示「冻结入口链路 v1」，不得先问题材。
6. 用户选择 `1/2/3` 后严格按“内容形态 -> 题材 -> 表现形式与视角 -> 具体动作与长度”继续；不得读取旧项目来替代任何一层选择。
7. 如果用户只说“模拟新用户”或“刚装好怎么用”，同样只展示冻结的一级菜单，不要直接进入任何具体题材 skill。

### 长正文长度路由

总路由不统一规定所有语言和体裁的长度。日本男频异世界与女频幻想恋爱的完整单篇/完整一集，无指定时统一以约 12,000 日文字符为生产预算；不得靠重复证明、手续、风景或情绪填充。其他语言和体裁遵循各自 skill。任何硬平台限制都需满足并如实报告。

## 查询降级

「查故事资料」「查资料」走 agent 前先做轻量可用性检查（路由只做这一层，不承担全局部署策略）：当前不在子代理上下文、Agent/Task 工具可用、且 `.claude/agents/{story-explorer|story-researcher}.md`、`.opencode/agents/{story-explorer|story-researcher}.md` 或 `.codex/agents/{story-explorer|story-researcher}.toml` 存在 → 可尝试 spawn。任一不满足，或 Codex 运行时返回 `unknown agent_type` / 未暴露 custom-agent registry，则降级，不硬失败：

- `story-explorer` 不可用 → 主线程直接用 Read/Grep 从项目文件检索（角色状态/伏笔/进度/设定），回答前标注 `Fallback: agent unavailable -> direct lookup`；项目尚未部署时提示先 `/story-setup`（Codex 中用 `$story-setup`）。
- `story-researcher` 不可用 → 主线程用现有检索/回答能力完成，或提示用户改用 `/browser-cdp` 采集，同样标注 `Fallback: agent unavailable -> direct lookup`。

## 项目状态感知

路由前先检查当前项目状态：

- **无项目目录**（没有包含 `追踪/` 或 `设定/` 的书名目录）：
  - 如果用户要写作，下一步是先运行 `/story-setup` 初始化环境（Codex 中用 `$story-setup`）
  - 如果用户要扫榜/拆文，直接路由
- **已有项目**：检查 `.story-deployed` 标记，如未部署则先运行 `/story-setup`（Codex 中用 `$story-setup`）

## 多书切换

用户想切换或查看在写的书时（一个项目可同时有多本）：

1. 在项目根查找所有书目录：包含 `追踪/` 或 `设定/` 子目录的目录（含 `长篇/`、`短篇/` 下的子目录）。
2. 列出书名，并标出当前 `.active-book` 指向的那本。
3. 让用户选择，把所选书的相对路径写入项目根 `.active-book`（覆盖原内容）。
4. 只发现一本时直接确认为活跃书，无需询问。

## 版本更新检查

用户问"有没有新版本""检查更新""升级"时执行。**只通知，更不更新由用户定，不自动安装。**

1. **当前版本**：读本 skill 同目录的 `VERSION` 文件；缺失则视为未知。
2. **最新版本**：优先 `gh release view --json tagName,name,url -R worldwonderer/oh-story-claudecode` 取 `tagName`；无 gh 用 `curl -fsS --max-time 5 https://api.github.com/repos/worldwonderer/oh-story-claudecode/releases/latest` 取 `.tag_name`（jq 或 grep）。查不到 → 告知"暂时拉不到最新版本，可手动看 [Releases](https://github.com/worldwonderer/oh-story-claudecode/releases)"，不报错。
3. **比较**：去掉 `v` 前缀按语义版本比（major.minor.patch）。`gh release` 默认取 latest 稳定版，不含 pre-release。
4. **告知**：
   - 已最新 → 「已是最新版 vX.Y.Z」。
   - 有新版 → 列出 当前 vA → 最新 vB + [Releases](https://github.com/worldwonderer/oh-story-claudecode/releases)/[CHANGELOG](https://github.com/worldwonderer/oh-story-claudecode/blob/main/CHANGELOG.md)（能拿到 release notes 就附本次要点），再用 AskUserQuestion 问「现在更新吗？」：
     - 选更新 → 跑 `npx skills add worldwonderer/oh-story-claudecode -y -g`（`-g` 全局，去掉则只更当前目录）；完成后提示：已部署过的项目在项目根重跑 `/story-setup`（Codex 中用 `$story-setup`）同步 hooks/agents/references，并**新开一个会话**让 agents 重新注册。
     - 选先不 → 不动，告知随时可再来。

## 技能包体检

用户要优化、审查或维护整个 skills 包时执行，不把请求误路由成版本更新：

1. 在技能包目录运行 `python scripts/audit_skill_bundle.py`；Windows 控制台乱码时先设置 `PYTHONUTF8=1`。
2. 先修 `ERROR`，再按收益处理 `WARN`。不要为了清零警告删除跨平台兼容字段或业务约束。
3. 对超过 500 行的 `SKILL.md`，优先把模板、长表格和领域细节移入一级 `references/`，主文件只保留触发后的决策流程与不可省略的守卫。
4. 修改后运行 `python scripts/audit_skill_bundle.py --strict`，并逐个运行当前 Codex 的 `quick_validate.py`。
5. 默认只修改 `.codex/skills/`；不碰 `episodes/`、正文、拆文库或其他创作产物。同步用户级 skills、提交 Git 或发布版本必须由用户另行授权。
