# JP Isekai Self-Check

Use this before delivering any saved Japanese male-audience isekai episode. The goal is to catch story bugs, localization leakage, RPG-rule contradictions, and packaging omissions before the user sees them.

## Codex AI Audit First

This self-check is an AI reasoning pass, not a mechanical gate. Spend tokens here. Codex must reread the story context and reason like an editor before delivery.

Mandatory AI audit steps:

1. Read the current outline, previous episode tail, current body, `追踪/上下文.md`, `追踪/伏笔.md`, `追踪/时间线.md`, and `追踪/角色状态.md`.
2. Reconstruct the episode's cause-effect chain in prose: what problem enters, what skill/rule is tested, what the protagonist chooses, what witnesses see, what reward/pressure/consequence changes, and what hook remains.
3. Compare that chain against the tracking files and the previous episode. Look for contradictions, missing setup, motivation gaps, RPG-rule drift, unexplained drops/rewards, and fake payoffs.
4. Fix the prose, prompts, package, cover prompt, or tracking files before handoff if the AI audit finds a real issue.

## No Mechanical Gate

Do not use a mechanical scan as the self-check system. The default self-check is Codex AI reading and reasoning over the actual story files.

## AI Story Bug Audit

- Continuity: the first scene follows the previous episode's exact unresolved item, location, enemy, debt, quest, drop, rank, injury, or public pressure.
- Cause and effect: every new skill use, boss weakness, rescue, reward, guild judgment, or faction reaction has setup on the page or in prior tracking.
- Character state: names, roles, injuries, equipment, money, rank, companions, monsters, and faction reputation match the tracking files.
- Character presence: every major named character introduced or used by the script has one prompt; `角色提示词.md` does not add anonymous extras merely for a cover.
- Prompt language and identity: prompt bodies are Japanese-only and lock face, hair, body, clothing, colors, and worn accessories rather than scene behavior.
- Empty-hand reference: no prompt contains a symbolic possession, keepsake, weapon, tool, work object, skill effect, aura, summoned creature, action pose, camera, or background scene. Move those details to a cover/shot prompt.
- Heroine lane: named female leads/companions retain distinct Japanese male-audience isekai harem-anime heroine appeal unless the user or premise explicitly requires another visual direction; occupation or hardship alone never justifies an old/tired documentary design.
- RPG rules: skills, cooldowns, drops, ranks, levels, guild rules, monster behavior, and money values do not contradict earlier episodes.
- Combat logic: wins come from established ability, tactics, preparation, terrain, enemy misread, or OP reveal; do not randomly nerf or buff characters.
- Payoff logic: rewards, rank-ups, loot, territory benefits, or slow-life gains follow visible action and witness reaction.
- Protagonist agency: the protagonist tests, chooses, negotiates, fights, trades, hides power, reveals power, or accepts responsibility for a consequence. Ability self-punishment is not required.
- Ending hook: the final hook points to a concrete enemy, quest, guild notice, drop, debt, faction threat, map, or identity problem.
- No production leakage: body prose does not mention episode numbers, previous/next episode labels, readers, viewers, outline, prompts, cover, or writing workflow.

## Localization Audit

- No Chinese/xianxia terms from `references/terminology.md`.
- No Chinese webnovel role labels such as `男主`, `女主`, `反派`, `人设`, `爽点`, `剧情`, `大纲`, `细纲`, or `伏笔` in body prose.
- If the source is Chinese 古言/朝堂/宫斗, Codex AI must confirm the power structure was rebuilt for Japanese RPG/fantasy. Do not leave literal `皇帝/后宫/嫡庶/冷宫/赐婚/夺嫡/太监宫女/抄家灭族` logic in a non-Chinese isekai.
- For every Chinese court-drama object or institution, identify its function first: royal order, succession feud, inheritance pressure, faction conflict, exile, punishment, permit, tax, or guild pressure. Then express that function through `王命`, `王太子`, `貴族院`, `領主`, `冒険者ギルド`, `爵位剥奪`, `領地没収`, `王都追放`, or another target-lane mechanism.
- No Chinese punctuation in Japanese prose: replace `，` with `、`, and replace Chinese quote marks with Japanese dialogue punctuation where needed.
- Japanese RPG terms remain consistent: `スキル`, `ステータス`, `冒険者ギルド`, `魔石`, `魔物`, `従魔`, `ポーション`, `魔道具`.

## Package Audit

For per-episode delivery folders, require:

- `正文.md` or `body_ja.md`
- `标题.md` or `title.md`
- `角色提示词.md` or `character_prompts.md`
- `封面.md` or `cover_prompt.md`
- `封面.png` or `cover.png`

If a cover is expected, verify the image is an actual file, landscape 16:9, and the cover prompt asks for both the episode click-title and the series/work title inside the image.

Run `../../jp-isekai/scripts/validate-character-prompts.py <prompt-file>` and fix every finding before package delivery.
