# Trend Benchmarking

Use this when the user wants current, hot, platform-fit, or trend-driven economics and finance angle generation.

## Source Protocol

Pick the trend source by audience:

- Japan: Google Trends JP, Yahoo Japan finance/news, Bank of Japan/current government sources when policy appears.
- United States: Google Trends US, FRED/BLS/BEA/Fed data, SEC/company filings for market topics.
- Europe: Google Trends by country or EU-wide, ECB, Eurostat, national statistics.
- Chinese-speaking: user-provided platform signals, official data, exchange/company/regulatory sources as needed.

For current events, use browsing or reliable data tools. Search volume alone is not enough.

## Gate Order

Trend-driven selection has three gates:

1. Collection scope: what trends are fetched.
2. Selected topic lane: the user's chosen economics/finance lane.
3. Explainer viability: whether the seed can become a durable mechanism question.

Do not output celebrity, sports, or entertainment trends unless they reveal a finance mechanism: contracts, betting, platform economics, pricing, labor, risk, or regulation.

## Finance Trend Filter

Accept trends that can become:

- household cost, wage, rent, debt, education, retirement, or consumption questions;
- inflation, exchange rate, interest rate, central-bank, or recession explainers;
- stock, IPO, default, banking, real-estate, fund, ETF, crypto, or leverage-risk explainers;
- tax, pension, healthcare finance, local debt, welfare, infrastructure, or public-service tradeoffs;
- AI, platform, creator economy, monopoly, pricing, labor bargaining, or subscription economy explainers;
- gambling, scams, misleading ads, insurance, or behavioral-bias explainers.

Reject:

- pure price-ticker reactions without mechanism;
- trade-call topics like "will X stock rise tomorrow";
- unverified rumors;
- topics that require private or personalized financial advice.

## Output Format For Trend Title Batch

For each title, include:

- Chinese working title.
- Target-language publish title.
- Trend seed.
- Topic pack.
- Market/audience.
- Promised mechanism.
- Why now.
- Fact-check note.

Example:

```markdown
1. 中文标题：为什么日元贬值不只是旅游便宜？
   日语标题：円安はなぜ、旅行の話だけでは終わらないのか
   - Trend seed: 円安
   - Topic pack: macro-money-policy
   - Market/audience: Japan
   - Promised mechanism: import prices, wages, energy dependence, and household purchasing power
   - Check: current exchange-rate and CPI data before drafting
```
