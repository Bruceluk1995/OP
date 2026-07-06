# Finance Hot Source Router

Use when the user has no finance topic, wants 热点选题, asks for TikTok/YouTube, wants all sources, or rejects Google Trends/news as boring.

The goal is to choose a source strategy before angle generation. Finance topics need both attention and verification: a viral hook is useful only if it leads to a real mechanism.

## Source Menu

Ask this when the source is missing:

```text
你想从哪个热点入口找财经选题？

1. YouTube/TikTok 热门视频：适合找消费、打工、平台、投资焦虑、骗局和生活化标题钩子
2. Google Trends：适合看大家正在搜的钱/工作/房价/物价/市场问题
3. 财经新闻/市场新闻：适合政策、市场、企业、银行、地产、汇率、就业事件
4. 社媒吐槽/消费投诉：适合订阅陷阱、平台抽成、价格刺客、劳动权益、骗局拆解
5. 官方数据/央行/统计局：适合利率、通胀、工资、债务、税、养老金和宏观解释
6. 全选：多源交叉筛，选最适合做长讲解的题
```

## All-Source Mode

When the user chooses `全选`, collect small batches from multiple sources:

- 3-5 Google Trends seeds for the selected market.
- 3-5 YouTube/TikTok hooks when public access works.
- 3-5 finance/news seeds.
- 2-4 official data or regulator seeds.
- 2-4 evergreen household/platform/market mechanisms.

Then score all candidates together. Prefer a seed where attention and mechanism both exist.

## Scoring

Score each candidate from 1-5:

- Money pain: does it touch wages, bills, rent, debt, taxes, jobs, prices, retirement, scams, or market risk?
- Mechanism clarity: can it explain cash flow, pricing power, leverage, incentives, regulation, risk transfer, or behavioral bias?
- Audience fit: does it match the chosen market/audience?
- Evidence availability: can data or reliable sources verify the core claims?
- Non-advice safety: can it avoid personalized trading, tax, legal, or debt advice?

Recommended pick:

- Main candidate needs total >= 20/25.
- Reject "will this stock go up tomorrow" unless reframed into a general mechanism.
- Prefer ordinary-money hooks over pure ticker movement unless the market event reveals a broader risk.

## Source-Specific Use

| Source | Best for | Avoid |
|---|---|---|
| YouTube/TikTok | consumer traps, side hustles, creator economy, platform labor, scams, budgeting, investment anxiety | copying creators, exact scripts, trade-call hype |
| Google Trends | public question demand, jobs, rent, prices, taxes, currency, rates | search spikes with no mechanism |
| Finance news | policy, banks, markets, firms, real estate, regulation | rumor-driven price chatter |
| Social complaints | hidden fees, subscriptions, BNPL, platform rules, gig work, customer service | unverified individual accusations |
| Official data | CPI, wages, rates, debt, demographics, fiscal policy | data dumps without a viewer-facing question |

## Output Fields

For title batches, include:

```text
- Hot source mode:
- Source seed:
- Source type:
- Market/audience:
- Topic pack:
- Promised economic mechanism:
- Why now:
- Fact-check/source note:
- Advice-risk note:
```

## Hard Rule

Never turn viral finance content into trade advice. Extract the mechanism, verify facts, and explain who pays, who gains, and where risk moves.
