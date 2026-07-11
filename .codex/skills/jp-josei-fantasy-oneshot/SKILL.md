---
name: jp-josei-fantasy-oneshot
description: Standalone Japanese female-audience fantasy romance skill for traditional web-novel prose or anime-recap/push narration, with first-person or third-person. Use for 女频幻想恋爱短篇, 女频推文, 女性向け異世界恋愛 one-shot, 15000字单篇, 悪役令嬢, 婚約破棄ざまぁ, 聖女, 契約婚, 辺境伯, 溺愛, ループ, 令嬢, trend conversion, or any complete romance fantasy resolving in one file.
metadata: {"openclaw":{"source":"https://github.com/worldwonderer/oh-story-claudecode"}}
---

# JP Josei Fantasy Oneshot

Write complete standalone Japanese female-audience fantasy romance short stories around 14,500-16,500 Japanese characters. This skill is for one-shot stories, not serial episodes, not 6-episode short seasons, and not long webnovel chapter planning.

## Core Contract

- Before building a one-shot, read `../jp-josei-fantasy/references/presentation-modes.md` and present its numbered 1-4 menu unless already explicit.
- When push narration is selected, read `../jp-josei-fantasy/references/push-opening-template-deck.md`, filter by lane, randomly draw one compatible card, and use only that card.
- Write audience-facing prose in Japanese unless the user asks otherwise. Keep planning notes in Chinese by default.
- Reject literary prose: avoid long environment description and long psychology description; use colloquial, direct everyday language to move the story through action, dialogue, choices, evidence, romance movement, and social consequence.
- Center the heroine's dignity, agency, emotional recovery, romance recognition, and happy ending.
- `ざまぁ` must be emotionally and logically earned through evidence, witness, etiquette, contract, law, church record, family ledger, or public social consequence.
- `溺愛` must be protective, respectful, and specific; avoid flattening the heroine into a reward object.
- A one-shot must resolve the core wound and relationship promise in one file.
- Do not create `6集`, previous-episode bridge, serial folder logic, or next-episode cliffhanger unless the user asks for a serial.
- Avoid male-audience RPG optimization, harem framing, and Chinese court/xianxia defaults.
- When adapting Chinese 古言、宫斗、朝堂、玄幻、穿书 material, rebuild the story function for Japanese female-audience fantasy romance instead of translating institutions literally. Do not carry over 皇帝/后宫/冷宫/赐婚/嫡庶/夺嫡/太监/宫女/抄家灭族 logic unless the user explicitly wants a Chinese setting.

## Workflow

1. Resolve presentation mode and viewpoint before premise intake. For push mode, draw the compatible fixed opening card after the lane is known.
2. If the user has no premise, ask a compact intake:
   - 选题来源: YouTube/TikTok 热门视频 / Google Trends JP 热点 / 日本离谱新闻或社会热点 / 女性向けランキング・タグ页 / 生活痛点关键词 / 常青类型 / 用户给关键词 / 全选.
   - 题材类型: 婚約破棄ざまぁ / 悪役令嬢 / 聖女 / 契約結婚 / 辺境伯溺愛 / 職人令嬢 / 相続家族 / ループ / 異類婚姻 / 強いヒロイン / 手紙すれ違い.
   - 情绪主轴: 屈辱逆转 / 证据反杀 / 被尊重治愈 / 契约变真爱 / 家族切割 / 公开名誉恢复.
   - 男主作用: 保护证据 / 公开承认 / 法律或爵位支持 / 温柔尊重 / 共犯式反击.
