# meme-self-evolving-patrol v0.5

BSC + SOL MEME / Alpha 自我进化轮巡系统。

## v0.5 目标

v0.5 在 v0.4.1 的基础上新增三件事：

1. **AVE Smart Wallet 周缓存接入框架**
   - AVE API Key 只放在 GitHub Secrets。
   - 不在代码里硬写未确认的 AVE endpoint。
   - 通过 `AVE_SMART_WALLET_ENDPOINT_TEMPLATE` 配置接口模板。
   - 每周刷新一次 Smart Wallet 身份库。

2. **Smart Wallet 持久保存**
   - 调用 AVE 后保存钱包地址、链、标签、画像、置信度、关联 Token、风险标签。
   - 新钱包追加。
   - 旧钱包更新 `last_seen_at` / `last_refresh_at`。
   - 新一轮未返回的钱包不直接删除，full refresh 时标记 `stale`。
   - 超过有效期的钱包标记 `stale` / `expired`。

3. **小时级钱包行为样本**
   - 每小时仍不调 AVE。
   - 每小时读取 `output/smart_wallet_cache.json`。
   - 新增 `output/wallet_behavior_latest.json`。
   - BSC 主观察 / 紧急精查候选会抓 ERC20 Transfer 样本。
   - 把本轮活跃钱包与 AVE 周缓存做命中匹配。

> 注意：v0.5 的 BSC 行为层只是 Transfer 样本，不是完整 Swap 留存。不能因为 Transfer 样本命中就直接判定真实聪明钱吸筹。

## 输出文件

| 文件 | 说明 |
|---|---|
| `output/latest_report.md` | 主报告 |
| `output/latest_snapshot.json` | 本轮扫描快照 |
| `output/previous_snapshot.json` | 上一轮快照 |
| `output/chain_verify_latest.json` | 链上地址/账户预检结果 |
| `output/wallet_behavior_latest.json` | v0.5 钱包行为样本与 AVE 命中 |
| `output/smart_wallet_cache.json` | AVE Smart Wallet 周缓存 |
| `output/ave_raw_smart_money.json` | AVE 周刷新原始响应/手动导入数据 |
| `output/strategy_patch.json` | 自我进化策略调整建议 |

## GitHub Secrets / Variables

### 必需 / 推荐 Secrets

| 名称 | 用途 |
|---|---|
| `BSC_RPC_URL` | BSC RPC；不配则使用公共 RPC fallback |
| `SOLANA_RPC_URL` | SOL RPC；不配则使用公共 RPC fallback |
| `HELIUS_API_KEY` | SOL 后续增强解析；v0.5 还未完整解析 |
| `AVE_API_KEY` | AVE API Key，周刷新使用 |
| `AVE_SMART_WALLET_ENDPOINT_TEMPLATE` | AVE Smart Wallet 接口模板 |
| `AVE_AUTH_HEADER` | AVE 鉴权 Header，默认 `X-API-KEY` |

### 可选 Variables

| 名称 | 默认值 | 用途 |
|---|---:|---|
| `AVE_TARGET_LIMIT` | 12 | 每周 AVE 刷新的候选数量 |
| `AVE_REFRESH_SCOPE` | incremental | `incremental` 或 `full`；full 会把未返回的旧钱包标记 stale |

## AVE endpoint template 写法

因为 AVE 的接口路径需要以你实际拿到的 API 文档为准，这里不硬编码 endpoint。

模板支持：

```text
{chain}
{token}
{token_address}
{address}
{pair_address}
```

示例格式：

```text
https://your-ave-endpoint.example/smart-wallets?chain={chain}&token={token_address}
```

如果接口要求 Authorization Bearer：

```text
AVE_AUTH_HEADER=Authorization
AVE_API_KEY=Bearer xxxxx
```

如果接口要求自定义 Header：

```text
AVE_AUTH_HEADER=X-API-KEY
AVE_API_KEY=xxxxx
```

## 手动导入 AVE 钱包数据

如果暂时没有确认 AVE endpoint，可以把钱包数据写入：

```text
output/ave_raw_smart_money.json
```

格式：

```json
{
  "wallets": [
    {
      "wallet_address": "0x...",
      "chain": "bsc",
      "labels": ["Smart Money", "Whale"],
      "confidence": "high",
      "related_tokens": ["0xToken..."],
      "risk_flags": []
    }
  ]
}
```

然后手动运行 GitHub Actions：

```text
AVE Smart Wallet 周缓存刷新 → Run workflow
```

系统会把这些钱包合并进 `output/smart_wallet_cache.json`。

## 运行方式

每小时轮巡：

```text
Actions → 自我进化轮巡 → Run workflow
```

每周 AVE 刷新：

```text
Actions → AVE Smart Wallet 周缓存刷新 → Run workflow
```

## v0.5 限制

| 限制 | 说明 |
|---|---|
| AVE endpoint 未硬编码 | 必须通过 Secret 配置真实 endpoint template |
| BSC Transfer 样本不是完整 Swap | 只能做预确认，不能直接高置信 |
| SOL 仍未完整行为解析 | 需要 v0.6 接 Helius enhanced tx 或 token balance diff |
| 钱包留存未完成 | v0.6 继续做买后 30m / 1h 留存 |
| Router/CEX 出货路径未完成 | v0.6 继续做 |

## 下一版 v0.6 方向

1. BSC 完整 Swap 路径解析。
2. Pair → Wallet 买入、Wallet → Pair 卖出、Router/CEX 转出识别。
3. 买后 30m / 1h 是否留存。
4. SOL Helius enhanced transaction 解析。
5. Smart Wallet 命中 + 留存 + 未出货，才提升到高置信。
