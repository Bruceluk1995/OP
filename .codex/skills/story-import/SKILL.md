---
name: story-import
description: "逆向导入已有小说。将半成品或完本小说解析为可继续写作的标准工程，并保留拆文库分析资产；按篇幅自动分流到长篇或短篇路径，衔接 story-long-write / story-short-write。触发方式：/story-import、「导入小说」「反向解析」「把我的书导进来」「把现有稿子做成可续写工程」。"
metadata: {"openclaw":{"source":"https://github.com/worldwonderer/oh-story-claudecode"}}
---
# story-import：逆向导入已有小说

把用户已有小说重建为可续写的写作工程。交付物不是一份孤立分析报告，而是：

- 可被后续写作 skill 直接识别的项目结构；
- 保留在 `拆文库/{书名}/` 的证据与分析资产；
- 从拆文库同步到项目 `对标/` 的写作侧引用视图。

不要重新实现拆文方法论。长篇调用 `story-long-analyze`，短篇调用 `story-short-analyze`；本 skill 只负责输入确认、完整管道契约、结构迁移、验收和激活。

## 执行边界

- 默认目标是“可续写工程”。用户只要拆文分析时，改走对应 analyze skill，不进入迁移阶段。
- 原文内容只做必要的文件拆分、命名和格式规范化，不擅自重写。
- 不把短篇误建成长篇目录，不把长篇压成单文件短篇工程。
- 不编造拆文证据中没有的关系、副线、钩子或状态；无法确定的字段标 `[待补充]`。
- 检查专业 agent 时按 `.claude/agents/` → `.opencode/agents/` → `.codex/agents/` 查找；运行时不可用就降级为主线程直接执行并报告 fallback。

## Phase 1：确认来源与分流

### 1.1 确认目标

用户意图不明确时只问一次：要“可续写工程”还是“仅拆文分析”。前者继续，后者路由到 analyze skill。

### 1.2 接收输入

支持：

- `.txt` / `.md` 单文件；
- 按文件名或章节号排序的目录；
- 用户直接粘贴的文本。

路径无效、目录为空或文本未提供时停下，明确缺少什么。直接粘贴的文本交给 analyze 管道保存为 `拆文库/{书名}/原文/原文.md`，不要重复备份。

### 1.3 自动检测并复述

检测书名、总章数、总字数、章节格式、是否完本、最后一章是否残缺。按 [references/length-routing.md](references/length-routing.md) 判定长篇/短篇，优先级为：

1. 用户明确声明；
2. 章节与工程结构信号；
3. 字数兜底。

把检测结果和分流结论复述给用户确认。残章要记录“基于残章续写”或“先补完再导入”的用户选择，不代替用户决定。

### 1.4 环境检查

检查 `.story-deployed` 与对应 agent 文件。未部署时让用户选择：

- 先运行 `story-setup`，再回来导入；
- 继续导入并接受串行/solo 降级。

环境缺失只影响速度和并行能力，不得降低交付物完整性。

## Phase 2：运行完整拆解管道

| 分流 | 调用 | 必须完成 | 产物根目录 |
|---|---|---|---|
| 长篇 | `story-long-analyze` | Stage 0-6 | `拆文库/{书名}/` |
| 短篇 | `story-short-analyze` | Stage 2-6 | `拆文库/{书名}/` |

### 长篇调用契约

从一开始就声明“完整拆解、一次跑完、不要停下询问”，让 long-analyze 自动越过 Stage 1 停靠点并跑完 Stage 2-6。若环境仍停在 Stage 1，自动继续全量拆解，不把该选择再次抛给用户。

长篇验收至少确认：

- 章节摘要数与识别到的章节数一致；
- Stage 3 聚合质量检查通过；
- `拆文报告.md` 与 `文风.md` 已生成；
- `剧情/节奏.md` 与 `剧情/情绪模块.md` 的契约状态已判定。

以下任一信号表示 v12 新契约拆文库：`_progress.md` 显示 Stage 3+ 完成，或 `拆文报告.md` 含“读者需求 / 情绪引擎”“关键信息与扩写技法总览”“节奏与情绪触动点”“可复现模块”。新契约库缺 `剧情/节奏.md` 或 `剧情/情绪模块.md` 时必须先修复或重跑 Stage 3，不得静默降级。

只有没有上述信号的 pre-v12 旧库可继续，并在报告标记：

- `legacy_deconstruction: true`
- `rhythm_missing`（如适用）
- `module_missing`（如适用）

### 短篇调用契约

short-analyze 是单一全量管道，不停靠。必须跑完并拿到 `拆文报告.md`、`情节节点.md`、`写作手法.md` 与原文备份。

### 中断恢复

长篇从 analyze 管道的进度文件恢复，不自建第二套进度协议。恢复时读取当前阶段、最后处理章节、已完成阶段与更新时间，从断点所在块继续。

## Phase 3：迁移为写作工程

先完整读取与分流对应的一级 reference，再执行迁移：

