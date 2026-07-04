# 02. 服务器和网站部署手册

## 服务器要求

测试版：

| 项目 | 建议 |
|---|---|
| CPU | 4 核 |
| 内存 | 8GB |
| 硬盘 | 100GB SSD |
| 系统 | Ubuntu 22.04 / 24.04 |
| 带宽 | 5-10Mbps 起 |

正式试运营：

| 项目 | 建议 |
|---|---|
| CPU | 8 核 |
| 内存 | 16GB |
| 硬盘 | 200GB SSD 起 |
| 带宽 | 10Mbps+ |
| 备份 | PostgreSQL 每日备份 |
| 监控 | CPU、内存、磁盘、服务存活 |

## 域名建议

```text
api.example.com       客户 API 接入地址
portal.example.com    客户用量看板
admin.example.com     内部管理后台，可选
```

第一版也可以只用两个：

```text
api.example.com
portal.example.com
```

## 端口规划

| 服务 | 内部端口 | 是否公网开放 |
|---|---:|---|
| Caddy/Nginx | 80/443 | 是 |
| sub2api-mod | 8080 | 否，只给反代访问 |
| TokLens | 3000 | 否，只给反代访问 |
| PostgreSQL | 5432 | 否 |
| Redis | 6379 | 否 |

## 部署 sub2api-mod

```bash
git clone https://github.com/alphane-ai/sub2api-mod.git
cd sub2api-mod/deploy
cp .env.example .env
```

编辑 `.env`：

```bash
SERVER_PORT=8080
POSTGRES_PASSWORD=change_this_to_a_strong_password
JWT_SECRET=use_openssl_rand_hex_32
TOTP_ENCRYPTION_KEY=use_openssl_rand_hex_32
ADMIN_EMAIL=admin@example.com
ADMIN_PASSWORD=change_this_admin_password
TZ=Asia/Shanghai
```

生成密钥：

```bash
openssl rand -hex 32
```

启动：

```bash
docker compose up -d
docker compose logs -f sub2api
```

健康检查：

```bash
curl http://127.0.0.1:8080/health
```

## 部署 TokLens

```bash
git clone https://github.com/alphane-ai/toklens.git
cd toklens
npm ci
npm run build
```

生产环境推荐用 Docker：

```bash
docker build -t toklens .
docker run -d \
  --name toklens \
  --restart unless-stopped \
  -p 127.0.0.1:3000:3000 \
  -e SUB2API_PROXY_TARGET=http://127.0.0.1:8080 \
  -e NEXT_PUBLIC_DEFAULT_LOCALE=zh \
  toklens
```

如果 TokLens 和 sub2api 在同一个 Docker 网络，可以改成：

```bash
SUB2API_PROXY_TARGET=http://sub2api:8080
```

## Caddy 反向代理示例

```caddyfile
api.example.com {
    reverse_proxy 127.0.0.1:8080
}

portal.example.com {
    reverse_proxy 127.0.0.1:3000
}
```

Caddy 会自动申请 HTTPS。

## Nginx 注意事项

如果用 Nginx，必须在 `http` 块里加：

```nginx
underscores_in_headers on;
```

原因：部分客户端和 sticky session 会用到带下划线的 header，例如 `session_id`。Nginx 默认可能丢弃这类 header，影响 Codex/Claude Code 请求归因和粘性会话。

## sub2api 后台初始配置步骤

1. 登录后台。
2. 修改管理员密码。
3. 开启 TOTP。
4. 创建上游账号。
5. 创建分组：

```text
trial_ecom_1d
ecom_light
ecom_pro
dev_pro
enterprise_default
```

6. 绑定上游账号到分组。
7. 设置每组模型范围、倍率、限流、并发。
8. 创建测试用户。
9. 给测试用户生成 API Key。
10. 用 curl 跑一次测试请求。
11. 用 TokLens 查询这个 Key 的用量。

## 客户 API 测试

OpenAI 兼容：

```bash
curl https://api.example.com/v1/chat/completions \
  -H "Authorization: Bearer sk-客户key" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "ecom-copywriter",
    "messages": [
      {"role": "user", "content": "给这个蓝牙耳机写 5 个亚马逊标题"}
    ]
  }'
```

Claude 兼容：

```bash
curl https://api.example.com/v1/messages \
  -H "Authorization: Bearer sk-客户key" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "claude-compatible-model",
    "max_tokens": 800,
    "messages": [
      {"role": "user", "content": "优化这段商品五点描述"}
    ]
  }'
```

查模型：

```bash
curl https://api.example.com/v1/models \
  -H "Authorization: Bearer sk-客户key"
```

查用量：

```bash
curl https://api.example.com/v1/usage \
  -H "Authorization: Bearer sk-客户key"
```

## 上线前检查

| 检查项 | 结果 |
|---|---|
| HTTPS 正常 | |
| `/health` 正常 | |
| 客户 API Key 可调用 | |
| TokLens 可查询用量 | |
| PostgreSQL 不暴露公网 | |
| Redis 不暴露公网 | |
| 管理后台强密码 | |
| JWT_SECRET 固定 | |
| TOTP_ENCRYPTION_KEY 固定 | |
| 数据库备份脚本已配置 | |
| 日志不打印完整 Key | |
| 销售文档不写违规宣传 | |

