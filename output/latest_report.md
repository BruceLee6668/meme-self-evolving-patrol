# 自我进化轮巡

**本轮时间 UTC：** 2026-06-20T08:47:11Z
**版本：** 0.5.0-ave-cache-wallet-behavior-prep
**S0 时间锚点：** 2026-06-16T16:15:17+09:00

## 一句话结论
本轮从 128 个合并Token中筛出 5 个主观察候选。v0.5已在v0.4.1基础上增加AVE周缓存真实接口接入框架、Smart Wallet持久保存、wallet_behavior_latest.json，以及BSC Transfer级钱包行为样本。注意：BSC当前是Transfer样本，不等同完整Swap解码。
合约地址可用 25 个，缺失 0 个；缺失地址的候选不能进入后续链上精查。

## 本轮扫描摘要
| 指标 | 数量 |
|---|---:|
| 原始池子记录 | 310 |
| 合并后Token | 128 |
| 输出候选 | 25 |
| 主观察 | 5 |
| 次观察 | 7 |
| PVP风险池 | 8 |
| 成熟池观察 | 5 |
| 低优先观察 | 0 |
| 多池Token | 13 |
| 多池冲突 | 2 |
| Symbol桥接合并 | 1 |
| 合约地址可用 | 25 |
| 合约地址缺失 | 0 |
| Micro层 | 10 |
| Early层 | 5 |
| Liquid层 | 6 |
| Mature层 | 4 |
| 需要链上确认 | 20 |
| 紧急精查候选 | 3 |

## v0.5 数据确认状态
| 项目 | 状态 |
|---|---|
| AVE Smart Wallet周缓存 | active，钱包数 200，刷新时间 2026-06-17T17:59:17Z，是否过期 否 |
| 链上预检 | 本轮检查 12 个，验证通过 12 个，失败 0 个 |
| Helius状态 | 未配置，SOL使用公共RPC或跳过增强解析 |
| 当前精查层级 | 0.5.0-chain-preflight-plus-wallet-behavior：地址/账户预检 + v0.5钱包行为样本，完整Swap留存仍待下一版 |
| 钱包行为样本 | 本轮检查 5 个，BSC Transfer样本 2 个，SOL签名级 3 个，AVE钱包命中 0 个 |

## 第一部分：生成结果表格

