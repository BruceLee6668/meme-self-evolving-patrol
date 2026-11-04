# 自我进化轮巡

**本轮时间 UTC：** 2026-11-04T01:49:41Z
**版本：** 0.5.0-ave-cache-wallet-behavior-prep
**S0 时间锚点：** 2026-06-16T16:15:17+09:00

## 一句话结论
本轮从 148 个合并Token中筛出 5 个主观察候选。v0.5已在v0.4.1基础上增加AVE周缓存真实接口接入框架、Smart Wallet持久保存、wallet_behavior_latest.json，以及BSC Transfer级钱包行为样本。注意：BSC当前是Transfer样本，不等同完整Swap解码。
合约地址可用 25 个，缺失 0 个；缺失地址的候选不能进入后续链上精查。

## 本轮扫描摘要
| 指标 | 数量 |
|---|---:|
| 原始池子记录 | 264 |
| 合并后Token | 148 |
| 输出候选 | 25 |
| 主观察 | 5 |
| 次观察 | 8 |
| PVP风险池 | 8 |
| 成熟池观察 | 4 |
| 低优先观察 | 0 |
| 多池Token | 2 |
| 多池冲突 | 2 |
| Symbol桥接合并 | 2 |
| 合约地址可用 | 25 |
| 合约地址缺失 | 0 |
| Micro层 | 5 |
| Early层 | 14 |
| Liquid层 | 6 |
| Mature层 | 0 |
| 需要链上确认 | 21 |
| 紧急精查候选 | 4 |

## v0.5 数据确认状态
| 项目 | 状态 |
|---|---|
| AVE Smart Wallet周缓存 | active，钱包数 2405，刷新时间 2026-11-02T03:39:47Z，是否过期 否 |
| 链上预检 | 本轮检查 12 个，验证通过 12 个，失败 0 个 |
| Helius状态 | 未配置，SOL使用公共RPC或跳过增强解析 |
| 当前精查层级 | 0.5.0-chain-preflight-plus-wallet-behavior：地址/账户预检 + v0.5钱包行为样本，完整Swap留存仍待下一版 |
| 钱包行为样本 | 本轮检查 5 个，BSC Transfer样本 2 个，SOL签名级 3 个，AVE钱包命中 0 个 |

## 第一部分：生成结果表格

