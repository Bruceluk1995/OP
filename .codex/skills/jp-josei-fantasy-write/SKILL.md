---
name: jp-josei-fantasy-write
description: "Write Japanese female-audience fantasy romance prose. Use for drafting or rewriting 女性向け異世界恋愛, 悪役令嬢, 婚約破棄, ざまぁ, 溺愛, 聖女, 契約婚, 令嬢, 宮廷ロマンス, frontier slow life, cursed prince/duke romance, time-loop villainess, and Japanese prose localized away from Chinese fantasy or male-audience RPG defaults."
---

# JP Josei Fantasy Write

Write Japanese web-novel prose for female-audience fantasy romance. Use this for audience-facing scenes, chapters, rewrites, and localization.

## Required Reads

- Read `references/style-guide.md` before writing prose.
- Read `references/terminology.md` before writing if the source material contains Chinese fantasy terms or the user asks to avoid Chinese elements.
- Read `references/episode-blueprint.md` before drafting any episode/chapter prose, especially serial episodes that must hold viewer retention.
- Read `references/anti-ai-gates.md` before drafting and again before final delivery when the user mentions AI flavor, wateriness, weak prose, or when producing a saved episode file.
- Read `references/push-episode-delivery.md` when writing episode 2 or later, YouTube/recap/push narration, per-episode folders, character prompts, covers, or when the user complains about AI flavor, weak hooks, wateriness, or failure to connect the previous episode.
- Read `references/self-check.md` before final delivery of any saved episode, project-bound output, or per-episode folder.
- Read `../jp-josei-fantasy/references/project-memory.md` before writing any saved/project-bound episode, continuing a serial, or checking anti-homogenization.
- If the outline or user names a lane, read the best available benchmark/type-pack material before prose: project拆文, live benchmark card, project-local `女频幻想恋爱知识库/type-packs/{lane}.md`, then bundled `../jp-josei-fantasy-plan/references/type-packs/{lane}.md` as fallback.

## Drafting Workflow

1. Confirm or infer the target:
   - Default: Japanese prose, heroine-centered, emotionally legible, romance-forward, happy-ending direction.
   - Use first person `私` or close third person. Pick the viewpoint that best supports the heroine's dignity and romantic tension.
   - If the user asks for a finished/full episode, YouTube/朗读/推文 narration, a 6-episode short-season installment, or "完整正文" without another target, use 14,500-16,500 Japanese characters as the default delivery range.
   - If the user gives an episode length, target that character count; otherwise keep chat drafts concise or save long chapters to a file.
   - For a 15,000-character episode, treat length as a functional-density target, not padding permission: the episode needs enough concrete evidence, choices, social consequences, romance movement, hooks, and purposeful breathing beats to justify the length.
2. For project-bound output, load project memory before prose:
   - Read `大纲/细纲_第XXX章.md`; if it is missing, create the outline before writing.
   - Read the previous episode/chapter, `追踪/上下文.md`, `追踪/伏笔.md`, `追踪/时间线.md`, relevant `追踪/角色状态.md`, and relevant `设定/` files.
   - Run the `女频幻想恋爱知识库` ledger summary/check and change the candidate if it repeats too many fields.
3. Build the full episode blueprint from `references/episode-blueprint.md` before prose:
   - Start with the episode's biggest social/emotional bomb in sentence one: humiliation, accusation, broken engagement, witness testimony, contract reveal, curse symptom, public choice, or betrayal.
   - For episode 2 or later, bridge from the exact previous ending before moving into new action.
   - Set target emotion, episode position, episode promise, core payoff, cost/risk, and ending hook.
   - Use a five-part shape: cause, development, turn, climax, ending state.
   - Break the episode into dense/sparse beats with target character budgets.
   - Make dense beats carry humiliation, evidence, heroine choice, male-lead recognition, zamaa, tenderness, or social consequence.
   - Compress sparse transitions; do not let etiquette, scenery, or sadness become filler.
   - Preserve the selected lane's payoff loop. Do not flatten craft, saintess, villainess, contract marriage, palace-family, interspecies, loop, or strong-heroine stories into generic court romance.
   - For 15,000 characters, do not force a fixed beat quota. Plan enough concrete beats for this episode's rhythm, and make any long stretch serve evidence, public pressure, heroine choice, romantic recognition, legal/family consequence, cost, setup, aftershock, or next threat.
   - End with a romance question, social threat, witness, document, or next-stage proof.
