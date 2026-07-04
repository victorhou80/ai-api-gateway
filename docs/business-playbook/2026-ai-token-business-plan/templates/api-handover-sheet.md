# API Handover Sheet

Use this sheet when handing API configuration to a customer. Do not store real secrets in this repository.

## Customer

```text
客户名称：
项目名称：
套餐：
服务期：
负责人：
```

## API Configuration

```text
API type: OpenAI-compatible
Base URL: https://<customer-endpoint>/v1
Full chat endpoint: https://<customer-endpoint>/v1/chat/completions
API Key: sk-********
Model Name: <model-name>
Streaming: supported / not supported
```

## Usage Boundary

```text
允许场景：
禁止场景：
预算上限：
速率限制：
服务期：
报表频率：
```

## Customer Notes

```text
1. 如果工具要求 Base URL，填到 /v1。
2. 如果工具要求完整 Endpoint，填到 /v1/chat/completions。
3. API Key 不要放在前端网页、公开代码、GitHub、共享文档或未打码截图里。
4. 测试时不要上传客户姓名、电话、地址、订单号、邮箱、支付信息或账号密码。
5. 如遇报错，请发打码截图和请求时间，不要发送完整密钥。
```

## First Test Prompt

```text
请用英文写 3 个适合 Shopify 独立站的蓝牙耳机商品标题，每个标题不超过 80 个字符。
```

## Support

```text
支持联系人：
服务群：
响应时间：
续费提醒：
```
