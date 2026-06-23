# 自我进化轮巡

**本轮时间 UTC：** 2026-06-23T10:33:18Z
**版本：** 0.5.0-ave-cache-wallet-behavior-prep
**S0 时间锚点：** 2026-06-16T16:15:17+09:00

## 一句话结论
本轮从 134 个合并Token中筛出 5 个主观察候选。v0.5已在v0.4.1基础上增加AVE周缓存真实接口接入框架、Smart Wallet持久保存、wallet_behavior_latest.json，以及BSC Transfer级钱包行为样本。注意：BSC当前是Transfer样本，不等同完整Swap解码。
合约地址可用 25 个，缺失 0 个；缺失地址的候选不能进入后续链上精查。

## 本轮扫描摘要
| 指标 | 数量 |
|---|---:|
| 原始池子记录 | 309 |
| 合并后Token | 134 |
| 输出候选 | 25 |
| 主观察 | 5 |
| 次观察 | 10 |
| PVP风险池 | 8 |
| 成熟池观察 | 2 |
| 低优先观察 | 0 |
| 多池Token | 8 |
| 多池冲突 | 0 |
| Symbol桥接合并 | 0 |
| 合约地址可用 | 25 |
| 合约地址缺失 | 0 |
| Micro层 | 5 |
| Early层 | 10 |
| Liquid层 | 9 |
| Mature层 | 1 |
| 需要链上确认 | 23 |
| 紧急精查候选 | 5 |

## v0.5 数据确认状态
| 项目 | 状态 |
|---|---|
| AVE Smart Wallet周缓存 | active，钱包数 311，刷新时间 2026-06-22T02:56:49Z，是否过期 否 |
| 链上预检 | 本轮检查 12 个，验证通过 12 个，失败 0 个 |
| Helius状态 | 未配置，SOL使用公共RPC或跳过增强解析 |
| 当前精查层级 | 0.5.0-chain-preflight-plus-wallet-behavior：地址/账户预检 + v0.5钱包行为样本，完整Swap留存仍待下一版 |
| 钱包行为样本 | 本轮检查 5 个，BSC Transfer样本 0 个，SOL签名级 5 个，AVE钱包命中 0 个 |

## 第一部分：生成结果表格

