# 自我进化轮巡

**本轮时间 UTC：** 2026-11-25T11:59:46Z
**版本：** 0.5.0-ave-cache-wallet-behavior-prep
**S0 时间锚点：** 2026-06-16T16:15:17+09:00

## 一句话结论
本轮从 146 个合并Token中筛出 5 个主观察候选。v0.5已在v0.4.1基础上增加AVE周缓存真实接口接入框架、Smart Wallet持久保存、wallet_behavior_latest.json，以及BSC Transfer级钱包行为样本。注意：BSC当前是Transfer样本，不等同完整Swap解码。
合约地址可用 25 个，缺失 0 个；缺失地址的候选不能进入后续链上精查。

## 本轮扫描摘要
| 指标 | 数量 |
|---|---:|
| 原始池子记录 | 238 |
| 合并后Token | 146 |
| 输出候选 | 25 |
| 主观察 | 5 |
| 次观察 | 7 |
| PVP风险池 | 8 |
| 成熟池观察 | 4 |
| 低优先观察 | 1 |
| 多池Token | 6 |
| 多池冲突 | 2 |
| Symbol桥接合并 | 1 |
| 合约地址可用 | 25 |
| 合约地址缺失 | 0 |
| Micro层 | 6 |
| Early层 | 11 |
| Liquid层 | 7 |
| Mature层 | 1 |
| 需要链上确认 | 20 |
| 紧急精查候选 | 5 |

## v0.5 数据确认状态
| 项目 | 状态 |
|---|---|
| AVE Smart Wallet周缓存 | active，钱包数 2927，刷新时间 2026-11-23T04:56:43Z，是否过期 否 |
| 链上预检 | 本轮检查 12 个，验证通过 12 个，失败 0 个 |
| Helius状态 | 未配置，SOL使用公共RPC或跳过增强解析 |
| 当前精查层级 | 0.5.0-chain-preflight-plus-wallet-behavior：地址/账户预检 + v0.5钱包行为样本，完整Swap留存仍待下一版 |
| 钱包行为样本 | 本轮检查 8 个，BSC Transfer样本 2 个，SOL签名级 6 个，AVE钱包命中 0 个 |

## 第一部分：生成结果表格

