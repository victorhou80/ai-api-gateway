# 10. Step-By-Step Sales Sequence

This document is the exact execution playbook for moving a lead from first touch to payment, activation, renewal, and referral.

Core rule:

> Every message must create the next step. Do not send vague "are you there?" messages. Ask for one concrete decision, one piece of information, or one scheduled action.

## 0. Pipeline Stages

| Stage | Goal | Exit Condition |
|---|---|---|
| S0 new lead | get first reply and identify scenario | customer answers use case |
| S1 quick qualification | decide A/B/C/D lead grade | use case, team size, budget/invoice need known |
| S2 diagnosis booking | schedule 15-minute call or paid diagnostic | time confirmed |
| S3 diagnosis | identify pain, budget, decision chain | package recommendation clear |
| S4 quote | send 3-option quote | customer confirms preferred option or objection |
| S5 contract/invoice | collect entity and invoice details | contract/quote accepted |
| S6 payment | collect payment | payment received |
| S7 activation | start service | customer can use service |
| S8 usage management | report, alert, support | usage reaches renewal trigger |
| S9 renewal/upgrade/referral | retain and expand | renewal paid or referral made |

## 1. S0 New Lead: First Reply

### Trigger

Customer comments, private messages, submits form, or enters live room.

### Objective

Get one reply that reveals use case.

### Message 1A: Generic Lead

```text
你是想先算 AI 用量成本，还是已经有团队/API 需要稳定调用和管控？
我先不报价，先看你是什么场景，避免你买多或买错。
```

### Message 1B: Customer Asks Price

```text
价格要看场景和月用量。
你先回我 3 个信息，我直接判断适合哪档：
1. 主要做内容、客服、知识库，还是 API 接入？
2. 个人用还是公司团队用？
3. 是否需要合同、普票或专票？
```

### Message 1C: Customer Asks Cheap Token

```text
如果只找最低价裸用量，我们可能不是最适合的。
我们做的是企业 AI 用量托管：预算上限、用量报表、技术支持、合同、普票/专票。
如果你是公司团队使用，我可以先帮你测算月预算。
```

### Branch Handling

| Customer Reply | Next Move |
|---|---|
| "个人用" | send C-grade response and template/diagnostic |
| "公司团队用" | go to S1 qualification |
| "电商小店/用不了大包" | use ecommerce lightweight branch, ask SKU/platform/pain point |
| "要发票/专票" | upgrade priority, go to S1 |
| "只要便宜" | clarify service boundary once; if still price-only, C-grade |
| "共享账号/无限量/绕规则" | reject politely |

## 2. S1 Quick Qualification

### Objective

Classify the lead within 3 minutes.

### Required Questions

```text
我快速确认 5 点：
1. 你们团队几个人用？
2. 现在每月 AI 大概花多少钱？
3. 主要场景是什么？
4. 这笔费用需要公司付款、合同、普票/专票吗？
5. 这件事是本周要定，还是先了解？
```

### Grade Rules

| Grade | Criteria | Action |
|---|---|---|
| A | company/team, monthly spend 5,000+, invoice or contract need, decision within 30 days | book diagnosis immediately |
| B | team use but spend unclear or under 5,000 | sell diagnostic/trial |
| C | individual, low budget, no invoice need | nurture |
| D | prohibited/risky request | reject |

### A-Lead Message

```text
你这个不是普通个人使用，更像企业用量管理问题。
建议约 15 分钟，我帮你把月预算、适合套餐、合同/开票流程一次算清楚。
今天 15:00 或 20:30 哪个方便？
```

### B-Lead Message

```text
你们还没到直接上大包的阶段。
建议先做一次用量诊断或 9,800 试跑包，先跑真实数据，再决定要不要托管。
```

### C-Lead Message

```text
你现在更适合先用轻量工具或模板，不建议买企业托管包。
我可以发你一份预算测算表，等月用量超过 5,000 或需要发票时再聊正式方案。
```

### D-Lead Rejection

```text
这个需求我们不能接。
我们不做共享账号、无限量承诺、绕平台/上游规则的服务。
如果是正常企业业务使用，可以重新按合规场景评估。
```

## 3. S2 Diagnosis Booking

### Objective

Get a confirmed time. Do not keep chatting endlessly.

