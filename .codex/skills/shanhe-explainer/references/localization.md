# Japanese and English Localization

## Shared Principles

- Preserve the argument architecture, not the Chinese sentence order.
- Keep planning notes, title explanations, and operator-facing summaries in Chinese unless the user asks otherwise.
- For Japanese-audience title batches, default to Chinese + Japanese bilingual title pairs: Chinese for operator judgment, Japanese for publish-facing use.
- Keep one idea per subtitle/narration line.
- Prefer vivid verbs over abstract nouns.
- Localize jokes only when they remain understandable without Chinese internet context.
- Explain Chinese historical titles, offices, dynasties, and idioms briefly on first use.
- For sensitive modern topics, keep claims evidence-based and avoid unsupported certainty.
- Choose audience before choosing analogies. A script for Japanese viewers, US viewers, and European viewers should not use the same opening object, institutional comparison, or final warning.

## Japanese Mode

Target: Japanese YouTube/Bilibili explainer narration for curious general viewers.

Voice:

- Use natural `です/ます` narration with occasional short fragments for punch.
- Use rhetorical pivots like `では、問題は何か`, `ここで重要なのは`, `つまり`, `ところが`, `ここが面白いところです`.
- Avoid overusing `本質的には`; rotate with `要するに`, `根っこにあるのは`, `決定的だったのは`.
- Use short lines and clear particles for TTS.

Avoid:

- Literal Chinese idioms.
- Overly academic kanbun style.
- Excessive honorifics for historical figures.
- Long nested clauses that TTS cannot breathe through.

Japanese title patterns:

- `なぜXは、Yできなかったのか`
- `Xの本当の敗因は、Zではなかった`
- `一見おかしなXを、構造から見る`
- `Xはなぜ最後まで生き残ったのか`

Audience pack: use `audience-packs/japan.md` after the user selects Japan, or when noninteractive fallback chooses Japan.

## English Mode

Target: conversational analytical explainer, not academic essay.

Voice:

- Use direct, clean sentences.
- Use pivots like `Here is the problem`, `The catch is`, `That sounds plausible, until you look at`, `So the real issue was not X, but Y`.
- Keep punchlines dry and understated.
- Prefer concrete nouns: roads, bills, maps, gates, payrolls, ports, incentives.

Avoid:

- "From ancient times to the present" openings.
- Overexplaining every name before the hook.
- Literal phrases like "the essence is" repeated too often.
- Imported Chinese memes that do not land in English.

English title patterns:

- `Why X Could Not Y`
- `The Real Reason X Failed`
- `How X Turned Its Strength Into a Trap`
- `The Hidden Constraint Behind X`
- `This Was Not About X. It Was About Y.`

Audience pack: use `audience-packs/united-states.md` after the user selects the United States, or when noninteractive fallback chooses US English. Use `audience-packs/europe.md` when the user says Europe, UK, EU, Germany, France, Italy, Spain, or the topic is clearly European.

## Audience Before Language

Language and audience are different. English can mean US, UK, EU-wide, or international. Japanese usually means Japanese viewers, but a Japanese-language script may still explain US or European topics through Japanese anxieties and analogies.

When unclear in interactive use, ask the audience first:

1. Japan
2. United States
3. Europe
4. Other/international

State an assumption and proceed only when the user asks the agent to decide or the workflow cannot pause for clarification.

## Name and Term Handling

- For Japanese, keep well-known Chinese names in kanji when conventional; add kana only if ambiguity matters.
- For English, use pinyin for Chinese names and add a brief role tag: `Sima Yi, the Grand Tutor`.
- Do not overload the opening with pronunciation notes.
- When the topic depends on a technical term, define it through action first, label second.

## Translation Direction

If adapting an existing Chinese script:

1. Extract thesis and beat outline first.
2. Rewrite each beat in the target language.
3. Add target-language pivots and line breaks.
4. Remove jokes that depend on Chinese homophones or platform memes.
5. Recount length after rewriting.