### A. 上次记录结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| CATE | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | 主观察 | Score 85; Tier Liquid; LP $1.26M; Vol24H $542.8K; 24H -1.89%; V/LP 0.43x; 池数 2; 分项 L19/V12/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| pippin | SOL | [Dfh5Dz...mApump](https://solscan.io/token/Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump) | 主观察 | Score 83; Tier Liquid; LP $3.36M; Vol24H $1.03M; 24H +4.14%; V/LP 0.31x; 池数 1; 分项 L20/V14/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [USEF](https://dexscreener.com/solana/5urqw6moinqmdn7t9v895qyhch2ki61uqrqjfjbracd3) | SOL | [JmBAjh...Tupump](https://solscan.io/token/JmBAjhHKp9btzABS5Eudfxbtg2ipqps2JrFzgTupump) | 主观察 | Score 77; Tier Early; LP $333.9K; Vol24H $174.9K; 24H +4.86%; V/LP 0.52x; 池数 1; 分项 L14/V9/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [BPF](https://dexscreener.com/solana/auqgamzwoygpjx9fvtry1i24vywukcxmwrq3zp9symcd) | SOL | [G6wuh4...Mtpump](https://solscan.io/token/G6wuh4ihzeLFtv35r7YX71picr4aga76KphKEMtpump) | 主观察 | Score 77; Tier Early; LP $360.7K; Vol24H $175.0K; 24H +4.85%; V/LP 0.49x; 池数 1; 分项 L14/V9/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [CLAUDIA](https://dexscreener.com/solana/fe7bpdycs74gqicuf14hwgumtopkv1d9mdyvx5btohfr) | SOL | [2j5SaS...hnW2ZM](https://solscan.io/token/2j5SaS7xy776qCBpyPQbZjyQSAtKiFgrwjfErthnW2ZM) | 次观察 | Score 72; Tier Early; LP $409.2K; Vol24H $676.5K; 24H -10.75%; V/LP 1.65x; 池数 1; 分项 L15/V13/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [NIO](https://dexscreener.com/solana/b4wmjc6pvjctu3qsvs3ett9mr4m5v5jbkrqctwantc71) | SOL | [7SL2Vn...LQpump](https://solscan.io/token/7SL2VnfYsChvog5oQY9Nmtqu1wceaMiQzWoqoLQpump) | 次观察 | Score 71; Tier Early; LP $136.4K; Vol24H $534.4K; 24H +5.33%; V/LP 3.92x; 池数 1; 分项 L10/V12/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [HOGE](https://dexscreener.com/solana/7cnc9ggegzeffk8flxiyuhdtmeefpqzond56u1mxhnor) | SOL | [FVzqGq...fopump](https://solscan.io/token/FVzqGqRmr4UH1Fif6dewmwbJ1p4YUZCu8dcw4Efopump) | 次观察 | Score 68; Tier Early; LP $111.2K; Vol24H $221.4K; 24H +8.96%; V/LP 1.99x; 池数 6; 分项 L10/V9/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [CBUCKS](https://dexscreener.com/solana/b4cp45pgifvm5faxfh6aev8qz3eunqnqgbw7kuc7mhnb) | SOL | [DtcicP...xZpump](https://solscan.io/token/DtcicPCKTKeAh7TDEzTym3hXeoHAoMiBdYJhMYxZpump) | 次观察 | Score 65; Tier Early; LP $256.7K; Vol24H $127.6K; 24H +20.13%; V/LP 0.50x; 池数 1; 分项 L13/V8/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [UDTF](https://dexscreener.com/solana/bmtxzpyywyqeo3nx49w9c1hwr53mg4urrhtmxbnf1uhf) | SOL | [piHrhM...ZDpump](https://solscan.io/token/piHrhMnWyJWE9yViN1KYK5p2mDAda9ajbUfxiZDpump) | 次观察 | Score 64; Tier Early; LP $297.7K; Vol24H $7.9K; 24H +7.34%; V/LP 0.03x; 池数 1; 分项 L14/V0/B22/Buy12/Risk-8 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| EVAA | BSC | [0xaa03...a628c1](https://bscscan.com/token/0xaa036928c9c0df07d525b55ea8ee690bb5a628c1) | PVP风险池 | Score 43; Tier Early; LP $216.2K; Vol24H $7.93M; 24H -24.73%; V/LP 36.69x; 池数 1; 分项 L12/V17/B17/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### B. 本轮扫描结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| ANSEM | SOL | [9cRCn9...TGpump](https://solscan.io/token/9cRCn9rGT8V2imeM2BaKs13yhMEais3ruM3rPvTGpump) | 主观察 | Score 88; Tier Liquid; LP $765.7K; Vol24H $4.14M; 24H -2.07%; V/LP 5.41x; 池数 3; 分项 L17/V17/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| SKYAI | BSC | [0x92aa...3ffb10](https://bscscan.com/token/0x92aa03137385f18539301349dcfc9ebc923ffb10) | 主观察 | Score 86; Tier Liquid; LP $4.46M; Vol24H $2.92M; 24H -4.77%; V/LP 0.65x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| $BANANA | BSC | [0x3d4f...a9a760](https://bscscan.com/token/0x3d4f0513e8a29669b960f9dbca61861548a9a760) | 主观察 | Score 85; Tier Liquid; LP $2.80M; Vol24H $2.41M; 24H -1.51%; V/LP 0.86x; 池数 1; 分项 L20/V16/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| CATE | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | 主观察 | Score 84; Tier Liquid; LP $1.21M; Vol24H $346.2K; 24H -6.45%; V/LP 0.29x; 池数 2; 分项 L19/V11/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [CBUCKS](https://dexscreener.com/solana/b4cp45pgifvm5faxfh6aev8qz3eunqnqgbw7kuc7mhnb) | SOL | [DtcicP...xZpump](https://solscan.io/token/DtcicPCKTKeAh7TDEzTym3hXeoHAoMiBdYJhMYxZpump) | 主观察 | Score 77; Tier Early; LP $256.4K; Vol24H $299.7K; 24H +7.55%; V/LP 1.17x; 池数 1; 分项 L13/V10/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [USEF](https://dexscreener.com/solana/5urqw6moinqmdn7t9v895qyhch2ki61uqrqjfjbracd3) | SOL | [JmBAjh...Tupump](https://solscan.io/token/JmBAjhHKp9btzABS5Eudfxbtg2ipqps2JrFzgTupump) | 次观察 | Score 77; Tier Early; LP $337.8K; Vol24H $174.7K; 24H +7.39%; V/LP 0.52x; 池数 1; 分项 L14/V9/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 次观察，不直接进攻 |
| [BPF](https://dexscreener.com/solana/auqgamzwoygpjx9fvtry1i24vywukcxmwrq3zp9symcd) | SOL | [G6wuh4...Mtpump](https://solscan.io/token/G6wuh4ihzeLFtv35r7YX71picr4aga76KphKEMtpump) | 次观察 | Score 77; Tier Early; LP $365.9K; Vol24H $174.9K; 24H +7.12%; V/LP 0.48x; 池数 1; 分项 L14/V9/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 次观察，不直接进攻 |
| mihao | SOL | [4CxjZy...8spump](https://solscan.io/token/4CxjZyMNoF1p6eXHXHv1TWpS2X47CuUmLwtGe18spump) | 次观察 | Score 77; Tier Early; LP $264.0K; Vol24H $1.34M; 24H -16.68%; V/LP 5.06x; 池数 2; 分项 L13/V15/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 次观察，不直接进攻 |
| [IGNIS](https://dexscreener.com/bsc/0x7a88ca451215c92fbccd4efb15424a67bf40ebf2) | BSC | [0x2D81...B4f183](https://bscscan.com/token/0x2D81A59dF5bEe318d74F47F25c04313443B4f183) | 次观察 | Score 71; Tier Early; LP $130.7K; Vol24H $646.9K; 24H +20.86%; V/LP 4.95x; 池数 3; 分项 L10/V12/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [CLAUDIA](https://dexscreener.com/solana/fe7bpdycs74gqicuf14hwgumtopkv1d9mdyvx5btohfr) | SOL | [2j5SaS...hnW2ZM](https://solscan.io/token/2j5SaS7xy776qCBpyPQbZjyQSAtKiFgrwjfErthnW2ZM) | 次观察 | Score 71; Tier Early; LP $396.1K; Vol24H $575.1K; 24H -11.72%; V/LP 1.45x; 池数 1; 分项 L15/V12/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [NIO](https://dexscreener.com/solana/b4wmjc6pvjctu3qsvs3ett9mr4m5v5jbkrqctwantc71) | SOL | [7SL2Vn...LQpump](https://solscan.io/token/7SL2VnfYsChvog5oQY9Nmtqu1wceaMiQzWoqoLQpump) | 次观察 | Score 69; Tier Early; LP $130.5K; Vol24H $308.6K; 24H -5.93%; V/LP 2.36x; 池数 1; 分项 L10/V10/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [UDTF](https://dexscreener.com/solana/bmtxzpyywyqeo3nx49w9c1hwr53mg4urrhtmxbnf1uhf) | SOL | [piHrhM...ZDpump](https://solscan.io/token/piHrhMnWyJWE9yViN1KYK5p2mDAda9ajbUfxiZDpump) | 次观察 | Score 64; Tier Early; LP $300.2K; Vol24H $9.3K; 24H +7.46%; V/LP 0.03x; 池数 1; 分项 L14/V0/B22/Buy12/Risk-8 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| GUA | BSC | [0xa5c8...9469be](https://bscscan.com/token/0xa5c8e1513b6a08334b479fe4d71f1253259469be) | PVP风险池 | Score 38; Tier Liquid; LP $1.13M; Vol24H $24.54M; 24H +47.01%; V/LP 21.67x; 池数 1; 分项 L19/V17/B8/Buy0/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| BASKET | SOL | [3Tg6Yn...baJN6f](https://solscan.io/token/3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f) | PVP风险池 | Score 31; Tier Early; LP $184.8K; Vol24H $3.70M; 24H +2429.02%; V/LP 20.04x; 池数 1; 分项 L12/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| JIMMY | SOL | [38M2z4...Nipump](https://solscan.io/token/38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump) | PVP风险池 | Score 28; Tier Micro; LP $90.9K; Vol24H $3.49M; 24H +218.41%; V/LP 38.42x; 池数 2; 分项 L9/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### C. PVP风险池明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| GUA | BSC | [0xa5c8...9469be](https://bscscan.com/token/0xa5c8e1513b6a08334b479fe4d71f1253259469be) | 24H未过热但已明显波动；LP达主观察门槛；24H成交合格；卖出笔数占优；Volume/LP极端偏高 | Score 38; Tier Liquid; LP $1.13M; Vol24H $24.54M; 24H +47.01%; V/LP 21.67x; 池数 1; 分项 L19/V17/B8/Buy0/Risk-30 | 只记录热度，不进入主榜 |
| BASKET | SOL | [3Tg6Yn...baJN6f](https://solscan.io/token/3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 31; Tier Early; LP $184.8K; Vol24H $3.70M; 24H +2429.02%; V/LP 20.04x; 池数 1; 分项 L12/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| JIMMY | SOL | [38M2z4...Nipump](https://solscan.io/token/38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 28; Tier Micro; LP $90.9K; Vol24H $3.49M; 24H +218.41%; V/LP 38.42x; 池数 2; 分项 L9/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| EVAA | BSC | [0xaa03...a628c1](https://bscscan.com/token/0xaa036928c9c0df07d525b55ea8ee690bb5a628c1) | 24H未过热但已明显波动；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP极端偏高；FDV超过早期Alpha主榜上限 | Score 23; Tier Early; LP $248.2K; Vol24H $7.56M; 24H +37.31%; V/LP 30.47x; 池数 1; 分项 L13/V17/B8/Buy3/Risk-42 | 只记录热度，不进入主榜 |
| DUVAL | SOL | [7fmD1p...Vypump](https://solscan.io/token/7fmD1p3jzva28EPP9bPqbDoxZGj5j398yJoE3EVypump) | 24H未过热但已明显波动；买卖略偏买入；LP未达主观察门槛；24H成交合格；LP偏薄；Volume/LP极端偏高 | Score 18; Tier Micro; LP $22.3K; Vol24H $1.71M; 24H -73.16%; V/LP 76.58x; 池数 1; 分项 L3/V15/B8/Buy8/Risk-40 | 只记录热度，不进入主榜 |
| Holders | SOL | [55RwtH...cXpump](https://solscan.io/token/55RwtHpoNB81SgfiNvogeZTMfik2SfMGa5FaxKcXpump) | 24H未过热但已明显波动；买卖略偏买入；LP未达主观察门槛；24H成交合格；LP偏薄；Volume/LP极端偏高 | Score 17; Tier Micro; LP $16.3K; Vol24H $1.78M; 24H +47.45%; V/LP 109.37x; 池数 1; 分项 L2/V15/B8/Buy8/Risk-40 | 只记录热度，不进入主榜 |
| [4CHAN](https://dexscreener.com/solana/ak4wr2ueeajmqzsecgpmx9ehcrwwrngp8cskvdeh1e6h) | SOL | [DVdWuN...GTpump](https://solscan.io/token/DVdWuNK8ncn79B6z8nCiwcNAiwyFcmBPfChgxJGTpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 15; Tier Micro; LP $44.6K; Vol24H $4.29M; 24H +992.00%; V/LP 96.30x; 池数 2; 分项 L6/V17/B0/Buy8/Risk-40 | 只记录热度，不进入主榜 |
| [PERRO](https://dexscreener.com/solana/4s1epxdedd7ty1utj7frou3sasxug98os7hcptneu8wh) | SOL | [4Di56U...98pump](https://solscan.io/token/4Di56UJzpnb7E4D7aLXFf7aLF5TrpJYv9Q3mR398pump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 13; Tier Micro; LP $32.2K; Vol24H $2.02M; 24H +535.00%; V/LP 62.68x; 池数 1; 分项 L5/V16/B0/Buy8/Risk-40 | 只记录热度，不进入主榜 |

### D. 成熟池观察明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| ARK | BSC | [0xcae1...618b9d](https://bscscan.com/token/0xcae117ca6bc8a341d2e7207f30e180f0e5618b9d) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 74; Tier Mature; LP $58.41M; Vol24H $5.76M; 24H -0.35%; V/LP 0.10x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| PIEVERSE | BSC | [0x0e63...0225a9](https://bscscan.com/token/0x0e63b9c287e32a05e6b9ab8ee8df88a2760225a9) | 24H接近横盘；LP达主观察门槛；24H成交合格；Volume/LP未失真；卖出笔数占优；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 71; Tier Liquid; LP $2.87M; Vol24H $17.26M; 24H -2.88%; V/LP 6.01x; 池数 1; 分项 L20/V17/B22/Buy0/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| ARIA | BSC | [0x5d3a...555238](https://bscscan.com/token/0x5d3a12c42e5372b2cc3264ab3cdcf660a1555238) | 24H接近横盘；LP达主观察门槛；24H成交合格；Volume/LP未失真；卖出笔数占优；FDV超过早期Alpha主榜上限；成熟大市值 | Score 71; Tier Liquid; LP $2.17M; Vol24H $3.85M; 24H -7.05%; V/LP 1.77x; 池数 1; 分项 L20/V17/B22/Buy0/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| AKE | BSC | [0x2c3a...12f7db](https://bscscan.com/token/0x2c3a8ee94ddd97244a93bc48298f97d2c412f7db) | 24H波动可控；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；成熟大市值 | Score 65; Tier Early; LP $545.8K; Vol24H $3.00M; 24H -14.29%; V/LP 5.49x; 池数 1; 分项 L16/V17/B17/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |

### E. 链上确认/紧急精查表
| Token | 链 | 合约地址 | 是否需要链上确认 | 紧急精查 | 预检状态 | 原因 |
|---|---|---|---|---|---|---|
| CATE | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| [CBUCKS](https://dexscreener.com/solana/b4cp45pgifvm5faxfh6aev8qz3eunqnqgbw7kuc7mhnb) | SOL | [DtcicP...xZpump](https://solscan.io/token/DtcicPCKTKeAh7TDEzTym3hXeoHAoMiBdYJhMYxZpump) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| [USEF](https://dexscreener.com/solana/5urqw6moinqmdn7t9v895qyhch2ki61uqrqjfjbracd3) | SOL | [JmBAjh...Tupump](https://solscan.io/token/JmBAjhHKp9btzABS5Eudfxbtg2ipqps2JrFzgTupump) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| [BPF](https://dexscreener.com/solana/auqgamzwoygpjx9fvtry1i24vywukcxmwrq3zp9symcd) | SOL | [G6wuh4...Mtpump](https://solscan.io/token/G6wuh4ihzeLFtv35r7YX71picr4aga76KphKEMtpump) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| mihao | SOL | [4CxjZy...8spump](https://solscan.io/token/4CxjZyMNoF1p6eXHXHv1TWpS2X47CuUmLwtGe18spump) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| ANSEM | SOL | [9cRCn9...TGpump](https://solscan.io/token/9cRCn9rGT8V2imeM2BaKs13yhMEais3ruM3rPvTGpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；多池数据冲突，需链上/聚合源复核 |
| SKYAI | BSC | [0x92aa...3ffb10](https://bscscan.com/token/0x92aa03137385f18539301349dcfc9ebc923ffb10) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| $BANANA | BSC | [0x3d4f...a9a760](https://bscscan.com/token/0x3d4f0513e8a29669b960f9dbca61861548a9a760) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [IGNIS](https://dexscreener.com/bsc/0x7a88ca451215c92fbccd4efb15424a67bf40ebf2) | BSC | [0x2D81...B4f183](https://bscscan.com/token/0x2D81A59dF5bEe318d74F47F25c04313443B4f183) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；多池数据冲突，需链上/聚合源复核 |
| [CLAUDIA](https://dexscreener.com/solana/fe7bpdycs74gqicuf14hwgumtopkv1d9mdyvx5btohfr) | SOL | [2j5SaS...hnW2ZM](https://solscan.io/token/2j5SaS7xy776qCBpyPQbZjyQSAtKiFgrwjfErthnW2ZM) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |

### F. 钱包行为 / AVE命中样本表
| Token | 链 | 合约地址 | 行为状态 | 行为层级 | AVE命中 | 判断 |
|---|---|---|---|---|---:|---|
| CATE | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| [CBUCKS](https://dexscreener.com/solana/b4cp45pgifvm5faxfh6aev8qz3eunqnqgbw7kuc7mhnb) | SOL | [DtcicP...xZpump](https://solscan.io/token/DtcicPCKTKeAh7TDEzTym3hXeoHAoMiBdYJhMYxZpump) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| [USEF](https://dexscreener.com/solana/5urqw6moinqmdn7t9v895qyhch2ki61uqrqjfjbracd3) | SOL | [JmBAjh...Tupump](https://solscan.io/token/JmBAjhHKp9btzABS5Eudfxbtg2ipqps2JrFzgTupump) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| [BPF](https://dexscreener.com/solana/auqgamzwoygpjx9fvtry1i24vywukcxmwrq3zp9symcd) | SOL | [G6wuh4...Mtpump](https://solscan.io/token/G6wuh4ihzeLFtv35r7YX71picr4aga76KphKEMtpump) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| mihao | SOL | [4CxjZy...8spump](https://solscan.io/token/4CxjZyMNoF1p6eXHXHv1TWpS2X47CuUmLwtGe18spump) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| ANSEM | SOL | [9cRCn9...TGpump](https://solscan.io/token/9cRCn9rGT8V2imeM2BaKs13yhMEais3ruM3rPvTGpump) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| SKYAI | BSC | [0x92aa...3ffb10](https://bscscan.com/token/0x92aa03137385f18539301349dcfc9ebc923ffb10) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| $BANANA | BSC | [0x3d4f...a9a760](https://bscscan.com/token/0x3d4f0513e8a29669b960f9dbca61861548a9a760) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |

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
| LP层级 | Micro 6 / Early 11 / Liquid 7 / Mature 1 | 下一步可以按层级分别设置进攻规则 |
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
| dexscreener_boosts | {'ok': True, 'count': 18, 'expanded': 18} |
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