4. Write in Japanese prose:
   - Use natural Japanese paragraphing and dialogue.
   - Let status, rank, magic, and setting emerge through action and social behavior.
   - Make `溺愛` visible through concrete choices: protection, listening, resources, public acknowledgement, remembering details.
   - Keep `ざまぁ` dramatic but coherent. The heroine can be kind without being passive.
5. Run the JP anti-AI pass from `references/anti-ai-gates.md`:
   - Remove generic abstract texture without deleting evidence, romance, or zamaa function.
   - Convert mood/summary lines into documents, hands, doors, witnesses, contracts, titles, injuries, choices, or social consequences.
   - Break uniform rhythm; keep dense beats visibly denser than transitions.
   - Delete or rewrite etiquette, scenery, sadness, beauty, or inner reflection that does not change information, reputation, relationship, evidence, risk, status, or the heroine's next action.
   - If prose was saved to a file, reread the saved file with Codex AI and revise any real issue directly. Do not use a mechanical gate as the default self-check.
6. Save long outputs to a file when the result would be too large for chat. For project-bound episodes, create or update the per-episode folder described in `references/push-episode-delivery.md`.
7. After saving a project-bound episode, update project memory:
   - Update `追踪/伏笔.md`, `追踪/时间线.md`, `追踪/角色状态.md`, and `追踪/上下文.md`.
   - Add one record to `女频幻想恋爱知识库/generated-ledger.jsonl` with heroine, wound, romance, pressure, proof, venue, aftertaste, and saved path.
8. Validate:
   - Count Japanese characters with Python.
   - For finished/full episode, YouTube/朗读/推文 narration, or 6-episode short-season prose, do not report completion below 14,500 Japanese characters unless the user explicitly approved a shorter length. If below target, continue expanding existing dense beats with more evidence movement, public pressure, heroine choice, male-lead recognition, legal/family consequence, romance shift, zamaa setup/payoff, or next threat.
   - Scan for Chinese/xianxia leakage using `references/terminology.md`.
   - If the source was Chinese 古言/宫斗/朝堂, verify the court-drama function was rebuilt for Japanese female-fantasy readers instead of directly carrying over emperor, harem, cold-palace, concubine, or legitimate/concubine-born systems.
   - Run the Codex AI story/package audit in `references/self-check.md`; fix story bugs, Chinese leakage, package omissions, unused character prompts, and cover-image problems before reporting completion.
   - Check that the heroine acts, the romance advances, and the scene promise matches the chosen tags.
   - Check the draft against `references/episode-blueprint.md`: target emotion delivered, dense beats expanded, sparse beats compressed, evidence/romance/status consequence present, and ending hook specific.
   - Scan the first 600 Japanese characters against `references/push-episode-delivery.md`: plot-bomb sentence, previous-episode recap bridge, concrete social pressure, and no generic AI-flavored filler.
   - Scan the whole draft against `references/anti-ai-gates.md`: no generic texture, stock summary lines, author explanation, uniform paragraph rhythm, or model/meta leakage.
   - For project-bound output, verify the outline was read, tracking files were updated, and the ledger record was appended.
   - If the prose reads like a synopsis, expand into scene-level action, dialogue, and internal reaction. If the prose hits length by padding, cut the padded text first and then expand real dense beats.

## Quality Bar

The result must feel like Japanese 女性向け異世界恋愛, not translated Chinese court fantasy and not male-audience RPG progression. The reader should understand the heroine's wound, why the male lead values her, what social injustice is being corrected, and why the happy ending feels emotionally deserved.
