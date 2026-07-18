# Google Trends JP To Isekai Skill

Use this when the user wants 热点, Google Trends JP, 蹭热点, or trend-driven skill/cheat selection. If the user wants 逆天新闻, 离谱新闻, 奇葩新闻, or says Trends items are boring, switch to `absurd-news-benchmarking.md`.

The goal is not to write a real-world news story. The goal is to extract the hot seed's fantasy function: what desire, fear, object, rule, competition, disaster, tool, or social pressure Japanese viewers are currently noticing, then convert it into a one-shot isekai skill and payoff.

## Source Protocol

0. Record `searched_at_jst` and `window_start_jst=searched_at_jst-24h`. Use only queries shown in Google Trends' `Past 24 hours` view or RSS entries whose activity/publication time is inside that window. A page crawled today is not proof that its item is current; reject undated or older entries and never widen to seven days.
1. Use Google Trends JP first only for plain trend requests:
   - Page: `https://trends.google.com/trending?geo=JP`
   - RSS fallback: `https://trends.google.com/trending/rss?geo=JP`
2. Use `scripts/google_trends_rss_preview.py --geo JP --limit 30` when browsing is awkward.
3. Keep collection scope and output scope separate:
   - Collection may include all trends.
   - Output must be male-audience Japanese isekai one-shot viable.
4. Reject seeds that cannot become a durable fantasy engine.
5. After choosing any viable seed, read `trend-theme-router.md` and select the best male-isekai theme route before proposing the cheat, title, or blueprint.

## Hot Seed Score

Do not rank by traffic alone. Score every candidate from 1-5:

- Everyday resonance: Is this close to daily life, money, work, school, family, food, heat/cold, commuting, apps, sleep, health, shopping, pets, or hobbies?
- Fantasy engine fit: Can it become a skill, dungeon rule, guild test, reward, rank, public proof, or zamaa mechanism?
- Male-audience payoff: Can it deliver visible strength, progression, OP reveal, tactical victory, public proof, or clean reversal?
- Safety and distance: Can it avoid real-person gossip, tragedy, politics, active scandals, and copyrighted plot dependence?
- Title clickability: Can a Japanese reader understand the fantasy promise without knowing the news background?

Recommended seed rule:

- Main pick needs everyday resonance >= 3 and total score >= 17/25.
- If everyday resonance is 1-2, use it only as a backup or transform it into a concrete everyday anxiety first.
- Prefer a lower-traffic lifestyle seed over a higher-traffic remote spectacle seed.
- If the top 10 trends are celebrity/science/sports names, collect more items before choosing.
- If the collected trends still lack conflict, ask or switch to absurd-news sourcing rather than forcing a weak trend.

## Mandatory User Selection Gate

- Collect 6-10 raw trends verified inside the rolling 24-hour window when available, score them, and present 3-5 viable numbered candidates. Return fewer if the strict window is thin.
- For each candidate, show the direct source, activity timestamp, `searched_at_jst`, raw seed, score, fantasy conversion, primary/backup route, one-shot promise, and risk note.
- Ask the user to choose a number or request another batch, then stop before final title, blueprint, prose, files, or ledger mutation.
- Choosing `Google Trends JP`, a subtype, payoff, or tone only selects the search lane; it is not approval of a concrete seed.
- Continue without the pause only when the user gives the exact seed/link/keyword or explicitly delegates the decision. State the selected candidate when using delegated choice.

## Trend Gate

Accept a trend seed only if it can become at least two of:

- a cheat skill;
- a dungeon rule;
- a monster ecology or boss pattern;
- a guild rank/test/event;
- a public proof or zamaa engine;
- a survival pressure;
- a reward/drop/crafting engine;
- a one-shot title hook Japanese readers can understand without real-world news context.

Reject or heavily transform:

- private celebrity gossip;
- crime/tragedy curiosity;
- real-person scandals;
- pure sports match results with no competition/ranking mechanic;
- political rage bait that would become a real-world argument instead of fantasy;
- seeds whose payoff depends on copying a copyrighted character or active franchise plot.

## Conversion Matrix

| Trend family | Convert to skill/engine | One-shot payoff |
|---|---|---|
| heat, rain, typhoon, disaster, weather | `天候予測`, `結界`, `氷結`, `排水`, `避難誘導`, `地形把握` | saves a town/dungeon party, gets public proof, exposes useless nobles |
| food, prices, cooking, restaurant | `保存`, `調理`, `発酵`, `鑑定`, `栽培`, `香辛料調合` | solves famine/poison/army supply, turns low skill into high value |
| AI, apps, gadgets, tech | `自動記録`, `最適化`, `鑑定`, `複製`, `遠隔操作`, `疑似思考` | beats bureaucracy/dungeon puzzles, OP productivity reveal |
| sports, tournament, athlete | `軌道予測`, `身体強化`, `反射`, `戦術眼`, `ランク戦` | guild tournament or duel, underdog tactical victory |
| travel, trains, airports, traffic | `転移門`, `地図作成`, `経路最短化`, `荷運び`, `安全帰還` | rescue, logistics, merchant/guild promotion |
| health, sleep, fatigue, wellness | `状態異常鑑定`, `回復`, `解毒`, `睡眠`, `疲労分配` | party survives hidden curse, healer underestimated zamaa |
| money, prices, tax, jobs | `価値鑑定`, `在庫管理`, `契約読解`, `徴税回避ではなく適正化`, `商談` | merchant/adventurer proof, corrupt official exposed |
| animals, pets, nature | `従魔契約`, `魔物翻訳`, `生態観察`, `繁殖管理` | tamer/familiar public payoff |
| school, exam, education | `試験対策`, `記憶整理`, `ルート知識`, `罠問看破` | academy exam, death flag avoidance, class reversal |
| electricity, phone, internet, utilities | `魔力節約`, `回線結界`, `充電`, `節電鑑定`, `通信妨害看破` | exposes wasteful city magic, protects guild infrastructure, proves low-cost skill |
| rent, wages, side jobs, shopping | `契約鑑定`, `相場感知`, `値切り`, `在庫圧縮`, `副業生成` | beats predatory contracts, merchant proof, support-class reversal |

## Output Format For Trend Title Batch

For each candidate:

```markdown
1. 中文标题：
   日语标题：
   - Trend seed:
   - Everyday resonance score:
   - Total hot-seed score:
   - Selected theme route:
   - Backup route:
   - Converted cheat/skill:
   - Subtype:
   - Why this route:
   - One-shot promise:
   - Payoff:
   - Risk note:
```

## Good Transformations

- `猛暑` -> a useless-looking ice skill that can only cool one cup, later saves a mine full of poisoned heat haze.
- `英会話` -> a translation cheat that does not translate words, only "intent", exposing a demon treaty trick.
- `整体` -> a fatigue-transfer skill that reveals the hero has been absorbing a whole party's debuffs.
- `電気代` -> a mana-efficiency skill that proves nobles are wasting city magic through broken contracts.
- `米価` or `値上げ` -> a storage/appraisal skill that stops guild food fraud and turns a mocked porter into a logistics hero.
- `通勤遅延` -> a route-optimization skill that saves a caravan and exposes a corrupt checkpoint.
- `睡眠不足` -> a fatigue-split or debuff-detection skill that reveals why a whole party keeps failing boss fights.
- `野球` or `サッカー` -> trajectory-prediction skill used in a guild projectile trial, not a real sports recap.
- `太陽フレア` -> usually downrank as remote spectacle; use only if converted into phone/network/electricity/weather disruption that ordinary viewers feel.

## Hard Rule

Do not make the story depend on the viewer knowing the exact trend. The trend is a spark, not the plot. The final one-shot must stand alone as Japanese male-audience isekai.
