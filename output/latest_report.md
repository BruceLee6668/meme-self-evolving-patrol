# 自我进化轮巡

**本轮时间 UTC：** 2026-08-18T08:29:07Z
**版本：** 0.5.0-ave-cache-wallet-behavior-prep
**S0 时间锚点：** 2026-06-16T16:15:17+09:00

## 一句话结论
本轮从 122 个合并Token中筛出 3 个主观察候选。v0.5已在v0.4.1基础上增加AVE周缓存真实接口接入框架、Smart Wallet持久保存、wallet_behavior_latest.json，以及BSC Transfer级钱包行为样本。注意：BSC当前是Transfer样本，不等同完整Swap解码。
合约地址可用 25 个，缺失 0 个；缺失地址的候选不能进入后续链上精查。

## 本轮扫描摘要
| 指标 | 数量 |
|---|---:|
| 原始池子记录 | 251 |
| 合并后Token | 122 |
| 输出候选 | 25 |
| 主观察 | 3 |
| 次观察 | 6 |
| PVP风险池 | 8 |
| 成熟池观察 | 3 |
| 低优先观察 | 5 |
| 多池Token | 9 |
| 多池冲突 | 2 |
| Symbol桥接合并 | 2 |
| 合约地址可用 | 25 |
| 合约地址缺失 | 0 |
| Micro层 | 4 |
| Early层 | 10 |
| Liquid层 | 9 |
| Mature层 | 2 |
| 需要链上确认 | 17 |
| 紧急精查候选 | 2 |

## v0.5 数据确认状态
| 项目 | 状态 |
|---|---|
| AVE Smart Wallet周缓存 | active，钱包数 1035，刷新时间 2026-08-17T00:45:08Z，是否过期 否 |
| 链上预检 | 本轮检查 12 个，验证通过 12 个，失败 0 个 |
| Helius状态 | 未配置，SOL使用公共RPC或跳过增强解析 |
| 当前精查层级 | 0.5.0-chain-preflight-plus-wallet-behavior：地址/账户预检 + v0.5钱包行为样本，完整Swap留存仍待下一版 |
| 钱包行为样本 | 本轮检查 3 个，BSC Transfer样本 0 个，SOL签名级 3 个，AVE钱包命中 0 个 |

## 第一部分：生成结果表格

