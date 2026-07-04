# OpenAI-compatible API 接入交付单

用途：给开发者、技术负责人、AI 工具使用者确认接入字段。公开视频只能展示 demo，不展示真实 key、真实客户域名或真实日志。

承接产品：399 API 适配诊断、2,980 技术试跑、4,980 API 路由试跑、9,800 出海模型包、29,800 工作流包。

## 1. 基础接入字段

| 字段 | 填写值 | 示例 | 备注 |
|---|---|---|---|
| API 类型 | OpenAI-compatible | OpenAI-compatible | 工具必须支持该类型 |
| 环境 | test/prod | test | 先测试再生产 |
| Base URL |  | https://api.example.com/v1 | 示例地址，公开视频用 demo |
| Endpoint |  | /chat/completions | 有些工具需要完整 endpoint |
| API Key |  | sk-demo-****masked**** | 永远打码，不进前端 |
| Model Name |  | high-tier-model-a | 按交付单填写 |
| Streaming | Yes/No | Yes | 是否支持流式 |
| Vision/Image | Yes/No | No | 是否支持图像 |
| Embeddings | Yes/No | No | 是否支持向量 |
| Tool Calling | Yes/No | Yes | 是否支持工具调用 |
| JSON 输出 | Yes/No | Yes | 是否要求结构化输出 |

## 2. 用量和安全边界

| 字段 | 填写值 | 示例 |
|---|---|---|
| 允许场景 |  | 商品标题、客服 FAQ、英文 listing |
| 禁止场景 |  | 敏感个人信息、支付信息、账号密码 |
| 预算上限 |  | RMB 4,980 |
| 预警线 |  | 70% / 85% / 95% |
| Rate Limit |  | 60 rpm |
| 并发限制 |  | 5 concurrent |
| Timeout |  | 20s |
| Retry |  | 最多 2 次，指数退避 |
| Fallback |  | 超时切 balanced-model-b |
| 日志字段 |  | request_id、status、latency、cost、error |
| 报表频率 |  | 日报/周报 |
| 数据脱敏 |  | 姓名、电话、邮箱、地址、订单号先脱敏 |

## 3. 客户工具映射

| 工具/系统 | 通常填写位置 | 注意事项 |
|---|---|---|
| Dify | Model Provider / OpenAI-compatible | Base URL 通常填到 /v1 |
| OpenWebUI | Connections / OpenAI API | 不要把 key 共享给所有用户 |
| Chatbox | Settings / Model Provider | 只适合个人或小团队测试 |
| 自研系统 | 环境变量/后端配置 | key 只放服务端，不进前端 |
| 电商脚本工具 | API settings | 限制场景和预算 |

## 4. 常见错误排查

| 错误 | 可能原因 | 处理 |
|---|---|---|
| 401 | API key 错误或过期 | 重新核对 key，确认环境 |
| 403 | 权限不足 | 确认模型权限和账号授权 |
| 404 | Base URL、endpoint 或 model name 错误 | 核对 /v1 和模型名 |
| 429 | 超出限流 | 降低并发，加重试和排队 |
| timeout | 模型响应慢或上下文太长 | 降低上下文、设置 fallback |
| context_length | 输入过长 | 做截断、摘要、分块 |
| model_not_found | 模型名不匹配 | 按交付单更新模型名 |

## 5. 录屏讲法

```text
OpenAI-compatible 接入不要只问能不能用。
先看 6 个字段：Base URL、Endpoint、API Key、Model Name、预算上限、限流规则。
测试时不要上传真实客户姓名、电话、地址、订单号和支付信息。
体验包不导出 key，生产接入要按合同和数据边界来。
```
