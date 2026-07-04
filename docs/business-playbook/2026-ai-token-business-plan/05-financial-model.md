# 05. Financial Model

## Base Assumptions

Date: 2026-06-14

Deadline: 2026-12-31

Two possible targets:

- company/business target: RMB 500,000 net profit
- personal target: RMB 500,000 personal commission income

Actual cost update:

- customer-facing reference price: RMB 1.2 for USD 1 face-value usage
- actual upstream cost: about 30% of that reference price
- internal cost per USD 1 face-value usage: about RMB 0.36
- raw gross profit per USD 1 face-value usage: about RMB 0.84
- raw gross margin before fees/tax/support/CAC: about 70%

Important: this is an internal calculation only. Do not put "3折成本" or upstream cost details in customer-facing materials.

## Updated Target GMV

The previous conservative plan assumed thin 10% economics. With actual cost at 30%, the year-end target should be planned around final all-in net margin, not raw gross margin.

### A. Company Net Profit Target

| Final Net Margin After All Costs | GMV Needed For RMB 500k Net Profit |
|---:|---:|
| 40% | RMB 1.25M |
| 35% | RMB 1.43M |
| 30% | RMB 1.67M |
| 25% | RMB 2.00M |
| 20% | RMB 2.50M |
| 15% | RMB 3.33M |

Recommended planning model:

- base GMV target: RMB 2,000,000
- all-in net margin floor: 25%
- target net profit: RMB 500,000
- stretch GMV target: RMB 3,000,000
- stretch profit buffer: RMB 600,000-900,000, depending on final execution quality

### B. Personal Commission Target

If the operator's commission is 10%-15% of collected revenue, RMB 500,000 personal commission income requires:

| Commission Rate | Collected Revenue Needed | Monthly Average From July To December | Daily Average From 2026-06-14 To 2026-12-31 |
|---:|---:|---:|---:|
| 10% | RMB 5.00M | about RMB 833k/month | about RMB 24.9k/day |
| 12% | RMB 4.17M | about RMB 694k/month | about RMB 20.7k/day |
| 15% | RMB 3.33M | about RMB 556k/month | about RMB 16.6k/day |

Planning rule:

- if the goal means company net profit, use the RMB 2M base plan
- if the goal means personal commission income, use the RMB 5M collected-revenue plan
- do not plan around the 15% best case unless the commission agreement is written and stable
- dashboard should separately track collected revenue, company gross/net profit, and personal commission

## Why Not Use 70% As The Profit Target

Raw usage margin is not final profit. The 70% raw margin can be eroded by:

- payment and platform fees
- VAT and corporate income tax
- refunds
- bad debt or postpaid leakage
- customer acquisition cost
- sales commission
- support labor
- setup and delivery labor
- tooling and monitoring
- upstream price changes
- abnormal trial abuse
- compliance and contract handling

So the operating dashboard should track three margins:

| Margin Type | Formula | Target |
|---|---|---:|
| Raw usage margin | received usage revenue - upstream usage cost | 60%-70% |
| Gross project margin | revenue - upstream cost - direct delivery labor | 40%-55% |
| Final net margin | revenue - all direct/indirect costs/tax/fees/CAC | 25%-35% |

## Low-Price Trial Economics

If the experience quota is USD 30 face-value:

`USD 30 x RMB 1.2 x 30% = RMB 10.8 internal cost`

| Trial Price | Internal Usage Cost If Full USD 30 Is Consumed | Gross Result Before Fees/Support | Decision |
|---:|---:|---:|---|
| RMB 2 | RMB 10.8 | about RMB -8.8 | only for invite-only connectivity checks, not public traffic |
| RMB 9.9 | RMB 10.8 | about RMB -0.9 | acceptable as CAC only if tightly capped and followed up |
| RMB 19.9 | RMB 10.8 | about RMB 9.1 | better public micro-trial floor |
| RMB 39 | RMB 10.8 | about RMB 28.2 | healthier developer/ecommerce trial |
| RMB 99 | RMB 10.8 | about RMB 88.2 | can include light support or task delivery |

