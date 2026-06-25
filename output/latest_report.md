# 自我进化轮巡

**本轮时间 UTC：** 2026-06-25T19:51:30Z
**版本：** 0.5.0-ave-cache-wallet-behavior-prep
**S0 时间锚点：** 2026-06-16T16:15:17+09:00

## 一句话结论
本轮从 135 个合并Token中筛出 3 个主观察候选。v0.5已在v0.4.1基础上增加AVE周缓存真实接口接入框架、Smart Wallet持久保存、wallet_behavior_latest.json，以及BSC Transfer级钱包行为样本。注意：BSC当前是Transfer样本，不等同完整Swap解码。
合约地址可用 25 个，缺失 0 个；缺失地址的候选不能进入后续链上精查。

## 本轮扫描摘要
| 指标 | 数量 |
|---|---:|
| 原始池子记录 | 289 |
| 合并后Token | 135 |
| 输出候选 | 25 |
| 主观察 | 3 |
| 次观察 | 6 |
| PVP风险池 | 8 |
| 成熟池观察 | 6 |
| 低优先观察 | 2 |
| 多池Token | 9 |
| 多池冲突 | 4 |
| Symbol桥接合并 | 0 |
| 合约地址可用 | 25 |
| 合约地址缺失 | 0 |
| Micro层 | 10 |
| Early层 | 5 |
| Liquid层 | 8 |
| Mature层 | 2 |
| 需要链上确认 | 18 |
| 紧急精查候选 | 2 |

## v0.5 数据确认状态
| 项目 | 状态 |
|---|---|
| AVE Smart Wallet周缓存 | active，钱包数 311，刷新时间 2026-06-22T02:56:49Z，是否过期 否 |
| 链上预检 | 本轮检查 12 个，验证通过 12 个，失败 0 个 |
| Helius状态 | 未配置，SOL使用公共RPC或跳过增强解析 |
| 当前精查层级 | 0.5.0-chain-preflight-plus-wallet-behavior：地址/账户预检 + v0.5钱包行为样本，完整Swap留存仍待下一版 |
| 钱包行为样本 | 本轮检查 3 个，BSC Transfer样本 1 个，SOL签名级 2 个，AVE钱包命中 0 个 |

## 第一部分：生成结果表格

