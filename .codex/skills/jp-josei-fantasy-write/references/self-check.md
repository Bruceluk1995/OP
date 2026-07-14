# JP Josei Fantasy Self-Check

Use this before delivering any saved Japanese female-audience fantasy romance episode. The goal is to catch story bugs, localization leakage, and packaging omissions before the user sees them.

## Codex AI Audit First

This self-check is an AI reasoning pass, not a mechanical gate. Spend tokens here. Codex must reread the story context and reason like an editor before delivery.

Mandatory AI audit steps:

1. Read the current outline, previous episode tail, current body, `追踪/上下文.md`, `追踪/伏笔.md`, `追踪/时间线.md`, and `追踪/角色状态.md`.
2. Reconstruct the episode's cause-effect chain in prose: what pressure enters, what evidence appears, what the heroine chooses, what society sees, what the male lead changes, and what hook remains.
3. Compare that chain against the tracking files and the previous episode. Look for contradictions, missing setup, motivation gaps, unexplained rule changes, and fake payoffs.
4. Fix the prose, prompts, package, cover prompt, or tracking files before handoff if the AI audit finds a real issue.

## No Mechanical Gate

Do not use a mechanical scan as the self-check system. The default self-check is Codex AI reading and reasoning over the actual story files.

## AI Story Bug Audit

- Continuity: the first scene follows the previous episode's exact unresolved item, location, promise, witness, injury, contract, or public pressure.
- Cause and effect: every big reveal, rescue, testimony, punishment, or romantic concession has setup on the page or in prior tracking.
- Character state: names, titles, injuries, curse marks, relationship status, contract status, and public reputation match the tracking files.
- Character presence: `角色提示词.md` only lists characters who actually appear or are directly needed for the cover of this episode.
- Rules: saintess power, contract clauses, church authority, noble law, curse rules, and demon/magic rules do not contradict earlier episodes.
- Zamaa logic: public punishment follows evidence, witness, title, law, church record, or social rule; it is not only narrator judgment.
- Romance logic: the male lead's protection is shown through a specific action or cost, not generic possession or sudden devotion.
- Heroine agency: the heroine chooses, asks, refuses, signs, testifies, heals, reveals evidence, or pays a cost herself.
- Ending hook: the final hook points to a concrete witness, document, public choice, romantic question, injury, or relic problem.
- No production leakage: body prose does not mention episode numbers, previous/next episode labels, readers, viewers, outline, prompts, cover, or writing workflow.

## Localization Audit

- No Chinese/xianxia terms from `references/terminology.md`.
- Character names pass `../../story/references/character-name-policy.md`: core everyday names are short and anime-readable, fantasy full names have at most two segments, and long legal names do not repeat in narration or prompt headings.
- No Chinese webnovel role labels such as `女主`, `男主`, `反派`, `男二`, `人设`, `爽点`, `剧情`, `大纲`, `细纲`, or `伏笔` in body prose.
- If the source is Chinese 古言/宫斗/朝堂, Codex AI must confirm the social engine was rebuilt for Japanese female fantasy. Do not leave literal `皇帝/后妃/嫡庶/冷宫/赐婚/夺嫡/太监宫女/抄家灭族` logic in the prose unless the user explicitly requested a Chinese setting.
- For every Chinese court-drama object or institution, identify its story function first: marriage order, inheritance pressure, palace faction, public punishment, exile, hidden birth, or reputation attack. Then express that function through `王命`, `王太子`, `公爵家`, `王妃教育`, `側妃`, `異母妹`, `貴族院`, `神殿`, `社交界`, `修道院送り`, `爵位剥奪`, or another target-genre mechanism.
- No Chinese punctuation in Japanese prose: replace `，` with `、`, and replace Chinese quote marks with Japanese dialogue punctuation where needed.
- Japanese honorifics, titles, and institutions remain consistent with the setting.

## Package Audit

For per-episode delivery folders, require:

- `正文.md` or `body_ja.md`
- `标题.md` or `title.md`
- `角色提示词.md` or `character_prompts.md`
- `封面.md` or `cover_prompt.md`
- `封面.png` or `cover.png`

If a cover is expected, verify the image is an actual file, landscape 16:9, and the cover prompt asks for both the episode click-title and the series/work title inside the image.
