# New project — 网文写作工具集（Codex）

## Skill 路由表

Codex CLI 中优先通过 `$skill-name` 或 `/skills` 调用；自然语言也可触发对应 skill。

| 命令/意图 | Skill | 说明 |
|------|-------|------|
| `$story-long-write`、写长篇 | story-long-write | 长篇网文写作（逐章推进） |
| `$story-short-write`、写短篇 | story-short-write | 短篇网文写作（情绪驱动） |
| `$story-long-analyze`、长篇拆文 | story-long-analyze | 长篇小说深度拆解 |
| `$story-short-analyze`、短篇拆文 | story-short-analyze | 短篇小说拆文分析 |
| `$story-long-scan`、长篇扫榜 | story-long-scan | 长篇小说榜单与市场趋势 |
| `$story-short-scan`、短篇扫榜 | story-short-scan | 短篇小说榜单与情绪风口 |
| `$story-deslop`、去 AI 味 | story-deslop | 去除 AI 写作痕迹 |
| `$story-cover`、封面 | story-cover | 生成封面图 |
| `$story-review`、审查 | story-review | 多视角对抗式审查 |
| `$story-import`、导入 | story-import | 逆向导入已有小说到项目结构 |
| `$story`、内容创作、网文 | story | 内容创作工具箱总入口 · 新用户/模糊意图自动分发 |
| `$story-setup`、准备写书 | story-setup | 环境部署 · hooks/agents/AGENTS.md 一键部署 |
| `$jp-isekai`、日式男频异世界 | jp-isekai | 日本男频 RPG 异世界路由，热点选题可参考中国小说站机制 |
| `$jp-isekai-plan`、男频异世界开书 | jp-isekai-plan | 设定、外挂、世界观、章节结构设计，支持中国小说榜单灵感的日式转译 |
| `$jp-isekai-write`、男频异世界正文 | jp-isekai-write | 日式男频异世界正文写作 |
| `$jp-isekai-oneshot`、男频异世界短篇、一发完结 | jp-isekai-oneshot | 14,500-16,500 日文字符的男频异世界单篇短篇，热点灵感可参考中国小说站，不走 6 集连续剧 |
| `$jp-isekai-review`、男频异世界审查 | jp-isekai-review | 检查日式本土化、爽点和中文玄幻泄漏 |
| `$jp-josei-fantasy`、日本女频幻想恋爱 | jp-josei-fantasy | 日本女性向け幻想恋爱路由，支持日本热点及中国女频小说站机制灵感转译 |
| `$jp-josei-fantasy-plan`、女频幻想恋爱开书 | jp-josei-fantasy-plan | 令嬢、婚約破棄、溺愛、ざまぁ等题材设计，支持热点及中国女频榜单灵感的日式重建 |
| `$jp-josei-fantasy-write`、女频幻想恋爱正文 | jp-josei-fantasy-write | 日本女性向け异世界恋爱正文写作 |
| `$jp-josei-fantasy-oneshot`、女频幻想恋爱短篇、一发完结 | jp-josei-fantasy-oneshot | 14,500-16,500 日文字符的女频幻想恋爱单篇短篇，支持热点/视频/新闻及中国女频小说站灵感，不走 6 集连续剧 |
| `$jp-josei-fantasy-review`、女频幻想恋爱审查 | jp-josei-fantasy-review | 检查恋爱爽点、ざまぁ逻辑、日式本土化 |
| `$silver-literature`、银发文学、熟年逆转 | silver-literature | 日本银发/熟年家庭逆转、介护、遗产、晚年再生写作 |
| `$shanhe-explainer`、山河有声、世界史/战略杂谈讲解 | shanhe-explainer | 山河有声式世界史、国际战略、科学与社会制度讲解，支持 YouTube/TikTok/Google Trends/新闻/数据/常青/全源热点选题 |
| `$econ-finance-explainer`、财经讲解、经济学科普 | econ-finance-explainer | 代数学家89式财经/经济学讲解，扩展为山河长度，支持 YouTube/TikTok/Google Trends/财经新闻/社媒投诉/官方数据/全源选题 |
| `$browser-cdp` | browser-cdp | 浏览器 CDP 工具 |

## 文件结构

- `拆文库/` — 拆文分析结果存放目录
- `New project/正文/` — 长篇小说正文章节
- `New project/正文.md` — 短篇小说正文
- `New project/设定/` — 角色设定、世界设定
- `New project/大纲/` — 卷纲、细纲
- `New project/追踪/` — 上下文.md、伏笔.md、时间线.md、角色状态.md
- `New project/对标/` — 对标作品分析

## Codex 项目约定

- Codex custom agents 部署在 `.codex/agents/*.toml`，需要新开 Codex 会话后才会稳定可用。
- Codex hooks 部署在 `.codex/hooks.json` 和 `.codex/hooks/`；项目 `.codex/` 层需要被信任，非 managed hooks 还需要在 `/hooks` 中 review/trust 后才会运行。
- 写正文前必须先有对应大纲：长篇 `大纲/细纲_第N章*.md`，短篇 `小节大纲.md`。Codex hooks 会做机械守卫，但 skill 流程本身也必须遵守。
- Compact 后优先读取 `New project/追踪/上下文.md` 恢复当前写作进度。

## 协作规则

Agent 间的协调关系由 `.codex/agents/*.toml` 的职责边界描述定义，不需要独立协调规则文件。

## Compact 后恢复上下文

写作中的关键上下文：
1. 当前写作项目名称和进度
2. 最近讨论的角色设定变更
3. 未完成的伏笔列表
4. 当前章节的情绪/节奏目标

如果存在 `New project/追踪/上下文.md`，compact 后首先读取该文件恢复上下文。