### Booking Message

```text
为了不空聊，我建议约 15 分钟做测算。
我会按「场景-用量-预算-发票-上线时间」给你一个明确建议。
你今天 15:00、17:30、20:30 哪个时间方便？
```

### If Customer Says "Just Send Price"

```text
可以，我可以先给区间：
微体验 9.9/19.9/39，轻试用包 2,980，标准试用包 4,980，企业试跑包 9,800，增长包 29,800，团队包 98,000。2 元只做邀约券，不公开投放。
但你适合哪档，要看月用量、团队人数和是否需要合同/专票。
如果不诊断就直接买，容易买多或买错。
```

### If Customer Delays

```text
没问题。我先把你放到本周待评估。
你只需要回复一个时间，我按 15 分钟给你算，不会硬推。
```

### CRM Action

Set:

- stage: diagnosis booking
- next action: call at agreed time
- lead grade
- invoice need
- expected package

## 4. S3 Diagnosis Call

### Call Structure

| Minute | Action |
|---|---|
| 0-2 | set agenda |
| 2-6 | business scenario |
| 6-9 | usage and cost |
| 9-11 | decision and invoice |
| 11-13 | risk and delivery boundary |
| 13-15 | recommendation and next step |

### Opening

```text
我先说明一下，今天不是直接推最贵套餐。
我会判断你们是否真的适合买托管服务；如果月用量太低，我会建议你们先别买。
我们按 5 个点走：场景、用量、团队、发票、上线时间。
```

### Question Sequence

1. Business:

```text
你们 AI 主要用在哪个业务环节？
是内部员工用，还是接到产品里给客户用？
```

2. Usage:

```text
每天大概多少请求？每月现在花多少钱？
有没有遇到账单失控、充值麻烦、接口不稳定、没人维护？
```

3. Team:

```text
现在几个人用？后面会扩到哪些部门？
是否需要按部门/项目看用量？
```

4. Invoice/procurement:

```text
这笔费用是公司付款吗？
需要合同吗？
需要普票还是专票？
付款主体和开票主体是否一致？
```

5. Decision:

```text
谁最终拍板？
预算大概在哪个区间？
是本周要上线，还是本月评估？
```

### Diagnosis Summary Template

```text
我复述一下：
你们现在不是单纯缺额度，而是要解决【场景】里的三个问题：
第一，【预算/稳定/团队权限】；
第二，【合同/发票/财务】；
第三，【用量报表/续费/售后】。

所以我建议你们不要买零散额度，先用【推荐套餐】跑【周期】。
```

### Recommendation Rules

| Situation | Recommend |
|---|---|
| just wants to see if it runs | RMB 9.9-39 micro connectivity check; RMB 2 invite-only coupon |
| monthly spend under 3,000 | diagnostic/template, no full package |
| monthly spend 3,000-5,000 | RMB 2,980 or RMB 4,980 trial |
| monthly spend 5,000-20,000, cautious first order | RMB 4,980 or RMB 9,800 trial |
| monthly spend 5,000-20,000, needs invoice and near-term use | RMB 29,800 growth |
| monthly spend 20,000+, team use | RMB 98,000 team |
| production SaaS / multiple departments | enterprise custom |

### Ecommerce Lightweight Recommendation Rules

If the customer is ecommerce and says they cannot use a large package, switch from usage-package selling to task-package selling.

Ask:

```text
你这个可能不适合买大包。
我先按电商任务判断：
1. 你们做哪个平台和类目？
2. 现在多少个 SKU？
3. 每月上新多少个商品？
4. 最卡的是标题卖点、客服话术、短视频脚本，还是直播脚本？
5. 是否公司付款、需要普票或专票？
```

Recommend:

| Situation | Package |
|---|---|
| only wants to see style | RMB 9.9/19.9/39 ecommerce sample; RMB 2 invite-only coupon |
| wants the cheapest usable paid version | RMB 39 single-product quick card |
| has one important product | RMB 99 hero-product copy card |
| has 3-5 products and low budget | RMB 199 small-store listing card |
| low usage but recurring monthly needs | RMB 599 monthly self-service card |
| SKU under 10 and self-service | RMB 99-199 template pack |
| does not know where to use AI | RMB 399 store AI diagnosis |
| wants 10 SKUs / small first batch | RMB 999 7-day small-store listing package |
| wants 30 SKUs or batch copy | RMB 1,999 SKU content sprint |
| customer-service questions repeat daily | RMB 2,999 customer-service script package |
| needs short-video/livestream content | RMB 2,999 content script package |
| small team, invoice, 14-day real trial | RMB 4,980 ecommerce standard trial |
| asks for ad guidance | RMB 299 pre-ad check or RMB 3,999/month ad testing support |
| asks for SEO/search | RMB 299 search title check or RMB 2,999/month SEO card |
| needs recurring materials | RMB 1,999/month material support or RMB 5,999/month content growth card |
| cross-border customer wants overseas API/model options | RMB 399 overseas API fit check or RMB 4,980 API routing trial |
| has official API key already | BYOK routing support RMB 599-2,999/month |
| needs managed overseas model access | RMB 9,800 cross-border model pack, only with authorization and data review |
| continuous listing/customer-service work | RMB 9,800 monthly light managed package |
| multi-store or multiple operators | RMB 29,800 growth package |

Use this close:

```text
你不用为了额度买单。
我们先按你这周最痛的任务做小包：SKU、客服、短视频或直播。
如果预算很敏感，先用 39、99 或 199 的平价任务卡。
跑完如果确实省时间，再升级 399、999、4,980 或 9,800。
```

If customer says even RMB 399/999 is expensive:

```text
可以，那我们先不上诊断和大包。
平价版有三档：
39 做 1 个商品的快写；
99 做 1 个重点商品的完整文案；
199 做 3-5 个商品的小店上新。

平价卡不含电话诊断和复杂修改，都是表单下单、异步交付。
你先发 1 个商品链接，我看 39 还是 99 合适。
```

If customer asks for materials, ad guidance, or SEO:

```text
这个就不是单次文案问题了。
我建议按「素材-搜索-投流-复盘」来拆：
1. 你现在最缺素材、搜索流量，还是投流测试？
2. 每月大概上新多少 SKU？
3. 是否已经投流，月预算多少？
4. 是否需要普票/专票？

我先判断你适合 299 检查卡、1,999 素材陪跑、2,999 SEO 月卡，还是 3,999 投流素材测试陪跑。
先说明：这类服务不承诺 ROI、排名、GMV，只做流程、素材和复盘优化。
```

If customer asks where materials come from:

```text
素材不要随便从网上扒，容易有版权和平台审核风险。
优先用你们自己的商品图、视频、说明书、详情页、客服问题和过去投放素材。
如果用供应商图、KOL/UGC、素材库或 AI 生成图，要先确认授权和使用范围。
竞品素材只能做结构和角度参考，不能复制图片、视频、文案或评价。

我会发你一份素材收集表，你把来源和授权情况一起填上。
```

If customer means material editing tools rather than photos:

```text
明白，你说的不是找照片，而是素材怎么处理和编辑。
这个要分工具链：
1. 商品图：Canva/稿定/创客贴/Photoroom/Photoshop；
2. 短视频：剪映/CapCut；
3. 团队模板：Figma；
4. 版本管理：飞书表格/Google Sheet/Notion/Airtable；
5. 批量生产：先做模板，再按 SKU 表批量替换。

我们可以做一套素材编辑工具包：模板、尺寸、命名、导出规则、审核清单和培训。
这样你后面不是每次重新做图，而是每个 SKU 都能复用流程。
```

If cross-border customer asks for overseas API/model options:

```text
出海电商用海外模型是合理的，但不要直接买来源不明的裸 API。
我先确认 5 点：
1. 你们做 Amazon、Shopify、TikTok Shop、独立站，还是其他？
2. 目标国家和语言是什么？
3. 主要用在 listing、广告素材、SEO、客服，还是 API 批量生成？
4. 你们有没有自己的官方 API key？
5. 会不会涉及订单、客户姓名、电话、地址、邮箱或聊天记录？

如果你们有官方 key，我们优先走 BYOK 路由；
如果需要我们托管接入，要先确认上游授权和数据边界。
```

## 5. S4 Quote

### Timing

Send quote within 2 hours after diagnosis.

### Configuration Card Rule

