---
name: jp-isekai-oneshot
description: Standalone Japanese male-audience isekai writing skill for traditional web-novel prose or anime-recap/push narration copy, each supporting first-person or third-person narration. Use for 日式男频异世界短篇, 男频异世界推文/动漫解说文案, 15000字单篇, one-shot, 一发完结, battle leveling, OP/龙傲天, dungeon, exile zamaa, YouTube/TikTok/Shorts hooks, Google Trends JP, absurd-news conversion, or any complete short that resolves in one file.
metadata: {"openclaw":{"source":"https://github.com/worldwonderer/oh-story-claudecode"}}
---

# JP Isekai Oneshot

## 数字交互契约

- 凡需用户在有限选项中决定，必须在普通对话中列出数字编号，并以“请只回复数字；可多选时用 +，如 1+3”收尾。
- 禁止用开放式问题代替可枚举选项；禁止依赖 AskUserQuestion、request_user_input 或自由文本选项完成有限选择。
- “自定义 / 其他 / 提供素材”也必须编为数字选项。用户选中后，下一轮只索取一个必要内容（如关键词、书名、路径、链接或正文）；这类实际内容不强行数字化。
- 是非确认统一写成 1. 是 / 2. 否，并要求只回复数字。

Write complete standalone Japanese male-audience isekai short stories around 14,500-16,500 Japanese characters. This skill is for one-shot stories, not serial episodes, not 6-episode short seasons, and not long webnovel chapter planning.

## Core Contract

- Before building a one-shot, read `../jp-isekai/references/presentation-modes.md` and present its numbered 1-4 menu with multiple selection allowed, unless the combination is already explicit.
- For either push option, read `../story/references/flan-push-strict-mode.md` and require the saved body to pass its validator before delivery.
- Write audience-facing prose in Japanese unless the user asks otherwise. Keep planning notes in Chinese by default.
- Reject literary prose: avoid long environment description and long psychology description; use colloquial, direct everyday language to move the plot through action, dialogue, choices, proof, cost, and consequence.
- Use Japanese RPG/light-novel isekai vocabulary: `スキル`, `ステータス`, `冒険者ギルド`, `ランク`, `魔物`, `ダンジョン`, `商会`, `貴族`, `魔力`.
- Avoid Chinese xianxia/wuxia terms and Chinese webnovel institutions unless the user explicitly requests them.
- When adapting Chinese 玄幻、修仙、朝堂、宫斗、赘婿、龙傲天 material, rebuild the power and institution logic into Japanese RPG/light-novel fantasy: guild ranks, dungeon rules, noble factions, royal succession, territory management, merchant contracts, magic academies, monster ecology, or church records. Do not preserve sect/cultivation/court-drama systems by direct translation unless the user wants that setting.
- A one-shot must contain a complete satisfaction arc in one file: hook, cheat/skill proof, escalation, climax, reward/consequence, and emotional closure.
- Do not create `6集`, `第2話への引き`, previous-episode bridge, or a next-episode cliffhanger unless the user asks for a serial.
- Use source/ranking works only as functional pattern references. Do not copy characters, scenes, guilds, kingdoms, prose, or named plots.

## Workflow

1. Resolve the numbered format gate before premise intake:
   - Offer options 1-4 exactly as defined in `presentation-modes.md` and say `可多选`.
   - For multiple selections, produce separate versions from the same premise unless the user requests different premises. Confirm whether the requested length is total or per version when that distinction materially changes scope.
   - Traditional mode stays scene-based in either person. Push mode keeps result-first hooks, oral information lines, causal compression, visible proof, and complete payoff in either person.
   - `短篇`, `15,000字`, `YouTube`, `Shorts`, or `一口气看完` decides neither choice.
2. If the user has no premise, ask a compact intake:
   - Present the grouped choices from `../jp-isekai/references/topic-menu.md`; allow multiple selections, auto-pick, custom keywords, or another batch. Do not limit the user to 4-6 generic topics.
   - 选题来源: YouTube/TikTok 热门视频 / 日本离谱新闻/逆天新闻 / Google Trends JP 热点 / 生活痛点关键词 / 常青类型 / 用户给关键词.
   - 题材类型: battle leveling / OP dominance / exile zamaa / dungeon boss / academy-game knowledge / tamer / earth-commute / dungeon-master / slow-life reward.
   - 爽点: 升级掉落 / 开局无敌 / 被低估后打脸 / 经营领地 / 魔物伙伴 / 现代知识碾压.
   - Tone: fast爽 / comedic practical / dark revenge / warm reward.
