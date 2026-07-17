# Trend To Josei Fantasy Route

Use only after the user has selected a specific Google Trends JP seed, absurd-news seed, social-video seed, Japanese ranking/tag signal, Chinese women-oriented novel-site mechanism, or all-source candidate, or explicitly delegated that selection, and before choosing the final title, heroine wound, male lead, proof object, or outline. Source/lane/emotion selection alone is not seed selection.

This router maps a hot seed to a Japanese female-audience fantasy romance engine. These routes mirror `../jp-josei-fantasy-plan/references/type-packs/`, but the output may be either a standalone one-shot or a serial concept. For one-shots, compress the selected route into 12-18 meaningful beats and keep closure.

## Routing Protocol

1. Score the seed with the matching hot-source reference before route selection.
2. Extract the reusable female-audience function: humiliation, public accusation, family wound, unfair rule, hidden cost, ceremony, contract, proof object, care desire, letter/message failure, comfort/home desire, status gap, stolen credit, pursuit/redemption pressure, identity reversal, or relationship recognition.
3. Reject direct use of real people, scandals, crime, tragedy, political rage bait, copyrighted franchise plots, creator jokes, songs, or exact video scenes.
4. Choose one primary josei route and one backup route.
5. Convert the seed into a heroine wound plus proof/romance mechanism that fits the primary route.
6. Run the ledger check with `trend_seed`, `josei_route`, `heroine_wound`, `proof_object`, `male_lead_recognition`, and `payoff_engine` before drafting when a ledger exists.

## Josei Routes

| Route | Use when the seed suggests | One-shot or concept compression |
|---|---|---|
| `engagement-annulment-zamaa` | public humiliation, apology failure, cheating, false accusation, ceremony, reputation loss | public accusation -> evidence/witness -> better match recognizes her -> earned social consequence |
| `villainess-otome-game` | school/game/ranking/route/flag talk, "everyone misunderstood her", performance reputation | condemned role -> route knowledge or record proof -> flag reversal -> chosen sincere romance |
| `saint-replacement-church` | health, healing, fatigue, public service, stolen credit, institution mistake | fake/ignored saint -> church record or miracle proof -> false saint exposed -> respectful devotion |
| `contract-marriage-white-marriage` | hidden fees, contracts, weddings, cohabitation, practical care, deadline | cold contract -> shared problem -> mutual care/proof -> public choosing |
| `beloved-duke-frontier` | weather, shelter, home repair, food/care, cursed person, remote place | rejected heroine -> feared home/manor -> competence and care -> safe belonging |
| `craft-job-competence` | food, prices, work skill, before/after, room/shop transformation, product proof | mocked work -> visible result -> stolen credit exposed -> love respects her craft |
| `palace-family-inheritance` | money, inheritance, dowry, family exploitation, records, property conflict | family wound -> ledger/legal proof -> chosen family or lawful shelter -> status restoration |
| `time-loop-foreknowledge` | deadlines, travel delays, repeated failure, "if only I knew", bad-ending anxiety | memory/loop -> changed action -> suspicious ripple -> tragedy prevention and chosen love |
| `monster-demon-interspecies-romance` | animals, pets, monsters, culture gap, misunderstood outsider, rescue | feared being/creature trusts heroine -> cultural rule -> acceptance proof -> protective devotion |
| `strong-heroine-status-gap` | sports, trials, public tests, action, underestimated competence | status gap -> public challenge -> heroine acts -> honored recognition |
| `letter-misunderstanding-comedy` | messages, apologies, translations, wrong delivery, comment misunderstandings | misread letter/message -> comedic/social fallout -> truth proof -> warm confession |

## Selection Bias

- Prefer routes that create heroine agency plus public proof. A trend is not enough if the heroine only receives rescue.
- For romance-heavy requests, prefer `contract-marriage-white-marriage`, `beloved-duke-frontier`, `letter-misunderstanding-comedy`, or `monster-demon-interspecies-romance`.
- For revenge/catharsis requests, prefer `engagement-annulment-zamaa`, `saint-replacement-church`, `palace-family-inheritance`, or `craft-job-competence`.
- For video hooks with visible before/after, prefer `craft-job-competence`, `beloved-duke-frontier`, or `engagement-annulment-zamaa`.
- For search trends about prices, work, or money, prefer `palace-family-inheritance`, `craft-job-competence`, or `contract-marriage-white-marriage`.
- For health/fatigue/weather trends, prefer `saint-replacement-church` or `beloved-duke-frontier`.
- If a celebrity/person name trends, do not build on that person. Extract only an abstract function such as public attention, disguise, performance, apology, reputation, or fan ritual, then downrank unless the abstraction is strong.
- If a sports name trends, route through public trial, academy ranking, knight test, or social proof, never a real sports recap.
- If a remote science or space trend appears, downrank unless the story hook becomes weather discomfort, communication failure, health anxiety, travel disruption, or court ceremony inconvenience.

## Required Output Fields

When presenting trend candidates or building a blueprint, include:

```text
- Selected josei route:
- Backup route:
- Hot-source score:
- Why this route:
- Rejected route(s):
- Converted heroine wound:
- Converted proof/romance mechanism:
- Male-lead recognition mode:
- One-shot or serial compression:
- Safety transform:
```

## Example Mappings

- `電気代` -> primary `palace-family-inheritance`, backup `contract-marriage-white-marriage`; convert to magic-light fees exposing stolen dowry and family debt.
- `猛暑` -> primary `beloved-duke-frontier`, backup `saint-replacement-church`; convert to a weak-looking cooling blessing that saves a cursed frontier manor.
- `米価` or `値上げ` -> primary `craft-job-competence`, backup `palace-family-inheritance`; convert to ration ledger proof that the heroine has been sustaining the estate.
- Public apology trend -> primary `engagement-annulment-zamaa`; convert to a royal annulment apology collapsing because the heroine kept the real contract.
- Pet rescue video -> primary `monster-demon-interspecies-romance`; convert to a feared dragon/familiar choosing the heroine as truthful witness.
- Message misunderstanding video -> primary `letter-misunderstanding-comedy`; convert to forged letters, mistranslated intent, and a warm public correction.
