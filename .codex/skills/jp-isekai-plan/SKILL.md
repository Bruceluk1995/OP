---
name: jp-isekai-plan
description: "Plan Japanese male-audience isekai as traditional web-novel prose or anime-recap/push narration copy, with either first-person or third-person narration. Use for 日式RPG异世界开书, 男频异世界推文/动漫解说文案, なろう系/カクヨム男性向け premise design, localization, cheat design, battle leveling, dungeon arcs, OP/龙傲天, exile reversal, slow life, and long or short story structure."
metadata: {"openclaw":{"source":"https://github.com/worldwonderer/oh-story-claudecode"}}
---

# JP Isekai Plan

## 数字交互契约

- 凡需用户在有限选项中决定，必须在普通对话中列出数字编号，并以“请只回复数字；可多选时用 +，如 1+3”收尾。
- 禁止用开放式问题代替可枚举选项；禁止依赖 AskUserQuestion、request_user_input 或自由文本选项完成有限选择。
- “自定义 / 其他 / 提供素材”也必须编为数字选项。用户选中后，下一轮只索取一个必要内容（如关键词、书名、路径、链接或正文）；这类实际内容不强行数字化。
- 是非确认统一写成 1. 是 / 2. 否，并要求只回复数字。

Build Japanese-style male-audience isekai plans. This skill is for concept and structure, not final prose.

Before premise or title work, read `../story/references/global-topic-history.md`, check the shared project ledger, and record every displayed candidate before output. Cross-domain re-skins of burned topics are blocked by default.

When planning prose beats, design colloquial, direct scene movement: action, dialogue, choices, proof, cost, and consequence. Do not plan long scenery passages, long psychology passages, or literary mood filler as a way to carry the story.

## Required Reads

- Read `../jp-isekai/references/presentation-modes.md` before planning any long or short male-isekai project. Present the numbered 1-4 menu and allow multiple selections unless the user already chose a combination explicitly.
- Read `../story/references/flan-push-strict-mode.md` for either push option and plan information/shot lines, narrated reactions, and sparse direct dialogue regardless of person.
- Read `../jp-isekai/references/topic-menu.md` when the user has not supplied a concrete premise. Do not replace the full grouped topic menu with a tiny handful of examples.
- Read `../jp-isekai/references/opening-innovation-engine.md` before finalizing any first-episode or one-shot push opening. Filter by subtype lane, randomly draw one compatible card, plan its chain, and record the card ID; do not invent a new structure.
- Read `references/terminology.md` whenever adapting from Chinese fantasy or when the user says "不要中式".
- Read `references/market-patterns.md` when the user asks for market fit, popular formulas, or gives なろう/Kakuyomu as reference.
- Read `references/planning-template.md` before producing a full concept package.
- Read `references/dynamic-benchmarking.md` when the user wants current market fit, website-based拆书, hottest works, or when no strong project benchmark exists for the chosen subtype.
- Read `../jp-isekai/references/project-memory.md` before opening a project, continuing a serial, creating chapter outlines, or trying to avoid repeated premises.
- Read `../story/references/character-name-policy.md` before naming the cast. Run `import-existing`, check every final name, apply `jp-female-fantasy` to important women, and add all selected names after saving the plan.
- Before planning any subtype, resolve its benchmark priority: project拆文 or live website benchmark first, project subtype notes second, bundled type pack only as fallback. Do not rely on the generic isekai rules alone.

Type pack routing:

- OP dominance / 龙傲天 / 主人公最強 / 骨王 vibe -> `references/type-packs/op-dominance.md`
- 打怪升级 / dungeon grind / boss drops / rank growth -> `references/type-packs/battle-leveling.md`
- 追放ざまぁ / support class / healer / porter / appraiser reversal -> `references/type-packs/exile-support-reversal.md`
- 学园 / game-world / mob / 原作知识 / death flag -> `references/type-packs/academy-game-knowledge.md`
- 日本往返 / modern goods / Earth supply -> `references/type-packs/earth-commute.md`
- 従魔 / テイマー / monster companion -> `references/type-packs/tamer-familiar.md`
- Dungeon master / territory / base management -> `references/type-packs/dungeon-master-territory.md`
- Secret society / subordinate operation / faction snowball -> `references/type-packs/secret-society-subordinates.md`
- Production / crafting / commerce / slow life -> `references/type-packs/craft-commerce-slowlife.md`

Benchmark priority:

1. If `对标/{lane}/{work}/拆文报告.md` or `拆文库/{work}/` exists, read it before bundled type packs.
2. If the user asks for current/hot/platform-fit or there is no project benchmark, browse the relevant public ranking/tag pages and create a Dynamic Benchmark Card from `references/dynamic-benchmarking.md`.
3. Read any project-local `男频异世界知识库/type-packs/{lane}.md`.
4. Read the bundled `references/type-packs/{lane}.md` only as fallback scaffolding.

## Planning Workflow

1. Resolve the numbered format gate first:
   - Offer options 1-4 exactly as defined in `presentation-modes.md` and say `可多选`.
   - Record every selected combination in the concept package and outline. Do not silently switch later.
   - For multiple selections, plan separate presentation/viewpoint variants from the same premise unless the user requests different premises.
   - For push mode, plan information/shot beats, causal gaps, oral transitions, proof moments, and retention turns. Do not force every story into a result-first opening; let the opening innovation engine select the strongest premise-specific information order. First-person push uses the protagonist's oral account; third-person push may use role labels and external reactions.