3. Before writing, read:
   - `../jp-josei-fantasy/references/presentation-modes.md`
   - `../jp-josei-fantasy/references/push-opening-template-deck.md` when push mode is selected.
   - `references/oneshot-blueprint.md`
   - `references/anti-water.md`
   - `../jp-josei-fantasy-write/references/terminology.md` when adapting from Chinese material, checking localization, or avoiding Chinese court/xianxia leakage.
   - `../jp-josei-fantasy-write/references/self-check.md` as the Codex AI self-check pattern, adapted to one-shot closure instead of serial continuity.
   - `../jp-josei-fantasy/references/hot-source-router.md` when the user has no premise, wants 热点选题, asks for all-source discovery, or asks which platform to search.
   - `../jp-josei-fantasy/references/trend-benchmarking.md` when the user asks for 热点, Google Trends, 蹭热点, current topic selection, or trend-to-romance conversion.
   - `../jp-josei-fantasy/references/absurd-news-benchmarking.md` when the user asks for 离谱新闻, 逆天新闻, 日本社会怪事, bizarre news, or stronger conflict than Google Trends.
   - `../jp-josei-fantasy/references/social-video-trends.md` when the user asks for TikTok, YouTube, Shorts, viral videos, 热门视频, or short-video hooks.
   - `../jp-josei-fantasy/references/trend-theme-router.md` only after the user has selected a specific hot seed, or explicitly delegated selection with “你选/自动选”, and wants it matched to a josei fantasy subtype/type-pack.
   - `references/oneshot-delivery.md` before saving a full one-shot package, character prompts, cover prompt, or any project-bound output.
4. If the user asks for current market, ranking, Google Trends, YouTube, TikTok, or "现在日本什么火", browse/fetch current sources before making market claims. For Japan hot-topic ideation, start with the user's chosen source; if no source is chosen, ask the source menu from `hot-source-router.md`.
   - Treat source selection and seed selection as different decisions. Choosing a platform/source, josei lane, emotion axis, or male-lead function does **not** authorize Codex to choose the concrete hot seed.
   - Collect raw items, filter them, then present 3-5 viable numbered candidates with source/date, scores, extracted mechanism, primary/backup josei route, heroine wound, proof/romance mechanism, one-shot promise, and safety transform.
   - Stop after the shortlist and ask the user to choose a candidate number or request another batch. Do not lock the final title, run a candidate ledger check, build the blueprint, draft prose, save a package, or append the ledger before that choice.
   - Skip this pause only when the user supplied the exact video/news/trend/ranking item/link/keyword, or explicitly said `你选`, `自动选`, `直接选最好的`, or equivalent. If choice was delegated, state which candidate was selected before continuing.
   - Do not pick the highest-traffic trend automatically. Score candidates by heroine empathy, romance/zamaa engine fit, female-audience payoff, safety, and title clickability.
   - Prefer女性向け可转译 seeds: public humiliation, reputation repair, unfair family/work/school rules, money or inheritance anxiety, beauty/health fatigue, food/home comfort, communication failure, weather/disaster shelter, pets/animals, weddings, contracts, etiquette, and "nobody believed me until proof appeared" hooks.
   - Downrank remote spectacle, celebrity gossip, crime/tragedy, politics rage bait, or pure sports results unless they can be converted into a fictional social rule, public proof, contract, ceremony, or relationship recognition scene.
   - After selecting a hot seed, route it to the best josei type route before choosing the final title, heroine wound, male lead, proof object, or outline.
5. If the user asks for 离谱新闻/逆天新闻 or rejects Google Trends as boring, browse current Japanese weird/social-news sources and use absurdity scoring first. The best female-fantasy seed is usually a fictionalizable unfair rule, etiquette trap, contract loophole, family/property conflict, service failure, school/workplace humiliation, mistaken record, or public apology failure.
6. If the user asks for TikTok/YouTube or rejects news/Trends as boring, browse current social-video trend sources and use video-hook scoring first. Prefer YouTube Japan category trends when TikTok public pages are blocked; use TikTok Creative Center or `$browser-cdp` with logged-in browser only when available.
7. Check anti-homogenization if a ledger exists:
   - `python .codex/skills/jp-josei-fantasy-oneshot/scripts/ledger.py --root . summary`
   - `python .codex/skills/jp-josei-fantasy-oneshot/scripts/ledger.py --root . check ...`
8. Build a brief one-shot blueprint before prose. Do not require project `大纲/细纲` files for one-shot work.
   - In push mode, record the randomly selected opening card ID, required chain, proof object, public venue, heroine decision, and body handoff.
   - Include a closure ledger: heroine wound, public/social pressure, midpoint irreversible choice, proof movement, romantic recognition, zamaa consequence, and final dignity/relationship state. Resolve every item inside this file.
   - Audit major scenes for a state delta in evidence, reputation, safety, legal/family position, resources, romantic trust, risk, or available choice; compress repeated sadness, etiquette, beauty, or comfort without change.
