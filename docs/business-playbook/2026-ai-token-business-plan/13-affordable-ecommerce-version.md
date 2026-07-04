# 13. Affordable Ecommerce Version

## Core Decision

电商线需要一个更平价的版本。

但平价版不能做成“便宜 token 包”，也不能做成“低价人工代运营”。正确形态是：

> 平价任务卡 + 表单化下单 + 固定交付物 + 严格修改次数 + 不给 API key。

平价版的目的不是赚大钱，而是：

- 降低第一次付款门槛
- 筛出认真客户
- 让小店感到“我用得起”
- 用交付结果引导到 399、999、2,999、4,980
- 避免客户因为 29,800 锚点太高而直接流失

## Recommended Affordable Product Ladder

| Product | Price | Best For | Delivery | Boundary |
|---|---:|---|---|---|
| 9.9 商品小样 | RMB 9.9 | 评论/私信来的低意向客户 | 1 个商品标题 + 3 个卖点 + 1 条客服回复 | 只展示能力，不修改，不开会 |
| 39 单品快写卡 | RMB 39 | 小店想低成本试一次 | 1 个 SKU：标题 3 版、卖点 5 条、详情页结构 1 版、短视频开头 3 条 | 表单下单，24-48h，0 次修改 |
| 99 爆品文案卡 | RMB 99 | 有 1 个重点商品要优化 | 1 个 SKU：标题 5 版、主图文案 5 条、详情页结构、FAQ 10 条、短视频脚本 3 条 | 1 次小修，不电话沟通 |
| 199 小店上新卡 | RMB 199 | 一次上新 3-5 个商品 | 5 个 SKU 标题/卖点，10 条 FAQ，5 条短视频脚本 | 1 个类目，1 轮统一修改 |
| 299 客服减负卡 | RMB 299 | 每天客服重复问答的小店 | 30 条售前/售后 FAQ，10 条催付/物流/退换货话术 | 不接入客服系统，不代替人工客服 |
| 399 店铺诊断卡 | RMB 399 | 不知道从哪里用 AI 的商家 | 30-45 分钟诊断 + 1 页 AI 使用建议 | 可升级到 999/2,999 |
| 599 月度自助卡 | RMB 599/month | 轻量持续使用的小店 | 每月任选 20 个小任务点，异步交付 | 不含电话、不含系统接入、不含周报 |
| 999 小店上新包 | RMB 999 | 有明确一批内容要做 | 10 个 SKU + 10 条客服回复 + 5 条短视频脚本 | 1 个店铺，1 个类目，1 轮修改 |

## What Is A Task Point

For the RMB 599 monthly self-service card, define task points clearly:

| Task | Points |
|---|---:|
| 1 个商品标题 3 版 | 1 |
| 1 个商品卖点 5 条 | 1 |
| 1 个 SKU 详情页结构 | 2 |
| 1 条短视频脚本 | 2 |
| 1 场直播 10 分钟口播流程 | 3 |
| 5 条客服 FAQ | 2 |
| 5 条售后/物流/退换货话术 | 2 |
| 1 个活动页文案框架 | 3 |

Rules:

- 每月 20 点，过期不滚动
- 每次提交最多 5 个任务点
- 交付周期 24-72 小时
- 不接受紧急插单
- 不做电话会议
- 不做无限修改
- 不承诺流量、转化、排名、GMV

## Recommended Public Offer

Publicly push only three affordable choices:

```text
39 单品快写卡
99 爆品文案卡
199 小店上新卡
```

Use 399/599/999 as upgrade options after the customer sends material.

Why:

- too many low-price SKUs confuse first-time customers
- 39/99/199 creates an easy first payment
- 399 diagnosis filters customers who need advice
- 599 monthly card tests recurring willingness
- 999 is the first meaningful service package

## Public Copy

```text
电商小店不用一上来买几千几万的 AI 包。
我们做了平价任务卡：

39：单品快写卡，适合先试 1 个商品；
99：爆品文案卡，适合重点商品优化；
199：小店上新卡，适合 3-5 个商品一起做；
599/月：月度自助卡，适合持续上新但用量不大的小店。

全部按任务交付，不卖无限额度，不承诺爆单。
先把你这周最痛的任务解决掉，再决定要不要升级。
```

## Private Message Copy

When customer says "too expensive":

```text
可以，那你不要先看大包。
如果你是电商小店，我建议从平价任务卡开始：

39：做 1 个商品的标题、卖点、详情页结构和短视频开头；
99：做 1 个重点商品的完整文案包；
199：做 3-5 个商品的小店上新卡；
599/月：适合持续上新，但每月用量不大的小店。

这类平价版都是表单下单、异步交付，不含电话诊断和复杂修改，所以价格才能低。
你先发 1 个商品链接，我判断 39、99 还是 199 更合适。
```

When customer says "can you make it cheaper":

```text
可以换成更轻的版本，但服务边界也会变轻。
平价卡只做固定交付物，不开会、不接系统、不做无限修改。
如果你只是想试效果，39 或 99 就够；
如果要一批商品一起做，选 199；
如果要每个月持续做，选 599 月度自助卡。
```

When customer says "can I try for free":

```text
免费样例可以看非常小的一段风格，但不做完整交付。
如果你要能直接用的内容，建议从 39 单品快写卡开始。
这个价格已经是低门槛体验，交付边界也比较清楚。
```

## Landing Page Copy

Title:

```text
电商小店 AI 平价任务卡
```

Subtitle:

