# 自我进化轮巡

**本轮时间 UTC：** 2026-10-04T10:21:32Z
**版本：** 0.5.0-ave-cache-wallet-behavior-prep
**S0 时间锚点：** 2026-06-16T16:15:17+09:00

## 一句话结论
本轮从 142 个合并Token中筛出 2 个主观察候选。v0.5已在v0.4.1基础上增加AVE周缓存真实接口接入框架、Smart Wallet持久保存、wallet_behavior_latest.json，以及BSC Transfer级钱包行为样本。注意：BSC当前是Transfer样本，不等同完整Swap解码。
合约地址可用 25 个，缺失 0 个；缺失地址的候选不能进入后续链上精查。

## 本轮扫描摘要
| 指标 | 数量 |
|---|---:|
| 原始池子记录 | 240 |
| 合并后Token | 142 |
| 输出候选 | 25 |
| 主观察 | 2 |
| 次观察 | 8 |
| PVP风险池 | 8 |
| 成熟池观察 | 6 |
| 低优先观察 | 1 |
| 多池Token | 6 |
| 多池冲突 | 1 |
| Symbol桥接合并 | 1 |
| 合约地址可用 | 25 |
| 合约地址缺失 | 0 |
| Micro层 | 2 |
| Early层 | 12 |
| Liquid层 | 9 |
| Mature层 | 2 |
| 需要链上确认 | 18 |
| 紧急精查候选 | 0 |

## v0.5 数据确认状态
| 项目 | 状态 |
|---|---|
| AVE Smart Wallet周缓存 | active，钱包数 1651，刷新时间 2026-09-28T02:48:12Z，是否过期 否 |
| 链上预检 | 本轮检查 12 个，验证通过 12 个，失败 0 个 |
| Helius状态 | 未配置，SOL使用公共RPC或跳过增强解析 |
| 当前精查层级 | 0.5.0-chain-preflight-plus-wallet-behavior：地址/账户预检 + v0.5钱包行为样本，完整Swap留存仍待下一版 |
| 钱包行为样本 | 本轮检查 2 个，BSC Transfer样本 2 个，SOL签名级 0 个，AVE钱包命中 0 个 |

## 第一部分：生成结果表格

