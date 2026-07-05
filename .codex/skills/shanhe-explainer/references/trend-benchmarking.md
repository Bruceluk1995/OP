# Trend Benchmarking

Use this when the user wants current, hot, platform-fit, or trend-driven angle/title generation. For Japanese audiences, Google Trends JP is the default trend source:

`https://trends.google.com/trending?geo=JP`

## Source Protocol

1. Open Google Trends JP.
2. Use `Past 24 hours` for hot reactions, `Past 7 days` for less noisy topics.
3. Prefer categories that can become explanatory scripts:
   - Business and Finance
   - Climate
   - Jobs and Education
   - Law and Government
   - Politics
   - Science
   - Technology
   - Travel and Transportation
4. Use `Search volume` and `Recency` as heat signals, but do not chase heat alone.
5. If the page is hard to scrape, ask the user for exported CSV/RSS/copy text or use the browser-visible trend list manually.

## Gate Order

Trend-driven selection has three gates. Apply them in this order:

1. **Collection scope**: what to fetch from Google Trends, such as all categories or strong-related categories.
2. **Selected topic lane**: what the user chose earlier. This is a hard gate.
3. **Explainer viability**: whether the seed can become a durable structural question.

Do not confuse collection scope with output scope. If the user chooses "all categories" but already selected `japan-history-society`, the output must still stay inside Japan-focused history, society, economy, institutions, public systems, work/education, disaster governance, energy, demographics, local finance, or island-state geopolitics.

If fewer than the requested number pass the selected-lane gate, do not pad with off-lane trends. Say how many passed and ask whether to:

- broaden to another topic lane;
- mix in evergreen Japan-focused topics;
- output fewer titles.

## Japan-Focused Lane Filter

For `japan-history-society`, accept trend seeds only when the final angle is directly about Japan's domestic structure. Good seed families:

- weather/disaster -> disaster governance, local infrastructure, evacuation, aging, transport disruption;
- education/language -> exams, English learning, school pressure, skill markets, company requirements;
- health/wellness -> work fatigue, aging, medical boundaries, preventive care, local service markets;
- energy/prices -> electricity bills, fuel imports, grid structure, postwar or post-Fukushima choices;
- tax/pension/public finance -> household burden, aging, local government, fiscal tradeoffs;
- workplace/labor -> transfers, overtime, seniority, skill shortage, labor mobility;
- housing/local decline -> vacant houses, regional population loss, transport and care access;
- security/alliance -> US bases, sea lanes, constitution, island-state dependence.

Reject for this lane:

- overseas sports match results;
- foreign player transfer or roster gossip;
- celebrity relationship news;
- pure entertainment releases;
- crime/tragedy curiosity;
- topics whose only Japan connection is that Japanese users searched for them.

## Trend-to-Explainer Conversion

Do not output raw trend queries as titles. Convert each trend seed into a durable question:

- Event query -> "What structural problem made this event possible?"
- Celebrity/sports query -> use only if it reveals media, labor, money, law, education, fandom, or institutional incentives.
- Policy query -> "Who pays, who gains, and why is the obvious fix hard?"
- Weather/climate query -> connect daily discomfort to infrastructure, energy, agriculture, or public finance.
- Technology query -> explain what changed in capability, cost, power, or social behavior.
- International query -> connect geography, alliance, supply chain, credibility, or domestic politics.

## Selection Filter

Keep a trend seed only if it can support at least two of:

- Japan-native audience anxiety.
- Structural mechanism beyond personality gossip.
- Strong question with a counterintuitive answer.
- Durable value after the trend fades.
- Available facts that can be verified quickly.

Reject or downrank:

- Pure celebrity relationship gossip.
- Sports match results with no broader mechanism.
- Crime/tragedy topics that would become spectacle.
- Medical, legal, or financial claims that cannot be verified.
- Topics whose payoff depends on a Chinese internet joke.
- Trends that only fit a different topic lane than the user selected.

## Output Format For Trend Title Batch

For each title, include:

- Chinese working title.
- Japanese publish title.
- Trend seed.
- Topic pack.
- Why now.
- Promised argument.
- Risk/fact-check note if needed.
- Lane gate: accepted/rejected reason when using noisy all-category trend sources.

Example:

```markdown
1. 中文标题：为什么日本电费很难真正降下来？
   日语标题：なぜ日本の電気代は、下がりにくいのか
   - Trend seed: 電気代 / energy price query
   - Topic pack: japan-history-society + institutions-economy-power
   - Why now: household cost searches are rising
   - Promised argument: the issue is not only fuel price, but island energy security, grid structure, and post-Fukushima choices
   - Check: current price data before drafting
```

## Angle Mix

For 10 titles, prefer this mix:

- 3 Japan society/institution angles.
- 2 economy/money/tax/energy angles.
- 2 geopolitics or world-history angles connected to Japan.
- 2 science/technology/climate angles.
- 1 wildcard if the trend is unusually strong.

Do not make all 10 titles about the same trend, same topic pack, or same emotional register.