### A. 上次记录结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| [Dacity](https://dexscreener.com/solana/g2uurbmvdzdfp4qyobjrskbxsi7d6v4bpp9thps36y4b) | SOL | [nxPqZ4...Rjpump](https://solscan.io/token/nxPqZ4F7ux8Vph5NFu25rEP6Kx9Gr1U6Fmj36Rjpump) | 主观察 | Score 85; Tier Early; LP $365.8K; Vol24H $1.99M; 24H -7.08%; V/LP 5.43x; 池数 1; 分项 L14/V16/B22/Buy12/Risk-3 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [ANSEM](https://dexscreener.com/solana/fnzky6x7entq1er3d225dqyt7ybfka4pskbmqhb8l3cc) | SOL | [9cRCn9...TGpump](https://solscan.io/token/9cRCn9rGT8V2imeM2BaKs13yhMEais3ruM3rPvTGpump) | 主观察 | Score 81; Tier Liquid; LP $1.21M; Vol24H $689.9K; 24H +6.80%; V/LP 0.57x; 池数 4; 分项 L19/V13/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| JAGENT | BSC | [0x8e64...e4ae15](https://bscscan.com/token/0x8e6442663a4f8c50b6132c68d42a30e7dfe4ae15) | 主观察 | Score 80; Tier Early; LP $503.7K; Vol24H $1.41M; 24H -18.97%; V/LP 2.81x; 池数 1; 分项 L16/V15/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| SAFU | BSC | [0xdd80...c87777](https://bscscan.com/token/0xdd806e436dda5588bf54061c11590c77ddc87777) | 主观察 | Score 79; Tier Early; LP $175.1K; Vol24H $1.13M; 24H +5.32%; V/LP 6.47x; 池数 1; 分项 L11/V14/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| TART | BSC | [0x7ab8...750314](https://bscscan.com/token/0x7ab8d02cbb51ff7223fde700eaaa2a91bf750314) | 主观察 | Score 76; Tier Liquid; LP $797.3K; Vol24H $297.7K; 24H +1.33%; V/LP 0.37x; 池数 1; 分项 L17/V10/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| FLOAT | SOL | [Bv1a7c...52BMmr](https://solscan.io/token/Bv1a7cEj5aRnJQhMw4kRQqAFesMSd5LwcDnUzq52BMmr) | 次观察 | Score 74; Tier Early; LP $301.0K; Vol24H $2.37M; 24H -35.50%; V/LP 7.89x; 池数 1; 分项 L14/V16/B8/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [NIO](https://dexscreener.com/solana/b4wmjc6pvjctu3qsvs3ett9mr4m5v5jbkrqctwantc71) | SOL | [7SL2Vn...LQpump](https://solscan.io/token/7SL2VnfYsChvog5oQY9Nmtqu1wceaMiQzWoqoLQpump) | 次观察 | Score 71; Tier Early; LP $104.4K; Vol24H $822.6K; 24H -22.92%; V/LP 7.88x; 池数 1; 分项 L9/V13/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [IOF](https://dexscreener.com/solana/7wcareycymxe2olsuaptqg4ybx5hfh1msinrhq4pvhjm) | SOL | [2sY7rk...6Bpump](https://solscan.io/token/2sY7rkMCQyFNcSpHm3fciJf2ptYRg3cYpn4srN6Bpump) | 次观察 | Score 68; Tier Early; LP $174.3K; Vol24H $172.2K; 24H -19.69%; V/LP 0.99x; 池数 1; 分项 L11/V8/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [CBUCKS](https://dexscreener.com/solana/b4cp45pgifvm5faxfh6aev8qz3eunqnqgbw7kuc7mhnb) | SOL | [DtcicP...xZpump](https://solscan.io/token/DtcicPCKTKeAh7TDEzTym3hXeoHAoMiBdYJhMYxZpump) | 次观察 | Score 67; Tier Early; LP $141.7K; Vol24H $95.7K; 24H -5.22%; V/LP 0.68x; 池数 1; 分项 L11/V7/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [NODF](https://dexscreener.com/solana/exulh1zrmfj1gpct8de8hbzqbgrtinalusjldegbmifd) | SOL | [gHeaay...AUpump](https://solscan.io/token/gHeaaywtSrrYWNGf6fAWifNNxnoM8HTE15zFmAUpump) | 次观察 | Score 66; Tier Early; LP $262.9K; Vol24H $203.5K; 24H -28.43%; V/LP 0.77x; 池数 1; 分项 L13/V9/B8/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |

### B. 本轮扫描结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| [ANSEM](https://dexscreener.com/solana/fnzky6x7entq1er3d225dqyt7ybfka4pskbmqhb8l3cc) | SOL | [9cRCn9...TGpump](https://solscan.io/token/9cRCn9rGT8V2imeM2BaKs13yhMEais3ruM3rPvTGpump) | 主观察 | Score 81; Tier Liquid; LP $1.23M; Vol24H $799.9K; 24H +6.50%; V/LP 0.65x; 池数 1; 分项 L19/V13/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [Dacity](https://dexscreener.com/solana/g2uurbmvdzdfp4qyobjrskbxsi7d6v4bpp9thps36y4b) | SOL | [nxPqZ4...Rjpump](https://solscan.io/token/nxPqZ4F7ux8Vph5NFu25rEP6Kx9Gr1U6Fmj36Rjpump) | 主观察 | Score 80; Tier Early; LP $359.0K; Vol24H $1.96M; 24H -8.35%; V/LP 5.45x; 池数 1; 分项 L14/V16/B17/Buy12/Risk-3 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| JAGENT | BSC | [0x8e64...e4ae15](https://bscscan.com/token/0x8e6442663a4f8c50b6132c68d42a30e7dfe4ae15) | 主观察 | Score 79; Tier Early; LP $551.7K; Vol24H $1.24M; 24H +18.06%; V/LP 2.25x; 池数 1; 分项 L16/V14/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| GANG | BSC | [0x0c63...20b405](https://bscscan.com/token/0x0c6302401aa5325c2e36f170f52c00b1d220b405) | 主观察 | Score 79; Tier Early; LP $227.4K; Vol24H $675.1K; 24H -0.03%; V/LP 2.97x; 池数 1; 分项 L12/V13/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [NIO](https://dexscreener.com/solana/b4wmjc6pvjctu3qsvs3ett9mr4m5v5jbkrqctwantc71) | SOL | [7SL2Vn...LQpump](https://solscan.io/token/7SL2VnfYsChvog5oQY9Nmtqu1wceaMiQzWoqoLQpump) | 主观察 | Score 77; Tier Early; LP $112.0K; Vol24H $770.4K; 24H -7.48%; V/LP 6.88x; 池数 1; 分项 L10/V13/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [UODF](https://dexscreener.com/solana/dfcrxve7mejyf8r6dr91klhveaoyve6lacgfp8airkxv) | SOL | [QreCV2...CVpump](https://solscan.io/token/QreCV24giHAXE9eofxhNXKX1uATsp82ReumMFCVpump) | 次观察 | Score 75; Tier Early; LP $352.8K; Vol24H $158.3K; 24H +14.33%; V/LP 0.45x; 池数 2; 分项 L14/V8/B17/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| SAFU | BSC | [0xdd80...c87777](https://bscscan.com/token/0xdd806e436dda5588bf54061c11590c77ddc87777) | 次观察 | Score 74; Tier Early; LP $173.5K; Vol24H $929.2K; 24H -9.32%; V/LP 5.36x; 池数 1; 分项 L11/V14/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| FLOAT | SOL | [Bv1a7c...52BMmr](https://solscan.io/token/Bv1a7cEj5aRnJQhMw4kRQqAFesMSd5LwcDnUzq52BMmr) | 次观察 | Score 73; Tier Early; LP $276.8K; Vol24H $2.16M; 24H -45.29%; V/LP 7.79x; 池数 1; 分项 L13/V16/B8/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [XCAT](https://dexscreener.com/solana/8kxzr2bikmkcgzhp4srlgyhbpsqqwzk2echqhxqrd589) | SOL | [1226TM...e5xfun](https://solscan.io/token/1226TMaWZiZYWdP7CBZBqfJGXoWXaKXJJiKf45e5xfun) | 次观察 | Score 68; Tier Early; LP $426.4K; Vol24H $112.5K; 24H +12.42%; V/LP 0.26x; 池数 1; 分项 L15/V7/B17/Buy8/Risk-3 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [IOF](https://dexscreener.com/solana/7wcareycymxe2olsuaptqg4ybx5hfh1msinrhq4pvhjm) | SOL | [2sY7rk...6Bpump](https://solscan.io/token/2sY7rkMCQyFNcSpHm3fciJf2ptYRg3cYpn4srN6Bpump) | 次观察 | Score 68; Tier Early; LP $167.1K; Vol24H $159.4K; 24H -24.22%; V/LP 0.95x; 池数 1; 分项 L11/V8/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [CBUCKS](https://dexscreener.com/solana/b4cp45pgifvm5faxfh6aev8qz3eunqnqgbw7kuc7mhnb) | SOL | [DtcicP...xZpump](https://solscan.io/token/DtcicPCKTKeAh7TDEzTym3hXeoHAoMiBdYJhMYxZpump) | 次观察 | Score 67; Tier Early; LP $145.6K; Vol24H $109.1K; 24H +3.14%; V/LP 0.75x; 池数 1; 分项 L11/V7/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [NODF](https://dexscreener.com/solana/exulh1zrmfj1gpct8de8hbzqbgrtinalusjldegbmifd) | SOL | [gHeaay...AUpump](https://solscan.io/token/gHeaaywtSrrYWNGf6fAWifNNxnoM8HTE15zFmAUpump) | 次观察 | Score 66; Tier Early; LP $263.4K; Vol24H $202.8K; 24H -29.80%; V/LP 0.77x; 池数 1; 分项 L13/V9/B8/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [EXFIL](https://dexscreener.com/solana/2zpfdgd48k7b2u9yqz4hjspaptovu9uiebfqyxeoexkv) | SOL | [6FhVPc...y6pump](https://solscan.io/token/6FhVPctYg363pQbs4iSvqyHe2cJzfsvFD96gePy6pump) | 次观察 | Score 65; Tier Early; LP $145.2K; Vol24H $136.9K; 24H +6.38%; V/LP 0.94x; 池数 1; 分项 L11/V8/B22/Buy0/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| AKE | BSC | [0x2c3a...12f7db](https://bscscan.com/token/0x2c3a8ee94ddd97244a93bc48298f97d2c412f7db) | PVP风险池 | Score 33; Tier Liquid; LP $1.00M; Vol24H $20.47M; 24H -36.09%; V/LP 20.44x; 池数 1; 分项 L18/V17/B8/Buy8/Risk-42 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [ANONVOYAGE](https://dexscreener.com/solana/2yx74z677vrmwjn4qnm9aqthbxqi1dsxrysifk4rsmma) | SOL | [8muc9D...zVpump](https://solscan.io/token/8muc9DdhqWfAPcvmEebNQCG89bLiwi12T2KtBtzVpump) | PVP风险池 | Score 32; Tier Early; LP $102.3K; Vol24H $3.50M; 24H +2276.00%; V/LP 34.18x; 池数 1; 分项 L9/V17/B0/Buy12/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### C. PVP风险池明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| AKE | BSC | [0x2c3a...12f7db](https://bscscan.com/token/0x2c3a8ee94ddd97244a93bc48298f97d2c412f7db) | 24H未过热但已明显波动；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP极端偏高；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 33; Tier Liquid; LP $1.00M; Vol24H $20.47M; 24H -36.09%; V/LP 20.44x; 池数 1; 分项 L18/V17/B8/Buy8/Risk-42 | 只记录热度，不进入主榜 |
| [ANONVOYAGE](https://dexscreener.com/solana/2yx74z677vrmwjn4qnm9aqthbxqi1dsxrysifk4rsmma) | SOL | [8muc9D...zVpump](https://solscan.io/token/8muc9DdhqWfAPcvmEebNQCG89bLiwi12T2KtBtzVpump) | 买入笔数占优；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 32; Tier Early; LP $102.3K; Vol24H $3.50M; 24H +2276.00%; V/LP 34.18x; 池数 1; 分项 L9/V17/B0/Buy12/Risk-30 | 只记录热度，不进入主榜 |
| [SPHERE](https://dexscreener.com/solana/hmcvp73epenjn2jdhqbws6syn56abcmpugdgouqznuok) | SOL | [31SYoq...fDpump](https://solscan.io/token/31SYoqWFhx3i9UsfnoXTjFp4ZwJA8F8UPrMxymfDpump) | 买入笔数占优；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 17; Tier Micro; LP $28.5K; Vol24H $2.65M; 24H +135.00%; V/LP 92.99x; 池数 1; 分项 L4/V17/B0/Buy12/Risk-40 | 只记录热度，不进入主榜 |
| BINGUS | SOL | [2HbNwn...5fLoat](https://solscan.io/token/2HbNwnhiL8HBK5mkdrcB9nbDxknPqGmJdXrtuH5fLoat) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 11; Tier Micro; LP $33.4K; Vol24H $1.00M; 24H -82.84%; V/LP 30.04x; 池数 1; 分项 L5/V14/B0/Buy8/Risk-40 | 只记录热度，不进入主榜 |
| [Ahsoka](https://dexscreener.com/solana/hpymxw5bzvks2lphuzljxwemyrpu7uu3vfqq3o5abzdj) | SOL | [4nuj5N...1dpump](https://solscan.io/token/4nuj5NLHMtQSezfmz6CwBpCRJisFie6F6MxNNz1dpump) | 买卖基本均衡；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 9; Tier Micro; LP $33.9K; Vol24H $2.76M; 24H -85.42%; V/LP 81.35x; 池数 1; 分项 L5/V17/B0/Buy3/Risk-40 | 只记录热度，不进入主榜 |
| MOGMAS | SOL | [4yxnt3...ULpump](https://solscan.io/token/4yxnt3xAdyBFFbzMWJy9sjGEoiBNkjwdSQZ8ZyULpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 8; Tier Micro; LP $22.2K; Vol24H $837.9K; 24H +98.63%; V/LP 37.81x; 池数 1; 分项 L3/V13/B0/Buy8/Risk-40 | 只记录热度，不进入主榜 |
| UNPOOLED | SOL | [FxQ5Gb...wepump](https://solscan.io/token/FxQ5GbqCBxNHDpFTpiL9RDVHiP58ar5nMkR3eMwepump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 6; Tier Micro; LP $4.3K; Vol24H $967.1K; 24H -87.35%; V/LP 223.92x; 池数 1; 分项 L0/V14/B0/Buy8/Risk-40 | 只记录热度，不进入主榜 |
| [AMD](https://dexscreener.com/solana/7rd5yalhcmlufkj8frepgd6ei11f15uxzf1rc7mpkecv) | SOL | [DDmGnu...zmpump](https://solscan.io/token/DDmGnuvroxVrb7CSyjYcezFU8gnAfhKasg4ZZezmpump) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高；年轻币短期暴拉；非主流报价池 | Score 2; Tier Early; LP $146.1K; Vol24H $8.64M; 24H +4008.00%; V/LP 59.16x; 池数 20; 分项 L11/V17/B0/Buy8/Risk-58 | 只记录热度，不进入主榜 |

### D. 成熟池观察明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| ARIA | BSC | [0x5d3a...555238](https://bscscan.com/token/0x5d3a12c42e5372b2cc3264ab3cdcf660a1555238) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；成熟大市值 | Score 74; Tier Liquid; LP $1.70M; Vol24H $3.64M; 24H +1.10%; V/LP 2.14x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| STONK | SOL | [6GmAFS...MpUNgx](https://solscan.io/token/6GmAFSYs4gk3FDao5FzzySQpPZaWsa4rUJHacpMpUNgx) | 24H波动可控；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限 | Score 74; Tier Liquid; LP $2.46M; Vol24H $7.30M; 24H +10.13%; V/LP 2.97x; 池数 1; 分项 L20/V17/B17/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| Q | BSC | [0xc07e...690589](https://bscscan.com/token/0xc07e1300dc138601fa6b0b59f8d0fa477e690589) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 73; Tier Liquid; LP $1.08M; Vol24H $7.22M; 24H +0.67%; V/LP 6.67x; 池数 1; 分项 L19/V17/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| [AODF](https://dexscreener.com/solana/cbyxncob6ckhnbkv6um7dnewomb4jmqb5httuvs5u5eu) | SOL | [GePXef...MRpump](https://solscan.io/token/GePXefzRNUT92fcn5u8VfXpPPc9BhCmyPefKW2MRpump) | 24H波动可控；买入笔数占优；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 69; Tier Liquid; LP $1.30M; Vol24H $198.8K; 24H +11.69%; V/LP 0.15x; 池数 1; 分项 L19/V9/B17/Buy12/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |

### E. 链上确认/紧急精查表
| Token | 链 | 合约地址 | 是否需要链上确认 | 紧急精查 | 预检状态 | 原因 |
|---|---|---|---|---|---|---|
| [Dacity](https://dexscreener.com/solana/g2uurbmvdzdfp4qyobjrskbxsi7d6v4bpp9thps36y4b) | SOL | [nxPqZ4...Rjpump](https://solscan.io/token/nxPqZ4F7ux8Vph5NFu25rEP6Kx9Gr1U6Fmj36Rjpump) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| JAGENT | BSC | [0x8e64...e4ae15](https://bscscan.com/token/0x8e6442663a4f8c50b6132c68d42a30e7dfe4ae15) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| GANG | BSC | [0x0c63...20b405](https://bscscan.com/token/0x0c6302401aa5325c2e36f170f52c00b1d220b405) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| [NIO](https://dexscreener.com/solana/b4wmjc6pvjctu3qsvs3ett9mr4m5v5jbkrqctwantc71) | SOL | [7SL2Vn...LQpump](https://solscan.io/token/7SL2VnfYsChvog5oQY9Nmtqu1wceaMiQzWoqoLQpump) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| [ANSEM](https://dexscreener.com/solana/fnzky6x7entq1er3d225dqyt7ybfka4pskbmqhb8l3cc) | SOL | [9cRCn9...TGpump](https://solscan.io/token/9cRCn9rGT8V2imeM2BaKs13yhMEais3ruM3rPvTGpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [UODF](https://dexscreener.com/solana/dfcrxve7mejyf8r6dr91klhveaoyve6lacgfp8airkxv) | SOL | [QreCV2...CVpump](https://solscan.io/token/QreCV24giHAXE9eofxhNXKX1uATsp82ReumMFCVpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；多池数据冲突，需链上/聚合源复核 |
| SAFU | BSC | [0xdd80...c87777](https://bscscan.com/token/0xdd806e436dda5588bf54061c11590c77ddc87777) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| FLOAT | SOL | [Bv1a7c...52BMmr](https://solscan.io/token/Bv1a7cEj5aRnJQhMw4kRQqAFesMSd5LwcDnUzq52BMmr) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [XCAT](https://dexscreener.com/solana/8kxzr2bikmkcgzhp4srlgyhbpsqqwzk2echqhxqrd589) | SOL | [1226TM...e5xfun](https://solscan.io/token/1226TMaWZiZYWdP7CBZBqfJGXoWXaKXJJiKf45e5xfun) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [IOF](https://dexscreener.com/solana/7wcareycymxe2olsuaptqg4ybx5hfh1msinrhq4pvhjm) | SOL | [2sY7rk...6Bpump](https://solscan.io/token/2sY7rkMCQyFNcSpHm3fciJf2ptYRg3cYpn4srN6Bpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |

### F. 钱包行为 / AVE命中样本表
| Token | 链 | 合约地址 | 行为状态 | 行为层级 | AVE命中 | 判断 |
|---|---|---|---|---|---:|---|
| [Dacity](https://dexscreener.com/solana/g2uurbmvdzdfp4qyobjrskbxsi7d6v4bpp9thps36y4b) | SOL | [nxPqZ4...Rjpump](https://solscan.io/token/nxPqZ4F7ux8Vph5NFu25rEP6Kx9Gr1U6Fmj36Rjpump) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| JAGENT | BSC | [0x8e64...e4ae15](https://bscscan.com/token/0x8e6442663a4f8c50b6132c68d42a30e7dfe4ae15) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| GANG | BSC | [0x0c63...20b405](https://bscscan.com/token/0x0c6302401aa5325c2e36f170f52c00b1d220b405) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| [NIO](https://dexscreener.com/solana/b4wmjc6pvjctu3qsvs3ett9mr4m5v5jbkrqctwantc71) | SOL | [7SL2Vn...LQpump](https://solscan.io/token/7SL2VnfYsChvog5oQY9Nmtqu1wceaMiQzWoqoLQpump) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| [ANSEM](https://dexscreener.com/solana/fnzky6x7entq1er3d225dqyt7ybfka4pskbmqhb8l3cc) | SOL | [9cRCn9...TGpump](https://solscan.io/token/9cRCn9rGT8V2imeM2BaKs13yhMEais3ruM3rPvTGpump) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |

## 第二部分：逻辑复盘表格

### A. 上次逻辑总结表
| 逻辑项 | 上次规则 | 本轮验证 |
|---|---|---|
| 主观察门槛 | LP >= $100K，且非PVP，且不过成熟 | v0.3继续保留，并新增LP层级避免不同阶段候选混在一起 |
| PVP过滤 | Volume/LP > 8x 降级，>20x 排除主榜 | v0.3增加PVP明细表，风险不再黑箱隐藏 |
| 多池处理 | symbol bridge合并，以最大LP池为代表 | v0.3保留，并继续标注多池冲突 |
| 合约地址 | v0.2未在主表强制展示 | v0.3强制展示合约地址；缺失时标注不可用 |
| Smart Money | AVE周缓存/本地钱包评分/代理指标分层 | v0.5已支持AVE周缓存接口框架与本地持久保存；缓存为空/过期时仍为低置信，命中后也要看链上行为 |

### B. 本轮逻辑总结表
| 逻辑项 | 本轮结果 | 判断 |
|---|---|---|
| 主观察候选 | 5 个 | 主榜继续稀缺，但必须结合合约地址进入链上确认 |
| PVP风险池 | 8 个 | v0.3已单独展示明细，便于判断噪声来源 |
| 成熟池观察 | 4 个 | 成熟资产不占早期Alpha主榜 |
| 合约地址覆盖 | 可用 25，缺失 0 | 地址缺失会阻断BSC RPC/Helius精查，需要优先补齐 |
| LP层级 | Micro 5 / Early 14 / Liquid 6 / Mature 0 | 下一步可以按层级分别设置进攻规则 |
| S0对比 | 尚未做精确历史回放 | 后续用GeckoTerminal OHLCV / 链上数据补齐 |
| 链上确认 | v0.5执行地址/账户预检 + BSC Transfer级钱包行为样本 | 可以初步看到活跃钱包/缓存命中，但仍不能替代完整Swap留存判断 |
| Smart Money | AVE周缓存 + 代理指标 | 无具体钱包映射前，不允许标记真实吸筹 |

### C. 本轮优化调整表
| 调整项 | 触发原因 | 对下轮筛选影响 |
|---|---|---|
| chain_verify_pipeline | 观察池候选需要链上Swap、钱包留存和大额买卖确认；v0.4.1已生成确认标记并强制落地chain_verify_latest.json | 下轮报告继续输出链上确认/紧急精查表，为接BSC RPC/Helius做准备 |
| emergency_precision_check_policy | 本轮出现满足LP、低波动、买盘占优、非多池冲突的高优先候选 | 下轮这类候选优先进入链上精查或AVE单币紧急刷新建议 |
| early_alpha_range_filter | 检测到成熟池候选，不能让大池成熟资产占用早期Alpha主榜 | 成熟大池进入成熟池观察，不作为底部MEME扫货主观察 |
| multi_pool_conflict_policy | 本轮存在多池数据冲突，不能用单池数据给高置信判断 | 多池价格/LP冲突的币降置信度，不直接升级主观察 |
| symbol_bridge_merge_policy | 本轮存在symbol桥接合并，说明重复输出问题正在被修正 | 减少同一Token在主观察/次观察中重复出现 |

### D. 挖掘策略调优表
| 项目 | 本轮判断 |
|---|---|
| 当前挖掘策略是否有效 | 部分有效：免费源可发现候选，v0.5能展示合约地址、PVP明细、成熟池明细、链上地址预检、AVE缓存状态和钱包行为样本 |
| 主要问题 | AVE接口已做可配置接入框架，BSC已做Transfer行为样本；仍缺完整Swap路径、钱包买后留存、Router/CEX出货和S0精确回放 |
| 假阳性风险 | 已降低，但代理指标仍可能误判买盘质量 |
| 漏筛风险 | 存在，DEXScreener/GeckoTerminal无法覆盖所有新池细节 |
| 候选来源调整 | 暂不新增高频外部源，下一步把v0.5 Transfer样本升级为完整Swap解析、钱包留存和Router/CEX路径 |
| 阈值调整 | 暂不改数值；先按Micro/Early/Liquid/Mature层级观察不同阶段表现 |
| 下轮挖掘方向 | 主观察必须有合约地址；优先对emergency_precision_check做完整Swap留存解析；AVE只周更保存Smart Wallet身份库，每小时只映射当前链上行为 |

## 第三部分：策略回写确认

| 项目 | 状态 |
|---|---|
| 是否已将本轮优化策略写回主定时策略 | 是 |
| 写回内容摘要 | 本轮确认结构性规则：合约地址强制展示、LP层级分离、PVP/成熟池明细、链上确认标记、早期Alpha过滤、多池冲突降置信 |
| 下轮是否生效 | 是 |
| 未写回原因 | - |

## 数据源状态
| 数据源 | 状态 |
|---|---|
| dexscreener_profiles | {'ok': True, 'count': 30, 'expanded': 30} |
| dexscreener_boosts | {'ok': True, 'count': 30, 'expanded': 25} |
| dexscreener_search | {'ok': True, 'count': 331} |
| geckoterminal_bsc_trending | {'ok': True, 'count': 20} |
| geckoterminal_solana_trending | {'ok': True, 'count': 20} |

## 数据限制
- This v0.4 scan uses free public sources plus lightweight chain address/account preflight when enabled.
- AVE Smart Money weekly cache structure is connected; real AVE API refresh is handled by the weekly workflow/cache file.
- S0 exact historical replay is not implemented yet; candidates are marked with current metrics only.
- Wallet-level buy/sell retention is not implemented yet; v0.4 only preflights token contract/account existence.
- v0.4 adds chain preflight status and Smart Wallet cache status on top of contract-address output, liquidity tiers, visible PVP/mature detail tables, and chain-verify flags.
- Contract addresses are extracted from DEXScreener baseToken or GeckoTerminal relationships when available; missing addresses are explicitly marked unavailable.