### A. 上次记录结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| CATE | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | 主观察 | Score 83; Tier Liquid; LP $763.6K; Vol24H $2.85M; 24H -10.99%; V/LP 3.74x; 池数 1; 分项 L17/V17/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [PUMP](https://dexscreener.com/solana/7q2dqbjtxxp4dqmhec2nsgxwsytq8jaxdygswmag3pfp) | SOL | [9593dF...ysD6A1](https://solscan.io/token/9593dFjsLKKRAaz4LX1eK2DDEgrzfu3idb6yvMysD6A1) | 主观察 | Score 79; Tier Liquid; LP $2.05M; Vol24H $295.3K; 24H +0.00%; V/LP 0.14x; 池数 2; 分项 L20/V10/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [TOESCOIN](https://dexscreener.com/solana/ee3zk9fxp9guair2xerefxf4tsexezffuwetrna2pkcv) | SOL | [6ehEcT...HDpump](https://solscan.io/token/6ehEcTMCc85aNF4x9CWx8HuvWGhxQtvKdhKVf2HDpump) | 主观察 | Score 77; Tier Early; LP $295.6K; Vol24H $175.9K; 24H -3.12%; V/LP 0.60x; 池数 10; 分项 L14/V9/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [memestock](https://dexscreener.com/bsc/0x7bdc9582aca6ca25e5db1f2c8e59003b880672cb) | BSC | [0x6FF4...057777](https://bscscan.com/token/0x6FF45323817d1d53bbb8A8dFbA9245aE74057777) | 次观察 | Score 71; Tier Micro; LP $99.9K; Vol24H $388.1K; 24H -2.27%; V/LP 3.88x; 池数 3; 分项 L9/V11/B22/Buy8/Risk-3 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| WKC | BSC | [0x6ec9...128edb](https://bscscan.com/token/0x6ec90334d89dbdc89e08a133271be3d104128edb) | 次观察 | Score 71; Tier Liquid; LP $1.30M; Vol24H $484.6K; 24H +25.60%; V/LP 0.37x; 池数 1; 分项 L19/V12/B8/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [PLASTIC](https://dexscreener.com/solana/83dtgbjqp1xgknjqdxvqzf9shqduhjgaid5yrvgkz4oh) | SOL | [58smR4...3vrise](https://solscan.io/token/58smR4GCZBxXfUUiX6KZ4JXkK6jmX42vjatWgA3vrise) | 次观察 | Score 70; Tier Liquid; LP $1.49M; Vol24H $3.00; 24H +0.00%; V/LP 0.00x; 池数 1; 分项 L20/V0/B22/Buy12/Risk-8 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [Jimothy](https://dexscreener.com/solana/5pghkctym6odbhgo2tkmst2ajmjsb2uzbqrkkn4zuft5) | SOL | [Ge87Et...xTpump](https://solscan.io/token/Ge87EtsjwRQbHaqQmKRno69RFTwh9bfSsm99XNxTpump) | 次观察 | Score 70; Tier Early; LP $498.6K; Vol24H $1.04M; 24H -74.72%; V/LP 2.08x; 池数 1; 分项 L16/V14/B8/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [SAOF](https://dexscreener.com/solana/ek7yhbdqn36w7et2unsystkcf7f2y4ep7ohmzjpdp8pi) | SOL | [EMADEv...VEpump](https://solscan.io/token/EMADEvnBdp6LoabjRCyN8mw36aVzRd7pYDpNLVEpump) | 次观察 | Score 69; Tier Early; LP $216.1K; Vol24H $137.9K; 24H +16.98%; V/LP 0.64x; 池数 1; 分项 L12/V8/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [UOTF](https://dexscreener.com/solana/dt2dgfdkdgafeqccx68a9j7gwvvabxbhdfefzk8pruxb) | SOL | [YyKEat...Vopump](https://solscan.io/token/YyKEatMcHfLaWJLrL6EmuFDNhxt3fCtz8LktQVopump) | 次观察 | Score 68; Tier Early; LP $159.8K; Vol24H $139.6K; 24H +18.78%; V/LP 0.87x; 池数 1; 分项 L11/V8/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [USTF](https://dexscreener.com/solana/d5e3kzfqty329v3suu95tfhgkfkefrquy6jsvyeuxcu1) | SOL | [CdXYkp...hmpump](https://solscan.io/token/CdXYkpp29NsiXHpKAkHX4KTCT7YtmQcEJSYYNhmpump) | 次观察 | Score 68; Tier Early; LP $144.7K; Vol24H $131.0K; 24H +16.26%; V/LP 0.91x; 池数 1; 分项 L11/V8/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |

### B. 本轮扫描结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| CATE | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | 主观察 | Score 83; Tier Liquid; LP $757.0K; Vol24H $2.87M; 24H -9.65%; V/LP 3.79x; 池数 1; 分项 L17/V17/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [TOESCOIN](https://dexscreener.com/solana/ee3zk9fxp9guair2xerefxf4tsexezffuwetrna2pkcv) | SOL | [6ehEcT...HDpump](https://solscan.io/token/6ehEcTMCc85aNF4x9CWx8HuvWGhxQtvKdhKVf2HDpump) | 主观察 | Score 80; Tier Early; LP $297.3K; Vol24H $544.5K; 24H -0.91%; V/LP 1.83x; 池数 10; 分项 L14/V12/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [PUMP](https://dexscreener.com/solana/7q2dqbjtxxp4dqmhec2nsgxwsytq8jaxdygswmag3pfp) | SOL | [9593dF...ysD6A1](https://solscan.io/token/9593dFjsLKKRAaz4LX1eK2DDEgrzfu3idb6yvMysD6A1) | 主观察 | Score 79; Tier Liquid; LP $2.05M; Vol24H $335.4K; 24H +0.00%; V/LP 0.16x; 池数 2; 分项 L20/V10/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| WKC | BSC | [0x6ec9...128edb](https://bscscan.com/token/0x6ec90334d89dbdc89e08a133271be3d104128edb) | 次观察 | Score 71; Tier Liquid; LP $1.32M; Vol24H $507.1K; 24H +29.71%; V/LP 0.38x; 池数 1; 分项 L19/V12/B8/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [SAOF](https://dexscreener.com/solana/ek7yhbdqn36w7et2unsystkcf7f2y4ep7ohmzjpdp8pi) | SOL | [EMADEv...VEpump](https://solscan.io/token/EMADEvnBdp6LoabjRCyN8mw36aVzRd7pYDpNLVEpump) | 次观察 | Score 69; Tier Early; LP $216.2K; Vol24H $137.9K; 24H +16.82%; V/LP 0.64x; 池数 1; 分项 L12/V8/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [UOTF](https://dexscreener.com/solana/dt2dgfdkdgafeqccx68a9j7gwvvabxbhdfefzk8pruxb) | SOL | [YyKEat...Vopump](https://solscan.io/token/YyKEatMcHfLaWJLrL6EmuFDNhxt3fCtz8LktQVopump) | 次观察 | Score 68; Tier Early; LP $159.8K; Vol24H $139.7K; 24H +18.80%; V/LP 0.87x; 池数 1; 分项 L11/V8/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [USTF](https://dexscreener.com/solana/d5e3kzfqty329v3suu95tfhgkfkefrquy6jsvyeuxcu1) | SOL | [CdXYkp...hmpump](https://solscan.io/token/CdXYkpp29NsiXHpKAkHX4KTCT7YtmQcEJSYYNhmpump) | 次观察 | Score 68; Tier Early; LP $145.0K; Vol24H $130.9K; 24H +17.39%; V/LP 0.90x; 池数 1; 分项 L11/V8/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| 牛来 | BSC | [0xbeea...377777](https://bscscan.com/token/0xbeea1d618e533a387d941f58a7d4c9b7bd377777) | 次观察 | Score 67; Tier Liquid; LP $1.10M; Vol24H $14.93M; 24H -8.34%; V/LP 13.52x; 池数 17; 分项 L19/V17/B17/Buy8/Risk-18 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [memestock](https://dexscreener.com/bsc/0x7bdc9582aca6ca25e5db1f2c8e59003b880672cb) | BSC | [0x6FF4...057777](https://bscscan.com/token/0x6FF45323817d1d53bbb8A8dFbA9245aE74057777) | 次观察 | Score 66; Tier Micro; LP $96.7K; Vol24H $387.8K; 24H -9.09%; V/LP 4.01x; 池数 3; 分项 L9/V11/B17/Buy8/Risk-3 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| MarsCoin | BSC | [0x1706...6f4444](https://bscscan.com/token/0x1706f1e06c69f3a8cf33cce179d5d78a5c6f4444) | PVP风险池 | Score 45; Tier Early; LP $353.5K; Vol24H $8.60M; 24H +16.35%; V/LP 24.34x; 池数 1; 分项 L14/V17/B17/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [LAYOOO](https://dexscreener.com/solana/9r27f7ibnqi9jfk5ldwhrhx7fajbppzyr5va35rywwoo) | SOL | [9sfCHM...ZBpump](https://solscan.io/token/9sfCHMLWSVy6MD6zr7pR1gD3qbT7C6K1E3dMf2ZBpump) | PVP风险池 | Score 42; Tier Early; LP $166.6K; Vol24H $4.64M; 24H -22.66%; V/LP 27.84x; 池数 2; 分项 L11/V17/B17/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [DPG](https://dexscreener.com/solana/8tbyi38uqcedfptvjn2rurlbgbgub3itp2hglvvs35hy) | SOL | [LFEJTx...JJpump](https://solscan.io/token/LFEJTxJ9yi6ojGDFpjbGfABLbH55Fc3oEK8syJJpump) | PVP风险池 | Score 41; Tier Early; LP $111.7K; Vol24H $5.90M; 24H -16.86%; V/LP 52.82x; 池数 1; 分项 L10/V17/B17/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [BULLSHIT](https://dexscreener.com/solana/cd5hdt23sjgud5vtwsv51bmpey2qf9qh5cyswwmjbddq) | SOL | [zj1jpp...F8ry2k](https://solscan.io/token/zj1jpp7QMveWHLs61vL9KMZf254KvW7j4AAmBF8ry2k) | PVP风险池 | Score 29; Tier Early; LP $113.7K; Vol24H $9.25M; 24H +5074.00%; V/LP 81.40x; 池数 1; 分项 L10/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [Z500](https://dexscreener.com/solana/2c7palgc7wtqzwr9wa7qt2bthqtdyzcbl6beyfgdsa5e) | SOL | [7fDdLy...mfkJBK](https://solscan.io/token/7fDdLy2rmQKsPCkqUXEd1mN7yDfEzArc4VrctWmfkJBK) | PVP风险池 | Score 28; Tier Early; LP $107.7K; Vol24H $19.25M; 24H +3387.00%; V/LP 178.80x; 池数 2; 分项 L9/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [EYE](https://dexscreener.com/solana/5jm4gnwpt62kphmheet6rjzzfjvsfnxnqdpeugwp2u9q) | SOL | [RmtMAY...KwNDYk](https://solscan.io/token/RmtMAYVTTFv2iK9muMrXEoAnSSsZPPgRPbqZCKwNDYk) | PVP风险池 | Score 27; Tier Early; LP $250.3K; Vol24H $36.19M; 24H +15160.00%; V/LP 144.62x; 池数 2; 分项 L13/V17/B0/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### C. PVP风险池明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| MarsCoin | BSC | [0x1706...6f4444](https://bscscan.com/token/0x1706f1e06c69f3a8cf33cce179d5d78a5c6f4444) | 24H波动可控；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 45; Tier Early; LP $353.5K; Vol24H $8.60M; 24H +16.35%; V/LP 24.34x; 池数 1; 分项 L14/V17/B17/Buy3/Risk-30 | 只记录热度，不进入主榜 |
| [LAYOOO](https://dexscreener.com/solana/9r27f7ibnqi9jfk5ldwhrhx7fajbppzyr5va35rywwoo) | SOL | [9sfCHM...ZBpump](https://solscan.io/token/9sfCHMLWSVy6MD6zr7pR1gD3qbT7C6K1E3dMf2ZBpump) | 24H波动可控；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 42; Tier Early; LP $166.6K; Vol24H $4.64M; 24H -22.66%; V/LP 27.84x; 池数 2; 分项 L11/V17/B17/Buy3/Risk-30 | 只记录热度，不进入主榜 |
| [DPG](https://dexscreener.com/solana/8tbyi38uqcedfptvjn2rurlbgbgub3itp2hglvvs35hy) | SOL | [LFEJTx...JJpump](https://solscan.io/token/LFEJTxJ9yi6ojGDFpjbGfABLbH55Fc3oEK8syJJpump) | 24H波动可控；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 41; Tier Early; LP $111.7K; Vol24H $5.90M; 24H -16.86%; V/LP 52.82x; 池数 1; 分项 L10/V17/B17/Buy3/Risk-30 | 只记录热度，不进入主榜 |
| [BULLSHIT](https://dexscreener.com/solana/cd5hdt23sjgud5vtwsv51bmpey2qf9qh5cyswwmjbddq) | SOL | [zj1jpp...F8ry2k](https://solscan.io/token/zj1jpp7QMveWHLs61vL9KMZf254KvW7j4AAmBF8ry2k) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 29; Tier Early; LP $113.7K; Vol24H $9.25M; 24H +5074.00%; V/LP 81.40x; 池数 1; 分项 L10/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [Z500](https://dexscreener.com/solana/2c7palgc7wtqzwr9wa7qt2bthqtdyzcbl6beyfgdsa5e) | SOL | [7fDdLy...mfkJBK](https://solscan.io/token/7fDdLy2rmQKsPCkqUXEd1mN7yDfEzArc4VrctWmfkJBK) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 28; Tier Early; LP $107.7K; Vol24H $19.25M; 24H +3387.00%; V/LP 178.80x; 池数 2; 分项 L9/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [EYE](https://dexscreener.com/solana/5jm4gnwpt62kphmheet6rjzzfjvsfnxnqdpeugwp2u9q) | SOL | [RmtMAY...KwNDYk](https://solscan.io/token/RmtMAYVTTFv2iK9muMrXEoAnSSsZPPgRPbqZCKwNDYk) | 买卖基本均衡；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 27; Tier Early; LP $250.3K; Vol24H $36.19M; 24H +15160.00%; V/LP 144.62x; 池数 2; 分项 L13/V17/B0/Buy3/Risk-30 | 只记录热度，不进入主榜 |
| [Z](https://dexscreener.com/solana/exormh6uapxi6abtqfnbcbdsdyvnp5zc6cyybzzvuolh) | SOL | [7MQSup...naN3eS](https://solscan.io/token/7MQSupJTpY31HGChEHUAsS1pQhLSrHS5CCsB9bnaN3eS) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 25; Tier Micro; LP $50.6K; Vol24H $4.54M; 24H +1108.00%; V/LP 89.86x; 池数 1; 分项 L6/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [HOBBES](https://dexscreener.com/solana/evzsg1nl7futu2rdztf5xcgf8jrbtuhvyazo7zyeg8pw) | SOL | [37Whvc...tBoR94](https://solscan.io/token/37WhvcVyK6Mzk1oUmqRoS5zbcdZKhrxcU9Ry1vtBoR94) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 15; Tier Micro; LP $48.8K; Vol24H $4.27M; 24H +939.00%; V/LP 87.48x; 池数 1; 分项 L6/V17/B0/Buy8/Risk-40 | 只记录热度，不进入主榜 |

### D. 成熟池观察明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| BTCB | BSC | [0x7130...3ead9c](https://bscscan.com/token/0x7130d2a12b9bcbfae4f2634d864a1ee1ce3ead9c) | 24H接近横盘；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 79; Tier Mature; LP $14.08M; Vol24H $5.22M; 24H +1.16%; V/LP 0.37x; 池数 1; 分项 L20/V17/B22/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| [ANSEM](https://dexscreener.com/solana/fnzky6x7entq1er3d225dqyt7ybfka4pskbmqhb8l3cc) | SOL | [9cRCn9...TGpump](https://solscan.io/token/9cRCn9rGT8V2imeM2BaKs13yhMEais3ruM3rPvTGpump) | 24H波动可控；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 74; Tier Liquid; LP $2.45M; Vol24H $12.95M; 24H +16.79%; V/LP 5.29x; 池数 3; 分项 L20/V17/B17/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| USDT | BSC | [0x55d3...197955](https://bscscan.com/token/0x55d398326f99059ff775485246999027b3197955) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 74; Tier Mature; LP $67.09M; Vol24H $33.81M; 24H +0.68%; V/LP 0.50x; 池数 2; 分项 L20/V17/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |

### E. 链上确认/紧急精查表
| Token | 链 | 合约地址 | 是否需要链上确认 | 紧急精查 | 预检状态 | 原因 |
|---|---|---|---|---|---|---|
| CATE | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| [TOESCOIN](https://dexscreener.com/solana/ee3zk9fxp9guair2xerefxf4tsexezffuwetrna2pkcv) | SOL | [6ehEcT...HDpump](https://solscan.io/token/6ehEcTMCc85aNF4x9CWx8HuvWGhxQtvKdhKVf2HDpump) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| [PUMP](https://dexscreener.com/solana/7q2dqbjtxxp4dqmhec2nsgxwsytq8jaxdygswmag3pfp) | SOL | [9593dF...ysD6A1](https://solscan.io/token/9593dFjsLKKRAaz4LX1eK2DDEgrzfu3idb6yvMysD6A1) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；多池数据冲突，需链上/聚合源复核 |
| WKC | BSC | [0x6ec9...128edb](https://bscscan.com/token/0x6ec90334d89dbdc89e08a133271be3d104128edb) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [SAOF](https://dexscreener.com/solana/ek7yhbdqn36w7et2unsystkcf7f2y4ep7ohmzjpdp8pi) | SOL | [EMADEv...VEpump](https://solscan.io/token/EMADEvnBdp6LoabjRCyN8mw36aVzRd7pYDpNLVEpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [UOTF](https://dexscreener.com/solana/dt2dgfdkdgafeqccx68a9j7gwvvabxbhdfefzk8pruxb) | SOL | [YyKEat...Vopump](https://solscan.io/token/YyKEatMcHfLaWJLrL6EmuFDNhxt3fCtz8LktQVopump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [USTF](https://dexscreener.com/solana/d5e3kzfqty329v3suu95tfhgkfkefrquy6jsvyeuxcu1) | SOL | [CdXYkp...hmpump](https://solscan.io/token/CdXYkpp29NsiXHpKAkHX4KTCT7YtmQcEJSYYNhmpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| 牛来 | BSC | [0xbeea...377777](https://bscscan.com/token/0xbeea1d618e533a387d941f58a7d4c9b7bd377777) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；多池数据冲突，需链上/聚合源复核 |
| [memestock](https://dexscreener.com/bsc/0x7bdc9582aca6ca25e5db1f2c8e59003b880672cb) | BSC | [0x6FF4...057777](https://bscscan.com/token/0x6FF45323817d1d53bbb8A8dFbA9245aE74057777) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| MarsCoin | BSC | [0x1706...6f4444](https://bscscan.com/token/0x1706f1e06c69f3a8cf33cce179d5d78a5c6f4444) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |

### F. 钱包行为 / AVE命中样本表
| Token | 链 | 合约地址 | 行为状态 | 行为层级 | AVE命中 | 判断 |
|---|---|---|---|---|---:|---|
| CATE | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| [TOESCOIN](https://dexscreener.com/solana/ee3zk9fxp9guair2xerefxf4tsexezffuwetrna2pkcv) | SOL | [6ehEcT...HDpump](https://solscan.io/token/6ehEcTMCc85aNF4x9CWx8HuvWGhxQtvKdhKVf2HDpump) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| [PUMP](https://dexscreener.com/solana/7q2dqbjtxxp4dqmhec2nsgxwsytq8jaxdygswmag3pfp) | SOL | [9593dF...ysD6A1](https://solscan.io/token/9593dFjsLKKRAaz4LX1eK2DDEgrzfu3idb6yvMysD6A1) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |

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
| 成熟池观察 | 3 个 | 成熟资产不占早期Alpha主榜 |
| 合约地址覆盖 | 可用 25，缺失 0 | 地址缺失会阻断BSC RPC/Helius精查，需要优先补齐 |
| LP层级 | Micro 4 / Early 10 / Liquid 9 / Mature 2 | 下一步可以按层级分别设置进攻规则 |
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
| dexscreener_search | {'ok': True, 'count': 338} |
| geckoterminal_bsc_trending | {'ok': True, 'count': 20} |
| geckoterminal_solana_trending | {'ok': True, 'count': 20} |

## 数据限制
- This v0.4 scan uses free public sources plus lightweight chain address/account preflight when enabled.
- AVE Smart Money weekly cache structure is connected; real AVE API refresh is handled by the weekly workflow/cache file.
- S0 exact historical replay is not implemented yet; candidates are marked with current metrics only.
- Wallet-level buy/sell retention is not implemented yet; v0.4 only preflights token contract/account existence.
- v0.4 adds chain preflight status and Smart Wallet cache status on top of contract-address output, liquidity tiers, visible PVP/mature detail tables, and chain-verify flags.
- Contract addresses are extracted from DEXScreener baseToken or GeckoTerminal relationships when available; missing addresses are explicitly marked unavailable.