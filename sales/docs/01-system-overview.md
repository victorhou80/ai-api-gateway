# 01. 系统说明书

## 总体判断

`alphane-ai/sub2api-mod` 和 `alphane-ai/toklens` 可以组成一套 AI API 销售与交付系统：

```text
sub2api-mod = 后台、网关、发 Key、计费、限流、模型路由、用量记录
TokLens     = 客户门户、用量看板、Key 查询、请求明细、接入辅助
```

这套系统适合支撑以下业务：

1. API 试用包。
2. 电商轻量 AI 文案包。
3. 开发者 OpenAI/Claude 兼容 API 包。
4. 企业 API 托管包。
5. 带用量表、预算控制、合同发票的企业服务。

## sub2api-mod 是什么

`sub2api-mod` 是 AI API 网关平台，核心作用是：

1. 管理上游账号、API Key、OAuth 资源。
2. 为下游客户生成平台自己的 API Key。
3. 接收客户请求并转发到上游模型服务。
4. 记录每次请求的模型、Token、成本、耗时、状态。
5. 做余额、订阅、限流、并发、调度、分组。
6. 给管理员提供后台：用户、账号、分组、渠道、用量、支付、监控、风控。

客户真正调用的是它：

```bash
https://api.example.com/v1/chat/completions
https://api.example.com/v1/messages
https://api.example.com/v1/models
https://api.example.com/v1/usage
```

## TokLens 是什么

`TokLens` 是客户用量门户，核心作用是：

1. 客户输入 API Key，查询这个 Key 的用量和状态。
2. 客户登录后绑定多个 Key。
3. 看 Dashboard：请求量、Token、模型分布、成本口径、趋势。
4. 看 Usage：每条请求的 model、endpoint、token、cost、duration、created_at。
5. 给客户一个“账能看、量能查”的信任界面。

TokLens 自身不是上游模型网关，它通过环境变量连接 sub2api-mod：

```bash
SUB2API_PROXY_TARGET=http://sub2api:8080
NEXT_PUBLIC_SUB2API_BASE_URL=https://api.example.com
NEXT_PUBLIC_DEFAULT_LOCALE=zh
```

## 两者怎么配合

推荐架构：

```text
客户系统 / 电商工具 / 程序员 IDE / Dify / Coze / 自研系统
        |
        | Authorization: Bearer sk-客户key
        v
api.example.com
        |
        v
sub2api-mod
        |
        | 认证、限流、计费、模型路由、用量记录
        v
上游 AI 模型资源池

客户浏览器
        |
        v
portal.example.com
        |
        v
TokLens
        |
        | 查询 /api/v1 和 /v1/usage
        v
sub2api-mod
```

## 适合销售包装成什么

不要包装成：

```text
便宜 token
官方内部渠道
不限量
低价倒卖 API Key
```

推荐包装成：

```text
企业 AI API 接入托管服务
模型用量管理服务
出海电商 AI 内容生产 API 服务
开发者模型网关服务
AI 预算控制和用量报表服务
```

## 这套系统的商业价值

| 客户痛点 | 系统能力 | 销售表达 |
|---|---|---|
 不会接 API | OpenAI/Claude 兼容接口 | 一份 Key 即可接入主流工具 |
 不知道用了多少 | TokLens 用量看板 | 每一笔请求都能查 |
 害怕超预算 | 分组、余额、限流 | 可设置月预算和超额暂停 |
 需要公司报销 | 月度用量表 | 支持合同、普票、专票 |
 技术团队人少 | 接入文档和支持 | 帮你完成 API 接入 |
 电商用量不稳定 | 轻量包和试用包 | 先试一天，再按月升级 |

## 第一版必须跑通的闭环

```text
创建客户
  -> 绑定套餐分组
  -> 生成 API Key
  -> 客户调用 API
  -> sub2api 记录用量
  -> TokLens 查到用量
  -> 导出客户用量表
  -> 内部算毛利
  -> 销售跟进续费
```

第一版如果这个闭环能跑通，就可以开始找试用客户。不要先做复杂商城。

