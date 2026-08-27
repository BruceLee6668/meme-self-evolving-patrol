# 自我进化轮巡

**本轮时间 UTC：** 2026-08-27T23:28:47Z
**版本：** 0.5.0-ave-cache-wallet-behavior-prep
**S0 时间锚点：** 2026-06-16T16:15:17+09:00

## 一句话结论
本轮从 137 个合并Token中筛出 4 个主观察候选。v0.5已在v0.4.1基础上增加AVE周缓存真实接口接入框架、Smart Wallet持久保存、wallet_behavior_latest.json，以及BSC Transfer级钱包行为样本。注意：BSC当前是Transfer样本，不等同完整Swap解码。
合约地址可用 25 个，缺失 0 个；缺失地址的候选不能进入后续链上精查。

## 本轮扫描摘要
| 指标 | 数量 |
|---|---:|
| 原始池子记录 | 238 |
| 合并后Token | 137 |
| 输出候选 | 25 |
| 主观察 | 4 |
| 次观察 | 6 |
| PVP风险池 | 8 |
| 成熟池观察 | 5 |
| 低优先观察 | 2 |
| 多池Token | 11 |
| 多池冲突 | 5 |
| Symbol桥接合并 | 2 |
| 合约地址可用 | 25 |
| 合约地址缺失 | 0 |
| Micro层 | 4 |
| Early层 | 12 |
| Liquid层 | 8 |
| Mature层 | 1 |
| 需要链上确认 | 19 |
| 紧急精查候选 | 3 |

## v0.5 数据确认状态
| 项目 | 状态 |
|---|---|
| AVE Smart Wallet周缓存 | active，钱包数 1089，刷新时间 2026-08-24T00:46:57Z，是否过期 否 |
| 链上预检 | 本轮检查 12 个，验证通过 12 个，失败 0 个 |
| Helius状态 | 未配置，SOL使用公共RPC或跳过增强解析 |
| 当前精查层级 | 0.5.0-chain-preflight-plus-wallet-behavior：地址/账户预检 + v0.5钱包行为样本，完整Swap留存仍待下一版 |
| 钱包行为样本 | 本轮检查 4 个，BSC Transfer样本 0 个，SOL签名级 4 个，AVE钱包命中 0 个 |

## 第一部分：生成结果表格

