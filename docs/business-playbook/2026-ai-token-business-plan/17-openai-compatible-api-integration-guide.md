# 17. OpenAI-Compatible API Integration Guide

## Core Idea

Most customer tools are different on the surface, but if they support an OpenAI-compatible API, the connection pattern is usually the same:

```text
Base URL + API Key + Model Name + Chat Completions request
```

This guide is for two audiences:

- ecommerce operators who configure tools but do not write code
- programmers who need to integrate the API into systems, scripts, bots, customer-service tools, listing tools, or internal workflows

Important note:

OpenAI's current official docs recommend the Responses API for new OpenAI-native projects, while the Chat Completions API remains the common compatibility interface many third-party tools mean when they say "OpenAI standard" or "OpenAI-compatible API." This guide focuses on `/v1/chat/completions` compatibility because it is the most widely supported by tools.

Official references:

- OpenAI API authentication: https://developers.openai.com/api/reference/overview/
- OpenAI Chat Completions overview: https://developers.openai.com/api/reference/chat-completions/overview/
- OpenAI Chat Completions create endpoint: https://developers.openai.com/api/reference/resources/chat/subresources/completions/methods/create/
- OpenAI SDKs and quickstart: https://developers.openai.com/api/docs/libraries

## What We Give The Customer

Every integration handoff should include only these fields:

```text
API type: OpenAI-compatible
Base URL: https://example.your-service.com/v1
API Key: sk-****************
Model name: model-name-here
Chat endpoint: POST /chat/completions
Streaming: supported / not supported
Embeddings: supported / not supported
Vision/images: supported / not supported
Tool calling: supported / not supported
Rate limit: according to contract
Budget cap: according to package
Support contact: service group or ticket owner
```

Do not hand over:

- upstream master key
- shared key used by multiple unrelated customers
- internal supplier account
- admin dashboard password
- personal account credential
- browser cookies, session tokens, or OAuth tokens

## One-Sentence Explanation For Customers

```text
只要你的工具支持 OpenAI-compatible API，就通常只需要填 3 个东西：Base URL、API Key、Model Name。测试通过后，就可以按 Chat Completions 格式调用。
```

## Ecommerce Operator Version

### Step 1: Confirm The Tool Supports OpenAI-Compatible API

Look for these names in the customer's tool:

```text
OpenAI
OpenAI Compatible
Custom OpenAI
OpenAI API
OpenAI API Base
Custom Model Provider
LLM Provider
API Host
Base URL
Model Name
API Key
```

Common tool categories:

- AI writing tools
- customer-service assistant tools
- listing generation tools
- Dify-like workflow tools
- Chatbox/LobeChat/NextChat/OpenWebUI-like chat tools
- internal ERP/CRM/customer-service systems
- custom scripts made by a developer

### Step 2: Fill In The Four Core Fields

| Field | What To Fill | Common Mistake |
|---|---|---|
| API type | OpenAI-compatible / Custom OpenAI | choosing Azure/OpenRouter/Anthropic mode by mistake |
| Base URL | `https://example.your-service.com/v1` | filling `/chat/completions` when the tool asks for base URL |
| API Key | customer-specific key | pasting the key into a public page or screenshot |
| Model Name | exact model name from handoff sheet | using a model alias that is not enabled |

If the tool asks for a full endpoint instead of a base URL, use:

```text
https://example.your-service.com/v1/chat/completions
```

If the tool asks for a base URL, use only:

```text
https://example.your-service.com/v1
```

Do not duplicate `/v1`:

```text
Wrong: https://example.your-service.com/v1/v1/chat/completions
Right: https://example.your-service.com/v1/chat/completions
```

### Step 3: Use A Safe Test Prompt

Use a non-sensitive test:

```text
请用英文写 3 个适合 Shopify 独立站的蓝牙耳机商品标题，每个标题不超过 80 个字符。
```

Do not test with:

- buyer names
- buyer phone numbers
- order IDs
- addresses
- emails
- customer-service chat logs
- ad account credentials
- platform passwords
- private supplier information

### Step 4: Screenshot Rules

When asking support for help, the customer can send screenshots, but must hide:

- API key
- authorization header
- order data
- customer personal information
- account passwords
- supplier credentials

Suggested customer line:

```text
你可以发错误截图，但请先把 API Key、客户信息、订单号和账号密码打码。
```

### Step 5: Scenario Prompt Setup

For ecommerce, configure one scenario at a time:

| Scenario | System Prompt Direction |
|---|---|
| SKU title | follow platform style, avoid false claims, keep concise |
| product selling points | use provided facts only, no exaggerated claims |
| SEO keywords | produce keyword groups and title structures, no ranking promise |
| customer service | follow store policy, do not overpromise refunds or delivery |
| ad hooks | create testable angles, no prohibited claims |
| cross-border listing | localize language, do not merely translate |

## Programmer Version

### Minimal HTTP Request

```bash
curl -sS "$AI_API_BASE_URL/chat/completions" \
  -H "Authorization: Bearer $AI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "'"$AI_MODEL"'",
    "messages": [
      {"role": "system", "content": "You are an ecommerce copy assistant. Use only facts provided by the user."},
      {"role": "user", "content": "Write 3 English product titles for a stainless steel water bottle."}
    ],
    "temperature": 0.3,
    "stream": false
  }'
```

Environment variables:

```bash
export AI_API_BASE_URL="https://example.your-service.com/v1"
export AI_API_KEY="sk-..."
export AI_MODEL="model-name-here"
```

Windows PowerShell:

```powershell
$env:AI_API_BASE_URL = "https://example.your-service.com/v1"
$env:AI_API_KEY = "sk-..."
$env:AI_MODEL = "model-name-here"
```

### JavaScript / Node.js

```javascript
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AI_API_KEY,
  baseURL: process.env.AI_API_BASE_URL,
});

const completion = await client.chat.completions.create({
  model: process.env.AI_MODEL,
  messages: [
    {
      role: "system",
      content: "You are an ecommerce copy assistant. Use only facts provided by the user.",
    },
    {
      role: "user",
      content: "Write 3 English product titles for a stainless steel water bottle.",
    },
  ],
  temperature: 0.3,
});

console.log(completion.choices[0]?.message?.content);
```

Install:

```bash
npm install openai
```

### Python

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AI_API_KEY"],
    base_url=os.environ["AI_API_BASE_URL"],
)

completion = client.chat.completions.create(
    model=os.environ["AI_MODEL"],
    messages=[
        {
            "role": "system",
            "content": "You are an ecommerce copy assistant. Use only facts provided by the user.",
        },
        {
            "role": "user",
            "content": "Write 3 English product titles for a stainless steel water bottle.",
        },
    ],
    temperature=0.3,
)

print(completion.choices[0].message.content)
```

Install:

```bash
pip install openai
```

### JSON Request Shape

Minimum:

```json
{
  "model": "model-name-here",
  "messages": [
    { "role": "system", "content": "You are a helpful assistant." },
    { "role": "user", "content": "Hello." }
  ]
}
```

Common optional fields:

```json
{
  "temperature": 0.2,
  "max_tokens": 1000,
  "stream": false
}
```

Compatibility caveat:

Not every OpenAI-compatible provider supports every OpenAI feature. Test these separately before promising them:

- streaming
- vision/image input
- embeddings
- tool/function calling
- JSON schema / structured output
- audio
- file upload
- long context
- reasoning-specific parameters

## Tool Configuration Cheat Sheet

Use this mapping when helping customers configure different tools:

| Tool Field Name | Meaning | Example |
|---|---|---|
| Provider | API type | OpenAI-compatible |
| API Host | base URL | `https://example.your-service.com/v1` |
| Base URL | base URL | `https://example.your-service.com/v1` |
| Endpoint | full endpoint if requested | `https://example.your-service.com/v1/chat/completions` |
| API Key | bearer token | `sk-...` |
| Model | exact model ID | `model-name-here` |
| Temperature | output randomness | `0.2-0.7` |
| Max Tokens | output length cap | according to package |
| Stream | streaming response | on only if supported |