### A. 上次记录结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| 龙虾 | BSC | [0xeccb...7e4444](https://bscscan.com/token/0xeccbb861c0dda7efd964010085488b69317e4444) | 主观察 | Score 81; Tier Liquid; LP $2.18M; Vol24H $7.49M; 24H +8.60%; V/LP 3.44x; 池数 15; 分项 L20/V17/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| PAID | SOL | [98kfF7...zypump](https://solscan.io/token/98kfF7rmsg1QDUEoCqNE7g7M1FdrTt92TEp2CLzypump) | 主观察 | Score 80; Tier Early; LP $578.7K; Vol24H $1.73M; 24H -16.65%; V/LP 2.98x; 池数 1; 分项 L16/V15/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| COLLECT | BSC | [0x4b3d...a087d3](https://bscscan.com/token/0x4b3d30992f003c8167699735f5ab2831b2a087d3) | 主观察 | Score 78; Tier Liquid; LP $2.18M; Vol24H $6.04M; 24H +11.74%; V/LP 2.77x; 池数 1; 分项 L20/V17/B17/Buy0/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| BREW | BSC | [0xfa6d...3f2159](https://bscscan.com/token/0xfa6d9b504848606eb9aec04ccc161d169b3f2159) | 次观察 | Score 72; Tier Liquid; LP $766.5K; Vol24H $398.4K; 24H -13.02%; V/LP 0.52x; 池数 1; 分项 L17/V11/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| SKHYB | BSC | [0xca75...7bdb61](https://bscscan.com/token/0xca750ef65f295bbecd685abf54e82caf297bdb61) | 次观察 | Score 65; Tier Liquid; LP $778.0K; Vol24H $10.29M; 24H +0.87%; V/LP 13.23x; 池数 1; 分项 L17/V17/B22/Buy3/Risk-18 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| PEPENOM | SOL | [EpEfnZ...fQpump](https://solscan.io/token/EpEfnZxQyiBXppSKi8sncc8w4corn1UJbF9G91fQpump) | 次观察 | Score 65; Tier Early; LP $123.4K; Vol24H $46.7K; 24H -2.53%; V/LP 0.38x; 池数 1; 分项 L10/V5/B22/Buy12/Risk-8 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [USDF](https://dexscreener.com/solana/aqp9ekhgp1u35usbdayglpgnvzuyezlshfxfzkw3cye9) | SOL | [7MuvW6...Ropump](https://solscan.io/token/7MuvW6G2pDTGSjzpjqeDYigUsXqqd6TmEzLgvRRopump) | 次观察 | Score 64; Tier Micro; LP $87.5K; Vol24H $74.7K; 24H +11.15%; V/LP 0.85x; 池数 1; 分项 L9/V6/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [GOIF](https://dexscreener.com/solana/4d56grhvrhh825hjbrkx4t6a5u9ujwcmgpsyv9bwhy3o) | SOL | [nZbPjC...6Dpump](https://solscan.io/token/nZbPjCn4GJcLxrdHWRnMhPt875EyHSNTzhFmD6Dpump) | 次观察 | Score 64; Tier Early; LP $310.1K; Vol24H $262.0K; 24H +28.20%; V/LP 0.85x; 池数 1; 分项 L14/V10/B8/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [swordcat](https://dexscreener.com/solana/8ewuf2o8acro7fqwepz3tkhkbbjndzu4ldk9scrpw83d) | SOL | [5tCju6...SFpump](https://solscan.io/token/5tCju6YNxHq5zrA6tGndr6F7TK42mpUFmeE31cSFpump) | PVP风险池 | Score 47; Tier Early; LP $161.3K; Vol24H $3.99M; 24H -13.72%; V/LP 24.76x; 池数 2; 分项 L11/V17/B17/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| DEBIT | BSC | [0x6666...83ce49](https://bscscan.com/token/0x66661c7229901f568f16bd1551b3ba826f83ce49) | PVP风险池 | Score 39; Tier Liquid; LP $1.61M; Vol24H $54.56M; 24H +12.54%; V/LP 33.83x; 池数 1; 分项 L20/V17/B17/Buy3/Risk-42 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### B. 本轮扫描结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| 龙虾 | BSC | [0xeccb...7e4444](https://bscscan.com/token/0xeccbb861c0dda7efd964010085488b69317e4444) | 主观察 | Score 86; Tier Liquid; LP $2.11M; Vol24H $5.50M; 24H +5.57%; V/LP 2.60x; 池数 11; 分项 L20/V17/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| SKHYB | BSC | [0xca75...7bdb61](https://bscscan.com/token/0xca750ef65f295bbecd685abf54e82caf297bdb61) | 主观察 | Score 82; Tier Liquid; LP $750.9K; Vol24H $1.95M; 24H -1.98%; V/LP 2.60x; 池数 1; 分项 L17/V16/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| COLLECT | BSC | [0x4b3d...a087d3](https://bscscan.com/token/0x4b3d30992f003c8167699735f5ab2831b2a087d3) | 次观察 | Score 72; Tier Liquid; LP $2.37M; Vol24H $13.83M; 24H +29.79%; V/LP 5.84x; 池数 1; 分项 L20/V17/B8/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| BREW | BSC | [0xfa6d...3f2159](https://bscscan.com/token/0xfa6d9b504848606eb9aec04ccc161d169b3f2159) | 次观察 | Score 72; Tier Liquid; LP $751.6K; Vol24H $433.1K; 24H -12.68%; V/LP 0.58x; 池数 1; 分项 L17/V11/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [EMBER](https://dexscreener.com/solana/2y6pcqa4fep3jlifdan9jvmw7lsk8f3gwstfy8p7trae) | SOL | [5dvXTZ...k4QEC6](https://solscan.io/token/5dvXTZ5qwgafnHtwu3Ls3QrWx1U4LQsFeCuJgkk4QEC6) | 次观察 | Score 69; Tier Early; LP $269.7K; Vol24H $312.7K; 24H -22.75%; V/LP 1.16x; 池数 1; 分项 L13/V10/B17/Buy8/Risk-3 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [USDF](https://dexscreener.com/solana/aqp9ekhgp1u35usbdayglpgnvzuyezlshfxfzkw3cye9) | SOL | [7MuvW6...Ropump](https://solscan.io/token/7MuvW6G2pDTGSjzpjqeDYigUsXqqd6TmEzLgvRRopump) | 次观察 | Score 64; Tier Micro; LP $89.0K; Vol24H $81.1K; 24H +13.07%; V/LP 0.91x; 池数 1; 分项 L9/V6/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [GOIF](https://dexscreener.com/solana/4d56grhvrhh825hjbrkx4t6a5u9ujwcmgpsyv9bwhy3o) | SOL | [nZbPjC...6Dpump](https://solscan.io/token/nZbPjCn4GJcLxrdHWRnMhPt875EyHSNTzhFmD6Dpump) | 次观察 | Score 64; Tier Early; LP $314.9K; Vol24H $269.2K; 24H +27.64%; V/LP 0.85x; 池数 1; 分项 L14/V10/B8/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [memestock](https://dexscreener.com/bsc/0x7bdc9582aca6ca25e5db1f2c8e59003b880672cb) | BSC | [0x6FF4...057777](https://bscscan.com/token/0x6FF45323817d1d53bbb8A8dFbA9245aE74057777) | 次观察 | Score 64; Tier Early; LP $130.8K; Vol24H $129.0K; 24H -10.29%; V/LP 0.99x; 池数 1; 分项 L10/V8/B17/Buy8/Risk-3 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| AIN | BSC | [0x9558...84f4a3](https://bscscan.com/token/0x9558a9254890b2a8b057a789f413631b9084f4a3) | 次观察 | Score 64; Tier Liquid; LP $1.38M; Vol24H $7.71M; 24H +129.76%; V/LP 5.58x; 池数 1; 分项 L20/V17/B0/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| PEPENOM | SOL | [EpEfnZ...fQpump](https://solscan.io/token/EpEfnZxQyiBXppSKi8sncc8w4corn1UJbF9G91fQpump) | 次观察 | Score 64; Tier Early; LP $122.0K; Vol24H $38.4K; 24H -4.48%; V/LP 0.32x; 池数 1; 分项 L10/V4/B22/Buy12/Risk-8 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| DEBIT | BSC | [0x6666...83ce49](https://bscscan.com/token/0x66661c7229901f568f16bd1551b3ba826f83ce49) | PVP风险池 | Score 39; Tier Liquid; LP $1.54M; Vol24H $52.29M; 24H -10.49%; V/LP 33.93x; 池数 1; 分项 L20/V17/B17/Buy3/Risk-42 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [MISTAKE](https://dexscreener.com/solana/867dkvaccyrrudp66bqnxbujxfjaxsnb9wtpc4cmbdad) | SOL | [HKZDfZ...9wpump](https://solscan.io/token/HKZDfZnkHZxd9agRDNPyDv4iT6LmAurJnpRtj9wpump) | PVP风险池 | Score 34; Tier Early; LP $396.5K; Vol24H $10.01M; 24H +236.00%; V/LP 25.26x; 池数 1; 分项 L15/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [Agency](https://dexscreener.com/solana/cyjwknliiy4fmiwqmcswfshxo7t9ubshgs2uraujcrk5) | SOL | [7Vertk...XVpump](https://solscan.io/token/7VertkgF9KLhxxJXHX6uaWuoYZTP9LdGj2bWmVXVpump) | PVP风险池 | Score 31; Tier Early; LP $645.3K; Vol24H $22.54M; 24H +1084.00%; V/LP 34.92x; 池数 2; 分项 L17/V17/B0/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| CRAWL | SOL | [BXoHJd...Dkpump](https://solscan.io/token/BXoHJddsWJLHtAopeiSbKUSELsu8hSFMs8baGMDkpump) | PVP风险池 | Score 31; Tier Early; LP $178.7K; Vol24H $11.39M; 24H +5533.23%; V/LP 63.72x; 池数 2; 分项 L12/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| CLAUDIA | SOL | [H7TuvD...Gosfas](https://solscan.io/token/H7TuvDxEKygh27zGfGcjKG8JGWgrbyKpPtvJEpGosfas) | PVP风险池 | Score 30; Tier Early; LP $151.9K; Vol24H $10.31M; 24H +3690.06%; V/LP 67.89x; 池数 2; 分项 L11/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### C. PVP风险池明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| DEBIT | BSC | [0x6666...83ce49](https://bscscan.com/token/0x66661c7229901f568f16bd1551b3ba826f83ce49) | 24H波动可控；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP极端偏高；FDV超过早期Alpha主榜上限；成熟大市值 | Score 39; Tier Liquid; LP $1.54M; Vol24H $52.29M; 24H -10.49%; V/LP 33.93x; 池数 1; 分项 L20/V17/B17/Buy3/Risk-42 | 只记录热度，不进入主榜 |
| [MISTAKE](https://dexscreener.com/solana/867dkvaccyrrudp66bqnxbujxfjaxsnb9wtpc4cmbdad) | SOL | [HKZDfZ...9wpump](https://solscan.io/token/HKZDfZnkHZxd9agRDNPyDv4iT6LmAurJnpRtj9wpump) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 34; Tier Early; LP $396.5K; Vol24H $10.01M; 24H +236.00%; V/LP 25.26x; 池数 1; 分项 L15/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [Agency](https://dexscreener.com/solana/cyjwknliiy4fmiwqmcswfshxo7t9ubshgs2uraujcrk5) | SOL | [7Vertk...XVpump](https://solscan.io/token/7VertkgF9KLhxxJXHX6uaWuoYZTP9LdGj2bWmVXVpump) | 买卖基本均衡；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 31; Tier Early; LP $645.3K; Vol24H $22.54M; 24H +1084.00%; V/LP 34.92x; 池数 2; 分项 L17/V17/B0/Buy3/Risk-30 | 只记录热度，不进入主榜 |
| CRAWL | SOL | [BXoHJd...Dkpump](https://solscan.io/token/BXoHJddsWJLHtAopeiSbKUSELsu8hSFMs8baGMDkpump) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 31; Tier Early; LP $178.7K; Vol24H $11.39M; 24H +5533.23%; V/LP 63.72x; 池数 2; 分项 L12/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| CLAUDIA | SOL | [H7TuvD...Gosfas](https://solscan.io/token/H7TuvDxEKygh27zGfGcjKG8JGWgrbyKpPtvJEpGosfas) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 30; Tier Early; LP $151.9K; Vol24H $10.31M; 24H +3690.06%; V/LP 67.89x; 池数 2; 分项 L11/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [knightcat](https://dexscreener.com/solana/dremamrc83ujtbvwuwrdqdaqughdbfgopmbtybm3tjfw) | SOL | [3Dgwn5...LRpump](https://solscan.io/token/3Dgwn5E7H5a8k6iGrz3qirkaJqUaJrKHEZ2xPcLRpump) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 30; Tier Early; LP $178.1K; Vol24H $8.96M; 24H +5529.00%; V/LP 50.33x; 池数 1; 分项 L11/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [Aiden](https://dexscreener.com/solana/5vbavvxs1nlmynjls3qbdorfsuhkn6rbzmfvqdwwsniq) | SOL | [9dSMwF...5WBLXd](https://solscan.io/token/9dSMwFfPezQ8WPcW1uZV7ns4rcviEj2LssSAg75WBLXd) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 29; Tier Early; LP $109.8K; Vol24H $8.34M; 24H +1834.00%; V/LP 75.90x; 池数 2; 分项 L10/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [SPLICE](https://dexscreener.com/solana/61xw4vm2ahziq2bqpthzynuhodzpj2tknynjhn4sjpmm) | SOL | [7bC8ug...mpFyhq](https://solscan.io/token/7bC8ugu1ZJn21MhA4ht483nX8brLNesa8R7XLimpFyhq) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 28; Tier Micro; LP $86.0K; Vol24H $6.17M; 24H +1253.00%; V/LP 71.72x; 池数 5; 分项 L9/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |

### D. 成熟池观察明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| [RAY](https://dexscreener.com/solana/2axxcn6on9bbt5owwmth53c7qhuxvhleu718kqt8rvy2) | SOL | [4k3Dyj...QrkX6R](https://solscan.io/token/4k3Dyjzvzp8eMZWUXbBCjEvwSkkk59S5iCNLY3QrkX6R) | 24H接近横盘；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 79; Tier Liquid; LP $4.35M; Vol24H $6.99M; 24H +2.57%; V/LP 1.60x; 池数 1; 分项 L20/V17/B22/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| ARK | BSC | [0xcae1...618b9d](https://bscscan.com/token/0xcae117ca6bc8a341d2e7207f30e180f0e5618b9d) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 74; Tier Mature; LP $58.14M; Vol24H $3.45M; 24H -0.16%; V/LP 0.06x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| AKE | BSC | [0x2c3a...12f7db](https://bscscan.com/token/0x2c3a8ee94ddd97244a93bc48298f97d2c412f7db) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 73; Tier Liquid; LP $2.86M; Vol24H $1.87M; 24H +4.11%; V/LP 0.65x; 池数 1; 分项 L20/V16/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| MarsCoin | BSC | [0xfe18...5c7777](https://bscscan.com/token/0xfe189e97832da1573e4e4ff034f4ffc3a15c7777) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限 | Score 67; Tier Early; LP $437.5K; Vol24H $1.44M; 24H +1.77%; V/LP 3.29x; 池数 1; 分项 L15/V15/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| [ZEC](https://dexscreener.com/bsc/0xd5e5f613c024ea161814085d281b996c6591647c) | BSC | [0x5ACF...1a3f9F](https://bscscan.com/token/0x5ACF7171C98FFD7E02B0939A7E0124B0031a3f9F) | 买入笔数占优；LP达主观察门槛；24H成交合格；Volume/LP未失真；24H涨跌幅过热；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 61; Tier Liquid; LP $1.46M; Vol24H $11.16M; 24H +138982.00%; V/LP 7.64x; 池数 1; 分项 L20/V17/B0/Buy12/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| [PUMP FUN](https://dexscreener.com/solana/hvth7essypg7ewzwd8ztect4wzlznxtgxbjn2xdztgez) | SOL | [3At4zC...js5R4x](https://solscan.io/token/3At4zCkWM5C9JV66WyVLBT4z9PcpGCUTPvBuhEjs5R4x) | 24H接近横盘；买入笔数占优；LP达主观察门槛；Volume/LP未失真；24H成交不足；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 58; Tier Mature; LP $56.85M; Vol24H $19.80; 24H +0.00%; V/LP 0.00x; 池数 1; 分项 L20/V0/B22/Buy12/Risk-20 | 成熟池观察，不占用早期Alpha主榜 |

### E. 链上确认/紧急精查表
| Token | 链 | 合约地址 | 是否需要链上确认 | 紧急精查 | 预检状态 | 原因 |
|---|---|---|---|---|---|---|
| 龙虾 | BSC | [0xeccb...7e4444](https://bscscan.com/token/0xeccbb861c0dda7efd964010085488b69317e4444) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；多池数据冲突，需链上/聚合源复核 |
| SKHYB | BSC | [0xca75...7bdb61](https://bscscan.com/token/0xca750ef65f295bbecd685abf54e82caf297bdb61) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| COLLECT | BSC | [0x4b3d...a087d3](https://bscscan.com/token/0x4b3d30992f003c8167699735f5ab2831b2a087d3) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| BREW | BSC | [0xfa6d...3f2159](https://bscscan.com/token/0xfa6d9b504848606eb9aec04ccc161d169b3f2159) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [EMBER](https://dexscreener.com/solana/2y6pcqa4fep3jlifdan9jvmw7lsk8f3gwstfy8p7trae) | SOL | [5dvXTZ...k4QEC6](https://solscan.io/token/5dvXTZ5qwgafnHtwu3Ls3QrWx1U4LQsFeCuJgkk4QEC6) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [USDF](https://dexscreener.com/solana/aqp9ekhgp1u35usbdayglpgnvzuyezlshfxfzkw3cye9) | SOL | [7MuvW6...Ropump](https://solscan.io/token/7MuvW6G2pDTGSjzpjqeDYigUsXqqd6TmEzLgvRRopump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [GOIF](https://dexscreener.com/solana/4d56grhvrhh825hjbrkx4t6a5u9ujwcmgpsyv9bwhy3o) | SOL | [nZbPjC...6Dpump](https://solscan.io/token/nZbPjCn4GJcLxrdHWRnMhPt875EyHSNTzhFmD6Dpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [memestock](https://dexscreener.com/bsc/0x7bdc9582aca6ca25e5db1f2c8e59003b880672cb) | BSC | [0x6FF4...057777](https://bscscan.com/token/0x6FF45323817d1d53bbb8A8dFbA9245aE74057777) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| AIN | BSC | [0x9558...84f4a3](https://bscscan.com/token/0x9558a9254890b2a8b057a789f413631b9084f4a3) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| PEPENOM | SOL | [EpEfnZ...fQpump](https://solscan.io/token/EpEfnZxQyiBXppSKi8sncc8w4corn1UJbF9G91fQpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |

### F. 钱包行为 / AVE命中样本表
| Token | 链 | 合约地址 | 行为状态 | 行为层级 | AVE命中 | 判断 |
|---|---|---|---|---|---:|---|
| 龙虾 | BSC | [0xeccb...7e4444](https://bscscan.com/token/0xeccbb861c0dda7efd964010085488b69317e4444) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| SKHYB | BSC | [0xca75...7bdb61](https://bscscan.com/token/0xca750ef65f295bbecd685abf54e82caf297bdb61) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |

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
| 主观察候选 | 2 个 | 主榜继续稀缺，但必须结合合约地址进入链上确认 |
| PVP风险池 | 8 个 | v0.3已单独展示明细，便于判断噪声来源 |
| 成熟池观察 | 6 个 | 成熟资产不占早期Alpha主榜 |
| 合约地址覆盖 | 可用 25，缺失 0 | 地址缺失会阻断BSC RPC/Helius精查，需要优先补齐 |
| LP层级 | Micro 2 / Early 12 / Liquid 9 / Mature 2 | 下一步可以按层级分别设置进攻规则 |
| S0对比 | 尚未做精确历史回放 | 后续用GeckoTerminal OHLCV / 链上数据补齐 |
| 链上确认 | v0.5执行地址/账户预检 + BSC Transfer级钱包行为样本 | 可以初步看到活跃钱包/缓存命中，但仍不能替代完整Swap留存判断 |
| Smart Money | AVE周缓存 + 代理指标 | 无具体钱包映射前，不允许标记真实吸筹 |

### C. 本轮优化调整表
| 调整项 | 触发原因 | 对下轮筛选影响 |
|---|---|---|
| chain_verify_pipeline | 观察池候选需要链上Swap、钱包留存和大额买卖确认；v0.4.1已生成确认标记并强制落地chain_verify_latest.json | 下轮报告继续输出链上确认/紧急精查表，为接BSC RPC/Helius做准备 |
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
| dexscreener_search | {'ok': True, 'count': 337} |
| geckoterminal_bsc_trending | {'ok': True, 'count': 20} |
| geckoterminal_solana_trending | {'ok': True, 'count': 20} |

## 数据限制
- This v0.4 scan uses free public sources plus lightweight chain address/account preflight when enabled.
- AVE Smart Money weekly cache structure is connected; real AVE API refresh is handled by the weekly workflow/cache file.
- S0 exact historical replay is not implemented yet; candidates are marked with current metrics only.
- Wallet-level buy/sell retention is not implemented yet; v0.4 only preflights token contract/account existence.
- v0.4 adds chain preflight status and Smart Wallet cache status on top of contract-address output, liquidity tiers, visible PVP/mature detail tables, and chain-verify flags.
- Contract addresses are extracted from DEXScreener baseToken or GeckoTerminal relationships when available; missing addresses are explicitly marked unavailable.