2. Identify the target subtype:
   - OP dominance / ruler fantasy: protagonist starts overwhelmingly strong; tension comes from information gaps, restraint, subordinates, territory, politics, public myth, and enemies choosing the wrong fight.
   - Battle leveling / monster grind: protagonist turns a weak-looking skill into combat value, kills stronger monsters, earns drops, rank-ups, and boss access.
   - Isekai return / Earth commute cheat: protagonist can go back to Japan or bring modern goods/knowledge across worlds; the engine is supply, secrecy, rescue, and culture mismatch.
   - Game-world / mob / academy knowledge: protagonist knows routes, hidden bosses, bad endings, class/job traps, or academy rankings and exploits that knowledge.
   - Exile zamaa / support class reversal: expelled support, rear guard, healer, appraiser, porter, or "E-rank" skill proves essential in combat, logistics, or boss clears.
   - Tamer/familiar/monster party: growth comes from taming, evolving, naming, feeding, combining, or commanding monsters and familiars.
   - Dungeon master / territory management: protagonist builds or controls a dungeon, town, guild branch, secret base, or domain and wins through traps, resources, and subordinates.
   - Secret society / subordinate operation: protagonist's power creates a faction;爽点 comes from subordinates overperforming, enemies misreading the organization, and reputation snowballing.
   - Cheat survival: weak start, unusual skill, visible optimization.
   - Slow life / farming: protagonist wants peace, plot keeps generating trouble.
   - Production/crafting: noncombat class, item creation, repair, appraisal, cooking, taming.
   - Dungeon/adventurer: guild ranks, party dynamics, drop economy, bosses.
   - Zamaa/reversal: mistreatment, public proof, overconfident opponent, clean emotional payoff.
   - Harem-adjacent: admiration and romantic tension without derailing the main progression unless requested.
   - For ambiguous male-audience爽文, offer OP dominance, battle leveling, exile reversal, dungeon/adventurer, tamer, academy/game-knowledge, and Earth-commute routes before slow-life. Slow life is a chosen flavor, not the default.
   - After choosing a subtype, follow the benchmark priority above. Use the bundled type pack only to fill gaps after dynamic/project benchmarks are loaded.
3. Create a localization map:
   - Chinese source concept -> Japanese isekai equivalent.
   - Institutions, creatures, rank names, currencies, food, clothes, and place names.
   - Name-ledger result for every named character. Use short daily call names; a formal noble name is plot metadata, not the repeated narration label.
4. Design the cheat as a repeatable engine:
   - Input, output, limitation, growth path, misunderstanding surface, and public-facing explanation.
   - Ensure every episode can generate one discovery, one problem, and one payoff.
   - For battle leveling, ensure every episode can generate one monster/combat problem, one tactical skill use, one visible drop/rank/level/status result, and one stronger next threat.
   - For OP dominance, the cheat/power may already be maxed. Design limits around unknown world rules, collateral damage, political cost, maintaining a public persona, protecting subordinates, resources, moral line, or incomplete information. Ensure every episode can generate one enemy misread, one restrained choice, one overwhelming reveal/command, and one reputation/territory/faction consequence.
5. Design the first arc around a concrete ladder:
   - Bottom status -> first monster win -> first drop/reward -> first helper/party contact -> first guild rank or dungeon access -> first boss/public win -> first stable base.
   - OP route ladder: hidden arrival -> first local insult/misread -> first controlled demonstration -> first subordinate or local faction reacts -> first territory/resource secured -> first larger power notices.
   - For every planned episode, record `promise -> pressure/test -> proof/payoff -> cost -> state delta -> next pressure`. The state delta must change at least one of power use, inventory/drop, rank, reputation, territory, faction alignment, knowledge, or immediate goal. If two adjacent episodes repeat the same delta, redesign one before drafting.
6. Set the project scale before making outlines:
   - Default for YouTube/push/episode-like serials: short-season novel, fixed 6 episodes/chapters.
   - Keep short-season outlines at exactly 6 episodes/chapters.
   - Keep the prose and files novel-style (`细纲_第XXX章.md`, episode folders, tracking files); do not switch to screenplay format.
   - Do not plan a hundred-chapter roadmap unless the user explicitly asks for a long webnovel.
7. If the task is project-bound, materialize the plan into the common project files:
   - Create or update `设定/题材定位.md`, reusable `设定/角色/`, `设定/势力/`, and `设定/世界观/` files.
   - Create `大纲/大纲.md`, `大纲/卷纲_第X卷.md`, and the first rolling batch of `大纲/细纲_第XXX章.md`.
   - Create or update `追踪/伏笔.md`, `追踪/时间线.md`, `追踪/角色状态.md`, and `追踪/上下文.md`.
   - Run the `男频异世界知识库` ledger check before finalizing a premise or outline engine, then add a compact record after generation.
8. Output a usable package:
   - Japanese title candidates, premise, protagonist, cheat, world rules, first arc, episode 1 beats, terminology map, banned Chinese leakage list.

## Output Rules

- Keep names and terms Japanese-friendly.
- Avoid explaining the Chinese original unless useful for mapping.
- Do not leave a project-bound plan only in chat when the user expects a reusable writing project; write the corresponding `设定/`, `大纲/`, and `追踪/` artifacts.
- If the user asks for Japanese prose next, hand off to `$jp-isekai-write` with the localization map and episode beats.