3. Before writing, read:
   - `../jp-isekai/references/presentation-modes.md`
   - `../jp-isekai/references/opening-innovation-engine.md` before selecting or writing a push opening. Filter by subtype lane, randomly draw one compatible card, fill its chain, and store the selected card ID with the package.
   - `../jp-isekai-write/references/push-narration-protocol.md` when push mode is selected.
   - `references/oneshot-blueprint.md`
   - `references/anti-water.md`
   - `../jp-isekai-write/references/terminology.md` when adapting from Chinese material, checking RPG localization, or avoiding xianxia/court-drama leakage.
   - `../jp-isekai-write/references/self-check.md` as the Codex AI self-check pattern, adapted to one-shot closure instead of serial continuity.
   - `references/trend-benchmarking.md` when the user asks for 热点, Google Trends, 蹭热点, current topic selection, or trend-to-skill conversion.
   - `references/absurd-news-benchmarking.md` when the user asks for 逆天新闻, 离谱新闻, 奇葩新闻, 日本社会怪事, bizarre news, or story-hot topics with stronger conflict than Google Trends.
   - `references/social-video-trends.md` when the user asks for TikTok, YouTube, Shorts, viral videos, 热门视频, or short-video hooks.
   - `references/trend-theme-router.md` only after the user has selected a specific trend seed, or has explicitly delegated the choice with “你选/自动选”, and wants it matched to a male-isekai subtype/theme-pack.
   - `references/oneshot-delivery.md` before saving a full one-shot package, character prompts, cover prompt, or any project-bound output.
4. If the user asks for current market, ranking, Google Trends, or "现在日本什么火", browse/fetch current source pages before making market claims. For Japan hot-topic ideation, use Google Trends JP first.
   - Treat source selection and seed selection as different decisions. Choosing `YouTube/TikTok`, `Google Trends`, `离谱新闻`, a subtype, a payoff, or a tone does **not** authorize Codex to choose the concrete hot seed.
   - Collect 6-10 raw items, filter them, then present 3-5 viable numbered candidates with source/date, seed, scores, extracted hook, primary/backup route, converted skill, one-shot promise, and safety transform.
   - Stop after the shortlist and ask the user to choose a candidate number or request another batch. Do not create the final title, run a candidate ledger check, build the blueprint, draft prose, save a package, or append the ledger before that choice.
   - Skip this pause only when the user supplied the exact video/news/trend/link/keyword to use, or explicitly said `你选`, `自动选`, `直接选最好的`, or equivalent. If choice was delegated, state which candidate was selected before continuing.
   - Do not pick the highest-traffic trend automatically. Score candidates by everyday resonance, fantasy-engine fit, male-audience payoff, safety, and title clickability.
   - Prefer生活贴近 seeds: prices, jobs, taxes, food, heat/cold people feel, sleep/health, commuting, exams, apps/tools, shopping, household costs, pets, local events, and sports-as-competition.
   - Downrank remote spectacle seeds like solar flares, space events, macro science, or celebrity names unless they can be converted into an everyday problem Japanese viewers immediately understand.
   - After selecting a hot seed, route it to the best theme-pack route before choosing the final cheat, title, or outline.
   - Treat `jp-isekai-plan/references/type-packs/*` as theme engines only. Do not inherit their six-episode structure inside one-shot work.
5. If the user asks for 离谱新闻/逆天新闻 or rejects Google Trends as boring, browse current Japanese weird-news/social-news sources and use absurdity scoring first. The best seed is usually a fictionalizable unfair rule, broken service, hidden cost, workplace/school absurdity, AI/tool failure, product/price oddity, or public-institution mistake.
6. If the user asks for TikTok/YouTube or rejects news/Trends as boring, browse current social-video trend sources and use video-hook scoring first. Prefer YouTube Japan category trends when TikTok public pages are blocked; use TikTok Creative Center or `$browser-cdp` with logged-in browser only when available.
7. Check anti-homogenization if a ledger exists:
   - `python .codex/skills/jp-isekai-oneshot/scripts/ledger.py --root . summary`
   - `python .codex/skills/jp-isekai-oneshot/scripts/ledger.py --root . check ...`
   - Include `opening_card`, a story-specific filled `opening_chain`, and a canonical `structure_fingerprint` in the candidate check. Do not store only the generic card slot names. A different opening card does not excuse a repeated macro structure.
8. Build a brief one-shot blueprint before prose. Do not require project `大纲/细纲` files for one-shot work.
   - Run `draw-opening-template.py --lane <lane> --root <project-root>` before locking the `opening promise`. Let the script exclude the last three ledger cards automatically. Fit the selected card truthfully to the story; one redraw is allowed only when the card cannot fit without fabricating facts.
   - Preserve the returned `required_chain`. Plan one exact opening fact for every slot; do not approve the blueprint while any slot is vague or borrowed from a different card.
   - Include a closure ledger: opening promise, midpoint irreversible change, public/observable proof, climax result, reward/cost, and final social/emotional state. Every item must resolve inside this file.
   - Audit major scenes for a state delta in skill knowledge, combat position, drop/resource, rank/reputation, relationship, risk, or objective; compress scenes that only repeat awe, travel, explanation, or inner commentary.