| 分流 | 必读规则 | 后续接手 |
|---|---|---|
| 长篇 | [references/structure-mapping-long.md](references/structure-mapping-long.md) + [references/character-state-reverse.md](references/character-state-reverse.md) | `story-long-write` 日更循环 |
| 短篇 | [references/structure-mapping-short.md](references/structure-mapping-short.md) + [references/format-and-structure.md](references/format-and-structure.md) | `story-short-write` Phase 3 |

### 3-L 长篇迁移守卫

严格以 `structure-mapping-long.md` 为唯一详细映射，主流程只保留执行顺序：

1. 创建长篇项目骨架并标准化 `正文/第XXX章_章名.md`，保留原文内容。
2. 迁移角色、关系、世界观与势力；已有主题拆分时 pass-through，单文件时才 re-split。
3. 从故事线和章节摘要反推大纲。原文没有明确卷界时，只提出候选卷界，等待用户确认后再写定卷纲。
4. 生成细纲；无法由证据稳定判断的钩子、关系、副线与代价字段标 `[待补充]`。
5. 按固定依赖顺序生成追踪文件：`伏笔.md` → `时间线.md` → `角色状态.md` → `上下文.md`。
6. 生成 `设定/题材定位.md`，维护完整 `对标书列表` 与最多一个 `主对标书`。
7. 同步 `剧情/节奏.md`、`剧情/情绪模块.md`、剧情/章节/角色/设定资产、`拆文报告.md` 和 `文风.md` 到项目 `对标/{书名}/`。

写作侧权威为 `对标/{书名}/剧情/节奏.md` 和 `对标/{书名}/剧情/情绪模块.md`；摘要冲突时保留冲突说明并以权威文件为准。新契约拆文库缺任一权威文件时停下修复，旧库才允许带 legacy 标记继续。

`追踪/角色状态.md` 不可遗漏。它依赖伏笔文件，并且是 long-write 日更前状态筛选的直接输入。半成品最后一章为残稿时，以残稿前最后一个完整章节作为状态基准并注明。

### 3-S 短篇迁移守卫

短篇工程固定为：

```text
{标题}/
├── 设定.md
├── 小节大纲.md
├── 正文.md
└── 对标/{书名}/（可选引用视图）
```

- `正文.md` 是单文件全文，只规范格式，不重写内容。
- `设定.md` 同时包含核心框架与对标摘要。
- `小节大纲.md` 从情节节点反推，不能稳定提取的钩子标 `[待补充]`。
- 严禁创建长篇专属的 `正文/`、`大纲/`、`追踪/` 目录。

## Phase 4：验收与激活

### 4.1 运行对应质量清单

- 长篇：执行 `structure-mapping-long.md` 末尾的完整清单。
- 短篇：执行 `structure-mapping-short.md` 末尾的完整清单。

任何阻塞项未通过时不要声称导入完成。先修复可自动修复项，再把确需用户判断的卷界、残章策略或 `[待补充]` 集中列出。

### 4.2 输出导入报告

报告必须包含：

- 源文件、识别篇幅、章数/字数、项目目录；
- 已生成文件与实际计数；
- 长篇的追踪四件套、对标节奏/情绪模块/文风同步状态与 legacy 标记；
- 短篇的 `正文.md`、`设定.md`、`小节大纲.md` 状态；
- 待补充项；
- 下一步明确命令。

长篇下一步默认是 `story-review lean` 后接 `story-long-write` 日更；短篇下一步默认是 `story-short-write` Phase 3。

### 4.3 激活项目

把项目根 `.active-book` 写为新导入书目录的相对路径，并确认对应 write skill 能识别工程。可用 `story-explorer` 做交叉验证；不可用时由主线程直接核对文件，不阻塞激活。

## 大型作品

超过 200 章的长篇采用增量导入：首期导入前 50 章与全书概要，剩余章节按批次继续；未导入章节先保留约 200 字/章的简化摘要。不要对短篇套用增量导入。

## Reference 路由

按需加载，不一次读取全部：

- 篇幅判定：`references/length-routing.md`
- 长篇迁移：`references/structure-mapping-long.md`
- 短篇迁移：`references/structure-mapping-short.md`
- 角色状态反推：`references/character-state-reverse.md`，需要字段协议时再读 `references/state-tracking.md`
- 短篇正文格式：`references/format-and-structure.md`

涉及拆解方法论时运行对应 analyze skill，由它加载自己的 references；不要从本 skill 深层追索别的 skill 文件。

## 流程衔接

| 时机 | 跳转到 |
|---|---|
| 长篇导入后续写 | `story-long-write` |
| 短篇导入后续写 | `story-short-write` |
| 导入后审查 | `story-review` |
| 只要长篇分析 | `story-long-analyze` |
| 只要短篇分析 | `story-short-analyze` |
| 环境未部署 | `story-setup` |

## 语言

跟随用户语言回复。中文回复遵循《中文文案排版指北》。
