# 15. Cross-Border Ecommerce API And Model Routing

## Core Decision

Cross-border ecommerce customers often prefer overseas model/API options because their business scenarios are overseas-facing:

- English and multilingual product copy
- Amazon, Shopify, TikTok Shop, independent sites, and overseas marketplace content
- overseas customer-service replies
- overseas SEO/search intent
- ad creative localization
- competitor and review analysis
- API integration into listing, CRM, customer-service, and content workflows

Do not present this as "foreign cheap API source" or "external token resale".

Present it as:

> 出海电商海外模型/API 接入与路由服务：多模型选择、BYOK/授权通道、用量管理、预算上限、数据脱敏、多语言电商工作流、成本报表。

## Positioning

Public line:

```text
我们帮出海电商团队把海外模型/API 接到商品、客服、素材、SEO 和广告工作流里，并做用量控制、模型路由、预算报表和合规边界。
```

Private line:

```text
如果你们做的是出海电商，只用单一国内模型可能不够。
海外平台的标题、广告素材、客服语气、SEO 关键词和本地化表达，确实更适合接多种海外模型做对比和路由。
我们做的不是卖裸 API key，而是帮你把模型选择、调用、预算、报表和数据边界管起来。
```

## Product Ladder

| Product | Price | Best For | Delivery | Boundary |
|---|---:|---|---|---|
| overseas API fit check | RMB 399 | wants to know which model/API fits | 30-45 minute diagnosis, scenario map, model/API shortlist | no live API integration |
| cross-border prompt pack | RMB 999 | self-service operators | English product, ad, SEO, customer-service prompts | no managed routing |
| overseas model trial | RMB 2,980 | cautious first test | 7 days, 1 scenario, limited usage, simple report | no production workload |
| cross-border API routing trial | RMB 4,980 | technical small team | 14 days, 1 workflow, routing plan, usage record | no SLA, no multi-system integration |
| cross-border ecommerce model pack | RMB 9,800 | team with real scenarios | 30 days, 2-3 scenarios, model comparison, budget alert, weekly report | no high-frequency production SLA |
| cross-border AI workflow package | RMB 29,800 | mature ecommerce team | model routing, prompt workflows, content/SEO/ad/customer-service templates, monthly review | no private deployment |
| cross-border API managed service | RMB 98,000+ | high-frequency API or multi-store team | custom routing, monitoring, usage dashboard, QBR, support | contract and legal review required |

## Service Modes

### Mode A: BYOK Routing

Customer brings their own official API key/account.

You provide:

- model routing logic
- prompt workflows
- usage logging
- budget alerts
- report templates
- scenario templates

This is usually the safest mode.

Use when:

- customer already has official overseas model access
- customer has compliance-sensitive data
- customer needs direct vendor relationship

### Mode B: Authorized Managed Access

You provide managed access only if upstream authorization permits integration, resale, and end-customer service delivery.

You provide:

- controlled backend access
- no raw API key export
- budget cap
- usage report
- customer scenario restrictions
- service contract and invoice

Use when:

- written supplier authorization exists
- use case is low-risk
- data is not sensitive or is anonymized
- customer accepts service boundaries

### Mode C: Consulting + Official Procurement

Customer buys directly from official overseas API/model provider. You provide consulting and implementation.

You provide:

- model selection
- account/procurement checklist
- workflow design
- prompt engineering
- usage dashboard plan
- integration support

Use when:

- customer wants direct official relationship
- legal/compliance review is strict
- resale authorization is unclear

## Cross-Border Ecommerce Scenarios

| Scenario | Models/API Need | Delivery |
|---|---|---|
| product listing localization | multilingual writing, native phrasing | title, bullet points, description, A+ content outline |
| ad creative localization | regional tone, hook testing | ad angles, hooks, scripts, image copy |
| overseas SEO | keyword intent, search phrasing | keyword library, title rules, content plan |
| customer-service replies | tone, policy, multilingual accuracy | FAQ replies, refund/return scripts, escalation rules |
| review analysis | sentiment and issue clustering | complaint themes, product improvement notes |
| competitor research | public information summarization | positioning, feature comparison, content angles |
| API workflow | stability, logging, cost control | routing, usage cap, dashboard, alert |