## Standard Onboarding Flow

### For Ecommerce Customers

```text
1. Confirm tool supports OpenAI-compatible API.
2. Send API handoff sheet.
3. Customer fills Base URL, API Key, Model Name.
4. Run safe product-title test.
5. Configure one ecommerce scenario.
6. Confirm budget cap and usage boundary.
7. Customer sends masked screenshot if error occurs.
8. After successful test, start formal usage and reporting.
```

### For Programmers

```text
1. Confirm API mode: BYOK or managed access.
2. Create customer-specific key.
3. Set environment variables.
4. Test /chat/completions with a safe prompt.
5. Add retry, timeout, and error handling.
6. Add logging without storing sensitive prompts.
7. Add budget cap and rate limit.
8. Confirm no API key is exposed in frontend code.
9. Prepare monitoring and usage report.
```

## Error Troubleshooting

| Error | Likely Cause | Fix |
|---|---|---|
| 401 Unauthorized | wrong key, missing `Bearer`, disabled key | check key and header |
| 403 Forbidden | package not enabled, model not authorized | confirm model/package permission |
| 404 Not Found | wrong base URL or endpoint path | check `/v1` and `/chat/completions` |
| model not found | model name typo or not enabled | use exact model from handoff sheet |
| 400 Bad Request | invalid JSON, unsupported parameter, wrong messages format | simplify request to minimum |
| context length error | prompt too long | shorten input or use allowed long-context model |
| 429 Rate Limit | too many requests or quota cap | reduce concurrency or upgrade package |
| timeout | network/proxy/provider slow | increase timeout, retry, or contact support |
| stream parse error | tool does not support SSE streaming | turn off streaming |
| empty or poor output | bad prompt or missing product facts | provide structured product facts |

## Security Rules

API keys are secrets.

Do:

- store keys in environment variables or server-side secret manager
- create separate keys per customer or per project
- rotate keys if leaked
- mask keys in screenshots
- log usage, not raw sensitive data
- enforce budget and rate limits

Do not:

- put API keys in frontend JavaScript
- commit keys to GitHub
- paste keys into shared docs
- send keys in group chats without access control
- use one shared key across unrelated customers
- upload customer personal data unless the contract and data path allow it

## Ecommerce Data Rules

Allowed for normal tests:

- public product title
- public product description
- public product images or URLs
- anonymized customer questions
- store policy text
- public competitor page summaries

Avoid unless explicitly approved:

- buyer names
- phone numbers
- addresses
- emails
- order IDs
- refund records
- private chat logs
- ad account credentials
- supplier contracts

## Delivery Message For Sales

```text
接入资料我发你四项：
1. API 类型：OpenAI-compatible；
2. Base URL；
3. API Key；
4. Model Name。

你的工具如果支持 OpenAI-compatible API，一般填这三项就能测试。
注意：如果工具要 Base URL，就填到 /v1；如果工具要完整 Endpoint，就填到 /v1/chat/completions。
测试时不要用客户姓名、电话、地址、订单号这类敏感信息。
```

## Acceptance Criteria

An integration is considered successful only when:

- customer can complete one safe test call
- output quality is acceptable for the selected scenario
- budget cap is confirmed
- key owner is recorded
- customer knows how to report errors
- sensitive-data boundary is acknowledged
- package and invoice status are recorded

## Final Rule

If a tool claims OpenAI compatibility but cannot configure `base_url`, `api_key`, and `model`, treat it as a special integration and ask a developer to evaluate it.

If a tool only supports the newer OpenAI Responses API, evaluate separately; do not assume Chat Completions compatibility.