9. Save complete long prose as a one-shot package under `episodes/oneshots/<short-title>/` unless the user asks for chat-only output.
   - Required package folders/files: `正文/正文.md`, `正文/标题.md`, `角色提示词/角色提示词.md`, `封面/封面.md`, and `作品资料.md`.
   - Generate `封面/封面.png` only when image generation is requested or available; otherwise mark `封面/封面.md` as prompt-only.
   - Do not deliver only a single mixed markdown file.
10. After saving, count only `正文/正文.md`. Do not report completion below 14,500 Japanese characters unless the user explicitly approved a shorter story.
11. After saving, run a Codex AI one-shot self-check by rereading the saved body, title file, character prompts, cover brief, and `作品资料.md`:
   - Verify the body is Japanese audience-facing prose only, with no Chinese planning notes, source-language leftovers, or meta/production leakage.
   - Verify one-shot closure: heroine wound, accusation/proof, romance recognition, zamaa/social consequence, and happy-ending promise all resolve in this file.
   - Verify localization: if the source came from Chinese court drama or xianxia, the functions have been rebuilt as Japanese romance fantasy mechanisms such as 王宮/貴族院/神殿/社交界/修道院/爵位剥奪/領地没収/王命, not literal 宫斗/后宫/冷宫/嫡庶/夺嫡 carryover.
   - Verify prose freshness with Codex judgment: cut repeated decorative adjectives, atmosphere padding, stacked tears, vague pain, and uniform short-sentence stutter; rewrite the saved body if the check finds real issues.
   - Treat this quality gate as a reasoning pass over the actual saved artifacts.
12. Append a ledger record unless the user says not to.

## One-Shot Defaults

- Target length: 14,500-16,500 Japanese characters.
- Package shape:
  - `正文/正文.md`: Japanese body only.
  - `正文/标题.md`: Chinese working title, Japanese publish title, and short click title.
  - `角色提示词/角色提示词.md`: image-ready character prompts for all major characters.
  - `封面/封面.md`: cover/thumbnail brief, final image prompt, text layers, and status.
  - `作品资料.md`: blueprint, source notes, character count, checks, and ledger notes.
- Ending: closed happy ending or satisfying hopeful ending. A lingering romantic future is allowed, but the central accusation, wound, or contract conflict must be resolved.
- Trend/news/video-driven titles: show Chinese working title + Japanese publish title + seed + selected josei route + converted proof/romance mechanism + why the seed becomes a female-audience payoff.

## Hard Rules

- Do not turn a one-shot into a season outline.
- Do not confuse “source/lane/emotion selected” with “hot seed selected.” For dynamic hot-source work, user confirmation of a numbered seed is mandatory unless the user explicitly delegates the choice or supplies the exact seed.
- Do not paste real trending celebrities, scandals, crime, tragedies, sports trivia, or private-person details into the romance story. Convert only the underlying desire, anxiety, object, rule, ceremony, social pressure, proof mechanism, or relationship tension.
- Do not copy TikTok/YouTube creators, scenes, jokes, clips, songs, anime/game IP, dialogue, or exact video order. Extract only the hook mechanic and rebuild an original romance-fantasy premise.
- Do not leave the core injustice, romance recognition, or heroine's choice unresolved.
- Do not use literary padding: no long scenery blocks, no long psychology blocks, no decorative atmosphere when action, dialogue, evidence, or consequence should carry the beat.
- Do not pad to 15k with room atmosphere, noble etiquette filler, repeated tears, vague pain, or decorative beauty.
- Do not make the male lead solve everything while the heroine only cries. She must make at least one costly choice.
- Do not make `ざまぁ` happen by coincidence; it must follow from evidence, witness, law, contract, church rule, or the antagonist's own action.
- Do not preserve Chinese palace-drama terms or logic by surface translation. Convert their function into Japanese female-fantasy equivalents: social rank, engagement law, church record, aristocratic inheritance, public trial, salon rumor, convent exile, territorial confiscation, or title loss.
- Do not report "done" until the saved body count is in range or the user approved shorter output.

## Deliverable

For a full one-shot:

1. Chinese working title + Japanese publish title.
2. Subtype/theme route, hot seed if any, heroine wound, romance engine, zamaa/proof engine, happy-ending shape.
3. Brief one-shot blueprint.
4. Saved package path and primary file paths.
5. Body character count.
6. Codex AI self-check result and ledger status.
