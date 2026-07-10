# Google Trends JP To Josei Fantasy Romance

Use when the user wants 热点, Google Trends JP, 蹭热点, current topic selection, or trend-driven female-audience fantasy romance ideas. If the user wants 离谱新闻, 逆天新闻, or stronger story conflict than search terms, switch to `absurd-news-benchmarking.md`.

The goal is not to write a real-world trend story. Extract the hot seed's romance-fantasy function: what desire, fear, pressure, ceremony, object, public proof, relationship anxiety, family tension, or comfort need Japanese viewers are noticing, then convert it into a Japanese josei fantasy premise.

## Source Protocol

1. Use Google Trends JP first only for plain trend requests:
   - Page: `https://trends.google.com/trending?geo=JP`
   - RSS fallback: `https://trends.google.com/trending/rss?geo=JP`
2. Use `scripts/google_trends_rss_preview.py --geo JP --limit 30` from the `jp-josei-fantasy` skill when browsing is awkward.
3. Keep collection scope and output scope separate:
   - Collection may include all trends.
   - Output must be Japanese female-audience fantasy romance viable.
4. Reject seeds that cannot become a durable heroine wound, public proof, romance recognition, or social reversal.
5. After choosing a viable seed, read `trend-theme-router.md` and select the best josei fantasy route before proposing the title, heroine wound, male lead, proof object, or blueprint.

## Hot Seed Score

Do not rank by traffic alone. Score every candidate from 1-5:

- Everyday empathy: Is this close to daily life, money, work, school, family, food, heat/cold, commuting, apps, sleep, health, shopping, pets, weddings, beauty, or seasonal events?
- Heroine-wound fit: Can it become humiliation, false accusation, family coldness, stolen credit, contract pressure, public reputation damage, or ignored competence?
- Romance/zamaa engine: Can it create a protective-but-respectful male lead, public proof, contract reversal, church/legal record, social consequence, or earned devotion?
- Safety and distance: Can it avoid real-person gossip, tragedy, politics, active scandals, and copyrighted plot dependence?
- Title clickability: Can a Japanese reader understand the romance-fantasy promise without knowing the trend background?

Recommended seed rule:

- Main pick needs everyday empathy >= 3 and total score >= 18/25.
- If everyday empathy is 1-2, use it only as a backup or transform it into a concrete household, reputation, contract, school, or ceremony anxiety first.
- Prefer a lower-traffic lifestyle/emotion seed over a higher-traffic remote spectacle seed.
- If the top trends are celebrity/science/sports names, collect more items before choosing.

## Mandatory User Selection Gate

- Collect raw current trends, score them, and present 3-5 viable numbered candidates instead of silently choosing a main pick.
- Show source/date, seed, score, josei conversion, selected/backup route, heroine wound, proof/romance mechanism, one-shot or serial promise, and risk note.
- Ask the user to choose a number or request another batch, then stop before title lock, outline, drafting, files, or ledger mutation.
- Selecting `Google Trends JP`, a josei lane, emotion axis, or male-lead function only selects the search lane; it is not seed approval.
- Continue without the pause only for an exact user-supplied seed/link/keyword or explicit delegated choice, and state the delegated selection before continuing.

## Trend Gate

Accept a trend seed only if it can become at least two of:

- a heroine wound;
- a contract, engagement, inheritance, church, academy, salon, or court rule;
- a public proof or zamaa mechanism;
- a male-lead recognition scene;
- a comfort/healing or new-home promise;
- a title hook Japanese romance-fantasy readers can understand without real-world trend context.

Reject or heavily transform:

- private celebrity gossip;
- crime/tragedy curiosity;
- real-person scandals;
- pure sports match results with no competition, ceremony, reputation, or proof mechanic;
- political rage bait that would become a real-world argument instead of fantasy romance;
- seeds whose payoff depends on copying a copyrighted character or active franchise plot.

## Conversion Matrix

| Trend family | Convert to romance-fantasy engine | Strong routes |
|---|---|---|
| heat, rain, typhoon, disaster, weather | cursed duke shelter, frontier relief, saint barrier, public rescue, exposed useless nobles | `beloved-duke-frontier`, `saint-replacement-church`, `strong-heroine-status-gap` |
| food, prices, cooking, restaurant | competent lady saves household/territory supply, stolen recipe credit, social tea-party proof | `craft-job-competence`, `palace-family-inheritance`, `beloved-duke-frontier` |
| AI, apps, gadgets, tech | magic ledger, auto-scribe error, message misunderstanding, proof record, false accusation reversal | `letter-misunderstanding-comedy`, `engagement-annulment-zamaa`, `academy-game-knowledge` |
| sports, tournament, athlete | academy ball contest, knight trial, public duel as social proof, reputation ranking | `strong-heroine-status-gap`, `villainess-otome-game`, `engagement-annulment-zamaa` |
| travel, trains, airports, traffic | delayed carriage/portal, missed ceremony, frontier rescue, contract deadline | `contract-marriage-white-marriage`, `beloved-duke-frontier`, `time-loop-foreknowledge` |
| health, sleep, fatigue, wellness | saint/healer underestimated, curse diagnosis, overworked heroine recovery, protective care | `saint-replacement-church`, `beloved-duke-frontier`, `contract-marriage-white-marriage` |
| money, prices, tax, jobs | inheritance ledger, dowry contract, merchant daughter proof, family exploitation exposed | `palace-family-inheritance`, `craft-job-competence`, `engagement-annulment-zamaa` |
| animals, pets, nature | dragon/demon/familiar trust, monster prince culture gap, rescued creature as witness | `monster-demon-interspecies-romance`, `beloved-duke-frontier` |
| school, exam, education | magic academy false evaluation, hidden route, villainess avoids bad-end by proof | `villainess-otome-game`, `time-loop-foreknowledge`, `strong-heroine-status-gap` |
| weddings, fashion, beauty, seasonal events | dress/salon humiliation, public annulment, makeover as self-respect not male reward | `engagement-annulment-zamaa`, `contract-marriage-white-marriage`, `letter-misunderstanding-comedy` |

## Output Format For Trend Title Batch

For each candidate:

```markdown
1. 中文标题：
   日语标题：
   - Trend seed:
   - Everyday empathy score:
   - Total hot-seed score:
   - Selected josei route:
   - Backup route:
   - Converted proof/romance mechanism:
   - Heroine wound:
   - Male-lead recognition mode:
   - One-shot or serial promise:
   - Payoff:
   - Risk note:
```

## Good Transformations

- `猛暑` -> a discarded saint candidate can cool only one room, then saves a cursed frontier manor and proves the church mismeasured her power.
- `米価` or `値上げ` -> a "useless" accounting lady exposes ration fraud in her fiance's house and earns a duke's public protection.
- `睡眠不足` -> a heroine sees exhaustion curses in court records and saves the feared prince without becoming his reward object.
- `英会話` -> letters are mistranslated by a magic clerk; the heroine's intent-reading correspondence proves who forged the engagement annulment.
- `電気代` -> mana-light fees expose a noble family's hidden debt and stolen dowry.
- `野球` or `サッカー` -> turn into a public academy trial or knight tournament proof, never a real sports recap.

## Hard Rule

Do not make the story depend on the reader knowing the exact trend. The trend is a spark, not the plot. The final premise must stand alone as Japanese female-audience fantasy romance.