Before quoting any package above RMB 4,980, send a configuration card.

The card must show:

- price
- service period
- included scenarios
- usage/budget rules
- report frequency
- support level
- contract and invoice
- exclusions
- renewal or upgrade trigger

For RMB 98,000 or above, do not send only a package name. Explain exactly what the customer buys.

### Quote Message

```text
我按刚才沟通给你五档：

1. 微体验 9.9/19.9/39：1-2 天，只验证连通性和场景，不是真实大额额度；2 元只做邀约券。
2. 轻试用包 2,980：跑 7 天，验证 1 个场景。
3. 标准试用包 4,980：跑 14 天，适合小团队拿基础用量数据。
4. 增长包 29,800：正式团队使用，包含预算上限、用量周报、基础支持、合同、普票/专票。
5. 团队包 98,000：适合确认长期团队使用，包含月度复盘和更完整支持。

我的建议：先用【推荐套餐】。
原因：你们【团队人数/用量/发票/上线时间】已经符合这档，不建议买太小，也不建议一上来买最大。
```

### If Customer Wants RMB 2 For USD 30 Usage

```text
2 元只适合邀约连通性验证，不适合公开放量。
现在可以做 9.9 元 1 天受控体验，最高 USD 30 面值体验预算。
但它不是裸额度包：只跑 1 个场景，不导出 API key，不支持批量任务，不支持文件上传，异常高频会自动停止。
如果你要真实团队试跑，建议用 2,980 或 4,980 企业试用包。
```

### If Customer Says The Formal Package Is Too Expensive

```text
可以，我们不用一上来做 29,800。
第一次合作建议先用 4,980 标准试用包，跑 14 天，只验证一个核心场景。
试用结束后，如果你们 7 天内升级到 29,800 增长包，试用费可以抵扣一部分正式服务费。
这样你们内部也有真实用量和报告，比较容易审批。
```

### Quote Attachment Checklist

Send:

- quote
- service scope
- invoice information form
- payment method
- service boundary
- prohibited-use list
- next-step deadline

### Follow-Up 2 Hours After Quote

```text
报价你看完了吗？
我主要想确认两个点：
1. 套餐方向是否认可？
2. 开票是普票还是专票？
确认后我就可以出合同和付款信息。
```

## 6. S5 Contract And Invoice

### Objective

Remove procurement friction.

### Invoice Info Request

```text
开票信息麻烦按这个发我：
1. 普票还是专票；
2. 公司抬头；
3. 税号；
4. 接收邮箱；
5. 如果是专票，再补地址电话、开户行和账号。
另外确认一下：付款主体和开票主体是否一致？
```

### Contract Push

```text
合同里会写清楚：
服务内容、服务周期、预算上限、用量报表、开票方式、退款规则、禁止用途和上游价格变化处理。
这样你给老板/财务/采购看会比较完整。
```

### If Customer Needs Internal Approval

```text
你内部审批可以这样概括：
采购内容不是单独 token，而是企业 AI 用量托管服务；
包含模型接入、预算控制、用量报表、技术支持、合同和普票/专票。
先用【套餐】跑【周期】，再根据真实数据决定是否升级。
```

## 7. S6 Payment

### Payment Message

```text
我把合同、报价和付款信息发你。
这个服务是预付制，因为模型用量会实时产生成本。
财务确认到账后，我们当天建服务群并开通；发票按你提供的信息开具。
```

### Payment Reminder D1

```text
这边提醒一下，报价和服务排期我给你保留到明天 18:00。
如果今天能确认付款和开票信息，我们可以按当前方案启动。
```

### Payment Reminder D3

```text
这版报价今天到期。
如果你们本周启动，我建议今天先确认；如果暂时不启动，我这边就按下次报价重新核算上游成本和排期。
```

### If Customer Still Hesitates

```text
我判断你现在卡在【预算/审批/技术/发票】。
如果是预算问题，可以降到 2,980/4,980 企业试用包；
如果是审批问题，我补一份内部说明；
如果是技术问题，我们拉技术 15 分钟对一下。
你看卡在哪个点？
```

## 8. S7 Activation

### Activation Message

```text
款项已确认。
接下来我们做 4 件事：
1. 建服务群；
2. 确认使用场景和负责人；
3. 设置预算上限和余额预警；
4. 约 20 分钟 onboarding。
```