### A. 上次记录结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| BASED | BSC | [0x1d28...958e4d](https://bscscan.com/token/0x1d28d989f9e3ccb8b15d0cec601734514f958e4d) | 主观察 | Score 85; Tier Liquid; LP $1.27M; Vol24H $7.61M; 24H +2.44%; V/LP 5.98x; 池数 1; 分项 L19/V17/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [three](https://dexscreener.com/solana/5byl7mzolabynwmpzkpkjf4mgkz7febzranos19pre2z) | SOL | [FeMbDo...VJpump](https://solscan.io/token/FeMbDoX7R1Psc4GEcvJdsbNbZA3bfztcyDCatJVJpump) | 主观察 | Score 81; Tier Early; LP $302.0K; Vol24H $1.29M; 24H +15.83%; V/LP 4.26x; 池数 7; 分项 L14/V14/B17/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| SOLANGELES | SOL | [8wxkvA...6cpump](https://solscan.io/token/8wxkvAfEns76yBzu4MnbV7VnXWjg3iDPA9uwAQ6cpump) | 主观察 | Score 76; Tier Early; LP $241.8K; Vol24H $1.27M; 24H +4.77%; V/LP 5.27x; 池数 2; 分项 L13/V14/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [Jotchua](https://dexscreener.com/solana/akqyqgeifbbhqmanukzrrurgokskkbv8nvdccc87frr8) | SOL | [BcHEaa...ySpump](https://solscan.io/token/BcHEaaTCvycPwwsJ9yQTXdHP9X2gCLkznDbZ8VySpump) | 次观察 | Score 75; Tier Early; LP $363.5K; Vol24H $548.0K; 24H -17.81%; V/LP 1.51x; 池数 1; 分项 L14/V12/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [PLASTIC](https://dexscreener.com/solana/83dtgbjqp1xgknjqdxvqzf9shqduhjgaid5yrvgkz4oh) | SOL | [58smR4...3vrise](https://solscan.io/token/58smR4GCZBxXfUUiX6KZ4JXkK6jmX42vjatWgA3vrise) | 次观察 | Score 72; Tier Liquid; LP $1.69M; Vol24H $19.0K; 24H -6.69%; V/LP 0.01x; 池数 1; 分项 L20/V2/B22/Buy12/Risk-8 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [GTAVI](https://dexscreener.com/solana/3jtcvdjp9cszn9mjgxwlw37m48aubsry5es6wfcznqlm) | SOL | [EpVHyK...zYpump](https://solscan.io/token/EpVHyKK8oxcLmp2C2NhAos1oDxgBNriw3wSLSozYpump) | 次观察 | Score 72; Tier Early; LP $114.8K; Vol24H $909.7K; 24H +8.12%; V/LP 7.93x; 池数 1; 分项 L10/V13/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [FISTFLOOR](https://dexscreener.com/solana/3fgmjpi5wgr9jhqf37lz8uh3dzsydjzslkrff4gagw5s) | SOL | [3XJb1B...Mirise](https://solscan.io/token/3XJb1BtqeXNNAeAAfCzqF5ReWjok11cnStJdM1Mirise) | 次观察 | Score 71; Tier Liquid; LP $2.02M; Vol24H $49.5K; 24H -5.60%; V/LP 0.02x; 池数 1; 分项 L20/V5/B22/Buy8/Risk-8 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| MAME | BSC | [0xe92f...c42302](https://bscscan.com/token/0xe92f7fe3eaf61df28b7b75f3faab199333c42302) | 次观察 | Score 71; Tier Liquid; LP $845.7K; Vol24H $3.78M; 24H +1108.37%; V/LP 4.47x; 池数 1; 分项 L18/V17/B0/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| ZERO | SOL | [EmcxFT...dwpump](https://solscan.io/token/EmcxFTNVDqyLHp11NvwvLZ4D7LKGbG9i7B8RF7dwpump) | 次观察 | Score 71; Tier Early; LP $264.3K; Vol24H $1.20M; 24H -20.53%; V/LP 4.55x; 池数 1; 分项 L13/V14/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [SPCX69](https://dexscreener.com/solana/5qphhqpaw3cz5anbnhqgzjxjm7ennrka6hwtzhmxj2dr) | SOL | [SPCXwB...a53N69](https://solscan.io/token/SPCXwBHVrKpRqMRawL3NNvt1sXP2Yf3edwRbta53N69) | 次观察 | Score 68; Tier Early; LP $147.7K; Vol24H $692.6K; 24H -40.38%; V/LP 4.69x; 池数 1; 分项 L11/V13/B8/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |

### B. 本轮扫描结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| [three](https://dexscreener.com/solana/5byl7mzolabynwmpzkpkjf4mgkz7febzranos19pre2z) | SOL | [FeMbDo...VJpump](https://solscan.io/token/FeMbDoX7R1Psc4GEcvJdsbNbZA3bfztcyDCatJVJpump) | 主观察 | Score 86; Tier Early; LP $299.1K; Vol24H $956.5K; 24H +5.21%; V/LP 3.20x; 池数 2; 分项 L14/V14/B22/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| TROLL | SOL | [5UUH9R...TBhgH2](https://solscan.io/token/5UUH9RTDiSpq6HKS6bp4NdU9PNJpXRXuiw6ShBTBhgH2) | 主观察 | Score 84; Tier Liquid; LP $2.72M; Vol24H $1.50M; 24H -10.56%; V/LP 0.55x; 池数 1; 分项 L20/V15/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [FISTFLOOR](https://dexscreener.com/solana/3fgmjpi5wgr9jhqf37lz8uh3dzsydjzslkrff4gagw5s) | SOL | [3XJb1B...Mirise](https://solscan.io/token/3XJb1BtqeXNNAeAAfCzqF5ReWjok11cnStJdM1Mirise) | 主观察 | Score 83; Tier Liquid; LP $2.00M; Vol24H $55.5K; 24H -6.49%; V/LP 0.03x; 池数 1; 分项 L20/V5/B22/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [TOESCOIN](https://dexscreener.com/solana/ee3zk9fxp9guair2xerefxf4tsexezffuwetrna2pkcv) | SOL | [6ehEcT...HDpump](https://solscan.io/token/6ehEcTMCc85aNF4x9CWx8HuvWGhxQtvKdhKVf2HDpump) | 主观察 | Score 82; Tier Early; LP $347.0K; Vol24H $1.77M; 24H -12.46%; V/LP 5.11x; 池数 6; 分项 L14/V15/B17/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [SOLANGELES](https://dexscreener.com/solana/ak7hdcxdsocd2zgjbca1zwlcudqz5f6n747a7rqtpxe3) | SOL | [8wxkvA...6cpump](https://solscan.io/token/8wxkvAfEns76yBzu4MnbV7VnXWjg3iDPA9uwAQ6cpump) | 主观察 | Score 76; Tier Early; LP $236.5K; Vol24H $1.21M; 24H +0.29%; V/LP 5.10x; 池数 1; 分项 L13/V14/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [Jotchua](https://dexscreener.com/solana/akqyqgeifbbhqmanukzrrurgokskkbv8nvdccc87frr8) | SOL | [BcHEaa...ySpump](https://solscan.io/token/BcHEaaTCvycPwwsJ9yQTXdHP9X2gCLkznDbZ8VySpump) | 次观察 | Score 75; Tier Early; LP $360.5K; Vol24H $522.6K; 24H -20.85%; V/LP 1.45x; 池数 1; 分项 L14/V12/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| ESPORTS | BSC | [0xf39e...508e48](https://bscscan.com/token/0xf39e4b21c84e737df08e2c3b32541d856f508e48) | 次观察 | Score 73; Tier Liquid; LP $1.01M; Vol24H $69.6K; 24H +3.23%; V/LP 0.07x; 池数 1; 分项 L18/V6/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| FRAG | SOL | [J4Y92j...szpump](https://solscan.io/token/J4Y92jy5Lr9ho1aV41bhguytnzBbsPhZJahmaVszpump) | 次观察 | Score 71; Tier Early; LP $105.4K; Vol24H $704.5K; 24H -5.84%; V/LP 6.68x; 池数 4; 分项 L9/V13/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| MAME | BSC | [0xe92f...c42302](https://bscscan.com/token/0xe92f7fe3eaf61df28b7b75f3faab199333c42302) | 次观察 | Score 71; Tier Liquid; LP $867.3K; Vol24H $3.92M; 24H +1189.62%; V/LP 4.52x; 池数 1; 分项 L18/V17/B0/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| ZERO | SOL | [EmcxFT...dwpump](https://solscan.io/token/EmcxFTNVDqyLHp11NvwvLZ4D7LKGbG9i7B8RF7dwpump) | 次观察 | Score 71; Tier Early; LP $278.0K; Vol24H $1.17M; 24H -15.12%; V/LP 4.22x; 池数 1; 分项 L13/V14/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| CLO | BSC | [0x81d3...bf89d2](https://bscscan.com/token/0x81d3a238b02827f62b9f390f947d36d4a5bf89d2) | 次观察 | Score 68; Tier Liquid; LP $1.78M; Vol24H $22.58M; 24H +6.00%; V/LP 12.68x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-18 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [ZINC](https://dexscreener.com/solana/8s2ohdw1mqudqcw4dfjvbfclbjxd2knbfe6kgcyfbway) | SOL | [zinc15...5SGyfi](https://solscan.io/token/zinc155BS4mSPk8GXQj4R5hkVDQXcW253pTYq5SGyfi) | 次观察 | Score 66; Tier Early; LP $198.3K; Vol24H $906.9K; 24H -8.75%; V/LP 4.57x; 池数 10; 分项 L12/V13/B17/Buy0/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [SON](https://dexscreener.com/solana/ec9rk1gqmn4d7tjp2efx6m1on1rmxxr5gh4pkswjqskx) | SOL | [ACpzkG...Nppump](https://solscan.io/token/ACpzkGJV3DDU8HXy8yjab7RL9qNmDGym2GwLkzNppump) | 次观察 | Score 66; Tier Early; LP $115.4K; Vol24H $622.2K; 24H +18.02%; V/LP 5.39x; 池数 1; 分项 L10/V12/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [VIN](https://dexscreener.com/bsc/0xde52cff316d8a70256bee647073312c1aa7ee2cf) | BSC | [0x85E4...06a988](https://bscscan.com/token/0x85E43bF8faAF04ceDdcD03d6C07438b72606a988) | 次观察 | Score 65; Tier Liquid; LP $930.6K; Vol24H $2.1K; 24H -2.16%; V/LP 0.00x; 池数 1; 分项 L18/V0/B22/Buy12/Risk-11 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [PLASTIC](https://dexscreener.com/solana/83dtgbjqp1xgknjqdxvqzf9shqduhjgaid5yrvgkz4oh) | SOL | [58smR4...3vrise](https://solscan.io/token/58smR4GCZBxXfUUiX6KZ4JXkK6jmX42vjatWgA3vrise) | 次观察 | Score 64; Tier Liquid; LP $1.47M; Vol24H $31.5K; 24H -17.87%; V/LP 0.02x; 池数 1; 分项 L20/V3/B17/Buy8/Risk-8 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |

### C. PVP风险池明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| ARX | BSC | [0xd5f6...1ca715](https://bscscan.com/token/0xd5f6ef5deabe61e6d5cdb49bfb6f156f2c1ca715) | 24H波动可控；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 51; Tier Liquid; LP $1.80M; Vol24H $87.47M; 24H -16.44%; V/LP 48.61x; 池数 1; 分项 L20/V17/B17/Buy3/Risk-30 | 只记录热度，不进入主榜 |
| BLESS | BSC | [0x7c82...9ae11f](https://bscscan.com/token/0x7c8217517ed4711fe2deccdfeffe8d906b9ae11f) | 24H未过热但已明显波动；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 37; Tier Early; LP $432.1K; Vol24H $10.29M; 24H +25.23%; V/LP 23.82x; 池数 1; 分项 L15/V17/B8/Buy3/Risk-30 | 只记录热度，不进入主榜 |
| ARX | SOL | [ARXwZk...gyDrFs](https://solscan.io/token/ARXwZkNAtzPfdcoqQiduJn8EPv9fKiDfGn2KyggyDrFs) | 24H波动可控；LP达主观察门槛；24H成交合格；卖出笔数占优；Volume/LP极端偏高；FDV超过早期Alpha主榜上限；成熟大市值 | Score 30; Tier Early; LP $313.6K; Vol24H $13.14M; 24H -8.07%; V/LP 41.89x; 池数 1; 分项 L14/V17/B17/Buy0/Risk-42 | 只记录热度，不进入主榜 |
| QUEST | SOL | [Et3nNi...4wpoke](https://solscan.io/token/Et3nNiuGyhQxwVW3W8pLTvsMXcSKiyogHrNjdr4wpoke) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 26; Tier Micro; LP $56.9K; Vol24H $4.41M; 24H +1497.02%; V/LP 77.64x; 池数 2; 分项 L7/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| CONDOR | SOL | [BQnsQ7...fLpump](https://solscan.io/token/BQnsQ7LrcKVUqB33cqkVmbN1GNvqCCVYqGLLG5fLpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 24; Tier Micro; LP $52.4K; Vol24H $1.65M; 24H +184.33%; V/LP 31.40x; 池数 2; 分项 L7/V15/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [Moonlake](https://dexscreener.com/solana/59xdiymnaukqk2kfwfukbc4krh99m6ljm4tvqhy7gapc) | SOL | [6RSCFP...4Gpump](https://solscan.io/token/6RSCFPsd7ZgiyCcxmZaHr3soUXREKk8EZmH2rH4Gpump) | 买卖基本均衡；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 21; Tier Micro; LP $63.2K; Vol24H $2.71M; 24H +643.00%; V/LP 42.84x; 池数 2; 分项 L7/V17/B0/Buy3/Risk-30 | 只记录热度，不进入主榜 |
| [RO](https://dexscreener.com/solana/cqf5qgwiywn8wwunigbxdt7qkn5g373sabrgt1n8t8sw) | SOL | [FgrnkD...r2ejRR](https://solscan.io/token/FgrnkD6Meh4yusagXu4duEx51HkEuEVrxUihG9r2ejRR) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 13; Tier Micro; LP $38.9K; Vol24H $2.36M; 24H +642.00%; V/LP 60.62x; 池数 1; 分项 L5/V16/B0/Buy8/Risk-40 | 只记录热度，不进入主榜 |
| Jetchua | SOL | [6jbx2P...o6pump](https://solscan.io/token/6jbx2PGZfXNaXxXSLzsUse5xQet3E5qnJqpMRso6pump) | 买卖基本均衡；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 3; Tier Micro; LP $5.4K; Vol24H $2.42M; 24H -99.04%; V/LP 445.42x; 池数 1; 分项 L0/V16/B0/Buy3/Risk-40 | 只记录热度，不进入主榜 |

### D. 成熟池观察明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| [RAY](https://dexscreener.com/solana/2axxcn6on9bbt5owwmth53c7qhuxvhleu718kqt8rvy2) | SOL | [4k3Dyj...QrkX6R](https://solscan.io/token/4k3Dyjzvzp8eMZWUXbBCjEvwSkkk59S5iCNLY3QrkX6R) | 24H接近横盘；买入笔数占优；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 78; Tier Liquid; LP $1.16M; Vol24H $912.1K; 24H -5.84%; V/LP 0.78x; 池数 2; 分项 L19/V13/B22/Buy12/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| [JUP](https://dexscreener.com/solana/3xngdc58axytrj64stqz5trdqwvtwhlr888irbbwznee) | SOL | [JUPyiw...NsDvCN](https://solscan.io/token/JUPyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；非主流报价池；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 71; Tier Mature; LP $131.22M; Vol24H $64.38M; 24H -3.82%; V/LP 0.49x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-15 | 成熟池观察，不占用早期Alpha主榜 |

### E. 链上确认/紧急精查表
| Token | 链 | 合约地址 | 是否需要链上确认 | 紧急精查 | 预检状态 | 原因 |
|---|---|---|---|---|---|---|
| [three](https://dexscreener.com/solana/5byl7mzolabynwmpzkpkjf4mgkz7febzranos19pre2z) | SOL | [FeMbDo...VJpump](https://solscan.io/token/FeMbDoX7R1Psc4GEcvJdsbNbZA3bfztcyDCatJVJpump) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| TROLL | SOL | [5UUH9R...TBhgH2](https://solscan.io/token/5UUH9RTDiSpq6HKS6bp4NdU9PNJpXRXuiw6ShBTBhgH2) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| [FISTFLOOR](https://dexscreener.com/solana/3fgmjpi5wgr9jhqf37lz8uh3dzsydjzslkrff4gagw5s) | SOL | [3XJb1B...Mirise](https://solscan.io/token/3XJb1BtqeXNNAeAAfCzqF5ReWjok11cnStJdM1Mirise) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| [TOESCOIN](https://dexscreener.com/solana/ee3zk9fxp9guair2xerefxf4tsexezffuwetrna2pkcv) | SOL | [6ehEcT...HDpump](https://solscan.io/token/6ehEcTMCc85aNF4x9CWx8HuvWGhxQtvKdhKVf2HDpump) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| [SOLANGELES](https://dexscreener.com/solana/ak7hdcxdsocd2zgjbca1zwlcudqz5f6n747a7rqtpxe3) | SOL | [8wxkvA...6cpump](https://solscan.io/token/8wxkvAfEns76yBzu4MnbV7VnXWjg3iDPA9uwAQ6cpump) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| [Jotchua](https://dexscreener.com/solana/akqyqgeifbbhqmanukzrrurgokskkbv8nvdccc87frr8) | SOL | [BcHEaa...ySpump](https://solscan.io/token/BcHEaaTCvycPwwsJ9yQTXdHP9X2gCLkznDbZ8VySpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| ESPORTS | BSC | [0xf39e...508e48](https://bscscan.com/token/0xf39e4b21c84e737df08e2c3b32541d856f508e48) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| FRAG | SOL | [J4Y92j...szpump](https://solscan.io/token/J4Y92jy5Lr9ho1aV41bhguytnzBbsPhZJahmaVszpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| MAME | BSC | [0xe92f...c42302](https://bscscan.com/token/0xe92f7fe3eaf61df28b7b75f3faab199333c42302) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| ZERO | SOL | [EmcxFT...dwpump](https://solscan.io/token/EmcxFTNVDqyLHp11NvwvLZ4D7LKGbG9i7B8RF7dwpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |

### F. 钱包行为 / AVE命中样本表
| Token | 链 | 合约地址 | 行为状态 | 行为层级 | AVE命中 | 判断 |
|---|---|---|---|---|---:|---|
| [three](https://dexscreener.com/solana/5byl7mzolabynwmpzkpkjf4mgkz7febzranos19pre2z) | SOL | [FeMbDo...VJpump](https://solscan.io/token/FeMbDoX7R1Psc4GEcvJdsbNbZA3bfztcyDCatJVJpump) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| TROLL | SOL | [5UUH9R...TBhgH2](https://solscan.io/token/5UUH9RTDiSpq6HKS6bp4NdU9PNJpXRXuiw6ShBTBhgH2) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| [FISTFLOOR](https://dexscreener.com/solana/3fgmjpi5wgr9jhqf37lz8uh3dzsydjzslkrff4gagw5s) | SOL | [3XJb1B...Mirise](https://solscan.io/token/3XJb1BtqeXNNAeAAfCzqF5ReWjok11cnStJdM1Mirise) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| [TOESCOIN](https://dexscreener.com/solana/ee3zk9fxp9guair2xerefxf4tsexezffuwetrna2pkcv) | SOL | [6ehEcT...HDpump](https://solscan.io/token/6ehEcTMCc85aNF4x9CWx8HuvWGhxQtvKdhKVf2HDpump) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| [SOLANGELES](https://dexscreener.com/solana/ak7hdcxdsocd2zgjbca1zwlcudqz5f6n747a7rqtpxe3) | SOL | [8wxkvA...6cpump](https://solscan.io/token/8wxkvAfEns76yBzu4MnbV7VnXWjg3iDPA9uwAQ6cpump) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |

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
| 成熟池观察 | 2 个 | 成熟资产不占早期Alpha主榜 |
| 合约地址覆盖 | 可用 25，缺失 0 | 地址缺失会阻断BSC RPC/Helius精查，需要优先补齐 |
| LP层级 | Micro 5 / Early 10 / Liquid 9 / Mature 1 | 下一步可以按层级分别设置进攻规则 |
| S0对比 | 尚未做精确历史回放 | 后续用GeckoTerminal OHLCV / 链上数据补齐 |
| 链上确认 | v0.5执行地址/账户预检 + BSC Transfer级钱包行为样本 | 可以初步看到活跃钱包/缓存命中，但仍不能替代完整Swap留存判断 |
| Smart Money | AVE周缓存 + 代理指标 | 无具体钱包映射前，不允许标记真实吸筹 |

### C. 本轮优化调整表
| 调整项 | 触发原因 | 对下轮筛选影响 |
|---|---|---|
| chain_verify_pipeline | 观察池候选需要链上Swap、钱包留存和大额买卖确认；v0.4.1已生成确认标记并强制落地chain_verify_latest.json | 下轮报告继续输出链上确认/紧急精查表，为接BSC RPC/Helius做准备 |
| emergency_precision_check_policy | 本轮出现满足LP、低波动、买盘占优、非多池冲突的高优先候选 | 下轮这类候选优先进入链上精查或AVE单币紧急刷新建议 |
| early_alpha_range_filter | 检测到成熟池候选，不能让大池成熟资产占用早期Alpha主榜 | 成熟大池进入成熟池观察，不作为底部MEME扫货主观察 |

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