### A. 上次记录结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| [TOESCOIN](https://dexscreener.com/solana/ee3zk9fxp9guair2xerefxf4tsexezffuwetrna2pkcv) | SOL | [6ehEcT...HDpump](https://solscan.io/token/6ehEcTMCc85aNF4x9CWx8HuvWGhxQtvKdhKVf2HDpump) | 主观察 | Score 80; Tier Early; LP $315.9K; Vol24H $692.6K; 24H -8.89%; V/LP 2.19x; 池数 6; 分项 L14/V13/B17/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| three | SOL | [FeMbDo...VJpump](https://solscan.io/token/FeMbDoX7R1Psc4GEcvJdsbNbZA3bfztcyDCatJVJpump) | 主观察 | Score 80; Tier Early; LP $260.9K; Vol24H $958.4K; 24H -12.62%; V/LP 3.67x; 池数 1; 分项 L13/V14/B17/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [KINS](https://dexscreener.com/solana/f42tznkpavq1vucrl6ymhc6yqvpt84fwwgzbntv2wb3w) | SOL | [Tqj8yF...9bpump](https://solscan.io/token/Tqj8yFmagrg7oorpQkVGYR52r96RFTamvWfth9bpump) | 次观察 | Score 71; Tier Early; LP $346.0K; Vol24H $756.8K; 24H -23.62%; V/LP 2.19x; 池数 1; 分项 L14/V13/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [memecoin](https://dexscreener.com/solana/ebpudz8eke1tavcrasmaaegzk3wjveesrxmidmxuyxay) | SOL | [Bb4jR9...d7pump](https://solscan.io/token/Bb4jR951QtVjeFAYFLBYXDSMKjbTDroCLPbFLdd7pump) | 次观察 | Score 70; Tier Early; LP $153.4K; Vol24H $62.0K; 24H -3.15%; V/LP 0.40x; 池数 1; 分项 L11/V5/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| ARX | BSC | [0xd5f6...1ca715](https://bscscan.com/token/0xd5f6ef5deabe61e6d5cdb49bfb6f156f2c1ca715) | 次观察 | Score 68; Tier Liquid; LP $1.71M; Vol24H $15.84M; 24H -5.09%; V/LP 9.25x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-18 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [CS](https://dexscreener.com/solana/c3hajo5hfxwcgsoxzeqsqzbtfhcdxujb4qna4aqpq6xg) | SOL | [9qwxah...topump](https://solscan.io/token/9qwxahBxcgKyn5X7kZvkN7qxKZg6pkVD8Lo4URtopump) | 次观察 | Score 66; Tier Micro; LP $50.7K; Vol24H $405.1K; 24H +8.81%; V/LP 7.99x; 池数 1; 分项 L6/V11/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| Jotchua | SOL | [BcHEaa...ySpump](https://solscan.io/token/BcHEaaTCvycPwwsJ9yQTXdHP9X2gCLkznDbZ8VySpump) | 次观察 | Score 65; Tier Early; LP $412.1K; Vol24H $1.71M; 24H +26.27%; V/LP 4.15x; 池数 2; 分项 L15/V15/B8/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [VIN](https://dexscreener.com/bsc/0xde52cff316d8a70256bee647073312c1aa7ee2cf) | BSC | [0x85E4...06a988](https://bscscan.com/token/0x85E43bF8faAF04ceDdcD03d6C07438b72606a988) | 次观察 | Score 65; Tier Liquid; LP $951.9K; Vol24H $3.3K; 24H +4.47%; V/LP 0.00x; 池数 1; 分项 L18/V0/B22/Buy12/Risk-11 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [PLASTIC](https://dexscreener.com/solana/83dtgbjqp1xgknjqdxvqzf9shqduhjgaid5yrvgkz4oh) | SOL | [58smR4...3vrise](https://solscan.io/token/58smR4GCZBxXfUUiX6KZ4JXkK6jmX42vjatWgA3vrise) | 次观察 | Score 64; Tier Liquid; LP $1.25M; Vol24H $32.6K; 24H -16.06%; V/LP 0.03x; 池数 1; 分项 L19/V4/B17/Buy8/Risk-8 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| NES | BSC | [0x3131...ac3fb5](https://bscscan.com/token/0x3131f6b80c26936ab03f7d9d29eb4ddf36ac3fb5) | PVP风险池 | Score 39; Tier Liquid; LP $1.36M; Vol24H $29.76M; 24H -24.22%; V/LP 21.93x; 池数 1; 分项 L20/V17/B17/Buy3/Risk-42 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### B. 本轮扫描结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| TOESCOIN | SOL | [6ehEcT...HDpump](https://solscan.io/token/6ehEcTMCc85aNF4x9CWx8HuvWGhxQtvKdhKVf2HDpump) | 主观察 | Score 80; Tier Early; LP $310.8K; Vol24H $666.6K; 24H -9.61%; V/LP 2.15x; 池数 2; 分项 L14/V13/B17/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| BASED | BSC | [0x1d28...958e4d](https://bscscan.com/token/0x1d28d989f9e3ccb8b15d0cec601734514f958e4d) | 主观察 | Score 80; Tier Liquid; LP $1.13M; Vol24H $7.79M; 24H -8.71%; V/LP 6.90x; 池数 1; 分项 L19/V17/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| three | SOL | [FeMbDo...VJpump](https://solscan.io/token/FeMbDoX7R1Psc4GEcvJdsbNbZA3bfztcyDCatJVJpump) | 主观察 | Score 80; Tier Early; LP $252.3K; Vol24H $974.8K; 24H -22.03%; V/LP 3.86x; 池数 1; 分项 L13/V14/B17/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [RINO](https://dexscreener.com/solana/8vy2nshplulrhfnvx2m2hebzgqx9nooxjqe4pfkkdebk) | SOL | [8bVP1R...twrise](https://solscan.io/token/8bVP1RqzpFa9zuVs5y84GV5zKAqYXworCfjoY1twrise) | 次观察 | Score 69; Tier Liquid; LP $1.04M; Vol24H $680.95; 24H +0.05%; V/LP 0.00x; 池数 1; 分项 L19/V0/B22/Buy12/Risk-8 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [FRAG](https://dexscreener.com/solana/jpqfphdxnejsaguhgcetz74pu5a5ef1fbov5u3an16b) | SOL | [J4Y92j...szpump](https://solscan.io/token/J4Y92jy5Lr9ho1aV41bhguytnzBbsPhZJahmaVszpump) | 次观察 | Score 68; Tier Micro; LP $98.6K; Vol24H $248.4K; 24H +3.73%; V/LP 2.52x; 池数 3; 分项 L9/V10/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| ARX | BSC | [0xd5f6...1ca715](https://bscscan.com/token/0xd5f6ef5deabe61e6d5cdb49bfb6f156f2c1ca715) | 次观察 | Score 68; Tier Liquid; LP $1.71M; Vol24H $15.51M; 24H -2.88%; V/LP 9.07x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-18 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [SPCX69](https://dexscreener.com/solana/5qphhqpaw3cz5anbnhqgzjxjm7ennrka6hwtzhmxj2dr) | SOL | [SPCXwB...a53N69](https://solscan.io/token/SPCXwBHVrKpRqMRawL3NNvt1sXP2Yf3edwRbta53N69) | 次观察 | Score 66; Tier Early; LP $141.8K; Vol24H $1.67M; 24H +5.99%; V/LP 11.80x; 池数 1; 分项 L11/V15/B22/Buy12/Risk-18 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| Jotchua | SOL | [BcHEaa...ySpump](https://solscan.io/token/BcHEaaTCvycPwwsJ9yQTXdHP9X2gCLkznDbZ8VySpump) | 次观察 | Score 65; Tier Early; LP $425.8K; Vol24H $1.69M; 24H +46.33%; V/LP 3.98x; 池数 2; 分项 L15/V15/B8/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [PLASTIC](https://dexscreener.com/solana/83dtgbjqp1xgknjqdxvqzf9shqduhjgaid5yrvgkz4oh) | SOL | [58smR4...3vrise](https://solscan.io/token/58smR4GCZBxXfUUiX6KZ4JXkK6jmX42vjatWgA3vrise) | 次观察 | Score 64; Tier Liquid; LP $1.25M; Vol24H $32.6K; 24H -16.23%; V/LP 0.03x; 池数 1; 分项 L19/V4/B17/Buy8/Risk-8 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| WEN | SOL | [66pQgf...8Apump](https://solscan.io/token/66pQgfLHEfbHSBgYSZSrKEdJHHaGiYbgCtNbz48Apump) | PVP风险池 | Score 23; Tier Micro; LP $48.3K; Vol24H $2.67M; 24H -49.80%; V/LP 55.30x; 池数 2; 分项 L6/V17/B8/Buy8/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [AIAIAI](https://dexscreener.com/solana/46ihtqjkskmdic66vextecoyukoa82t5ycg86c7e9rqk) | SOL | [AVPJS6...PMpump](https://solscan.io/token/AVPJS61gZmWKtaEpb7qYPKo8Fk2xQUsayYQxPiPMpump) | PVP风险池 | Score 9; Tier Micro; LP $34.7K; Vol24H $3.06M; 24H +562.00%; V/LP 88.45x; 池数 1; 分项 L5/V17/B0/Buy3/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| GLUE | SOL | [Npqouc...JSGLUE](https://solscan.io/token/NpqoucNKKJ62PwikH4NBvTm3R7mgREXoTtv7nJSGLUE) | PVP风险池 | Score 9; Tier Micro; LP $44.4K; Vol24H $1.83M; 24H +1112.40%; V/LP 41.28x; 池数 2; 分项 L6/V16/B0/Buy3/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [AYAI](https://dexscreener.com/solana/8w1trbuppi6aptyrzhfsddlqz15jwng32xmpzyfe25ca) | SOL | [J1CGp9...b8pump](https://solscan.io/token/J1CGp9QmaCZhXSCAs7LfBkNZJ1NEeUHFrzjb1ob8pump) | PVP风险池 | Score 9; Tier Micro; LP $2.7K; Vol24H $674.2K; 24H -97.55%; V/LP 253.27x; 池数 3; 分项 L0/V13/B0/Buy12/Risk-40 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| EAGLE250 | SOL | [AXLmMW...zLpump](https://solscan.io/token/AXLmMWkRmSPdPxkuMqAD4nzYBK7QRssNkYZ6RXzLpump) | PVP风险池 | Score 8; Tier Micro; LP $5.0K; Vol24H $2.12M; 24H -99.55%; V/LP 419.85x; 池数 1; 分项 L0/V16/B0/Buy8/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [MITHRIL](https://dexscreener.com/solana/8yhaycx2e4ukwd9rb3kvi73fyxxxwbmr2hlwwqad9r22) | SOL | [4vZMrP...DhTCn1](https://solscan.io/token/4vZMrPEimCDZNLsbT3jjGTnpnvPhJZnnzo8jgVDhTCn1) | PVP风险池 | Score 8; Tier Micro; LP $8.0K; Vol24H $724.2K; 24H -56.33%; V/LP 90.50x; 池数 3; 分项 L0/V13/B8/Buy3/Risk-40 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### C. PVP风险池明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| WEN | SOL | [66pQgf...8Apump](https://solscan.io/token/66pQgfLHEfbHSBgYSZSrKEdJHHaGiYbgCtNbz48Apump) | 24H未过热但已明显波动；买卖略偏买入；LP未达主观察门槛；24H成交合格；LP偏薄；Volume/LP极端偏高 | Score 23; Tier Micro; LP $48.3K; Vol24H $2.67M; 24H -49.80%; V/LP 55.30x; 池数 2; 分项 L6/V17/B8/Buy8/Risk-40 | 只记录热度，不进入主榜 |
| [AIAIAI](https://dexscreener.com/solana/46ihtqjkskmdic66vextecoyukoa82t5ycg86c7e9rqk) | SOL | [AVPJS6...PMpump](https://solscan.io/token/AVPJS61gZmWKtaEpb7qYPKo8Fk2xQUsayYQxPiPMpump) | 买卖基本均衡；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 9; Tier Micro; LP $34.7K; Vol24H $3.06M; 24H +562.00%; V/LP 88.45x; 池数 1; 分项 L5/V17/B0/Buy3/Risk-40 | 只记录热度，不进入主榜 |
| GLUE | SOL | [Npqouc...JSGLUE](https://solscan.io/token/NpqoucNKKJ62PwikH4NBvTm3R7mgREXoTtv7nJSGLUE) | 买卖基本均衡；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 9; Tier Micro; LP $44.4K; Vol24H $1.83M; 24H +1112.40%; V/LP 41.28x; 池数 2; 分项 L6/V16/B0/Buy3/Risk-40 | 只记录热度，不进入主榜 |
| [AYAI](https://dexscreener.com/solana/8w1trbuppi6aptyrzhfsddlqz15jwng32xmpzyfe25ca) | SOL | [J1CGp9...b8pump](https://solscan.io/token/J1CGp9QmaCZhXSCAs7LfBkNZJ1NEeUHFrzjb1ob8pump) | 买入笔数占优；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 9; Tier Micro; LP $2.7K; Vol24H $674.2K; 24H -97.55%; V/LP 253.27x; 池数 3; 分项 L0/V13/B0/Buy12/Risk-40 | 只记录热度，不进入主榜 |
| EAGLE250 | SOL | [AXLmMW...zLpump](https://solscan.io/token/AXLmMWkRmSPdPxkuMqAD4nzYBK7QRssNkYZ6RXzLpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 8; Tier Micro; LP $5.0K; Vol24H $2.12M; 24H -99.55%; V/LP 419.85x; 池数 1; 分项 L0/V16/B0/Buy8/Risk-40 | 只记录热度，不进入主榜 |
| [MITHRIL](https://dexscreener.com/solana/8yhaycx2e4ukwd9rb3kvi73fyxxxwbmr2hlwwqad9r22) | SOL | [4vZMrP...DhTCn1](https://solscan.io/token/4vZMrPEimCDZNLsbT3jjGTnpnvPhJZnnzo8jgVDhTCn1) | 24H未过热但已明显波动；买卖基本均衡；LP未达主观察门槛；24H成交合格；LP偏薄；Volume/LP极端偏高 | Score 8; Tier Micro; LP $8.0K; Vol24H $724.2K; 24H -56.33%; V/LP 90.50x; 池数 3; 分项 L0/V13/B8/Buy3/Risk-40 | 只记录热度，不进入主榜 |
| [KOG](https://dexscreener.com/solana/4ywwhdjwzhhvaz33w1syeh6qvths7tpkzkdshsywzvz8) | SOL | [8ExMqk...oZpump](https://solscan.io/token/8ExMqkAWaDgqB5V4kS5s1yrLtwjoGQtRz6C2NuoZpump) | 买入笔数占优；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高；年轻币短期暴拉 | Score 7; Tier Micro; LP $94.6K; Vol24H $3.94M; 24H +4115.00%; V/LP 41.70x; 池数 1; 分项 L9/V17/B0/Buy12/Risk-55 | 只记录热度，不进入主榜 |
| [DUMPSTR](https://dexscreener.com/solana/ehvhezg15sztmpcbb2azmtvsfh1huh8ybprj5zetehbi) | SOL | [7U74V3...4jpump](https://solscan.io/token/7U74V3oJy4U2V2YmwJEQ1UcoZ5woTXGBvpKKXE4jpump) | 买入笔数占优；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高；年轻币短期暴拉 | Score 0; Tier Micro; LP $38.1K; Vol24H $1.38M; 24H +353.00%; V/LP 36.15x; 池数 5; 分项 L5/V15/B0/Buy12/Risk-65 | 只记录热度，不进入主榜 |

### D. 成熟池观察明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| [BELIEVE](https://dexscreener.com/solana/2wxvyw2ktmaosoanirquo4mejuu5mwah19rxsgygqxx8) | SOL | [BLVxek...tEaCMf](https://solscan.io/token/BLVxek8YMXUQhcKmMvrFTrzh5FXg8ec88Crp6otEaCMf) | 24H接近横盘；买入笔数占优；LP达主观察门槛；24H成交合格；Volume/LP未失真；非主流报价池；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 79; Tier Liquid; LP $3.16M; Vol24H $2.06M; 24H +3.24%; V/LP 0.65x; 池数 1; 分项 L20/V16/B22/Buy12/Risk-15 | 成熟池观察，不占用早期Alpha主榜 |
| [NEVERZERO](https://dexscreener.com/solana/dmryq83qiugurjd36qky5y2cefzajqrhuxw8kyvg1z2e) | SOL | [7MsJCv...g2rise](https://solscan.io/token/7MsJCvDi5t5U3Ya2UAs5bR75VJyVMr2FKdzGmeg2rise) | 24H接近横盘；买入笔数占优；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限；成熟大池 | Score 76; Tier Mature; LP $17.22M; Vol24H $258.9K; 24H -0.34%; V/LP 0.01x; 池数 1; 分项 L20/V10/B22/Buy12/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| [JUP](https://dexscreener.com/solana/3xngdc58axytrj64stqz5trdqwvtwhlr888irbbwznee) | SOL | [JUPyiw...NsDvCN](https://solscan.io/token/JUPyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN) | 24H接近横盘；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；非主流报价池；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 76; Tier Mature; LP $140.06M; Vol24H $203.69M; 24H +5.64%; V/LP 1.45x; 池数 1; 分项 L20/V17/B22/Buy8/Risk-15 | 成熟池观察，不占用早期Alpha主榜 |
| UB | BSC | [0x40b8...db6fde](https://bscscan.com/token/0x40b8129b786d766267a7a118cf8c07e31cdb6fde) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 74; Tier Liquid; LP $2.91M; Vol24H $12.39M; 24H +3.17%; V/LP 4.26x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| [RAY](https://dexscreener.com/solana/eugpamyuasiemf51xqggb9j8e4wwvqn7seahzdxidx5n) | SOL | [4k3Dyj...QrkX6R](https://solscan.io/token/4k3Dyjzvzp8eMZWUXbBCjEvwSkkk59S5iCNLY3QrkX6R) | 24H接近横盘；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；非主流报价池；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 69; Tier Liquid; LP $3.78M; Vol24H $313.5K; 24H +5.98%; V/LP 0.08x; 池数 4; 分项 L20/V10/B22/Buy8/Risk-15 | 成熟池观察，不占用早期Alpha主榜 |
| SLX | BSC | [0x02bc...4bc54d](https://bscscan.com/token/0x02bcc4c181b83a8c0a342bc003389cbecb4bc54d) | 24H未过热但已明显波动；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；市值超过早期Alpha主榜上限 | Score 59; Tier Liquid; LP $1.18M; Vol24H $6.17M; 24H +45.80%; V/LP 5.23x; 池数 1; 分项 L19/V17/B8/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |

### E. 链上确认/紧急精查表
| Token | 链 | 合约地址 | 是否需要链上确认 | 紧急精查 | 预检状态 | 原因 |
|---|---|---|---|---|---|---|
| TOESCOIN | SOL | [6ehEcT...HDpump](https://solscan.io/token/6ehEcTMCc85aNF4x9CWx8HuvWGhxQtvKdhKVf2HDpump) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| three | SOL | [FeMbDo...VJpump](https://solscan.io/token/FeMbDoX7R1Psc4GEcvJdsbNbZA3bfztcyDCatJVJpump) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| BASED | BSC | [0x1d28...958e4d](https://bscscan.com/token/0x1d28d989f9e3ccb8b15d0cec601734514f958e4d) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [RINO](https://dexscreener.com/solana/8vy2nshplulrhfnvx2m2hebzgqx9nooxjqe4pfkkdebk) | SOL | [8bVP1R...twrise](https://solscan.io/token/8bVP1RqzpFa9zuVs5y84GV5zKAqYXworCfjoY1twrise) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [RAY](https://dexscreener.com/solana/eugpamyuasiemf51xqggb9j8e4wwvqn7seahzdxidx5n) | SOL | [4k3Dyj...QrkX6R](https://solscan.io/token/4k3Dyjzvzp8eMZWUXbBCjEvwSkkk59S5iCNLY3QrkX6R) | 是 | 否 | verified / address_preflight_v0.4 | 多池数据冲突，需链上/聚合源复核 |
| [FRAG](https://dexscreener.com/solana/jpqfphdxnejsaguhgcetz74pu5a5ef1fbov5u3an16b) | SOL | [J4Y92j...szpump](https://solscan.io/token/J4Y92jy5Lr9ho1aV41bhguytnzBbsPhZJahmaVszpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| ARX | BSC | [0xd5f6...1ca715](https://bscscan.com/token/0xd5f6ef5deabe61e6d5cdb49bfb6f156f2c1ca715) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [SPCX69](https://dexscreener.com/solana/5qphhqpaw3cz5anbnhqgzjxjm7ennrka6hwtzhmxj2dr) | SOL | [SPCXwB...a53N69](https://solscan.io/token/SPCXwBHVrKpRqMRawL3NNvt1sXP2Yf3edwRbta53N69) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| Jotchua | SOL | [BcHEaa...ySpump](https://solscan.io/token/BcHEaaTCvycPwwsJ9yQTXdHP9X2gCLkznDbZ8VySpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [PLASTIC](https://dexscreener.com/solana/83dtgbjqp1xgknjqdxvqzf9shqduhjgaid5yrvgkz4oh) | SOL | [58smR4...3vrise](https://solscan.io/token/58smR4GCZBxXfUUiX6KZ4JXkK6jmX42vjatWgA3vrise) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |

### F. 钱包行为 / AVE命中样本表
| Token | 链 | 合约地址 | 行为状态 | 行为层级 | AVE命中 | 判断 |
|---|---|---|---|---|---:|---|
| TOESCOIN | SOL | [6ehEcT...HDpump](https://solscan.io/token/6ehEcTMCc85aNF4x9CWx8HuvWGhxQtvKdhKVf2HDpump) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| three | SOL | [FeMbDo...VJpump](https://solscan.io/token/FeMbDoX7R1Psc4GEcvJdsbNbZA3bfztcyDCatJVJpump) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| BASED | BSC | [0x1d28...958e4d](https://bscscan.com/token/0x1d28d989f9e3ccb8b15d0cec601734514f958e4d) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |

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
| 主观察候选 | 3 个 | 主榜继续稀缺，但必须结合合约地址进入链上确认 |
| PVP风险池 | 8 个 | v0.3已单独展示明细，便于判断噪声来源 |
| 成熟池观察 | 6 个 | 成熟资产不占早期Alpha主榜 |
| 合约地址覆盖 | 可用 25，缺失 0 | 地址缺失会阻断BSC RPC/Helius精查，需要优先补齐 |
| LP层级 | Micro 10 / Early 5 / Liquid 8 / Mature 2 | 下一步可以按层级分别设置进攻规则 |
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