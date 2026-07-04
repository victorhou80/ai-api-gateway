# 05. 客户接入说明书模板

## 给客户的交付清单

```text
服务名称：AI API 接入托管服务
客户名称：
套餐名称：
有效期：
API Base URL：
API Key：
用量看板：
可用模型：
技术支持：
发票类型：普票 / 专票
```

## 标准接入信息

API Base URL：

```text
https://api.example.com/v1
```

认证方式：

```text
Authorization: Bearer sk-你的客户key
```

用量看板：

```text
https://portal.example.com
```

## OpenAI 兼容接口

请求：

```bash
curl https://api.example.com/v1/chat/completions \
  -H "Authorization: Bearer sk-你的客户key" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "ecom-copywriter",
    "messages": [
      {"role": "user", "content": "帮我写 10 个亚马逊商品标题"}
    ]
  }'
```

Python 示例：

```python
from openai import OpenAI

client = OpenAI(
    api_key="sk-你的客户key",
    base_url="https://api.example.com/v1",
)

resp = client.chat.completions.create(
    model="ecom-copywriter",
    messages=[
        {"role": "user", "content": "帮我写 10 个亚马逊商品标题"}
    ],
)

print(resp.choices[0].message.content)
```

JavaScript 示例：

```javascript
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: "sk-你的客户key",
  baseURL: "https://api.example.com/v1",
});

const resp = await client.chat.completions.create({
  model: "ecom-copywriter",
  messages: [
    { role: "user", content: "帮我写 10 个亚马逊商品标题" },
  ],
});

console.log(resp.choices[0].message.content);
```

## Claude 兼容接口

```bash
curl https://api.example.com/v1/messages \
  -H "Authorization: Bearer sk-你的客户key" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "claude-compatible-model",
    "max_tokens": 1000,
    "messages": [
      {"role": "user", "content": "优化这段商品五点描述"}
    ]
  }'
```

## 查询模型列表

```bash
curl https://api.example.com/v1/models \
  -H "Authorization: Bearer sk-你的客户key"
```

## 查询用量

客户优先登录 TokLens 看用量：

```text
https://portal.example.com
```

也可以用 API 查询：

```bash
curl https://api.example.com/v1/usage \
  -H "Authorization: Bearer sk-你的客户key"
```

## 电商客户推荐场景

### 商品标题

```text
你是亚马逊运营专家。请根据以下商品信息生成 10 个英文商品标题。
要求：
1. 适合美国站。
2. 包含核心关键词。
3. 避免夸大承诺。
4. 每个标题控制在 180 字符以内。

商品信息：
{商品信息}
核心关键词：
{关键词}
```

### 五点描述

```text
请为以下商品生成亚马逊五点描述。
要求：
1. 每点突出一个卖点。
2. 语言自然，适合英语母语用户。
3. 不写虚假认证。
4. 不承诺无法证明的效果。

商品信息：
{商品信息}
目标人群：
{目标人群}
```

### SEO 关键词

```text
请根据商品信息生成 SEO 关键词分组。
输出：
1. 核心关键词 10 个
2. 长尾关键词 20 个
3. 场景关键词 10 个
4. 竞品替代关键词 10 个

商品信息：
{商品信息}
```

## 常见问题

### 1. 这个 API 是官方接口吗

对客户建议回答：

```text
我们提供的是 AI API 接入托管服务，接口兼容 OpenAI/Claude 常见调用方式。
具体模型、额度、可用性以当前套餐和用量看板显示为准。
```

不要说“官方内部渠道”。

### 2. 能不能开发票

```text
可以。正式套餐支持合同、普票和专票。试用包默认不单独开票，升级正式套餐后可按实际付款开具。
```

### 3. 用量怎么算

```text
每次请求会记录模型、时间、输入输出 Token、请求状态和成本口径。
你可以在用量看板中查看，也可以按月导出对账表。
```

### 4. 超预算怎么办

```text
可以设置额度、并发和用量提醒。企业客户可以配置月预算，达到阈值后提醒或暂停。
```

