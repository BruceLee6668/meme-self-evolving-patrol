# 自我进化轮巡

**本轮时间 UTC：** 2026-10-17T19:58:20Z
**版本：** 0.5.0-ave-cache-wallet-behavior-prep
**S0 时间锚点：** 2026-06-16T16:15:17+09:00

## 一句话结论
本轮从 147 个合并Token中筛出 5 个主观察候选。v0.5已在v0.4.1基础上增加AVE周缓存真实接口接入框架、Smart Wallet持久保存、wallet_behavior_latest.json，以及BSC Transfer级钱包行为样本。注意：BSC当前是Transfer样本，不等同完整Swap解码。
合约地址可用 25 个，缺失 0 个；缺失地址的候选不能进入后续链上精查。

## 本轮扫描摘要
| 指标 | 数量 |
|---|---:|
| 原始池子记录 | 243 |
| 合并后Token | 147 |
| 输出候选 | 25 |
| 主观察 | 5 |
| 次观察 | 6 |
| PVP风险池 | 8 |
| 成熟池观察 | 4 |
| 低优先观察 | 2 |
| 多池Token | 7 |
| 多池冲突 | 2 |
| Symbol桥接合并 | 1 |
| 合约地址可用 | 25 |
| 合约地址缺失 | 0 |
| Micro层 | 7 |
| Early层 | 7 |
| Liquid层 | 9 |
| Mature层 | 2 |
| 需要链上确认 | 20 |
| 紧急精查候选 | 4 |

## v0.5 数据确认状态
| 项目 | 状态 |
|---|---|
| AVE Smart Wallet周缓存 | active，钱包数 1888，刷新时间 2026-10-12T03:31:42Z，是否过期 否 |
| 链上预检 | 本轮检查 12 个，验证通过 12 个，失败 0 个 |
| Helius状态 | 未配置，SOL使用公共RPC或跳过增强解析 |
| 当前精查层级 | 0.5.0-chain-preflight-plus-wallet-behavior：地址/账户预检 + v0.5钱包行为样本，完整Swap留存仍待下一版 |
| 钱包行为样本 | 本轮检查 6 个，BSC Transfer样本 3 个，SOL签名级 3 个，AVE钱包命中 0 个 |

## 第一部分：生成结果表格

