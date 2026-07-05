# Anti-Homogenization

The channel should stay vertical: sharp historical, strategic, scientific, and institutional explanations. It should not become repetitive. Vary the question shape, opening analogy, evidence axis, and final thesis.

## Required Preflight

Before generating titles, outlines, or full scripts:

1. Read `山河讲解知识库/generated-ledger.jsonl` if it exists.
2. Compare the candidate with the last 20 records.
3. Do not repeat more than three of these fields from any recent record:
   - topic_pack
   - audience_pack
   - domain
   - question_type
   - opening_analogy
   - evidence_axis
   - thesis_shape
   - target_language
   - trend_source
   - trend_seed
4. If the user explicitly asks for a similar topic, keep the requested field but vary at least three others.

## Variation Matrix

| Field | Options |
|---|---|
| topic_pack | japan-history-society, world-history, geopolitics-strategy, institutions-economy-power, science-technology, social-common-sense |
| audience_pack | japan, united-states, europe |
| trend_source | google-trends-jp, evergreen, user-seed, none |
| trend_seed | original trend keyword or query cluster |
| domain | world history, modern history, foreign history, geopolitics, military logistics, institutional design, science history, everyday economics, social common sense |
| question_type | why failed, why survived, why misunderstood, how possible, what hidden constraint, which choice was least bad, why obvious answer is wrong |
| opening_analogy | historical scene, current news snapshot, internet meme, household object, workplace problem, school exam, map/geography image, bill/accounting image, island/resource anxiety, federal-state conflict, EU-border problem |
| evidence_axis | money, manpower, geography, logistics, succession, class, technology, law, information control, foreign pressure, climate, resource extraction |
| thesis_shape | strength became trap, visible villain was symptom, no good options remained, institution selected for bad behavior, geography wrote the bill, technology changed the game |
| tone | dry irony, cold audit, tragic clarity, amused dismantling, strategic warning, science curiosity |

## Hard Blocks

Block a new script and redesign if it repeats all of:

- same domain
- same audience_pack
- same question_type
- same opening_analogy
- same evidence_axis
- same thesis_shape

Prefer changing audience pack, opening analogy, and evidence axis first, because those most strongly alter the viewing experience.

## Ledger Schema

Append one JSON line after each generated concept, outline, or script:

```json
{"date":"YYYY-MM-DD","title":"...","topic_pack":"world-history","audience_pack":"japan","trend_source":"google-trends-jp","trend_seed":"...","domain":"foreign history","question_type":"why failed","opening_analogy":"map/geography image","evidence_axis":"logistics","thesis_shape":"strength became trap","target_language":"ja","path":"chat-only","notes":"one-line promise"}
```
