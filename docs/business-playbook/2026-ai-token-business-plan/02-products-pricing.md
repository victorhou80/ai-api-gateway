# 02. Products And Pricing

## Product Strategy

Do not sell the cheapest usage. Sell controlled, auditable, business-ready AI usage.

Internal cost update on 2026-06-13: actual upstream cost is about 30% of the customer-facing face-value price. If the reference price is RMB 1.2 for USD 1 face-value usage, the internal cost is about RMB 0.36 for USD 1 face-value usage. This creates room for controlled low-price trials, but the public product should still be service, reporting, budget control, contract/invoice handling, and support. Do not disclose "3折成本" in customer-facing copy.

Public value proposition:

> Stable access, RMB settlement, ordinary/special VAT invoices, invoiceable procurement, usage reports, budget alerts, model routing, and technical support.

## Main B2B Packages

| Package | Price | Target Customer | Delivery | Renewal Trigger |
|---|---:|---|---|---|
| Micro connectivity check | RMB 9.9-39 | first-touch leads, anti-friction test; RMB 2 only as invite-only coupon | 24-48 hours, demo-only, 1 scenario, controlled capped usage, no API key export | same day follow-up |
| Affordable ecommerce task cards | RMB 39-599 | small ecommerce stores with low usage | fixed SKU/customer-service/short-video task cards, form-based order, async delivery | after delivery, upgrade to 399/999/2,999 |
| Light trial package | RMB 2,980 | cautious first-time enterprise leads | 7 days, 1 scenario, limited usage, simple usage record, 1 onboarding session | day 5 or 70% usage |
| Standard trial package | RMB 4,980 | small team validation | 14 days, 1 scenario, basic budget cap, simple report, 1 review call | day 10 or 70% usage |
| Ecommerce lightweight packages | RMB 399-2,999 | stores that cannot consume large usage packages | task-based SKU, customer-service, livestream, or short-video copy delivery | after delivery or when repeat task appears |
| Ecommerce value-added services | RMB 199-9,800/month | stores needing materials, ad guidance, SEO/search, or review | material production, ad test guidance, search optimization, monthly review | monthly renewal and package upgrade |
| Ecommerce standard trial | RMB 4,980 | ecommerce teams with invoice need | 14 days, 1 ecommerce scenario, basic usage record, delivery checklist | day 10 or after first batch delivery |
| Cross-border ecommerce API/model routing | RMB 399-98,000+ | cross-border teams preferring overseas model/API options | BYOK routing, authorized managed access, model comparison, multilingual workflows, usage reports | trial result, budget usage, or monthly review |
| Ecommerce monthly light managed package | RMB 9,800 | stores with continuous listing or customer-service workload | 30 days, small usage pool, weekly report, 1 workflow optimization | week 3 or 70% usage |
| Trial package | RMB 9,800 | first-time teams, studios, early tests | 7-14 days, basic setup, usage report, cost diagnosis | 70% usage or day 10 |
| Growth package | RMB 29,800 | content teams, ecommerce, customer service, knowledge-base users | 30-60 days, usage pool, budget cap, weekly report, basic support | 70% balance used |
| Team package | RMB 98,000 | teams with stable usage | 90-180 days, permissions, monthly review, optimization advice | 60% balance used or 30 days before expiry |
| Enterprise package | RMB 300,000+ | AI SaaS, education, marketing systems, high-frequency users | custom contract, dedicated support, monitoring, quarterly review | QBR and annual budget cycle |

## Low-Price Enterprise Trial Design

Enterprise users should have a low-price trial option. The goal is to reduce first-payment friction and produce real usage data, not to provide a discounted long-term service.

## Ecommerce Lightweight Packages

Ecommerce customers often cannot consume a large enterprise usage pool. Do not force them into RMB 29,800 or RMB 98,000 packages unless they have continuous team usage.

For ecommerce, sell task packages first:

