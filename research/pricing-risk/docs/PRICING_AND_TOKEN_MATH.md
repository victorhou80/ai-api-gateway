# 价格与 Token 计算方法

## 1. 统一变量

```text
C = 买到官方标准牌价 $1 的 Token 用量需要支付的人民币
P_in = 官方输入价格，美元/百万 Token
P_out = 官方输出价格，美元/百万 Token
s = 输入 Token 在总 Token 中的比例，0≤s≤1
```

## 2. 核心公式

```text
每 1 元官方美元购买力 = 1 / C

每元输入 Token = 1,000,000 / (C × P_in)
每元输出 Token = 1,000,000 / (C × P_out)

混合场景每百万总 Token 的人民币成本：
Cost_mix = C × (s × P_in + (1-s) × P_out)

混合场景每元总 Token：
Tokens_mix = 1,000,000 / Cost_mix
```

## 3. GPT-5.6 Sol 示例

官方标准价：

```text
P_in = 5
P_out = 30
```

### C=1.00

```text
输入：1,000,000 / (1 × 5) = 200,000 Token/元
输出：1,000,000 / (1 × 30) = 33,333 Token/元

90% 输入 + 10% 输出：
1,000,000 / (1 × (0.9×5 + 0.1×30))
= 133,333 Token/元
```

### C=0.30

```text
输入：1,000,000 / (0.3 × 5) = 666,667 Token/元
输出：1,000,000 / (0.3 × 30) = 111,111 Token/元

90% 输入 + 10% 输出：
1,000,000 / (0.3 × (0.9×5 + 0.1×30))
= 444,444 Token/元
```

## 4. 从充值和模型倍率计算 C

如果：

- 用户支付 `R` 元人民币获得 1 个站内美元余额；
- 模型按官方牌价数字的 `M` 倍扣站内余额；
- VIP 折扣系数为 `V`；
- 充值赠送使有效余额增加 `B` 倍，例如充 10 送 5 则 `B=1.5`；

则：

```text
C = R × M × V / B
```

示例：OneHop 常规价：

```text
R=6.8
M=0.10
V=1
B=1

C=6.8×0.10=0.68
```

活动赠送必须验证适用模型、有效期、次数和到账规则后才可代入 `B`。

## 5. 缓存与 reasoning 的注意事项

- 缓存输入和普通输入不是同一个价格；
- 首次输入、缓存写入、缓存读取可能分别计费；
- 输出和隐藏 reasoning tokens 通常属于高价侧；
- 工具调用、Web 搜索、容器、图像和视频可能另行计费；
- 失败请求是否扣费取决于网关和上游实际处理阶段；
- 长上下文可能触发不同价格区间；
- 单看“总 Token”会掩盖输入/输出结构差异。

因此，生产账单至少应分别记录：

```text
input_uncached_tokens
input_cache_write_tokens
input_cache_read_tokens
output_visible_tokens
output_reasoning_tokens
tool_calls
upstream_error
charged_amount
```

## 6. 运行计算器

```powershell
python scripts/price_calculator.py `
  --c 0.30 `
  --input-price 5 `
  --output-price 30 `
  --input-share 0.9
```

如果比较其他模型，只需替换官方输入和输出价格。