```text
不买大额度，不开复杂项目。按商品、客服、短视频任务交付，适合预算有限的小店先试。
```

Price section:

```text
39 单品快写卡
适合：先试 1 个商品
包含：标题 3 版、卖点 5 条、详情页结构 1 版、短视频开头 3 条
边界：0 次修改，24-48h 异步交付

99 爆品文案卡
适合：重点商品优化
包含：标题 5 版、主图文案 5 条、详情页结构、FAQ 10 条、短视频脚本 3 条
边界：1 次小修，48h 异步交付

199 小店上新卡
适合：3-5 个商品上新
包含：5 个 SKU 标题/卖点、10 条 FAQ、5 条短视频脚本
边界：1 个类目，1 轮统一修改，72h 异步交付

599 月度自助卡
适合：持续上新但用量不大的小店
包含：每月 20 个任务点，可做标题、卖点、FAQ、短视频、直播口播
边界：不含电话、不含系统接入、不含周报，任务点月底清零
```

CTA:

```text
先发 1 个商品链接，我帮你判断适合买 39、99、199 还是 599。
```

## Order Form

Every affordable order must use a form. Do not start with open-ended chat.

Required fields:

```text
1. 店铺平台：
2. 商品链接或商品图片：
3. 商品名称：
4. 类目：
5. 当前标题：
6. 当前卖点：
7. 目标人群：
8. 价格区间：
9. 不能写的词：
10. 想要风格：专业 / 种草 / 直播口语 / 简洁直接 / 高级感
11. 选择套餐：39 / 99 / 199 / 599
12. 是否需要发票：不需要 / 普票 / 专票
```

## Invoice Policy

Because low-price orders have administrative cost, set a clear invoice policy:

| Order Amount | Suggested Invoice Rule |
|---:|---|
| below RMB 199 | no separate special invoice; guide to platform order record or combine monthly |
| RMB 199+ | ordinary invoice can be supported if finance confirms |
| RMB 999+ | ordinary/special invoice and simple service order can be supported |
| RMB 4,980+ | contract, ordinary/special invoice, and delivery checklist should be standard |

Customer-facing wording:

```text
低价任务卡主要是体验和轻量交付。
如果需要专票和正式合同，建议从 999 小店上新包或 4,980 电商试用包开始。
199 以上可按财务规则处理普票；多笔小单也可以合并开票。
```

## Delivery Workflow

### Step 1: Customer Picks Card

```text
你先选一档：
39 适合试 1 个商品；
99 适合重点商品；
199 适合 3-5 个商品；
599 适合每月持续上新。

选好后我发你资料表，填完付款，按排期交付。
```

### Step 2: Customer Fills Form

```text
为了保证交付准确，平价卡都走表单。
你把商品链接、现有标题、卖点、目标人群、禁用词填好。
资料不完整会影响效果，也会延长交付时间。
```

### Step 3: Payment

```text
确认一下，本次是【套餐名】，金额【价格】。
交付内容：【交付物】。
交付时间：【24-72h】。
修改规则：【0/1 轮】。
付款后开始排期。
```

### Step 4: Delivery

Use a table:

| Field | Content |
|---|---|
| 商品 | name/link |
| 标题 | 3-5 versions |
| 卖点 | bullet points |
| 详情页结构 | section outline |
| FAQ | customer questions and replies |
| 短视频脚本 | hook, body, CTA |
| 风险提醒 | claims customer must confirm |

### Step 5: Upgrade

```text
这次平价卡已经交付。
如果你觉得能省时间，下一步有 3 个选择：
1. 199：继续做一批上新；
2. 599/月：适合每月持续上新；
3. 999：适合 10 个 SKU + 客服回复 + 短视频脚本一起做。
```

## Margin Guardrails

| Product | Max Token Cost | Max Human Time | If Exceeded |
|---|---:|---:|---|
| RMB 9.9 sample | RMB 0.5 | 0 min | auto only |
| RMB 39 quick card | RMB 2 | 5 min | remove manual review |
| RMB 99 copy card | RMB 5 | 12 min | reduce revision or raise price |
| RMB 199 listing card | RMB 12 | 25 min | batch with template |
| RMB 299 customer-service card | RMB 15 | 30 min | require FAQ source material |
| RMB 599 monthly card | RMB 60 | 90 min/month | cap task points strictly |

If a customer needs strategy, calls, repeated revisions, brand tone calibration, or invoice/contract support, do not keep them on the cheap card. Move them to 399, 999, 2,999, or 4,980.

## Risk Controls

Reject these requests:

- fake reviews
- fake orders
- fake transaction screenshots
- false medical/health/beauty/financial claims
- guaranteed ranking, conversion, traffic, GMV
- unlimited revision
- urgent same-day delivery at low price
- API key, shared account, raw token access

## Daily Review For Affordable Version

```text
日期：

1. 今日平价卡咨询数：
2. 今日付款数：
3. 成交档位：9.9 / 39 / 99 / 199 / 299 / 599
4. 平均交付耗时：
5. 平均 token 成本：
6. 是否有人要求超范围修改：
7. 是否有人升级到 399/999/2,999：
8. 哪个价格最容易成交：
9. 哪个价格最容易亏时间：
10. 明天要删除/收紧/涨价的边界：
```

## Final Rule

Affordable does not mean vague.

平价版必须比高价版更标准、更少沟通、更少修改。

If the cheap version requires custom discussion, it is no longer a cheap version. It is a discounted consulting project, and it should be stopped or repriced.