## Why Overseas Model Variety Matters

Use this explanation:

```text
出海电商不是只翻译中文。
海外平台的标题、广告、客服和 SEO 都有本地表达习惯。
不同模型在英文、日语、西语、广告语气、长文本、结构化输出上的表现不一样。
所以我们会按场景做模型选择和路由，而不是所有任务都用同一个模型。
```

## Model Selection Matrix

Do not publicly overclaim exact model superiority. Use scenario-based testing:

| Need | Evaluation Criteria |
|---|---|
| English product listing | accuracy, native phrasing, platform fit, hallucination rate |
| ad hooks | variation quality, emotional angle, clarity, policy risk |
| SEO keywords | intent match, structure, long-tail coverage |
| customer service | politeness, policy consistency, no overpromise |
| batch SKU generation | cost, speed, consistency, structured output |
| API integration | latency, error handling, logging, budget control |

Suggested evaluation process:

1. choose 1 real product
2. choose 2-3 candidate models/APIs
3. generate the same output set
4. score with customer: accuracy, tone, usability, cost
5. choose default model and fallback model
6. set budget cap and reporting

## Data And Compliance Rules

Cross-border ecommerce data can include personal information and business secrets. Do not treat it as harmless marketing copy by default.

Default rules:

- no raw customer lists unless authorized and necessary
- no private buyer messages without consent or anonymization
- no payment, address, phone, ID, or logistics personal information in prompts
- no ad account credentials in chat
- no marketplace account passwords
- no trade secrets unless contract permits
- use anonymized samples for model testing
- customer must confirm product facts, claims, and compliance wording

If the customer is China-based and sends personal information to overseas models, review cross-border data requirements with legal counsel before scaling.

Customer-facing line:

```text
出海场景可以用海外模型，但不要把客户手机号、地址、订单号、账号密码、支付信息直接发进模型。
我们会优先用脱敏样例、公开商品信息和业务规则来做测试。
```

## API Access Boundaries

Never promise:

- official status unless written authorization exists
- unlimited usage
- no ban
- bypass of geography/payment/KYC restrictions
- hidden relay
- raw shared API key export
- permanent fixed price
- guaranteed overseas platform approval

Use:

- authorized access
- BYOK routing
- managed backend
- usage cap
- budget alert
- model comparison
- fallback routing
- monthly report

## Pricing Structure

Quote in three parts:

```text
1. API/model usage budget
2. routing and management service fee
3. workflow/implementation service fee
```

Example:

```text
Cross-border model pack: RMB 9,800
- RMB 6,500 usage budget
- RMB 2,300 model routing and reporting service
- RMB 1,000 onboarding/workflow setup
```

For BYOK:

```text
BYOK routing support: RMB 599-2,999/month
Customer pays model provider directly. We charge routing, prompt workflow, logging, and reporting service.
```

## Sales Qualification Questions

Ask:

```text
1. 你们主要做哪个出海平台：Amazon、Shopify、TikTok Shop、独立站、还是其他？
2. 主要国家/语言是什么？
3. AI 主要用在 listing、客服、广告素材、SEO，还是 API 接入？
4. 现在有没有自己的海外 API key 或模型账号？
5. 是否需要我们做 BYOK 路由，还是需要托管接入？
6. 每月大概生成多少 SKU、脚本、客服回复或 API 请求？
7. 是否会涉及客户订单、聊天记录、邮箱、电话、地址等个人信息？
8. 是否需要合同、普票/专票、用量报表和预算上限？
```

## Sales Scripts

### Customer Says They Prefer Overseas API Options

