# Flan-Style Push Narration Strict Mode

Use this for every male- or female-audience output selected as 动漫解说／推文口播. It is the default push surface profile, not an optional flavor.

## Non-Negotiable Axis Rule

Presentation and person are independent:

- First person changes only pronouns, knowledge boundaries, and brief self-reaction.
- Third person changes only role labels and access to external reactions.
- Both keep the same recap architecture, line compression, turn density, dialogue scarcity, and shot logic.

Never turn first-person push into web-novel scenes, inner-monologue prose, or complete dialogue exchanges. Convert role labels to 俺／私 or natural subject omission while preserving the push surface.

## Surface Contract

- One action, reveal, reaction, consequence, or causal link per non-empty line.
- For Japanese, target median line length 8-20, 90th percentile <=32, and maximum <=60 characters, excluding headings.
- Lines over 32 characters must be at most 12 percent.
- Lines containing two or more 、 must be at most 15 percent.
- Direct-quote lines containing Japanese quote marks must be at most 5 percent. Narrate most dialogue as intent, refusal, proof, or reaction.
- Use a turn or causal connector at least once per 12 lines. Vary ところが, すると, だが, しかし, しかも, その直後, 結果, そこで, and equivalent natural phrasing.
- Establish identity, abnormal event, and curiosity gap within the first 3-6 lines.
- Keep backstory to the minimum needed for the next payoff. Do not reset into biography after the hook.
- Every 3-6 lines should produce a new fact, test, reversal, witness reaction, evidence move, romance move, reward, status change, or danger.
- Do not add timestamps, copied source wording, ASR debris, or disconnected highlight lists.

## Person-Specific Mapping

First person:

- Use 俺／僕／私 only when needed; omit the subject naturally on adjacent lines.
- Keep self-comment to short practical punchlines.
- Narrate only known facts or clearly mark later-learned facts.
- Do not expand thoughts, sensory scene-setting, or dialogue because the viewpoint is intimate.

Third person:

- Use stable Japanese role labels such as 主人公, 男, 少女, 令嬢, 聖女, 公爵, or a name after identification.
- Keep labels sparse but clear enough for listening.
- External reactions may be narrated directly.

## Audience Adaptation

- Male: prioritize skill proof, tactical change, monster/item behavior, money/rank/drop, faction reaction, practical complaint, and visible payoff.
- Female: prioritize accusation, evidence, heroine choice, status/reputation movement, male-lead recognition, romance action, zamaa consequence, and dignity recovery.
- Female push remains recap narration. Romance does not authorize long psychology, decorative beauty, or dialogue-heavy scenes.

## Hard Validation

For every saved push body, run:

    python .codex/skills/story/scripts/validate-flan-push.py --body <正文.md> --person first

Use --person third for third-person output. A failure blocks delivery. Do not satisfy the validator by chopping a novel mechanically: reread the result and confirm every line is a coherent visual or information beat.