| Product | Price | Use Case | Includes | Limit |
|---|---:|---|---|---|
| ecommerce AI sample | RMB 9.9/19.9/39 | first-touch lead; RMB 2 only as invite-only coupon | 1 product sample, title/selling-point/customer-service reply preview | demo only, no API key, no full delivery |
| single-product quick card | RMB 39 | very small store first payment | 1 SKU title/selling-point/detail outline/short-video hooks | form order, async delivery, no revision |
| hero-product copy card | RMB 99 | one important product | 1 SKU titles, main-image copy, detail outline, 10 FAQ, 3 short-video scripts | 1 minor revision, no calls |
| small-store listing card | RMB 199 | 3-5 products | 5 SKU titles/selling points, 10 FAQ, 5 short-video scripts | 1 category, 1 batch revision |
| monthly self-service card | RMB 599/month | low-usage store with continuous listing | 20 monthly task points for titles, FAQ, short videos, livestream copy | async only, no rollover, no calls |
| ecommerce prompt template pack | RMB 99-199 | self-service small shop | title, detail-page, customer-service, livestream, short-video templates | no manual diagnosis |
| store AI scenario diagnosis | RMB 399 | customer unsure where to use AI | 30-45 minute diagnosis and 1-page recommendation | no ongoing generation |
| 7-day small-store listing package | RMB 999 | low-SKU shop | 10 SKU titles/selling points, 10 customer-service replies, 5 short-video scripts | 1 store, 1 category, 1 revision |
| SKU content sprint | RMB 1,999 | batch listing | 30 SKU title/selling-point/detail-page structures, 20 FAQ items | customer provides product material |
| customer-service script package | RMB 2,999 | repetitive presales/aftersales questions | 50 FAQ replies, presales/aftersales scripts, negative-review reply principles | no fake reviews, no customer-service system integration |
| livestream/short-video package | RMB 2,999 | content cadence | 20 short-video scripts, 5 livestream outlines, campaign talking points | no traffic or GMV guarantee |
| ecommerce standard trial | RMB 4,980 | small team validation | 14 days, 1 scenario, delivery checklist, basic usage record, invoice available | no multi-store integration |
| ecommerce monthly light managed package | RMB 9,800 | continuous listing or customer-service work | 30 days, small usage pool, weekly report, 1 workflow optimization | 1-2 core scenarios only |

Positioning:

> 小店按任务买，团队按月托管，大团队再按企业用量管理。

When a customer says they cannot use that much:

```text
对，小店不适合一上来买大额度。
电商客户我们一般按任务做：SKU 标题卖点、客服话术、短视频脚本、直播脚本。
如果预算很敏感，可以先从 39、99、199 的平价任务卡开始。
跑完觉得能省时间，再升级 399 诊断、999 小店上新包或 599 月度自助卡。
```

Margin guardrail:

- price by deliverable, not by raw token quota
- affordable cards must be form-based and async
- no phone calls or open-ended consulting below RMB 399
- no special custom contract for low-price task cards
- define SKU/script/FAQ count before payment
- define revision rounds before payment
- cap internal usage and support time
- do not promise conversion, traffic, ranking, or GMV
- do not write fake reviews, fake orders, false advertising, or prohibited product claims

## Micro Trial / Connectivity Check

A 1-2 day micro trial is allowed, but it must be a controlled connectivity check, not a cheap raw-usage package.

Do not sell "RMB 2 for USD 30 real usable quota". With the updated 30% cost structure, USD 30 face-value usage costs about RMB 10.8 internally. RMB 2 still loses about RMB 8.8 before fees/support, and 48 hours is enough for a customer or script to consume it.

RMB 9.9 for 1 day and up to USD 30 face-value can be used as a controlled acquisition hook, but it must not become unrestricted raw quota. RMB 19.9 or RMB 39 is the healthier public micro-trial floor when traffic quality is unknown.

Safer micro-trial configuration:

| Item | Recommended Rule |
|---|---|
| name | 1-day AI connectivity check / 2-day enterprise micro trial |
| price | RMB 9.9, RMB 19.9, RMB 39, or invite-only RMB 2 coupon |
| duration | 24-48 hours |
| usage cap | cap by duration, scenario, face-value budget, request count, and internal risk rules |
| suggested cap | for RMB 9.9: up to USD 30 face-value, 24 hours, 1 scenario, no key export; for RMB 19.9/39: 1-2 days with stricter identity and rate limits |
| access | controlled demo page or your backend; do not expose API key |
| scope | 1 scenario, no batch jobs, no file upload by default |
| rate limit | low QPS, daily cap, abnormal-use auto-stop |
| identity limit | one phone/company/payment account/device/IP cluster per trial |
| invoice | for micro amount, follow finance policy; for enterprise invoice demand, push RMB 399+ diagnostic or RMB 2,980+ trial |
| upgrade | upgrade within 48 hours to RMB 2,980/4,980/9,800; micro fee may be ignored or used as a token coupon |

Suggested public wording:

> RMB 9.9 is a 1-day controlled experience, not a raw API quota sale. It verifies whether one scenario can run, whether latency is acceptable, and whether the customer is serious enough to continue.

If a marketing hook mentions USD 30, write "up to USD 30 face-value experience budget under a controlled trial", not "USD 30 raw quota" or "随便调用".

Recommended trial ladder:

| Trial | Price | Best For | Includes | Excludes |
|---|---:|---|---|---|
| Light trial | RMB 2,980 | first enterprise contact | 7 days, 1 use case, limited usage, 1 onboarding, simple usage record, ordinary/special invoice available | multi-user management, custom development, SLA, complex API integration, monthly report |
| Standard trial | RMB 4,980 | small teams that need proof before approval | 14 days, 1 use case, basic budget cap, simple usage report, 1 review call, ordinary/special invoice available | production workload, multi-department use, advanced routing, dedicated support |
| Enterprise trial | RMB 9,800 | teams with invoice/contract need and near-term purchase intent | 14-30 days, budget alert, weekly report, basic support, contract, ordinary/special invoice | long-term SLA, private deployment, complex customization |

Rules:

- trial is prepaid
- trial is limited to one business scenario
- trial does not include unlimited support
- trial does not promise production stability for high-frequency workloads
- trial fee can be credited toward Growth package if upgraded within 7 days after trial ends
- trial customers must still pass risk review
- no shared account, no unlimited usage, no bypassing platform/upstream rules

Upgrade trigger:

> If the trial uses more than 70% of quota, needs more than 3 active users, needs a formal monthly report, or needs continuous use after the trial, recommend upgrading to the RMB 29,800 Growth package.

## Quote Structure

Use transparent split pricing:

`AI usage prepayment + management service fee + optional implementation fee`

Example for RMB 29,800:

- RMB 26,500 usage prepayment
- RMB 3,300 management service fee

The service fee protects margin and clarifies that the offer is not just markup on quota.

## Invoice Positioning

Being able to issue both ordinary VAT invoices and special VAT invoices should be explicitly included in B2B product packaging:

- for bosses: "company payment, contract, invoice, monthly usage report"
- for finance: "clear service item, invoice type, amount, and refund/red-invoice process"
- for procurement: "vendor-like service package instead of informal resource resale"
- for technical teams: "usage management plus documentation for internal reimbursement"

Suggested package wording:

| Package | Invoice message |
|---|---|
| Light trial package | supports ordinary/special invoice, useful for low-risk enterprise validation |
| Standard trial package | supports ordinary/special invoice, useful for internal proof before procurement |
| Trial package | supports ordinary/special invoice after payment, useful for internal pilot approval |
| Growth package | contract + invoice + weekly report, suitable for department budget |
| Team package | contract + invoice + monthly review, suitable for recurring enterprise use |
| Enterprise package | formal procurement process, invoice handling, and quarterly business review |

## Higher-Margin Add-Ons

| Offer | Price | Purpose |
|---|---:|---|
| AI usage diagnostic | RMB 399-999 | filter serious leads |
| BYOK model routing | RMB 599-2,999/month | customer brings own key, you provide routing/logging/templates |
| enterprise knowledge base | RMB 9,800 setup + RMB 1,980/month | easy first B2B project |
| ecommerce content workflow | RMB 3,999-14,800 | visible deliverable, higher margin |
| ecommerce material support | RMB 1,999/month | recurring content/material production |
| ecommerce SEO/search optimization | RMB 2,999/month | keyword, title, and content search planning |
| ecommerce ad testing guidance | RMB 3,999/month | material testing plan and data review, no ROI guarantee |
| ecommerce content growth card | RMB 5,999/month | materials + SEO + monthly review |
| ecommerce AI growth companion | RMB 9,800/month | AI workflow, material calendar, SEO, ad testing guidance, weekly review |
| cross-border overseas API fit check | RMB 399 | diagnose overseas model/API fit and data risk |
| cross-border API routing trial | RMB 4,980 | 14-day BYOK or authorized managed routing trial |
| cross-border model pack | RMB 9,800 | overseas model comparison and multilingual ecommerce workflows |
| cross-border managed API service | RMB 98,000+ | custom routing, monitoring, dashboard, and support |
| sales/customer-service copilot | RMB 19,800 setup + RMB 3,980/month | B2B scenario with recurring support |
| enterprise AI workshop | RMB 19,800/2 days | high-margin consultative sale |
| SLA support | RMB 5,980-9,800/month | retention and service margin |

## Low-Ticket Entry Products

Use these only as lead filters:

- RMB 99-199 template pack
- RMB 399 diagnostic
- RMB 999 pilot assessment

Do not let low-ticket customers consume senior support.

## Delivery Boundaries

Every order must define:

- service period
- quota/usage accounting method
- model/source boundaries
- service fee and usage cost split
- modification rounds
- support response time
- excluded custom development
- prohibited industries and use cases
- data restrictions
- refund method
- price-change handling

## Refund Rules

Suggested:

- diagnostics: refundable before appointment confirmation; non-refundable after delivery
- trial package: unused usage may be refunded according to contract; service fee is usually non-refundable after setup
- implementation: milestone-based refund; completed milestones not refunded
- monthly support: prepaid monthly; unused hours do not automatically roll over unless agreed
- abusive/illegal use: suspend immediately; consumed usage and delivered services not refunded

## Pricing Guardrails

- never discount below approved margin
- never publish a package above RMB 4,980 without a configuration card
- packages above RMB 29,800 must show service period, scenarios, usage/budget, reports, support, contract, invoice, exclusions, and renewal trigger
- do not offer unlimited usage
- do not promise fixed model price forever
- do not promise upstream models never fail
- do not accept postpaid terms except approved strategic customers
- do not sell packages below RMB 9,800 as full-service B2B accounts; RMB 2,980 and RMB 4,980 are trial-only offers with strict limits

## Recommended Revenue Mix

| Revenue Source | Target Share |
|---|---:|
| enterprise usage management | 50% |
| workflow/implementation | 25% |
| knowledge-base/tool setup | 15% |
| training/diagnostic/support | 10% |

This mix raises blended margin and reduces dependence on low-margin raw usage.