### API Integration Message

If the customer needs API/tool integration:

```text
接入资料我发你四项：
1. API 类型：OpenAI-compatible；
2. Base URL；
3. API Key；
4. Model Name。

你的工具如果支持 OpenAI-compatible API，一般填这三项就能测试。
如果工具要 Base URL，就填到 /v1；
如果工具要完整 Endpoint，就填到 /v1/chat/completions。

测试时先用非敏感内容，不要上传客户姓名、电话、地址、订单号、邮箱、支付信息或账号密码。
```

For technical customers, attach `17-openai-compatible-api-integration-guide.md` and `templates/api-handover-sheet.md`.

### Onboarding Checklist

- customer owner
- technical contact
- finance contact
- use case
- service start date
- budget cap
- balance alert thresholds: 70%, 85%, 95%
- report frequency
- support channel
- invoice status

### First-Day Check

```text
今天先确认两件事：
1. 是否能正常使用；
2. 当前场景是否和诊断时一致。
如果场景变化，先告诉我们，避免预算和用量估算偏掉。
```

## 9. S8 Usage Management

### Day 3 Message

```text
我们看了前三天用量，主要集中在【场景】。
目前消耗速度是【正常/偏快/偏慢】。
如果按这个速度，预计【日期】会到 70% 预警。
```

### Weekly Report Message

```text
本周用量简报：
1. 总消耗：【金额/额度】
2. 主要场景：【场景】
3. 异常消耗：【有/无】
4. 余额比例：【比例】
5. 下周建议：【维持/优化/升级】
```

### Abnormal Usage Message

```text
我们发现今天【时间段】用量明显偏高，可能和【场景/重试/批量任务】有关。
建议先暂停新增批量任务，确认是否正常业务消耗。
如果确认正常，我们再调整预算上限。
```

## 10. S9 Renewal / Upgrade

### 70% Alert

```text
你们这期已经使用约 70%，主要消耗在【场景】。
按当前速度预计【X】天后到 85%。
建议现在先确定续费方向，避免中途停用。
```

### 85% Upgrade Push

```text
你们这期已经到 85%。
如果继续按当前频率使用，不建议继续买小包，建议升到【套餐】。
原因是：用量更稳定、续费次数更少、月度报表和预算管理更完整。
```

### Renewal Close

```text
我给你保留当前续费方案到【日期】。
确认后只需要补充付款和开票信息；如果开票信息不变，我们按上期信息处理。
```

### Referral Ask

```text
你们这期已经跑顺了。
如果身边有团队也需要 AI 用量、合同、普票/专票和预算管理，可以介绍给我。
我会先帮他算预算，不会硬卖；成交后你们下期服务费可以做减免。
```

## 11. Multi-Day Follow-Up Map

| Day | Lead Status | Message Goal | Message |
|---|---|---|---|
| D0 | new lead | get scenario | "你主要是内容、客服、知识库还是 API？" |
| D0 | after diagnosis | send quote | "我按刚才沟通给你三档..." |
| D1 | quote sent | identify obstacle | "主要卡在预算、审批、技术，还是发票？" |
| D2 | no decision | create deadline | "报价和排期保留到明天 18:00。" |
| D3 | still no payment | downgrade or close | "如果本周不启动，我先按暂停处理。" |
| D7 | dormant | reframe | "本月继续推进，还是先放到下月预算？" |
| D14 | nurture | provide useful asset | "发你一份 AI 用量月报模板。" |
| D30 | reactivation | new budget cycle | "这个月 AI 预算是否重新评估？" |

## 12. What To Log After Every Interaction

In CRM, update:

- current stage
- last customer reply
- next action
- next action time
- expected package
- expected amount
- invoice type
- decision maker
- blocker
- probability
- owner

If any field is unknown, the next message should ask for that field.

## 13. Manager Review Rules

A lead is not allowed to stay in a stage without a next step:

- new lead over 24h without qualification: mark nurture or lost
- diagnosed over 2h without quote: sales owner penalty
- quote over 3 days without clear next action: downgrade or close
- paid customer without onboarding within 24h: support escalation
- usage over 70% without renewal alert: account-owner escalation
