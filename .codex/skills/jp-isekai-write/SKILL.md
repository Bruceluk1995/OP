---
name: jp-isekai-write
description: "Write and package Japanese male-audience isekai episodes as traditional web-novel prose or anime-recap/push narration copy, with either first-person or third-person narration. Use for なろう系/カクヨム風 episodes, 男频异世界推文/动漫解说文案, 1万-2万字 installments, battle leveling, dungeon bosses, OP/龙傲天, exile reversal, rank/status growth, slow life, localization, and project-bound video assets."
metadata: {"openclaw":{"source":"https://github.com/worldwonderer/oh-story-claudecode"}}
---

# JP Isekai Write

Required global read: `../story/references/audience-comprehension-floor.md`. Apply its plain-core and five-line gates before opening selection, drafting, rewriting, and packaging.

Write Japanese web-novel episodes for male-audience isekai. Use this for final prose.

## Execution Profiles

- **Fast draft (default):** read the current outline/context and matching lane material; draft through protagonist choice and state change, blind-edit, and save the requested body. Do not run unrelated menus, cards, package generation, ledger checks, or surface lint.
- **Full project:** retain all project memory, tracking, ledger, delivery package, character prompt, cover, and self-check capabilities below.
- **Research/variation:** retain market browsing, dynamic benchmarks, type packs, and optional opening-card experiments when requested.

Choose one profile from the request. Full capabilities remain available; they are not simultaneous mandatory reads.

## Conditional Capability Reads

- Read `../jp-isekai/references/presentation-modes.md` only when presentation/viewpoint is unclear or the user asks to compare versions.
- Read `../story/references/flan-push-strict-mode.md` only for push formatting; its script is optional surface lint and never a quality verdict.
- Read `../jp-isekai/references/opening-innovation-engine.md` only when the user requests an opening-card experiment or the current opening needs variation. Cards are optional prompts.
- Read `references/style-guide.md` for full-project work or when style repair is needed; the fast profile uses the studio editorial core.
- Read `references/terminology.md` before writing if the source material contains Chinese fantasy terms or the user asks to avoid Chinese elements.
- Read `references/episode-blueprint.md` for serial continuity or a requested saved blueprint; the fast profile uses a compact change outline.
- Read `references/anti-ai-gates.md` before drafting and again before final delivery when the user mentions AI flavor, wateriness, weak prose, or when producing a saved episode file.
- Read `references/episode-delivery.md` when the user wants a finished episode, long-form serialization, per-episode files, character prompts, covers/thumbnails, YouTube, or project-bound output.
- Read `references/push-narration-protocol.md` whenever push narration mode is selected, and for serial continuity in that mode.
- Read `references/self-check.md` before final delivery of any saved episode, project-bound output, or per-episode folder.
- Read `../jp-isekai/references/project-memory.md` before writing any saved/project-bound episode, continuing a serial, or checking anti-homogenization.
- If the outline or user request names a subtype lane, read the loaded project benchmark card or `对标/{lane}/` report first when available, then project subtype notes, then the matching `../jp-isekai-plan/references/type-packs/{lane}.md` only as fallback. The episode must follow the selected lane's benchmark/payoff engine instead of generic isekai.

## Drafting Workflow

1. Resolve format/viewpoint only when missing; otherwise begin from the user's explicit choice:
   - Offer options 1-4 only when the choice is genuinely unclear; do not delay a clear request.
   - For multiple selections, draft separate labeled versions from the same premise unless the user requests another arrangement. Never blend viewpoints merely because multiple options were chosen.
   - Traditional first person commonly uses `俺`; traditional third person keeps scene depth and must not collapse into summary.
   - Push first person keeps the result-first hook, oral lines, causal compression, and dense turns through the protagonist's account; push third person may use `男主`, role labels, and external reactions.
   - Do not use `YouTube`, `朗读`, `推送`, `一口气看完`, length, or an existing outline as a substitute for either choice.
   - If no target is given, use approximately 12,000 Japanese characters for a complete episode in either presentation mode.
   - Treat 12,000 as a functional-density target, not a minimum gate or padding permission.
2. For project-bound output, load project memory before prose:
   - Read `大纲/细纲_第XXX章.md`; if it is missing, create the outline before writing.
   - Read the previous episode/chapter, `追踪/上下文.md`, `追踪/伏笔.md`, `追踪/时间线.md`, relevant `追踪/角色状态.md`, and relevant `设定/` files.
   - Run the `男频异世界知识库` ledger summary/check and change the candidate if it repeats too many fields.
3. Build the full episode blueprint from `references/episode-blueprint.md` before prose:
   - Start with the strongest concrete event. Use `opening-innovation-engine.md` only in the optional variation profile.
   - For episode 2 or later, bridge from the exact previous ending before moving into new action.
   - Set target emotion, episode position, episode promise, core payoff, cost/risk, and ending hook.
   - Use a five-part shape: cause, development, turn, climax, ending state.
   - Break the episode into change modules; character budgets are optional production aids.
   - Make dense beats carry skill experiments, monster combat, tactical adjustment, OP restraint/reveal, subordinate reaction, public proof, comic reaction, zamaa, practical reward/drop/rank-up, or new danger.
   - Compress sparse transitions; do not let travel, explanation, or mood become filler.
   - For a long target, add new conflict, choice, mechanism, cost, or consequence. Do not extend one proof through more tests or witnesses.
   - If the chosen route is battle leveling, do not replace the combat/progression payoff with shopkeeping or slow-life comfort. Each episode needs a monster/conflict, a skill use under pressure, a visible win or loss, and a drop/rank/skill/status consequence.
   - If the chosen route is OP dominance, do not fake tension by weakening the protagonist at random. Build tension through enemy misread, restraint, information gaps, collateral risk, subordinate/faction pressure, public identity, and the consequences of revealing power.
   - For any other subtype lane, preserve that type pack's required payoff loop. Do not flatten all lanes into generic guild errands, herbs, shopkeeping, or slow-life comfort.
   - End with a specific next-episode trouble hook.