### A. 上次记录结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| CATE | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | 主观察 | Score 91; Tier Liquid; LP $2.33M; Vol24H $7.46M; 24H +1.66%; V/LP 3.20x; 池数 2; 分项 L20/V17/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| WKC | BSC | [0x6ec9...128edb](https://bscscan.com/token/0x6ec90334d89dbdc89e08a133271be3d104128edb) | 主观察 | Score 86; Tier Liquid; LP $1.34M; Vol24H $147.2K; 24H +3.49%; V/LP 0.11x; 池数 1; 分项 L20/V8/B22/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [Jimothy](https://dexscreener.com/solana/5pghkctym6odbhgo2tkmst2ajmjsb2uzbqrkkn4zuft5) | SOL | [Ge87Et...xTpump](https://solscan.io/token/Ge87EtsjwRQbHaqQmKRno69RFTwh9bfSsm99XNxTpump) | 主观察 | Score 83; Tier Liquid; LP $986.5K; Vol24H $2.16M; 24H +22.84%; V/LP 2.19x; 池数 1; 分项 L18/V16/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| BNBCAT | BSC | [0x3efb...6a7777](https://bscscan.com/token/0x3efbfff95576e1d23cf6ead0acd2e73f4d6a7777) | 主观察 | Score 81; Tier Early; LP $217.0K; Vol24H $1.32M; 24H +4.67%; V/LP 6.09x; 池数 1; 分项 L12/V15/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [UOTF](https://dexscreener.com/solana/6aawvpx5fcsxyit8fsnlp4k1uczqlrdptxxh4jm9vmoi) | SOL | [HSW5aw...dHpump](https://solscan.io/token/HSW5awUERBe17pB149mmFnHY4xwrNxbRa6HXMRdHpump) | 主观察 | Score 77; Tier Early; LP $449.7K; Vol24H $204.9K; 24H +19.39%; V/LP 0.46x; 池数 1; 分项 L15/V9/B17/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [DOPAMEME](https://dexscreener.com/solana/fmgbfthlpryd6irj9xwtos4j7rrgnayuumghuncbvxtr) | SOL | [Ab1sTF...BXpump](https://solscan.io/token/Ab1sTFNv2tV5DX1XpriwNehXgiJhdq2RQ5LtD5BXpump) | 次观察 | Score 73; Tier Early; LP $212.1K; Vol24H $642.0K; 24H +9.29%; V/LP 3.03x; 池数 3; 分项 L12/V12/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [HBULL](https://dexscreener.com/solana/edx18gjcdijqslaja2pp5c2vma3btrrx4utxkejufrtq) | SOL | [7V6Sk6...k9pump](https://solscan.io/token/7V6Sk63y8Rr1MvcN5mYNp61wgFhy4EeQg5gUASk9pump) | 次观察 | Score 70; Tier Early; LP $154.2K; Vol24H $256.4K; 24H +9.00%; V/LP 1.66x; 池数 5; 分项 L11/V10/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| DEBIT | BSC | [0x6666...83ce49](https://bscscan.com/token/0x66661c7229901f568f16bd1551b3ba826f83ce49) | PVP风险池 | Score 49; Tier Liquid; LP $1.56M; Vol24H $40.26M; 24H +6.37%; V/LP 25.82x; 池数 1; 分项 L20/V17/B22/Buy8/Risk-42 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [Sky](https://dexscreener.com/solana/3styqkcmxretqslon7zqnx8ketts2h1pap3rkoxdv2gi) | SOL | [CcgRSw...Z7pump](https://solscan.io/token/CcgRSw62atZK9EEAQVGyTcsshgtGJxtLHK2ZGwZ7pump) | PVP风险池 | Score 42; Tier Early; LP $139.0K; Vol24H $3.11M; 24H -55.77%; V/LP 22.38x; 池数 1; 分项 L11/V17/B8/Buy12/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [Pistacio](https://dexscreener.com/solana/22cfmlna8bsh7xrbyvgss6ndd31ifj1ufvnwb7eberwu) | SOL | [FZqdw6...rrjKa2](https://solscan.io/token/FZqdw6oSDCbHtKYxmhnfbi97SnyVy8jaYpdCoMrrjKa2) | PVP风险池 | Score 40; Tier Early; LP $275.3K; Vol24H $8.61M; 24H -49.62%; V/LP 31.26x; 池数 2; 分项 L13/V17/B8/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### B. 本轮扫描结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| CATE | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | 主观察 | Score 86; Tier Liquid; LP $2.21M; Vol24H $7.60M; 24H -18.51%; V/LP 3.43x; 池数 2; 分项 L20/V17/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [neet](https://dexscreener.com/solana/5wnu5qhdprgrl37ffcd6tmmqzugqgxwafgz477rshthy) | SOL | [Ce2gx9...o3pump](https://solscan.io/token/Ce2gx9KGXJ6C9Mp5b5x1sn9Mg87JwEbrQby4Zqo3pump) | 主观察 | Score 80; Tier Liquid; LP $2.17M; Vol24H $2.05M; 24H +17.93%; V/LP 0.95x; 池数 1; 分项 L20/V16/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [Jimothy](https://dexscreener.com/solana/5pghkctym6odbhgo2tkmst2ajmjsb2uzbqrkkn4zuft5) | SOL | [Ge87Et...xTpump](https://solscan.io/token/Ge87EtsjwRQbHaqQmKRno69RFTwh9bfSsm99XNxTpump) | 主观察 | Score 80; Tier Liquid; LP $1.05M; Vol24H $2.62M; 24H +19.55%; V/LP 2.49x; 池数 1; 分项 L19/V17/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [DOPAMEME](https://dexscreener.com/solana/fmgbfthlpryd6irj9xwtos4j7rrgnayuumghuncbvxtr) | SOL | [Ab1sTF...BXpump](https://solscan.io/token/Ab1sTFNv2tV5DX1XpriwNehXgiJhdq2RQ5LtD5BXpump) | 主观察 | Score 78; Tier Early; LP $203.7K; Vol24H $531.6K; 24H -6.56%; V/LP 2.61x; 池数 3; 分项 L12/V12/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| SPX | BSC | [0xca56...903827](https://bscscan.com/token/0xca56094722450016f280c4fd6a333e5c36903827) | 次观察 | Score 74; Tier Early; LP $172.7K; Vol24H $1.20M; 24H -0.10%; V/LP 6.97x; 池数 1; 分项 L11/V14/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [BULLSHIT](https://dexscreener.com/solana/cd5hdt23sjgud5vtwsv51bmpey2qf9qh5cyswwmjbddq) | SOL | [zj1jpp...F8ry2k](https://solscan.io/token/zj1jpp7QMveWHLs61vL9KMZf254KvW7j4AAmBF8ry2k) | 次观察 | Score 73; Tier Early; LP $293.6K; Vol24H $1.92M; 24H +16.30%; V/LP 6.54x; 池数 1; 分项 L13/V16/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [FTFS](https://dexscreener.com/solana/hccadvhjbyozkzklkgpr2dajgori7j1m5qqp8cvoycl1) | SOL | [CaMeaY...XCpump](https://solscan.io/token/CaMeaYEk28iDgYArXg8eiLKgqMa1yuHcPnTGdXCpump) | 次观察 | Score 70; Tier Early; LP $215.1K; Vol24H $230.3K; 24H +23.41%; V/LP 1.07x; 池数 1; 分项 L12/V9/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [Pistacio](https://dexscreener.com/solana/22cfmlna8bsh7xrbyvgss6ndd31ifj1ufvnwb7eberwu) | SOL | [FZqdw6...rrjKa2](https://solscan.io/token/FZqdw6oSDCbHtKYxmhnfbi97SnyVy8jaYpdCoMrrjKa2) | 次观察 | Score 67; Tier Early; LP $295.4K; Vol24H $4.64M; 24H +3.58%; V/LP 15.72x; 池数 7; 分项 L14/V17/B22/Buy8/Risk-18 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [GATO](https://dexscreener.com/solana/5e3dxlxgwmtdcoka51wyyakttjfzbwqcoyuhbui5gt2m) | SOL | [HsprHx...k6pump](https://solscan.io/token/HsprHxBRgiVaQdRf3TnKNuZZtaX9JUSPgMFdAkk6pump) | 次观察 | Score 67; Tier Early; LP $105.9K; Vol24H $218.3K; 24H +1.13%; V/LP 2.06x; 池数 1; 分项 L9/V9/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [WOFI](https://dexscreener.com/solana/4pmjufrlwrcefzqw3pxxjsmoafzs5ggercdupd5skxsn) | SOL | [69hu9Q...mepump](https://solscan.io/token/69hu9QpSHcU916Ax6Vc1gM8PW7ZGh6t4omfpApmepump) | 次观察 | Score 65; Tier Early; LP $242.2K; Vol24H $135.1K; 24H +50.84%; V/LP 0.56x; 池数 1; 分项 L13/V8/B8/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| DEBIT | BSC | [0x6666...83ce49](https://bscscan.com/token/0x66661c7229901f568f16bd1551b3ba826f83ce49) | PVP风险池 | Score 49; Tier Liquid; LP $1.58M; Vol24H $80.15M; 24H +6.05%; V/LP 50.70x; 池数 1; 分项 L20/V17/B22/Buy8/Risk-42 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| BTR | BSC | [0xfed1...d75c51](https://bscscan.com/token/0xfed13d0c40790220fbde712987079eda1ed75c51) | PVP风险池 | Score 40; Tier Liquid; LP $805.2K; Vol24H $37.49M; 24H +32.07%; V/LP 46.56x; 池数 1; 分项 L18/V17/B8/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| fone | SOL | [CTPoyC...gGpump](https://solscan.io/token/CTPoyCwkjMvoJwU4xvZZqoD8tiYk6yDchySiN5gGpump) | PVP风险池 | Score 36; Tier Early; LP $672.1K; Vol24H $61.01M; 24H +51084.06%; V/LP 90.78x; 池数 3; 分项 L17/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| TOADS | SOL | [DMXBsV...FEpump](https://solscan.io/token/DMXBsVBwfuzc5axa2vz6Ba2BzAxcUmn6V7ZtsJFEpump) | PVP风险池 | Score 29; Tier Early; LP $110.7K; Vol24H $2.96M; 24H +376.06%; V/LP 26.77x; 池数 2; 分项 L10/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [ANTSEM](https://dexscreener.com/solana/eytdjhqisrqj2cgh71mxcsttqqhzdjtx3zufb7qgonzp) | SOL | [DuVgdH...pEpump](https://solscan.io/token/DuVgdHeEk7ejWPxWY5G3PQA99oEGGLmnbWuWWxpEpump) | PVP风险池 | Score 26; Tier Micro; LP $62.3K; Vol24H $2.84M; 24H +914.00%; V/LP 45.66x; 池数 1; 分项 L7/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### C. PVP风险池明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| DEBIT | BSC | [0x6666...83ce49](https://bscscan.com/token/0x66661c7229901f568f16bd1551b3ba826f83ce49) | 24H接近横盘；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP极端偏高；FDV超过早期Alpha主榜上限；成熟大市值 | Score 49; Tier Liquid; LP $1.58M; Vol24H $80.15M; 24H +6.05%; V/LP 50.70x; 池数 1; 分项 L20/V17/B22/Buy8/Risk-42 | 只记录热度，不进入主榜 |
| BTR | BSC | [0xfed1...d75c51](https://bscscan.com/token/0xfed13d0c40790220fbde712987079eda1ed75c51) | 24H未过热但已明显波动；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 40; Tier Liquid; LP $805.2K; Vol24H $37.49M; 24H +32.07%; V/LP 46.56x; 池数 1; 分项 L18/V17/B8/Buy3/Risk-30 | 只记录热度，不进入主榜 |
| fone | SOL | [CTPoyC...gGpump](https://solscan.io/token/CTPoyCwkjMvoJwU4xvZZqoD8tiYk6yDchySiN5gGpump) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 36; Tier Early; LP $672.1K; Vol24H $61.01M; 24H +51084.06%; V/LP 90.78x; 池数 3; 分项 L17/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| TOADS | SOL | [DMXBsV...FEpump](https://solscan.io/token/DMXBsVBwfuzc5axa2vz6Ba2BzAxcUmn6V7ZtsJFEpump) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 29; Tier Early; LP $110.7K; Vol24H $2.96M; 24H +376.06%; V/LP 26.77x; 池数 2; 分项 L10/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [ANTSEM](https://dexscreener.com/solana/eytdjhqisrqj2cgh71mxcsttqqhzdjtx3zufb7qgonzp) | SOL | [DuVgdH...pEpump](https://solscan.io/token/DuVgdHeEk7ejWPxWY5G3PQA99oEGGLmnbWuWWxpEpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 26; Tier Micro; LP $62.3K; Vol24H $2.84M; 24H +914.00%; V/LP 45.66x; 池数 1; 分项 L7/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [POKEMON](https://dexscreener.com/solana/4qg7fcgscjzpurfwf8snd93zu9yfqdqku67pmfuhaxag) | SOL | [EhCzWh...V8pump](https://solscan.io/token/EhCzWhMyUAo87bQ663fV2A6reLhXgdhdcf9ynJV8pump) | 24H未过热但已明显波动；买卖略偏买入；LP未达主观察门槛；24H成交合格；LP偏薄；Volume/LP极端偏高 | Score 18; Tier Micro; LP $15.7K; Vol24H $2.43M; 24H -37.37%; V/LP 155.10x; 池数 3; 分项 L2/V16/B8/Buy8/Risk-40 | 只记录热度，不进入主榜 |
| [richape](https://dexscreener.com/solana/auwujv41xgnszggqvzu6t3xb6kccvvk2yevatmkswr6l) | SOL | [66yZvY...fjpump](https://solscan.io/token/66yZvYMAeXwhJksabztzCASnqTShbW5v6V3Crpfjpump) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高；年轻币短期暴拉 | Score 5; Tier Early; LP $158.2K; Vol24H $12.35M; 24H +4286.00%; V/LP 78.09x; 池数 6; 分项 L11/V17/B0/Buy8/Risk-55 | 只记录热度，不进入主榜 |
| [RAX](https://dexscreener.com/solana/cg9hzojt2y3vmuakb8bgptymcbikc4wvbtnxbcjnuyhw) | SOL | [4PFGKQ...37pump](https://solscan.io/token/4PFGKQbJYRZbk8SHNzqQf4DcpyrKJ7r5UKwj4f37pump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高；年轻币短期暴拉 | Score 0; Tier Micro; LP $70.1K; Vol24H $1.58M; 24H +1197.00%; V/LP 22.49x; 池数 4; 分项 L8/V15/B0/Buy8/Risk-55 | 只记录热度，不进入主榜 |

### D. 成熟池观察明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| [RAY](https://dexscreener.com/solana/2axxcn6on9bbt5owwmth53c7qhuxvhleu718kqt8rvy2) | SOL | [4k3Dyj...QrkX6R](https://solscan.io/token/4k3Dyjzvzp8eMZWUXbBCjEvwSkkk59S5iCNLY3QrkX6R) | 24H接近横盘；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 78; Tier Liquid; LP $1.45M; Vol24H $2.35M; 24H +5.73%; V/LP 1.62x; 池数 4; 分项 L20/V16/B22/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| BTCB | BSC | [0x7130...3ead9c](https://bscscan.com/token/0x7130d2a12b9bcbfae4f2634d864a1ee1ce3ead9c) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 74; Tier Mature; LP $24.18M; Vol24H $14.94M; 24H +1.83%; V/LP 0.62x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| Beat | BSC | [0xcf32...8a3e36](https://bscscan.com/token/0xcf3232b85b43bca90e51d38cc06cc8bb8c8a3e36) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限 | Score 69; Tier Early; LP $673.8K; Vol24H $1.46M; 24H -2.11%; V/LP 2.16x; 池数 1; 分项 L17/V15/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| [SOL](https://dexscreener.com/bsc/0xbffec96e8f3b5058b1817c14e4380758fada01ef) | BSC | [0x570A...fD43dF](https://bscscan.com/token/0x570A5D26f7765Ecb712C0924E4De545B89fD43dF) | 24H波动可控；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 68; Tier Liquid; LP $1.31M; Vol24H $3.51M; 24H +8.93%; V/LP 2.68x; 池数 1; 分项 L19/V17/B17/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| ANSEM | SOL | [9cRCn9...TGpump](https://solscan.io/token/9cRCn9rGT8V2imeM2BaKs13yhMEais3ruM3rPvTGpump) | 24H波动可控；LP达主观察门槛；24H成交合格；Volume/LP未失真；卖出笔数占优；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 66; Tier Liquid; LP $3.49M; Vol24H $4.95M; 24H +14.58%; V/LP 1.42x; 池数 3; 分项 L20/V17/B17/Buy0/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |

### E. 链上确认/紧急精查表
| Token | 链 | 合约地址 | 是否需要链上确认 | 紧急精查 | 预检状态 | 原因 |
|---|---|---|---|---|---|---|
| CATE | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| [Jimothy](https://dexscreener.com/solana/5pghkctym6odbhgo2tkmst2ajmjsb2uzbqrkkn4zuft5) | SOL | [Ge87Et...xTpump](https://solscan.io/token/Ge87EtsjwRQbHaqQmKRno69RFTwh9bfSsm99XNxTpump) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| [DOPAMEME](https://dexscreener.com/solana/fmgbfthlpryd6irj9xwtos4j7rrgnayuumghuncbvxtr) | SOL | [Ab1sTF...BXpump](https://solscan.io/token/Ab1sTFNv2tV5DX1XpriwNehXgiJhdq2RQ5LtD5BXpump) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| [neet](https://dexscreener.com/solana/5wnu5qhdprgrl37ffcd6tmmqzugqgxwafgz477rshthy) | SOL | [Ce2gx9...o3pump](https://solscan.io/token/Ce2gx9KGXJ6C9Mp5b5x1sn9Mg87JwEbrQby4Zqo3pump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [RAY](https://dexscreener.com/solana/2axxcn6on9bbt5owwmth53c7qhuxvhleu718kqt8rvy2) | SOL | [4k3Dyj...QrkX6R](https://solscan.io/token/4k3Dyjzvzp8eMZWUXbBCjEvwSkkk59S5iCNLY3QrkX6R) | 是 | 否 | verified / address_preflight_v0.4 | 多池数据冲突，需链上/聚合源复核 |
| SPX | BSC | [0xca56...903827](https://bscscan.com/token/0xca56094722450016f280c4fd6a333e5c36903827) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [BULLSHIT](https://dexscreener.com/solana/cd5hdt23sjgud5vtwsv51bmpey2qf9qh5cyswwmjbddq) | SOL | [zj1jpp...F8ry2k](https://solscan.io/token/zj1jpp7QMveWHLs61vL9KMZf254KvW7j4AAmBF8ry2k) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [FTFS](https://dexscreener.com/solana/hccadvhjbyozkzklkgpr2dajgori7j1m5qqp8cvoycl1) | SOL | [CaMeaY...XCpump](https://solscan.io/token/CaMeaYEk28iDgYArXg8eiLKgqMa1yuHcPnTGdXCpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [Pistacio](https://dexscreener.com/solana/22cfmlna8bsh7xrbyvgss6ndd31ifj1ufvnwb7eberwu) | SOL | [FZqdw6...rrjKa2](https://solscan.io/token/FZqdw6oSDCbHtKYxmhnfbi97SnyVy8jaYpdCoMrrjKa2) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [GATO](https://dexscreener.com/solana/5e3dxlxgwmtdcoka51wyyakttjfzbwqcoyuhbui5gt2m) | SOL | [HsprHx...k6pump](https://solscan.io/token/HsprHxBRgiVaQdRf3TnKNuZZtaX9JUSPgMFdAkk6pump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |

### F. 钱包行为 / AVE命中样本表
| Token | 链 | 合约地址 | 行为状态 | 行为层级 | AVE命中 | 判断 |
|---|---|---|---|---|---:|---|
| CATE | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| [Jimothy](https://dexscreener.com/solana/5pghkctym6odbhgo2tkmst2ajmjsb2uzbqrkkn4zuft5) | SOL | [Ge87Et...xTpump](https://solscan.io/token/Ge87EtsjwRQbHaqQmKRno69RFTwh9bfSsm99XNxTpump) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| [DOPAMEME](https://dexscreener.com/solana/fmgbfthlpryd6irj9xwtos4j7rrgnayuumghuncbvxtr) | SOL | [Ab1sTF...BXpump](https://solscan.io/token/Ab1sTFNv2tV5DX1XpriwNehXgiJhdq2RQ5LtD5BXpump) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| [neet](https://dexscreener.com/solana/5wnu5qhdprgrl37ffcd6tmmqzugqgxwafgz477rshthy) | SOL | [Ce2gx9...o3pump](https://solscan.io/token/Ce2gx9KGXJ6C9Mp5b5x1sn9Mg87JwEbrQby4Zqo3pump) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |

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
| 主观察候选 | 4 个 | 主榜继续稀缺，但必须结合合约地址进入链上确认 |
| PVP风险池 | 8 个 | v0.3已单独展示明细，便于判断噪声来源 |
| 成熟池观察 | 5 个 | 成熟资产不占早期Alpha主榜 |
| 合约地址覆盖 | 可用 25，缺失 0 | 地址缺失会阻断BSC RPC/Helius精查，需要优先补齐 |
| LP层级 | Micro 4 / Early 12 / Liquid 8 / Mature 1 | 下一步可以按层级分别设置进攻规则 |
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