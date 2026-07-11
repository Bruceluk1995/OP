# Male-Isekai Presentation Modes

Read this before planning or drafting any male-audience isekai, regardless of length.

## Mandatory Mode Gate

Before choosing structure, length, or package shape, present this fixed numbered menu unless the user already selected a combination explicitly in the current request:

> 请选择成品形式（可多选，例如 `2+4`）：
> 1. 传统小说网文・第一人称
> 2. 传统小说网文・第三人称
> 3. 动漫解说／推文口播・第一人称
> 4. 动漫解说／推文口播・第三人称

Allow one or multiple selections. Presentation mode and narrative person remain separate axes, but the menu makes the four valid combinations easy to choose. These are blocking creative choices. Do not infer them from `长篇`, `短篇`, `15,000字`, `YouTube`, `朗读`, `一口气看完`, or the existence of an outline.

When multiple options are selected, default to producing separate versions from the same premise so the user can compare them. Do not mix first and third person or novel and push presentation inside one body unless the user explicitly requests an intentional hybrid. Before drafting multiple full-length versions, state the expected output scope and follow any requested total/per-version length.

If the user says only `推文`, treat it as push narration presentation but still ask them to choose first person or third person through options 3 and 4. If they mean a different kind of promotional copy, adapt after they correct the label.

## Axis A: Presentation Mode

### Mode A1: Traditional Web Novel

- Unit of writing: scene and paragraph.
- Carry the story through action, dialogue, decision, sensory detail, and short inner commentary.
- Let important confrontations play out instead of summarizing every action.
- Use web-novel chapter or one-shot packaging.
- Keep the existing novel length targets and anti-water gates of the selected skill.

### Mode A2: Anime-Recap / Push Narration Copy

- Unit of writing: spoken line, shot, or information beat rather than literary paragraph.
- Open with the strongest premise-specific attention mechanism selected by `opening-innovation-engine.md`: result, evidence, cost, decision, rule collision, witness reaction, abnormal object, or another derived structure.
- Establish a clear causal or informational gap quickly, but vary what is withheld and the order in which it is revealed.
- Advance mainly in chronological cause-effect chains. Compress travel, scenery, and repeated emotion.
- Use colloquial narration, light internet language, and occasional short dialogue only when it sharpens a reaction or turn.
- Maintain frequent information changes: new obstacle, hidden rule, tactic, reveal, witness reaction, reward, status change, or next danger.
- Optimize for oral readability and picture matching. One line should normally express one action, reaction, or causal link.
- Long push copy is an extended narration script, not a long web novel with `男主` substituted for `俺`.
- Short push copy is a complete high-density recap segment, not a synopsis that skips the payoff.

## Axis B: Narrative Person

Choose this after presentation mode. Do not let the choice silently change halfway through a piece.

### First-person traditional novel

- Use `俺/私` as appropriate to the protagonist voice.
- Let the reader experience scenes through what the protagonist sees, knows, misreads, decides, and feels.
- Do not narrate hidden enemy thoughts unless the structure explicitly changes viewpoint.

### Third-person traditional novel

- Use close or limited third person by default rather than omniscient head-hopping.
- Keep scene depth, dialogue, action, and dramatized proof; third person does not turn the work into a summary.

### First-person push narration

- The protagonist narrates his own abnormal result and causal chain using `我/俺`.
- Keep a high-clarity hook, oral lineation, causal compression, dense turns, and visible payoff. The hook does not have to be result-first.
- Use short practical reactions, but do not expand into long interior monologue or literary reflection.
- Reveal only what the narrator can know, or clearly mark later-learned information.

### Third-person push narration

- Use `男主`, role labels, or names after the cast is established.
- Keep names sparse until necessary; role labels reduce listening load.
- External reactions, misunderstandings, and public proof can be shown directly by the narrator.

### Push-copy macro shape

1. Click promise: use the selected opening mechanism; do not force the strongest event/result into sentence one when another information order is stronger.
2. Causal gap: `只因/原来/殊不知` function without mechanically repeating the same connector.
3. Minimum setup: only the backstory needed to understand the current advantage or injustice.
4. Escalation loop: problem -> action/skill -> unexpected change -> reaction/consequence.
5. Core proof: the title promise becomes visible and specific.
6. Aftershock: reward, reputation, relationship, inventory, rank, territory, or new threat changes.
7. Ending: closed payoff for a one-shot; concrete next-pressure hook for a serial.

### Retention and language rules

- Title pattern: recognizable setting/time marker + protagonist/role + extreme event + unexpected consequence. Use the pattern, not copied wording.
- First 3-6 lines must identify protagonist, abnormal event, and contradiction or curiosity gap.
- Prefer concrete verbs and consequences over evaluation. Replace `他非常强` with the observable result of that strength.
- Vary connectors. Do not turn `没想到/不料/竟然/就在这时` into a verbal tic.
- In third person, keep names sparse until necessary; in first person, keep supporting-character labels stable to reduce listening load.
- Preserve setup-payoff logic even under compression. Do not produce a list of unrelated highlights.
- Remove subtitle timestamps, duplicated lines, source-dialogue debris, ASR errors, mistranscribed names, and fragments that cannot be understood without the original audio.
- Do not copy source titles, narration sentences, dialogue, scene order, character names, or IP-specific plot beats into an original story. Extract only presentation mechanics.

## Benchmark Basis

The push-copy rules above were abstracted from the local benchmark folder `C:\Users\Administrator\Desktop\下载\861072_弗兰动漫` on 2026-07-11:

- 116 Chinese subtitle files across episodic clips and eight long `一口气看完` compilations.
- 108 shorter files, with a median of about 1,914 characters and a median non-empty line length of about 10 Chinese characters.
- Repeated useful surface patterns: clear click promises, contradiction and information gaps, role labels, short oral lines, chronological cause-effect narration after the hook, dense reversals, visible proof, and consequence-led endings.

Treat those files as noisy subtitles, not clean prose. Their useful signal is structure and delivery; their recognition errors, stray original dialogue, repetitive connectors, and translation artifacts are negative examples.