### A. 上次记录结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| SIREN | BSC | [0x997a...fc18e1](https://bscscan.com/token/0x997a58129890bbda032231a52ed1ddc845fc18e1) | 主观察 | Score 93; Tier Liquid; LP $2.40M; Vol24H $1.73M; 24H +5.48%; V/LP 0.72x; 池数 1; 分项 L20/V15/B22/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| fone | SOL | [CTPoyC...gGpump](https://solscan.io/token/CTPoyCwkjMvoJwU4xvZZqoD8tiYk6yDchySiN5gGpump) | 主观察 | Score 87; Tier Early; LP $490.0K; Vol24H $902.2K; 24H +7.44%; V/LP 1.84x; 池数 1; 分项 L16/V13/B22/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| CATE | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | 主观察 | Score 84; Tier Liquid; LP $2.98M; Vol24H $1.46M; 24H +10.03%; V/LP 0.49x; 池数 2; 分项 L20/V15/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| COLLECT | BSC | [0x4b3d...a087d3](https://bscscan.com/token/0x4b3d30992f003c8167699735f5ab2831b2a087d3) | 主观察 | Score 83; Tier Liquid; LP $2.21M; Vol24H $3.61M; 24H -0.23%; V/LP 1.63x; 池数 1; 分项 L20/V17/B22/Buy0/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [DAWG](https://dexscreener.com/bsc/0x9e83be1267e9a6d43bb7f3a8c0dc3c092ccae63e) | BSC | [0x7D04...237777](https://bscscan.com/token/0x7D0443CdDFc8E11AF105F4fE44Dd28c630237777) | 主观察 | Score 78; Tier Early; LP $200.6K; Vol24H $788.8K; 24H -21.52%; V/LP 3.93x; 池数 2; 分项 L12/V13/B17/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [ATFS](https://dexscreener.com/solana/6tgnyxvuwgvtqpkovvgrqnvodvdrvtt8rr8gtya7wmeu) | SOL | [rQkzN8...phpump](https://solscan.io/token/rQkzN8ZvvVn3sonN4kBH6tHDwxQSG88nrRLBHphpump) | 次观察 | Score 77; Tier Early; LP $421.9K; Vol24H $191.7K; 24H +19.01%; V/LP 0.45x; 池数 1; 分项 L15/V9/B17/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 次观察，不直接进攻 |
| AEON | BSC | [0x277a...ec9b80](https://bscscan.com/token/0x277add739c6e0477616948357af9e79fe1ec9b80) | 次观察 | Score 77; Tier Liquid; LP $1.12M; Vol24H $3.11M; 24H +16.95%; V/LP 2.79x; 池数 1; 分项 L19/V17/B17/Buy0/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，不直接进攻 |
| [IOF](https://dexscreener.com/solana/7wcareycymxe2olsuaptqg4ybx5hfh1msinrhq4pvhjm) | SOL | [2sY7rk...6Bpump](https://solscan.io/token/2sY7rkMCQyFNcSpHm3fciJf2ptYRg3cYpn4srN6Bpump) | 次观察 | Score 75; Tier Early; LP $286.0K; Vol24H $160.2K; 24H -4.14%; V/LP 0.56x; 池数 1; 分项 L13/V8/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [DOPE](https://dexscreener.com/solana/6iep3egqksbzwgzmbcyajtivtvykcgl9bnpbewlr8agq) | SOL | [33jENU...CNpump](https://solscan.io/token/33jENUQnjoitkMFpvNJcSHyLAHFWJuHwT6E3E8CNpump) | 次观察 | Score 72; Tier Early; LP $247.9K; Vol24H $1.39M; 24H -10.70%; V/LP 5.61x; 池数 1; 分项 L13/V15/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| SI276 | SOL | [HMYd9t...6upump](https://solscan.io/token/HMYd9tosnUXuNHmq7pXmoePRVBLBBjA3JBfydq6upump) | 次观察 | Score 71; Tier Micro; LP $85.4K; Vol24H $234.1K; 24H -8.82%; V/LP 2.74x; 池数 1; 分项 L9/V9/B17/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |

### B. 本轮扫描结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| SIREN | BSC | [0x997a...fc18e1](https://bscscan.com/token/0x997a58129890bbda032231a52ed1ddc845fc18e1) | 主观察 | Score 93; Tier Liquid; LP $2.39M; Vol24H $1.74M; 24H +2.05%; V/LP 0.73x; 池数 1; 分项 L20/V15/B22/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| fone | SOL | [CTPoyC...gGpump](https://solscan.io/token/CTPoyCwkjMvoJwU4xvZZqoD8tiYk6yDchySiN5gGpump) | 主观察 | Score 87; Tier Early; LP $496.3K; Vol24H $895.9K; 24H +5.03%; V/LP 1.81x; 池数 1; 分项 L16/V13/B22/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| COLLECT | BSC | [0x4b3d...a087d3](https://bscscan.com/token/0x4b3d30992f003c8167699735f5ab2831b2a087d3) | 主观察 | Score 86; Tier Liquid; LP $2.22M; Vol24H $3.50M; 24H +0.29%; V/LP 1.58x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| CATE | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | 主观察 | Score 84; Tier Liquid; LP $3.06M; Vol24H $1.57M; 24H +11.28%; V/LP 0.51x; 池数 2; 分项 L20/V15/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [DAWG](https://dexscreener.com/bsc/0x9e83be1267e9a6d43bb7f3a8c0dc3c092ccae63e) | BSC | [0x7D04...237777](https://bscscan.com/token/0x7D0443CdDFc8E11AF105F4fE44Dd28c630237777) | 主观察 | Score 83; Tier Early; LP $210.9K; Vol24H $727.4K; 24H +5.42%; V/LP 3.45x; 池数 2; 分项 L12/V13/B22/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [ATFS](https://dexscreener.com/solana/6tgnyxvuwgvtqpkovvgrqnvodvdrvtt8rr8gtya7wmeu) | SOL | [rQkzN8...phpump](https://solscan.io/token/rQkzN8ZvvVn3sonN4kBH6tHDwxQSG88nrRLBHphpump) | 次观察 | Score 77; Tier Early; LP $426.1K; Vol24H $185.9K; 24H +15.62%; V/LP 0.44x; 池数 1; 分项 L15/V9/B17/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 次观察，不直接进攻 |
| AEON | BSC | [0x277a...ec9b80](https://bscscan.com/token/0x277add739c6e0477616948357af9e79fe1ec9b80) | 次观察 | Score 77; Tier Liquid; LP $1.06M; Vol24H $3.73M; 24H +10.22%; V/LP 3.52x; 池数 1; 分项 L19/V17/B17/Buy0/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，不直接进攻 |
| [SI276](https://dexscreener.com/solana/12jc1dzjpzbcdakum4brakh9jcfry2tlg1ffgsl4ftcg) | SOL | [HMYd9t...6upump](https://solscan.io/token/HMYd9tosnUXuNHmq7pXmoePRVBLBBjA3JBfydq6upump) | 次观察 | Score 71; Tier Micro; LP $84.6K; Vol24H $220.8K; 24H -19.42%; V/LP 2.61x; 池数 2; 分项 L9/V9/B17/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| TART | BSC | [0x7ab8...750314](https://bscscan.com/token/0x7ab8d02cbb51ff7223fde700eaaa2a91bf750314) | 次观察 | Score 67; Tier Liquid; LP $751.8K; Vol24H $189.6K; 24H -9.44%; V/LP 0.25x; 池数 1; 分项 L17/V9/B17/Buy0/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [MISTAKE](https://dexscreener.com/solana/867dkvaccyrrudp66bqnxbujxfjaxsnb9wtpc4cmbdad) | SOL | [HKZDfZ...9wpump](https://solscan.io/token/HKZDfZnkHZxd9agRDNPyDv4iT6LmAurJnpRtj9wpump) | 次观察 | Score 66; Tier Early; LP $213.9K; Vol24H $260.2K; 24H +16.60%; V/LP 1.22x; 池数 2; 分项 L12/V10/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [CLAUDIA](https://dexscreener.com/solana/fe7bpdycs74gqicuf14hwgumtopkv1d9mdyvx5btohfr) | SOL | [2j5SaS...hnW2ZM](https://solscan.io/token/2j5SaS7xy776qCBpyPQbZjyQSAtKiFgrwjfErthnW2ZM) | 次观察 | Score 65; Tier Early; LP $353.8K; Vol24H $2.19M; 24H +74.18%; V/LP 6.19x; 池数 1; 分项 L14/V16/B8/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [simulator](https://dexscreener.com/solana/ezjv2ygpbs3vm5qwmgqyq4gpvi77ldhwgfhay6u4ts1u) | SOL | [8hnMfF...jvHje4](https://solscan.io/token/8hnMfF4XL717GVwzDmvqjJvULozKW6w7BhHFABjvHje4) | PVP风险池 | Score 29; Tier Early; LP $122.5K; Vol24H $5.44M; 24H +653.00%; V/LP 44.41x; 池数 2; 分项 L10/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| PRIME | SOL | [rVWG97...u3pump](https://solscan.io/token/rVWG97Yj6ZbuF9zeQo8TosQG6mUcUeL8BocfHu3pump) | PVP风险池 | Score 29; Tier Micro; LP $20.9K; Vol24H $2.98M; 24H +23.18%; V/LP 142.47x; 池数 1; 分项 L3/V17/B17/Buy8/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [onboard](https://dexscreener.com/solana/dbzf8tq3mtlsdgmlcdj1ya7e8hqatq22jafqma92fi4) | SOL | [5ubruM...4bpump](https://solscan.io/token/5ubruMYpgKqw9ip5J1qrXbVGmMdn2VCsMg421B4bpump) | PVP风险池 | Score 28; Tier Micro; LP $35.1K; Vol24H $4.58M; 24H -17.79%; V/LP 130.49x; 池数 1; 分项 L5/V17/B17/Buy8/Risk-43 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| AGT | BSC | [0x5dbd...cae274](https://bscscan.com/token/0x5dbde81fce337ff4bcaaee4ca3466c00aecae274) | PVP风险池 | Score 22; Tier Liquid; LP $2.78M; Vol24H $132.11M; 24H +81.69%; V/LP 47.50x; 池数 1; 分项 L20/V17/B0/Buy3/Risk-42 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### C. PVP风险池明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| [simulator](https://dexscreener.com/solana/ezjv2ygpbs3vm5qwmgqyq4gpvi77ldhwgfhay6u4ts1u) | SOL | [8hnMfF...jvHje4](https://solscan.io/token/8hnMfF4XL717GVwzDmvqjJvULozKW6w7BhHFABjvHje4) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 29; Tier Early; LP $122.5K; Vol24H $5.44M; 24H +653.00%; V/LP 44.41x; 池数 2; 分项 L10/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| PRIME | SOL | [rVWG97...u3pump](https://solscan.io/token/rVWG97Yj6ZbuF9zeQo8TosQG6mUcUeL8BocfHu3pump) | 24H波动可控；买卖略偏买入；LP未达主观察门槛；24H成交合格；LP偏薄；Volume/LP极端偏高 | Score 29; Tier Micro; LP $20.9K; Vol24H $2.98M; 24H +23.18%; V/LP 142.47x; 池数 1; 分项 L3/V17/B17/Buy8/Risk-40 | 只记录热度，不进入主榜 |
| [onboard](https://dexscreener.com/solana/dbzf8tq3mtlsdgmlcdj1ya7e8hqatq22jafqma92fi4) | SOL | [5ubruM...4bpump](https://solscan.io/token/5ubruMYpgKqw9ip5J1qrXbVGmMdn2VCsMg421B4bpump) | 24H波动可控；买卖略偏买入；LP未达主观察门槛；24H成交合格；LP偏薄；Volume/LP极端偏高；非主流报价池 | Score 28; Tier Micro; LP $35.1K; Vol24H $4.58M; 24H -17.79%; V/LP 130.49x; 池数 1; 分项 L5/V17/B17/Buy8/Risk-43 | 只记录热度，不进入主榜 |
| AGT | BSC | [0x5dbd...cae274](https://bscscan.com/token/0x5dbde81fce337ff4bcaaee4ca3466c00aecae274) | 买卖基本均衡；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高；FDV超过早期Alpha主榜上限；成熟大市值 | Score 22; Tier Liquid; LP $2.78M; Vol24H $132.11M; 24H +81.69%; V/LP 47.50x; 池数 1; 分项 L20/V17/B0/Buy3/Risk-42 | 只记录热度，不进入主榜 |
| Q | BSC | [0xc07e...690589](https://bscscan.com/token/0xc07e1300dc138601fa6b0b59f8d0fa477e690589) | 买卖基本均衡；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 22; Tier Liquid; LP $1.48M; Vol24H $33.82M; 24H +124.30%; V/LP 22.91x; 池数 1; 分项 L20/V17/B0/Buy3/Risk-42 | 只记录热度，不进入主榜 |
| [Eternia](https://dexscreener.com/solana/abqxgs5c78p8nix49kqsbtnqjammahcbh2mvjq1zqqz2) | SOL | [CY27Qv...5Ypump](https://solscan.io/token/CY27QvCQBCmLBuz3V7c8snEeD4z67iyoSTkwo35Ypump) | 买入笔数占优；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 19; Tier Micro; LP $49.0K; Vol24H $11.58M; 24H +413.00%; V/LP 236.21x; 池数 1; 分项 L6/V17/B0/Buy12/Risk-40 | 只记录热度，不进入主榜 |
| [MAKERS](https://dexscreener.com/solana/d6g4brfhugystkpcbkmueqesnd7gjugzdczenicattmy) | SOL | [3XEqNH...86pump](https://solscan.io/token/3XEqNHe3jHTRWAZCTHbb1UwpSfNbJL9oU1ErsM86pump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 14; Tier Micro; LP $36.3K; Vol24H $2.70M; 24H +286.00%; V/LP 74.37x; 池数 3; 分项 L5/V17/B0/Buy8/Risk-40 | 只记录热度，不进入主榜 |
| [Aloooong](https://dexscreener.com/solana/6cwezyjcrn2zqedjd7nke38nidn99h9wy48zbhyqbvpw) | SOL | [1htv5N...Vopurp](https://solscan.io/token/1htv5Nzfdy44FJWAdTXZoACJW4BWbB2XwZC6SVopurp) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高；非主流报价池 | Score 10; Tier Micro; LP $38.7K; Vol24H $2.34M; 24H +474.00%; V/LP 60.46x; 池数 1; 分项 L5/V16/B0/Buy8/Risk-43 | 只记录热度，不进入主榜 |

### D. 成熟池观察明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| PUMP | SOL | [pumpCm...7H9Dfn](https://solscan.io/token/pumpCmXqMfrsAkQ5r49WcJnRayYRqmXz6ae8H7H9Dfn) | 24H接近横盘；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 79; Tier Mature; LP $23.58M; Vol24H $4.82M; 24H +3.02%; V/LP 0.20x; 池数 1; 分项 L20/V17/B22/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| ARK | BSC | [0xcae1...618b9d](https://bscscan.com/token/0xcae117ca6bc8a341d2e7207f30e180f0e5618b9d) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 73; Tier Mature; LP $57.35M; Vol24H $2.02M; 24H +0.08%; V/LP 0.04x; 池数 1; 分项 L20/V16/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| [GDF](https://dexscreener.com/solana/8beaprgrcgqv8o7es15n4cq2pp5ajt5quugobpct1ueo) | SOL | [5RfRCK...vcpump](https://solscan.io/token/5RfRCKvGMDqQDQAraRv6S7HG2xQH4wje3uFWFevcpump) | 24H未过热但已明显波动；买入笔数占优；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 63; Tier Liquid; LP $1.42M; Vol24H $349.3K; 24H +28.79%; V/LP 0.25x; 池数 1; 分项 L20/V11/B8/Buy12/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| [XTO](https://dexscreener.com/solana/2aewsofkaipyotedsswvdl5pacmb9gvk9dtg5w8uhhgj) | SOL | [3rF2NS...G2pump](https://solscan.io/token/3rF2NSivMQcHgKJfSQST2SHESmsHr6vHbzfkVgG2pump) | 买入笔数占优；LP达主观察门槛；24H成交合格；Volume/LP未失真；24H涨跌幅过热；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 58; Tier Liquid; LP $2.11M; Vol24H $1.13M; 24H +6006.00%; V/LP 0.53x; 池数 1; 分项 L20/V14/B0/Buy12/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |

### E. 链上确认/紧急精查表
| Token | 链 | 合约地址 | 是否需要链上确认 | 紧急精查 | 预检状态 | 原因 |
|---|---|---|---|---|---|---|
| SIREN | BSC | [0x997a...fc18e1](https://bscscan.com/token/0x997a58129890bbda032231a52ed1ddc845fc18e1) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| fone | SOL | [CTPoyC...gGpump](https://solscan.io/token/CTPoyCwkjMvoJwU4xvZZqoD8tiYk6yDchySiN5gGpump) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| CATE | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| [ATFS](https://dexscreener.com/solana/6tgnyxvuwgvtqpkovvgrqnvodvdrvtt8rr8gtya7wmeu) | SOL | [rQkzN8...phpump](https://solscan.io/token/rQkzN8ZvvVn3sonN4kBH6tHDwxQSG88nrRLBHphpump) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| COLLECT | BSC | [0x4b3d...a087d3](https://bscscan.com/token/0x4b3d30992f003c8167699735f5ab2831b2a087d3) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [DAWG](https://dexscreener.com/bsc/0x9e83be1267e9a6d43bb7f3a8c0dc3c092ccae63e) | BSC | [0x7D04...237777](https://bscscan.com/token/0x7D0443CdDFc8E11AF105F4fE44Dd28c630237777) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；多池数据冲突，需链上/聚合源复核 |
| AEON | BSC | [0x277a...ec9b80](https://bscscan.com/token/0x277add739c6e0477616948357af9e79fe1ec9b80) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [SI276](https://dexscreener.com/solana/12jc1dzjpzbcdakum4brakh9jcfry2tlg1ffgsl4ftcg) | SOL | [HMYd9t...6upump](https://solscan.io/token/HMYd9tosnUXuNHmq7pXmoePRVBLBBjA3JBfydq6upump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| TART | BSC | [0x7ab8...750314](https://bscscan.com/token/0x7ab8d02cbb51ff7223fde700eaaa2a91bf750314) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [MISTAKE](https://dexscreener.com/solana/867dkvaccyrrudp66bqnxbujxfjaxsnb9wtpc4cmbdad) | SOL | [HKZDfZ...9wpump](https://solscan.io/token/HKZDfZnkHZxd9agRDNPyDv4iT6LmAurJnpRtj9wpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |

### F. 钱包行为 / AVE命中样本表
| Token | 链 | 合约地址 | 行为状态 | 行为层级 | AVE命中 | 判断 |
|---|---|---|---|---|---:|---|
| SIREN | BSC | [0x997a...fc18e1](https://bscscan.com/token/0x997a58129890bbda032231a52ed1ddc845fc18e1) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| fone | SOL | [CTPoyC...gGpump](https://solscan.io/token/CTPoyCwkjMvoJwU4xvZZqoD8tiYk6yDchySiN5gGpump) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| CATE | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| [ATFS](https://dexscreener.com/solana/6tgnyxvuwgvtqpkovvgrqnvodvdrvtt8rr8gtya7wmeu) | SOL | [rQkzN8...phpump](https://solscan.io/token/rQkzN8ZvvVn3sonN4kBH6tHDwxQSG88nrRLBHphpump) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| COLLECT | BSC | [0x4b3d...a087d3](https://bscscan.com/token/0x4b3d30992f003c8167699735f5ab2831b2a087d3) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| [DAWG](https://dexscreener.com/bsc/0x9e83be1267e9a6d43bb7f3a8c0dc3c092ccae63e) | BSC | [0x7D04...237777](https://bscscan.com/token/0x7D0443CdDFc8E11AF105F4fE44Dd28c630237777) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |

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
| LP层级 | Micro 7 / Early 7 / Liquid 9 / Mature 2 | 下一步可以按层级分别设置进攻规则 |
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
| dexscreener_search | {'ok': True, 'count': 332} |
| geckoterminal_bsc_trending | {'ok': True, 'count': 20} |
| geckoterminal_solana_trending | {'ok': True, 'count': 20} |

## 数据限制
- This v0.4 scan uses free public sources plus lightweight chain address/account preflight when enabled.
- AVE Smart Money weekly cache structure is connected; real AVE API refresh is handled by the weekly workflow/cache file.
- S0 exact historical replay is not implemented yet; candidates are marked with current metrics only.
- Wallet-level buy/sell retention is not implemented yet; v0.4 only preflights token contract/account existence.
- v0.4 adds chain preflight status and Smart Wallet cache status on top of contract-address output, liquidity tiers, visible PVP/mature detail tables, and chain-verify flags.
- Contract addresses are extracted from DEXScreener baseToken or GeckoTerminal relationships when available; missing addresses are explicitly marked unavailable.