---
name: story
description: "内容创作工具箱总入口。根据用户需求自动路由到对应 skill；当用户是新用户、刚装 skills、不知道用哪个 skill、意图不明确、只说想写内容/写小说/做视频/找选题时触发。分发到网文长短篇、日式男频异世界、女频幻想恋爱、银发文学、山河式讲解、财经讲解、扫榜/拆文/去AI味/封面/导入/审查/环境部署。触发方式：/story、$story、/网文、「我想写小说」「帮我写书」「写网文」「做讲解视频」「刚装好怎么用」「检查更新」「有新版本吗」。"
metadata: {"openclaw":{"source":"https://github.com/worldwonderer/oh-story-claudecode"}}
---
# story：内容创作工具箱路由

你是整个内容创作工具箱的路由入口。用户的请求模糊时由你分发到具体 skill。不要在用户选择前预设他要写男频异世界、女频、银发、讲解稿或传统网文。

## 新用户总入口

当用户说自己是新用户、刚装好 skills、想从零开始、只说“我要做内容/写作品/写视频/写小说”，或没有明确点名具体 skill 时，先问一级大类：

```text
你想先做哪类内容？

1. 小说/网文创作
2. 视频讲解稿/知识科普
3. 拆文/对标/扫榜/热点选题
4. 已有作品处理：导入、续写、审查、去AI味、封面
5. 环境部署/检查更新/不知道怎么用

请回复数字。
```

用户选择后再进入二级路由：

- 选 `1 小说/网文创作`：继续问题材方向：`1 日式男频异世界`、`2 日本女频幻想恋爱`、`3 银发文学/熟年逆转`、`4 通用网文`、`5 还不确定，帮我推荐`。
- 选 `2 视频讲解稿/知识科普`：继续问讲解方向：`1 山河式历史/社会/制度/国际杂谈`、`2 财经/经济学/金融/普通人钱的问题`。
- 选 `3 拆文/对标/扫榜/热点选题`：继续问长篇、短篇、男频异世界、女频幻想恋爱、银发文学、讲解稿热点，或 Google Trends JP。
- 选 `4 已有作品处理`：根据用户动作路由到导入、续写、审查、去AI味、封面。
- 选 `5 环境/更新`：路由到 `$story-setup` 或版本更新检查。

只在用户明确选择或语义已经足够明确后，才进入 `$jp-isekai`、`$jp-isekai-oneshot`、`$jp-josei-fantasy`、`$silver-literature`、`$shanhe-explainer`、`$econ-finance-explainer` 等具体 skill。

## 路由表

> Codex CLI 中优先使用 `$story-*` 或 `/skills` 触发；Claude Code / OpenCode 继续使用 `/story-*`；OpenClaw 可用 `/skill story-*` 或自然语言点名 skill。下表以 slash command 展示，Codex 可将 `/story-long-write` 等价替换为 `$story-long-write`，OpenClaw 可将其等价替换为 `/skill story-long-write`。

| 用户意图 | 关键词示例 | 路由到 |
|---|---|---|
| 写长篇 | 开书、写大纲、长篇、连载 | `/story-long-write` |
| 短季分集小说 | 短季、分集、每集、6集、油管朗读连载 | `/story-long-write`（短季模式：固定首季 6 集） |
| 写短篇 | 短篇、盐言、一万字 | `/story-short-write` |
| 日式男频异世界 | 男频异世界、なろう系、RPG、打怪升级、龙傲天 | `$jp-isekai` |
| 男频异世界短篇 | 男频异世界短篇、一发完结、15000字单篇、不是6集 | `$jp-isekai-oneshot` |
| 日本女频幻想恋爱 | 女频幻想恋爱、悪役令嬢、婚約破棄、溺愛、ざまぁ | `$jp-josei-fantasy` |
| 女频幻想恋爱短篇 | 女频幻想恋爱短篇、一发完结、15000字单篇、不是6集 | `$jp-josei-fantasy-oneshot` |
| 银发文学 | 银发、熟年、介护、遗产、退休金、老后逆转 | `$silver-literature` |
| 山河式讲解 | 山河有声、世界史、日本社会、制度、国际战略、科学杂谈 | `$shanhe-explainer` |
| 财经经济学讲解 | 财经、经济学、金融、房价、债务、就业、普通人赚钱 | `$econ-finance-explainer` |
| 长篇拆文 | 拆文、分析这本书、黄金三章 | `/story-long-analyze` |
| 短篇拆文 | 拆短篇、分析这个故事 | `/story-short-analyze` |
| 长篇扫榜 | 长篇排行、什么火、起点/番茄/晋江 | `/story-long-scan` |
| 选题决策 | 写什么能爆、帮我选题、选题方向 | `/story-long-scan` |
| 短篇扫榜 | 短篇排行、知乎盐言排行 | `/story-short-scan` |
| 去 AI 味 | 去 AI 味、太 AI、去味 | `/story-deslop` |
| 封面 | 封面、封面图 | `/story-cover` |
| 环境部署 | 准备写书、搭环境、初始化 | `/story-setup` |
| 浏览器操控 | 浏览器、抓取、登录态 | `/browser-cdp` |
| 导入小说 | 导入、反向解析、导入小说、把我的书导进来 | `/story-import` |
| 检查/更新版本 | 检查更新、有新版本吗、升级、更新工具箱 | 见下方「版本更新检查」 |
| 切换/列出书目 | 切书、换书、列出我的书、我在写哪几本、切换项目 | 见下方「多书切换」 |
| 查故事资料 | 查角色、查伏笔、查进度、查设定、什么状态、写到哪了 | spawn `story-explorer` agent（结构化 prompt：`项目目录：{dir}\n查询类型：{根据意图选择}\n查询参数：{用户查询}`）；agent 不可用时见下方「查询降级」 |
| 查资料 | 查资料、帮我查资料、调研、搜索一下、搜一下 | spawn `story-researcher` agent；agent 不可用时见下方「查询降级」 |

## 路由流程

1. 分析用户请求，提取意图关键词
2. 匹配上表，找到对应的 skill
3. 如果能明确匹配，直接调用对应 skill（Claude/OpenCode 可用 `Skill("skill-name")` 或 slash command；Codex 用 `$skill-name` / `/skills`；OpenClaw 用 `/skill skill-name` 或自然语言点名）
4. 如果无法匹配，询问用户想做什么（从上表中选择）
5. 如果用户说"我想写小说"但未指定形态，先走「新用户总入口」的小说二级路由，再询问篇幅/工程类型：长篇连载、短篇单篇、短季分集小说（固定首季 6 集，仍按小说章节文件写，不做几百章规划）、日式男频异世界、女频幻想恋爱、银发文学、通用网文。
6. 如果用户只说"模拟新用户"或"刚装好怎么用"，只展示一级大类，不要直接进入任何具体题材 skill。

### 长正文长度门槛

当用户选择完整正文、YouTube、朗读、推文、或 6 集短季单集正文，且没有另给长度时，路由到具体写作 skill 后默认按 14,500-16,500 日文字符交付。写作 skill 必须在交付前计数；低于 14,500 不算完成，除非用户明确同意较短版本。扩写只能扩真实密集情节：证据、见证、战斗/技能、社会压力、恋爱推进、法律/家庭/金钱/照护后果、下一钩子；不能用风景、情绪、形容词、水回忆补字数。

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