```text
这个很正常。
出海电商的英文 listing、广告素材、SEO 关键词、客服语气，确实需要看海外模型的表现。
但我不建议直接买来源不明的裸 API。
更稳的方式是做模型/API 路由：先用真实商品测试 2-3 个模型，再确定默认模型、备用模型、预算上限和用量报表。
如果你们已有官方 API key，我们可以走 BYOK；如果需要托管接入，要先确认上游授权和数据边界。
```

### Customer Asks "Can You Provide Foreign API?"

```text
可以做海外模型/API 接入服务，但不是卖共享 key。
有三种方式：
1. 你们自带官方 key，我们做 BYOK 路由和报表；
2. 我们走已授权的托管接入，不导出 API key；
3. 如果授权边界不清楚，我们只做选型、采购和实施咨询。

这样合同、发票、数据边界和后续稳定性都更清楚。
```

### Customer Only Wants Cheap API

```text
如果只是找最低价裸 API，我们可能不是最适合。
出海电商真正麻烦的是：模型选型、海外语气、本地化 SEO、广告素材、客服回复、预算上限和接口稳定。
我们更适合帮你把 API 接成可管理的业务流程，而不是卖一个没人负责的 key。
```

### Technical Customer

```text
技术上我们可以按三层做：
第一，模型路由层：不同场景走不同模型；
第二，用量治理层：预算、日志、异常、报表；
第三，业务模板层：listing、广告、SEO、客服、多语言输出。
先用一个场景试 7-14 天，跑出成本和质量数据，再决定是否接生产流程。
```

## Product Bundles For Cross-Border Ecommerce

| Bundle | Price | Includes |
|---|---:|---|
| 399 overseas API fit check | diagnosis, model/API shortlist, data-risk notes |
| 2,980 overseas model trial | 7 days, 1 scenario, limited usage, simple report |
| 4,980 API routing trial | 14 days, 1 workflow, usage record, budget cap |
| 9,800 cross-border model pack | model comparison, 2-3 scenarios, weekly report |
| 29,800 workflow package | model routing + cross-border content/SEO/ad/customer-service templates |
| 98,000+ managed service | custom routing, dashboard, monitoring, support |

## Upgrade Path

Recommended path:

```text
399 overseas API fit check
→ 2,980 overseas model trial
→ 4,980 API routing trial
→ 9,800 cross-border model pack
→ 29,800 cross-border workflow package
→ 98,000+ managed API service
```

For low-budget ecommerce customers:

```text
99/199 cross-border copy card
→ 399 overseas API fit check
→ 999 cross-border prompt pack
→ 2,980 overseas model trial
```

## Delivery Checklist

Before activation:

- customer entity
- invoice type
- target countries/languages
- platform
- scenario
- data sensitivity level
- BYOK or managed access
- allowed models/APIs
- prohibited data
- budget cap
- rate limit
- usage report frequency
- output review owner
- fallback plan

## Monthly Report

```text
客户：
月份：

1. 使用场景：
2. 使用模型/API：
3. 总用量：
4. 成本：
5. 主要输出语言：
6. 质量评分：
7. 异常请求：
8. 数据风险事件：
9. 下月推荐模型/路由：
10. 是否建议升级：
```

## Compliance Checklist

Reject or escalate if:

- customer asks for bypassing geography, KYC, payment, or platform restrictions
- customer wants shared API keys
- customer wants to upload personal order data without consent/anonymization
- customer requests fake reviews, fake orders, platform manipulation, spam, or prohibited content
- supplier authorization cannot be documented for managed resale/integration
- customer wants guaranteed overseas platform approval, ranking, ROI, or GMV

## Final Positioning

Use this sentence:

```text
出海电商用海外模型是合理的，但不要把它做成来源不明的裸 API。我们把它做成可采购、可开票、可控预算、可看报表、可切换模型的 API 路由和业务工作流服务。
```