### A. 上次记录结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| KINS | SOL | [Tqj8yF...9bpump](https://solscan.io/token/Tqj8yFmagrg7oorpQkVGYR52r96RFTamvWfth9bpump) | 主观察 | Score 84; Tier Early; LP $467.6K; Vol24H $1.49M; 24H -4.67%; V/LP 3.19x; 池数 3; 分项 L15/V15/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| SIREN | BSC | [0x997a...fc18e1](https://bscscan.com/token/0x997a58129890bbda032231a52ed1ddc845fc18e1) | 主观察 | Score 84; Tier Early; LP $528.7K; Vol24H $1.29M; 24H -3.23%; V/LP 2.44x; 池数 1; 分项 L16/V14/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [CHOPPER](https://dexscreener.com/solana/dr3gxgtmv2uwyn7pccs6srp5a8joeeew9lczf54rnex9) | SOL | [6Z5k1o...P5aeaA](https://solscan.io/token/6Z5k1oLLfbBtmZC6xr2J12m7GTeaAqLK1Y18vyP5aeaA) | 主观察 | Score 81; Tier Liquid; LP $940.6K; Vol24H $6.40M; 24H +7.49%; V/LP 6.80x; 池数 1; 分项 L18/V17/B22/Buy3/Risk-3 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [three](https://dexscreener.com/solana/5byl7mzolabynwmpzkpkjf4mgkz7febzranos19pre2z) | SOL | [FeMbDo...VJpump](https://solscan.io/token/FeMbDoX7R1Psc4GEcvJdsbNbZA3bfztcyDCatJVJpump) | 主观察 | Score 79; Tier Early; LP $280.2K; Vol24H $663.4K; 24H +13.63%; V/LP 2.37x; 池数 2; 分项 L13/V13/B17/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| ODIC | BSC | [0x3da1...1c0fa9](https://bscscan.com/token/0x3da14529289ea39368298657071033b0c81c0fa9) | 主观察 | Score 79; Tier Liquid; LP $1.01M; Vol24H $3.56M; 24H -72.19%; V/LP 3.51x; 池数 1; 分项 L18/V17/B8/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [SPCX69](https://dexscreener.com/solana/5qphhqpaw3cz5anbnhqgzjxjm7ennrka6hwtzhmxj2dr) | SOL | [SPCXwB...a53N69](https://solscan.io/token/SPCXwBHVrKpRqMRawL3NNvt1sXP2Yf3edwRbta53N69) | 次观察 | Score 69; Tier Early; LP $164.7K; Vol24H $1.17M; 24H -44.89%; V/LP 7.08x; 池数 1; 分项 L11/V14/B8/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| BASED | BSC | [0x1d28...958e4d](https://bscscan.com/token/0x1d28d989f9e3ccb8b15d0cec601734514f958e4d) | 次观察 | Score 67; Tier Liquid; LP $1.27M; Vol24H $25.04M; 24H +1.81%; V/LP 19.73x; 池数 1; 分项 L19/V17/B22/Buy3/Risk-18 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| 67 | SOL | [9Avytn...Chpump](https://solscan.io/token/9AvytnUKsLxPxFHFqS6VLxaxt5p6BhYNr53SD2Chpump) | 次观察 | Score 67; Tier Early; LP $292.5K; Vol24H $60.3K; 24H +0.14%; V/LP 0.21x; 池数 1; 分项 L13/V5/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [VIRL](https://dexscreener.com/solana/8px97np5wy871smszwhqyl9z97k3vzhgjvkfvat7carz) | SOL | [BiywH8...sypump](https://solscan.io/token/BiywH8Eq2CbGhwMHKwCnfTiccWJwN7r1Q4Qn9hsypump) | 次观察 | Score 66; Tier Micro; LP $70.4K; Vol24H $189.2K; 24H +4.47%; V/LP 2.69x; 池数 2; 分项 L8/V9/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| GTAVI | SOL | [EpVHyK...zYpump](https://solscan.io/token/EpVHyKK8oxcLmp2C2NhAos1oDxgBNriw3wSLSozYpump) | PVP风险池 | Score 27; Tier Micro; LP $94.9K; Vol24H $2.43M; 24H +128.68%; V/LP 25.66x; 池数 2; 分项 L9/V16/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### B. 本轮扫描结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| KINS | SOL | [Tqj8yF...9bpump](https://solscan.io/token/Tqj8yFmagrg7oorpQkVGYR52r96RFTamvWfth9bpump) | 主观察 | Score 84; Tier Early; LP $447.4K; Vol24H $1.40M; 24H -5.52%; V/LP 3.12x; 池数 2; 分项 L15/V15/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [three](https://dexscreener.com/solana/5byl7mzolabynwmpzkpkjf4mgkz7febzranos19pre2z) | SOL | [FeMbDo...VJpump](https://solscan.io/token/FeMbDoX7R1Psc4GEcvJdsbNbZA3bfztcyDCatJVJpump) | 主观察 | Score 83; Tier Early; LP $275.3K; Vol24H $515.1K; 24H -3.70%; V/LP 1.87x; 池数 2; 分项 L13/V12/B22/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| SIREN | BSC | [0x997a...fc18e1](https://bscscan.com/token/0x997a58129890bbda032231a52ed1ddc845fc18e1) | 主观察 | Score 79; Tier Early; LP $532.2K; Vol24H $1.03M; 24H -0.41%; V/LP 1.94x; 池数 1; 分项 L16/V14/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| ODIC | BSC | [0x3da1...1c0fa9](https://bscscan.com/token/0x3da14529289ea39368298657071033b0c81c0fa9) | 主观察 | Score 79; Tier Liquid; LP $922.8K; Vol24H $3.62M; 24H -77.64%; V/LP 3.92x; 池数 1; 分项 L18/V17/B8/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [CHOPPER](https://dexscreener.com/solana/dr3gxgtmv2uwyn7pccs6srp5a8joeeew9lczf54rnex9) | SOL | [6Z5k1o...P5aeaA](https://solscan.io/token/6Z5k1oLLfbBtmZC6xr2J12m7GTeaAqLK1Y18vyP5aeaA) | 主观察 | Score 76; Tier Liquid; LP $939.0K; Vol24H $6.12M; 24H +9.39%; V/LP 6.52x; 池数 1; 分项 L18/V17/B17/Buy3/Risk-3 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| 67 | SOL | [9Avytn...Chpump](https://solscan.io/token/9AvytnUKsLxPxFHFqS6VLxaxt5p6BhYNr53SD2Chpump) | 次观察 | Score 73; Tier Early; LP $289.8K; Vol24H $67.2K; 24H -0.60%; V/LP 0.23x; 池数 1; 分项 L13/V6/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| ESPORTS | BSC | [0xf39e...508e48](https://bscscan.com/token/0xf39e4b21c84e737df08e2c3b32541d856f508e48) | 次观察 | Score 71; Tier Liquid; LP $1.04M; Vol24H $142.1K; 24H -15.97%; V/LP 0.14x; 池数 1; 分项 L19/V8/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [SPCX69](https://dexscreener.com/solana/5qphhqpaw3cz5anbnhqgzjxjm7ennrka6hwtzhmxj2dr) | SOL | [SPCXwB...a53N69](https://solscan.io/token/SPCXwBHVrKpRqMRawL3NNvt1sXP2Yf3edwRbta53N69) | 次观察 | Score 69; Tier Early; LP $167.4K; Vol24H $1.19M; 24H -38.45%; V/LP 7.12x; 池数 1; 分项 L11/V14/B8/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [PLASTIC](https://dexscreener.com/solana/83dtgbjqp1xgknjqdxvqzf9shqduhjgaid5yrvgkz4oh) | SOL | [58smR4...3vrise](https://solscan.io/token/58smR4GCZBxXfUUiX6KZ4JXkK6jmX42vjatWgA3vrise) | 次观察 | Score 68; Tier Liquid; LP $1.92M; Vol24H $24.6K; 24H +9.38%; V/LP 0.01x; 池数 1; 分项 L20/V3/B17/Buy12/Risk-8 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| BASED | BSC | [0x1d28...958e4d](https://bscscan.com/token/0x1d28d989f9e3ccb8b15d0cec601734514f958e4d) | 次观察 | Score 67; Tier Liquid; LP $1.27M; Vol24H $21.19M; 24H -3.61%; V/LP 16.73x; 池数 1; 分项 L19/V17/B22/Buy3/Risk-18 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [VIRL](https://dexscreener.com/solana/8px97np5wy871smszwhqyl9z97k3vzhgjvkfvat7carz) | SOL | [BiywH8...sypump](https://solscan.io/token/BiywH8Eq2CbGhwMHKwCnfTiccWJwN7r1Q4Qn9hsypump) | 次观察 | Score 66; Tier Micro; LP $70.4K; Vol24H $189.1K; 24H -4.56%; V/LP 2.69x; 池数 1; 分项 L8/V9/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [memes](https://dexscreener.com/bsc/0xd3c8668bff07b02d78019afe7f9a6e581499def2) | BSC | [0xF745...EE4444](https://bscscan.com/token/0xF74548802f4c700315F019FdE17178b392EE4444) | 次观察 | Score 65; Tier Micro; LP $85.5K; Vol24H $56.9K; 24H +1.60%; V/LP 0.67x; 池数 7; 分项 L9/V5/B22/Buy8/Risk-3 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| GTAVI | SOL | [EpVHyK...zYpump](https://solscan.io/token/EpVHyKK8oxcLmp2C2NhAos1oDxgBNriw3wSLSozYpump) | PVP风险池 | Score 49; Tier Micro; LP $93.6K; Vol24H $2.09M; 24H +0.29%; V/LP 22.29x; 池数 2; 分项 L9/V16/B22/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| FARM | SOL | [yMJPZb...7epump](https://solscan.io/token/yMJPZbnhoHib3ib8n8PfiVcp9yauk1vnaGKLx7epump) | PVP风险池 | Score 39; Tier Micro; LP $96.2K; Vol24H $2.22M; 24H -9.41%; V/LP 23.03x; 池数 2; 分项 L9/V16/B17/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [bullieve](https://dexscreener.com/solana/fyjrvzeehvg29k31bdfaq9rgnn6dcfzxtm514azhpges) | SOL | [9G4Z9w...XcXw1W](https://solscan.io/token/9G4Z9wkL851RZfMFHQETQ6v5GSNqkUTXC5oBtUXcXw1W) | PVP风险池 | Score 26; Tier Micro; LP $53.6K; Vol24H $3.15M; 24H +1241.00%; V/LP 58.81x; 池数 2; 分项 L7/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### C. PVP风险池明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| GTAVI | SOL | [EpVHyK...zYpump](https://solscan.io/token/EpVHyKK8oxcLmp2C2NhAos1oDxgBNriw3wSLSozYpump) | 24H接近横盘；买卖略偏买入；LP未达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 49; Tier Micro; LP $93.6K; Vol24H $2.09M; 24H +0.29%; V/LP 22.29x; 池数 2; 分项 L9/V16/B22/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| FARM | SOL | [yMJPZb...7epump](https://solscan.io/token/yMJPZbnhoHib3ib8n8PfiVcp9yauk1vnaGKLx7epump) | 24H波动可控；买卖基本均衡；LP未达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 39; Tier Micro; LP $96.2K; Vol24H $2.22M; 24H -9.41%; V/LP 23.03x; 池数 2; 分项 L9/V16/B17/Buy3/Risk-30 | 只记录热度，不进入主榜 |
| [bullieve](https://dexscreener.com/solana/fyjrvzeehvg29k31bdfaq9rgnn6dcfzxtm514azhpges) | SOL | [9G4Z9w...XcXw1W](https://solscan.io/token/9G4Z9wkL851RZfMFHQETQ6v5GSNqkUTXC5oBtUXcXw1W) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 26; Tier Micro; LP $53.6K; Vol24H $3.15M; 24H +1241.00%; V/LP 58.81x; 池数 2; 分项 L7/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [Nudaeng](https://dexscreener.com/solana/bgk8umqrdg3qxql32jjbc89u41n3gschhzamwdpjt4b9) | SOL | [DT5Bdf...bUpump](https://solscan.io/token/DT5BdfBKRkyAE6NU5Towb578LNADT841P7yUzZbUpump) | 24H波动可控；买卖基本均衡；LP未达主观察门槛；24H成交合格；LP偏薄；Volume/LP极端偏高 | Score 26; Tier Micro; LP $37.0K; Vol24H $2.81M; 24H +22.18%; V/LP 75.90x; 池数 2; 分项 L5/V17/B17/Buy3/Risk-40 | 只记录热度，不进入主榜 |
| [JAMESON](https://dexscreener.com/solana/hfsywti5xphqknuw4xysgiypqlrtb2nbxgby4go1x7ck) | SOL | [E8UXwq...xZpump](https://solscan.io/token/E8UXwqhNiiMwVRRV4F81rUBUYXNUd4bA78ZxpQxZpump) | 买卖基本均衡；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 22; Tier Micro; LP $95.4K; Vol24H $1.94M; 24H +383.00%; V/LP 20.37x; 池数 1; 分项 L9/V16/B0/Buy3/Risk-30 | 只记录热度，不进入主榜 |
| [WASABICRAFT](https://dexscreener.com/solana/ennqcmuufobvegcgqxlp8u12d2tij4ohvkddd2mzvedh) | SOL | [2pL9J9...yrpump](https://solscan.io/token/2pL9J9mTD9RAGS9jnNeB2kKR62ar8pnQAV2sMgyrpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 13; Tier Micro; LP $27.4K; Vol24H $3.68M; 24H +106.00%; V/LP 134.14x; 池数 2; 分项 L4/V17/B0/Buy8/Risk-40 | 只记录热度，不进入主榜 |
| CookingTrump | SOL | [Hepc74...e4pump](https://solscan.io/token/Hepc74vYP9HUBJ25yFJe63XEMxx9TpWAzChzxUe4pump) | 买卖基本均衡；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 0; Tier Micro; LP $4.9K; Vol24H $922.3K; 24H -98.28%; V/LP 188.17x; 池数 1; 分项 L0/V13/B0/Buy3/Risk-40 | 只记录热度，不进入主榜 |
| [BTL](https://dexscreener.com/solana/9gpmkobtuhaacrhevzclwsxpyxgkwhu1a1pfdtnuyvbp) | SOL | [3bBQrz...bVpump](https://solscan.io/token/3bBQrzzq9DRXXFfC9nUno9m1MBm9Y7dVnBBK44bVpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP偏高；年轻币短期暴拉 | Score 0; Tier Micro; LP $40.3K; Vol24H $711.3K; 24H +877.00%; V/LP 17.65x; 池数 5; 分项 L6/V13/B0/Buy8/Risk-53 | 只记录热度，不进入主榜 |

### D. 成熟池观察明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| ARK | BSC | [0xcae1...618b9d](https://bscscan.com/token/0xcae117ca6bc8a341d2e7207f30e180f0e5618b9d) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 74; Tier Mature; LP $56.88M; Vol24H $4.35M; 24H -5.69%; V/LP 0.08x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| BSB | BSC | [0x595d...4679cc](https://bscscan.com/token/0x595deaad1eb5476ff1e649fdb7efc36f1e4679cc) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大池 | Score 74; Tier Mature; LP $18.83M; Vol24H $29.72M; 24H -2.86%; V/LP 1.58x; 池数 2; 分项 L20/V17/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| [RAY](https://dexscreener.com/solana/2axxcn6on9bbt5owwmth53c7qhuxvhleu718kqt8rvy2) | SOL | [4k3Dyj...QrkX6R](https://solscan.io/token/4k3Dyjzvzp8eMZWUXbBCjEvwSkkk59S5iCNLY3QrkX6R) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 71; Tier Liquid; LP $1.20M; Vol24H $1.30M; 24H +4.69%; V/LP 1.08x; 池数 2; 分项 L19/V15/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| [JUP](https://dexscreener.com/solana/ckcao25f3vhavglixgx45lkqqmfcahh2pb7zkrmfirq7) | SOL | [JUPyiw...NsDvCN](https://solscan.io/token/JUPyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN) | 24H接近横盘；LP达主观察门槛；24H成交合格；Volume/LP未失真；卖出笔数占优；非主流报价池；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 68; Tier Mature; LP $122.26M; Vol24H $12.62M; 24H +3.77%; V/LP 0.10x; 池数 2; 分项 L20/V17/B22/Buy0/Risk-15 | 成熟池观察，不占用早期Alpha主榜 |
| [BOME](https://dexscreener.com/solana/dsuvc5qf5ljhhv5e2td184ixotsncnwj7i4jja4xsrmt) | SOL | [ukHH6c...Z74J82](https://solscan.io/token/ukHH6c7mMyiWCf1b9pnWe25TSpkDDt3H5pQZgZ74J82) | 24H接近横盘；LP达主观察门槛；24H成交合格；Volume/LP未失真；卖出笔数占优；LP超过早期Alpha主榜上限 | Score 65; Tier Mature; LP $8.87M; Vol24H $347.6K; 24H +0.09%; V/LP 0.04x; 池数 2; 分项 L20/V11/B22/Buy0/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |

### E. 链上确认/紧急精查表
| Token | 链 | 合约地址 | 是否需要链上确认 | 紧急精查 | 预检状态 | 原因 |
|---|---|---|---|---|---|---|
| KINS | SOL | [Tqj8yF...9bpump](https://solscan.io/token/Tqj8yFmagrg7oorpQkVGYR52r96RFTamvWfth9bpump) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| [three](https://dexscreener.com/solana/5byl7mzolabynwmpzkpkjf4mgkz7febzranos19pre2z) | SOL | [FeMbDo...VJpump](https://solscan.io/token/FeMbDoX7R1Psc4GEcvJdsbNbZA3bfztcyDCatJVJpump) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| SIREN | BSC | [0x997a...fc18e1](https://bscscan.com/token/0x997a58129890bbda032231a52ed1ddc845fc18e1) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| ODIC | BSC | [0x3da1...1c0fa9](https://bscscan.com/token/0x3da14529289ea39368298657071033b0c81c0fa9) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [CHOPPER](https://dexscreener.com/solana/dr3gxgtmv2uwyn7pccs6srp5a8joeeew9lczf54rnex9) | SOL | [6Z5k1o...P5aeaA](https://solscan.io/token/6Z5k1oLLfbBtmZC6xr2J12m7GTeaAqLK1Y18vyP5aeaA) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| 67 | SOL | [9Avytn...Chpump](https://solscan.io/token/9AvytnUKsLxPxFHFqS6VLxaxt5p6BhYNr53SD2Chpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| ESPORTS | BSC | [0xf39e...508e48](https://bscscan.com/token/0xf39e4b21c84e737df08e2c3b32541d856f508e48) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [SPCX69](https://dexscreener.com/solana/5qphhqpaw3cz5anbnhqgzjxjm7ennrka6hwtzhmxj2dr) | SOL | [SPCXwB...a53N69](https://solscan.io/token/SPCXwBHVrKpRqMRawL3NNvt1sXP2Yf3edwRbta53N69) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [PLASTIC](https://dexscreener.com/solana/83dtgbjqp1xgknjqdxvqzf9shqduhjgaid5yrvgkz4oh) | SOL | [58smR4...3vrise](https://solscan.io/token/58smR4GCZBxXfUUiX6KZ4JXkK6jmX42vjatWgA3vrise) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| BASED | BSC | [0x1d28...958e4d](https://bscscan.com/token/0x1d28d989f9e3ccb8b15d0cec601734514f958e4d) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |

### F. 钱包行为 / AVE命中样本表
| Token | 链 | 合约地址 | 行为状态 | 行为层级 | AVE命中 | 判断 |
|---|---|---|---|---|---:|---|
| KINS | SOL | [Tqj8yF...9bpump](https://solscan.io/token/Tqj8yFmagrg7oorpQkVGYR52r96RFTamvWfth9bpump) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| [three](https://dexscreener.com/solana/5byl7mzolabynwmpzkpkjf4mgkz7febzranos19pre2z) | SOL | [FeMbDo...VJpump](https://solscan.io/token/FeMbDoX7R1Psc4GEcvJdsbNbZA3bfztcyDCatJVJpump) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| SIREN | BSC | [0x997a...fc18e1](https://bscscan.com/token/0x997a58129890bbda032231a52ed1ddc845fc18e1) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| ODIC | BSC | [0x3da1...1c0fa9](https://bscscan.com/token/0x3da14529289ea39368298657071033b0c81c0fa9) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| [CHOPPER](https://dexscreener.com/solana/dr3gxgtmv2uwyn7pccs6srp5a8joeeew9lczf54rnex9) | SOL | [6Z5k1o...P5aeaA](https://solscan.io/token/6Z5k1oLLfbBtmZC6xr2J12m7GTeaAqLK1Y18vyP5aeaA) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |

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
| 成熟池观察 | 5 个 | 成熟资产不占早期Alpha主榜 |
| 合约地址覆盖 | 可用 25，缺失 0 | 地址缺失会阻断BSC RPC/Helius精查，需要优先补齐 |
| LP层级 | Micro 10 / Early 5 / Liquid 6 / Mature 4 | 下一步可以按层级分别设置进攻规则 |
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
| dexscreener_search | {'ok': True, 'count': 330} |
| geckoterminal_bsc_trending | {'ok': True, 'count': 20} |
| geckoterminal_solana_trending | {'ok': True, 'count': 20} |

## 数据限制
- This v0.4 scan uses free public sources plus lightweight chain address/account preflight when enabled.
- AVE Smart Money weekly cache structure is connected; real AVE API refresh is handled by the weekly workflow/cache file.
- S0 exact historical replay is not implemented yet; candidates are marked with current metrics only.
- Wallet-level buy/sell retention is not implemented yet; v0.4 only preflights token contract/account existence.
- v0.4 adds chain preflight status and Smart Wallet cache status on top of contract-address output, liquidity tiers, visible PVP/mature detail tables, and chain-verify flags.
- Contract addresses are extracted from DEXScreener baseToken or GeckoTerminal relationships when available; missing addresses are explicitly marked unavailable.