9. Save complete long prose as a one-shot package under `episodes/oneshots/<short-title>/` unless the user asks for chat-only output.
   - Required package folders/files: `正文/正文.md`, `正文/标题.md`, `角色提示词/角色提示词.md`, `封面/封面.md`, `作品资料.md`, and `开头抽卡证据.json`.
   - Generate `封面/封面.png` only when image generation is requested or available; otherwise mark `封面/封面.md` as prompt-only.
   - Do not deliver only a single mixed markdown file.
10. After saving, count only `正文/正文.md`. Do not report completion below 14,500 Japanese characters unless the user explicitly approved a shorter story.
11. After saving, run a Codex AI one-shot self-check by rereading the saved body, title file, character prompts, cover brief, and `作品资料.md`:
   - Run `validate-opening-evidence.py` against the saved body and `开头抽卡证据.json`. Any missing, duplicate, invented, out-of-order, or late evidence is blocking; rewrite the opening within the drawn card and rerun.
   - Verify the body is Japanese audience-facing prose only, with no Chinese planning notes, source-language leftovers, or meta/production leakage.
   - Verify one-shot closure: hook, cheat/skill proof, escalation, public consequence, reward, zamaa/status change, and emotional/social closure all resolve in this file.
   - Verify localization: if the source came from Chinese xianxia, court drama, or webnovel power fantasy, its functions have been rebuilt as Japanese RPG/light-novel mechanisms such as スキル, ギルド, ランク, ダンジョン, 王国, 貴族派閥, 領地, 商会, 魔法学院, 魔物, and 魔力, not literal sect/cultivation/palace terms.
   - Verify prose freshness with Codex judgment: cut repeated scenery, generic awe, destiny talk, travel padding, duplicated inner monologue, and dry status-panel dumping; rewrite the saved body if the check finds real issues.
   - Treat this quality gate as a reasoning pass over the actual saved artifacts.
12. Append a ledger record unless the user says not to. Store `opening_card`, a compact `opening_chain`, and the canonical `structure_fingerprint` as structured fields, not only inside `notes`.

## One-Shot Defaults

- Target length: 14,500-16,500 Japanese characters.
- Subtype/theme packs supply genre tactics only; this skill always owns the one-shot length, closure, and 12-18 beat compression unless the user asks for a serial.
- Package shape:
  - `正文/正文.md`: Japanese body only.
  - `正文/标题.md`: Chinese working title, Japanese publish title, and short click title.
  - `角色提示词/角色提示词.md`: image-ready character prompts for all major characters.
  - `封面/封面.md`: cover/thumbnail brief, final image prompt, text layers, and status.
  - `作品资料.md`: blueprint, source notes, character count, checks, and ledger notes.
- Ending: closed satisfaction, not next-episode hook. A final "larger world" aftertaste is allowed only after the central conflict is resolved.
- Trend/news/video-driven titles: show Chinese working title + Japanese publish title + seed + selected theme route + converted cheat/skill + why the seed becomes a fantasy payoff.

## Hard Rules

- Do not turn a one-shot into a season outline.
- Do not confuse “source/type/tone selected” with “hot seed selected.” For dynamic hot-source work, user confirmation of a numbered seed is mandatory unless the user explicitly delegates the choice or supplies the exact seed.
- Do not paste real trending celebrities, scandals, crime, tragedies, or sports match trivia into the fantasy story. Convert only the underlying desire, anxiety, object, rule, competition, weather, tool, or social mechanism into a fantasy skill/quest engine.
- Do not turn real absurd news into disguised defamation or tragedy exploitation. Fictionalize names, places, companies, victims, and legal facts; keep only the absurd mechanism.
- Do not copy TikTok/YouTube creators, scenes, jokes, clips, songs, anime/game IP, dialogue, or exact video order. Extract only the hook mechanic.
- Do not leave the main enemy, proof, reward, or emotional promise unresolved.
- Do not use literary padding: no long scenery blocks, no long psychology blocks, no decorative atmosphere when action, dialogue, or consequence should carry the beat.
- Do not pad to 15k with travel, weather, generic awe, destiny, repeated inner monologue, or scenery.
- Do not weaken OP protagonists randomly. Tension comes from unknown rules, public identity, collateral cost, information control, faction consequence, or restraint.
- Do not let battle leveling become only commerce, herbs, or comfort scenes. Include a visible skill/combat/progression result.
- Do not preserve Chinese xianxia, wuxia, sect, or palace-drama systems by surface translation. Convert their function into Japanese RPG fantasy equivalents: guild rank, skill tree, dungeon law, noble faction, royal decree, territory reward, magic academy rule, merchant contract, or church record.
- Do not report "done" until the saved body count is in range or the user approved shorter output.

## Deliverable

For a full one-shot:

1. Chinese working title + Japanese publish title.
2. Subtype/theme route, target emotion, protagonist/cheat, complete payoff.
3. Brief one-shot blueprint.
4. Saved package path and primary file paths.
5. Body character count.
6. Codex AI self-check result and ledger status.