4. Write in the selected presentation mode and narrative person:
   - Traditional: write scene-based Japanese web-novel prose. Use `俺` or close/limited third person as chosen; carry scenes through action, dialogue, choice, cost, reward, or consequence.
   - Push: follow `references/push-narration-protocol.md`; use one action/reaction/causal link per short line and make the title promise visibly pay off. The protocol applies to both first and third person.
   - In all combinations, reject literary padding and avoid long scenery or psychology blocks.
   - Use short inner-commentary beats for humor.
   - Keep paragraphs readable for web serialization.
   - Do not insert Chinese names, cultivation terms, sect terms, or Chinese monster taxonomy.
5. Run the JP anti-AI pass from `references/anti-ai-gates.md`:
   - Remove generic abstract texture without deleting plot function.
   - Convert mood/summary lines into objects, actions, dialogue, body response, price, rule, witness, or consequence.
   - Break uniform rhythm; keep dense beats visibly denser than transitions.
   - Delete or rewrite scenery, adjectives, atmosphere, or inner reflection that does not change information, risk, resources, status, relationship, or the protagonist's next action.
   - If prose was saved to a file, reread the saved file with Codex AI and revise any real issue directly. Do not use a mechanical gate as the default self-check.
6. Save long outputs to a file when the result would be too large for chat. For project-bound episodes, create the per-episode delivery folder described in `references/episode-delivery.md`.
7. Package delivery assets when applicable:
   - `正文.md`, `标题.md`, `角色提示词.md`, `封面.md`, and an actual generated `封面.png`.
   - Continue syncing a flat `episodes/episode_XXX_ja.md` only for compatibility when the project already uses it.
8. After saving a project-bound episode, update project memory:
   - Update `追踪/伏笔.md`, `追踪/时间线.md`, `追踪/角色状态.md`, and `追踪/上下文.md`.
   - Add one record to `男频异世界知识库/generated-ledger.jsonl` with protagonist, cheat, pressure, payoff, venue, aftertaste, and saved path.
9. Validate:
   - In strict push-surface work, optionally run `python .codex/skills/story/scripts/validate-flan-push.py --body <saved-body> --person <first|third>`. A `surface_fail` blocks only the requested surface format; `surface_pass` never approves story quality.
   - Run the studio blind-editor pass regardless of surface lint. Flowchart narration split into short lines is still a story failure.
   - Audit every major scene as `entry state -> pressure/choice -> exit state`. At least one of skill knowledge, combat position, inventory/drop, rank, reputation, territory, faction relationship, risk, or next objective must change. Travel, explanation, repeated awe, and status-panel restatement without a state delta must be compressed or removed.
   - Verify the episode promise is paid or meaningfully advanced, the win has a concrete result/cost, and the ending threat grows from the new state rather than appearing as an unrelated cliffhanger.
   - Count Japanese characters with Python.
   - Report the actual character count. If below a requested target, return to structure for a genuinely new turn or disclose the shortfall; never add repeated tests, witnesses, or procedure.
   - Scan for banned Chinese leakage using `references/terminology.md`.
   - If the source was Chinese 古言/朝堂/宫斗, verify the power structure was rebuilt for Japanese RPG/fantasy readers instead of directly carrying over emperor, harem, cold-palace, concubine, or legitimate/concubine-born systems.
   - Run the Codex AI story/package audit in `references/self-check.md`; fix story bugs, Chinese leakage, package omissions, unused character prompts, and cover-image problems before reporting completion.
   - Check the draft against `references/episode-blueprint.md`: target emotion delivered, dense beats expanded, sparse beats compressed, cost/reward/status consequence present, and ending hook specific.
   - In push mode, scan the opening and whole draft against `references/push-narration-protocol.md`: click promise, causal gap, concrete conflict, oral readability, information turns, title payoff, consistent narrative person, and no subtitle/ASR debris.
   - Scan the whole draft against `references/anti-ai-gates.md`: no generic texture, stock summary lines, author explanation, uniform paragraph rhythm, or model/meta leakage.
   - Confirm the prose stays colloquial and direct, with no long literary scenery or psychology passages.
   - For project-bound output, verify the outline was read, tracking files were updated, and the ledger record was appended.
   - If below target by more than 10%, expand existing dense beats rather than adding random scenes. If at target but padded, cut the padded text first and then expand real dense beats.
   - If a cover is expected, verify `封面.png` exists, is 16:9, includes the episode click-title and the series/work title, and is an actual image file rather than only a prompt.

## Quality Bar

The episode must feel like Japanese isekai, not translated Chinese xianxia or Chinese court drama with RPG labels pasted on top. The reader should immediately understand the social system, the cheat's rule, why the protagonist wants survival/profit/level-up/slow life, and what problem pulls him into the next installment.