Conclusion:

- RMB 9.9 for 1 day and up to USD 30 face-value can be used as an acquisition hook.
- It must not expose an API key or become unrestricted quota.
- It should be limited by identity, scenario, duration, rate, and abnormal-use rules.
- RMB 19.9 or RMB 39 is the better default when traffic quality is unknown.

## Monthly Ramp

Use RMB 2M GMV as the base company-net-profit target.

| Period | Monthly GMV | Cumulative GMV | Purpose |
|---|---:|---:|---|
| 2026-06-13 to 2026-06-30 | RMB 50,000 | RMB 50,000 | test paid trials, scripts, fulfillment |
| July | RMB 150,000 | RMB 200,000 | validate acquisition channels and first 29,800 orders |
| August | RMB 250,000 | RMB 450,000 | stabilize trial-to-growth conversion |
| September | RMB 350,000 | RMB 800,000 | close repeatable 29,800 packages |
| October | RMB 400,000 | RMB 1,200,000 | add 98,000 team packages |
| November | RMB 400,000 | RMB 1,600,000 | channel/referral and renewals |
| December | RMB 400,000-500,000 | RMB 2,000,000-2,100,000 | quarterly/half-year prepayments |

At RMB 2,000,000 GMV and 25% final net margin, the business reaches about RMB 500,000 net profit.

If the goal is RMB 500,000 personal commission, use this more aggressive ramp:

| Period | Monthly Collected Revenue | Cumulative Collected Revenue | Approx Personal Commission At 10%-15% |
|---|---:|---:|---:|
| 2026-06-14 to 2026-06-30 | RMB 50,000 | RMB 50,000 | RMB 5,000-7,500 |
| July | RMB 300,000 | RMB 350,000 | RMB 35,000-52,500 |
| August | RMB 600,000 | RMB 950,000 | RMB 95,000-142,500 |
| September | RMB 850,000 | RMB 1,800,000 | RMB 180,000-270,000 |
| October | RMB 1,000,000 | RMB 2,800,000 | RMB 280,000-420,000 |
| November | RMB 1,100,000 | RMB 3,900,000 | RMB 390,000-585,000 |
| December | RMB 1,100,000 | RMB 5,000,000 | RMB 500,000-750,000 |

This is the safer personal-income target because it still works at the 10% commission floor.

## Customer Count Model

| Average Order Value | Customers Needed For RMB 2M GMV | Customers Needed For RMB 3M GMV |
|---:|---:|---:|
| RMB 99 | 20,202 | 30,303 |
| RMB 599 | 3,339 | 5,008 |
| RMB 3,000 | 667 | 1,000 |
| RMB 10,000 | 200 | 300 |
| RMB 29,800 | 68 | 101 |
| RMB 98,000 | 21 | 31 |
| RMB 300,000 | 7 | 10 |

Low-ticket alone cannot reach the target efficiently. The correct structure is a funnel:

| Module | Target Count | Average Price | GMV | Role |
|---|---:|---:|---:|---|
| micro/affordable paid entries | 300 | RMB 39 | RMB 11,700 | paid lead filter |
| ecommerce task/service packages | 120 | RMB 999 | RMB 119,880 | small-customer conversion |
| enterprise/ecommerce trials | 80 | RMB 4,980 | RMB 398,400 | proof and qualification |
| growth packages | 30 | RMB 29,800 | RMB 894,000 | main GMV engine |
| team packages | 6 | RMB 98,000 | RMB 588,000 | profit and retention engine |
| Total | - | - | RMB 2,011,980 | reaches base GMV target |

For the RMB 5M personal-commission target, the funnel must lean much harder on RMB 29,800, RMB 98,000, and enterprise prepayments:

| Module | Target Count | Average Price | Collected Revenue | Role |
|---|---:|---:|---:|---|
| micro/affordable paid entries | 500 | RMB 39 | RMB 19,500 | paid lead filter |
| ecommerce task/service packages | 150 | RMB 999 | RMB 149,850 | small-customer conversion |
| enterprise/ecommerce trials | 100 | RMB 4,980 | RMB 498,000 | proof and qualification |
| growth packages | 70 | RMB 29,800 | RMB 2,086,000 | main sales engine |
| team packages | 14 | RMB 98,000 | RMB 1,372,000 | high-ticket retention engine |
| enterprise/custom packages | 3 | RMB 300,000 | RMB 900,000 | year-end accelerator |
| Total | - | - | RMB 5,025,350 | reaches personal commission target at 10% |

## Trial-To-Package Conversion Targets

| Funnel Step | Minimum Target | Strong Target |
|---|---:|---:|
| new lead -> paid micro/task order | 5% | 10% |
| paid micro/task order -> diagnostic/trial | 15% | 25% |
| trial -> RMB 29,800 growth package | 20% | 35% |
| growth package -> renewal/team package | 15% | 25% |
| team package -> referral | 20% | 35% |

The most important metric is not how many people buy RMB 9.9. It is how many RMB 9.9 or RMB 39 buyers become RMB 399, RMB 2,980, RMB 4,980, RMB 9,800, or RMB 29,800 customers.

For the personal commission target, the decisive metric is:

```text
weekly collected revenue from RMB 29,800+ packages
```

If weekly collected revenue from RMB 29,800+ packages is below RMB 150,000 for two consecutive weeks after August, the RMB 500,000 personal commission target is at risk.

## Cash Flow Rule

`Collect first. Activate second. Allocate third.`

Do not stock more than 7-14 days of upstream usage.

Do not offer postpaid terms by default.

At 30% cost ratio and December GMV of RMB 500,000:

| Collection Method | Peak Working Capital Need |
|---|---:|
| 100% prepaid | about RMB 0 |
| 70% prepaid, 30% T+15 | about RMB 45,000 |
| 50% prepaid, 50% T+15 | about RMB 75,000 |
| full monthly billing T+30 | about RMB 150,000 |
| full monthly billing T+45 | about RMB 225,000 |

The 30% cost structure can carry more risk than the old 90% cost structure, but postpaid still creates unnecessary financing pressure and bad-debt risk.

## Channel Commission Cap

Because raw margin is stronger, channel commission can be more competitive, but it must still be tied to collected cash and customer quality.

Recommended:

- micro/low-ticket orders: no commission, or fixed small reward
- diagnostics/trials: 5%-8% of received amount
- RMB 29,800+ packages: 8%-12% of received amount
- strategic channel with repeated enterprise customers: up to 15%, approved case by case
- never pay commission before customer payment clears
- claw back or pause commission for refund/chargeback/abusive use

## Stop-Loss Rules

Stop or restructure if:

- final net margin stays below 20% for two consecutive months
- project gross margin stays below 35% for two consecutive weeks
- customer acquisition cost exceeds 50% of first-order gross profit
- refund rate exceeds 3%
- support tickets exceed 3 per RMB 10,000 GMV
- low-price trial abuse exceeds 5% of trial users
- upstream authorization remains unclear
- upstream invoice/cost chain cannot support tax treatment
- one upstream provider exceeds 60% of usage supply

## Daily Margin Audit

Every day, record:

```text
1. 今日收款：
2. 今日消耗面值：
3. 今日实际上游成本：
4. 今日交付人工耗时：
5. 今日投流/获客成本：
6. 今日退款/异常：
7. 今日毛利：
8. 今日预计净利：
9. 今日个人提成测算，按 10% / 12% / 15%：
10. 是否有低价试用被滥用：
11. 哪个入口带来了高意向客户：
```

Decision rule:

- if RMB 9.9 buyers do not upgrade, reduce public exposure and push RMB 19.9/39 instead
- if RMB 39/99 buyers ask many questions, move them to RMB 399 diagnosis
- if trials consume support time but do not upgrade, tighten qualification
- if 29,800 packages close smoothly, increase content and channel spend around that package
