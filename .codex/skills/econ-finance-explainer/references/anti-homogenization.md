# Anti-Homogenization

The channel should stay vertical: economics and finance explained through ordinary-life mechanisms. It should not repeat the same trap, same fictional town, or same villain.

## Required Preflight

Before generating titles, outlines, or full scripts:

1. Read `财经讲解知识库/generated-ledger.jsonl` if it exists.
2. Compare the candidate with the last 20 records.
3. Do not repeat more than three of these fields from any recent record:
   - topic_pack
   - audience_pack
   - market_region
   - domain
   - question_type
   - opening_analogy
   - mechanism_axis
   - risk_transfer
   - thesis_shape
   - target_language
   - trend_source
   - trend_seed
4. If the user explicitly asks for a similar topic, keep the requested field but vary at least three others.

## Variation Matrix

| Field | Options |
|---|---|
| topic_pack | household-money, macro-money-policy, markets-risk, public-finance-debt, platform-labor-capital, behavioral-risk-scams |
| audience_pack | japan, united-states, europe, chinese-speaking, international |
| market_region | Japan, US, Eurozone, UK, China, global |
| domain | household budget, labor market, housing, public finance, asset markets, credit, insurance, platform economy, AI economy, scams, gambling, retirement |
| question_type | who pays, why looks cheap, why risk spreads, why hard to exit, why effort fails, how leverage amplifies, why policy tradeoff, why free is not free |
| opening_analogy | salary notification, bill, casino table, theater seating, broken bucket, toll gate, app dashboard, local government project, school credential race, subscription trap |
| mechanism_axis | cash flow, leverage, interest rate, duration risk, information asymmetry, pricing power, labor bargaining, regulation, demographic pressure, platform traffic |
| risk_transfer | lender to borrower, platform to creator, employer to worker, government to future taxpayers, seller to retail investor, insurer to consumer, household to women/elderly, no transfer |
| thesis_shape | free is prepaid, efficiency became quota, debt hid income problem, risk was repackaged, credential became toll, monopoly taxes attention, policy solved one bill by creating another |

## Hard Blocks

Block a new script and redesign if it repeats all of:

- same topic_pack
- same audience_pack
- same question_type
- same opening_analogy
- same mechanism_axis
- same thesis_shape

Prefer changing opening analogy, mechanism axis, and market region first.

## Ledger Schema

Append one JSON line after each generated concept, outline, or script:

```json
{"date":"YYYY-MM-DD","title":"...","topic_pack":"household-money","audience_pack":"japan","market_region":"Japan","trend_source":"google-trends-jp","trend_seed":"...","domain":"household budget","question_type":"who pays","opening_analogy":"salary notification","mechanism_axis":"cash flow","risk_transfer":"platform to consumer","thesis_shape":"free is prepaid","target_language":"ja","path":"chat-only","notes":"one-line promise"}
```
