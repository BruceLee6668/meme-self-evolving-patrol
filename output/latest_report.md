# 自我进化轮巡

**本轮时间 UTC：** 2026-11-27T04:42:59Z
**版本：** 0.5.0-ave-cache-wallet-behavior-prep
**S0 时间锚点：** 2026-06-16T16:15:17+09:00

## 一句话结论
本轮从 148 个合并Token中筛出 5 个主观察候选。v0.5已在v0.4.1基础上增加AVE周缓存真实接口接入框架、Smart Wallet持久保存、wallet_behavior_latest.json，以及BSC Transfer级钱包行为样本。注意：BSC当前是Transfer样本，不等同完整Swap解码。
合约地址可用 25 个，缺失 0 个；缺失地址的候选不能进入后续链上精查。

## 本轮扫描摘要
| 指标 | 数量 |
|---|---:|
| 原始池子记录 | 258 |
| 合并后Token | 148 |
| 输出候选 | 25 |
| 主观察 | 5 |
| 次观察 | 6 |
| PVP风险池 | 8 |
| 成熟池观察 | 6 |
| 低优先观察 | 0 |
| 多池Token | 6 |
| 多池冲突 | 2 |
| Symbol桥接合并 | 1 |
| 合约地址可用 | 25 |
| 合约地址缺失 | 0 |
| Micro层 | 6 |
| Early层 | 9 |
| Liquid层 | 10 |
| Mature层 | 0 |
| 需要链上确认 | 19 |
| 紧急精查候选 | 5 |

## v0.5 数据确认状态
| 项目 | 状态 |
|---|---|
| AVE Smart Wallet周缓存 | active，钱包数 2927，刷新时间 2026-11-23T04:56:43Z，是否过期 否 |
| 链上预检 | 本轮检查 12 个，验证通过 12 个，失败 0 个 |
| Helius状态 | 未配置，SOL使用公共RPC或跳过增强解析 |
| 当前精查层级 | 0.5.0-chain-preflight-plus-wallet-behavior：地址/账户预检 + v0.5钱包行为样本，完整Swap留存仍待下一版 |
| 钱包行为样本 | 本轮检查 5 个，BSC Transfer样本 0 个，SOL签名级 5 个，AVE钱包命中 0 个 |

## 第一部分：生成结果表格

### A. 上次记录结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| SPCX | SOL | [SPCXxc...5BimGb](https://solscan.io/token/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | 主观察 | Score 86; Tier Liquid; LP $2.41M; Vol24H $3.46M; 24H +1.85%; V/LP 1.43x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| CATE | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | 主观察 | Score 85; Tier Liquid; LP $1.30M; Vol24H $582.3K; 24H +2.07%; V/LP 0.45x; 池数 2; 分项 L19/V12/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [ANSEM](https://dexscreener.com/solana/fnzky6x7entq1er3d225dqyt7ybfka4pskbmqhb8l3cc) | SOL | [9cRCn9...TGpump](https://solscan.io/token/9cRCn9rGT8V2imeM2BaKs13yhMEais3ruM3rPvTGpump) | 主观察 | Score 84; Tier Early; LP $749.5K; Vol24H $741.0K; 24H -4.43%; V/LP 0.99x; 池数 2; 分项 L17/V13/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [TROLL](https://dexscreener.com/solana/4w2cysotx6czaugmmwg13hdpy4qemg2czekyeqyk9ama) | SOL | [5UUH9R...TBhgH2](https://solscan.io/token/5UUH9RTDiSpq6HKS6bp4NdU9PNJpXRXuiw6ShBTBhgH2) | 主观察 | Score 84; Tier Liquid; LP $1.86M; Vol24H $261.1K; 24H +4.78%; V/LP 0.14x; 池数 1; 分项 L20/V10/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| mihao | SOL | [4CxjZy...8spump](https://solscan.io/token/4CxjZyMNoF1p6eXHXHv1TWpS2X47CuUmLwtGe18spump) | 主观察 | Score 81; Tier Early; LP $300.1K; Vol24H $1.03M; 24H +20.71%; V/LP 3.43x; 池数 2; 分项 L14/V14/B17/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [BPF](https://dexscreener.com/solana/auqgamzwoygpjx9fvtry1i24vywukcxmwrq3zp9symcd) | SOL | [G6wuh4...Mtpump](https://solscan.io/token/G6wuh4ihzeLFtv35r7YX71picr4aga76KphKEMtpump) | 次观察 | Score 78; Tier Early; LP $381.1K; Vol24H $175.4K; 24H +5.04%; V/LP 0.46x; 池数 1; 分项 L15/V9/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 次观察，不直接进攻 |
| [USEF](https://dexscreener.com/solana/5urqw6moinqmdn7t9v895qyhch2ki61uqrqjfjbracd3) | SOL | [JmBAjh...Tupump](https://solscan.io/token/JmBAjhHKp9btzABS5Eudfxbtg2ipqps2JrFzgTupump) | 次观察 | Score 77; Tier Early; LP $351.0K; Vol24H $175.4K; 24H +5.11%; V/LP 0.50x; 池数 1; 分项 L14/V9/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 次观察，不直接进攻 |
| [CLAUDIA](https://dexscreener.com/solana/fe7bpdycs74gqicuf14hwgumtopkv1d9mdyvx5btohfr) | SOL | [2j5SaS...hnW2ZM](https://solscan.io/token/2j5SaS7xy776qCBpyPQbZjyQSAtKiFgrwjfErthnW2ZM) | 次观察 | Score 77; Tier Early; LP $439.4K; Vol24H $833.5K; 24H +6.09%; V/LP 1.90x; 池数 1; 分项 L15/V13/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，不直接进攻 |
| [BRUH](https://dexscreener.com/solana/ehpzesdxtymvwz1iy5nt3lrnjy1xbc1kgqspl1kqnyiv) | SOL | [PgFtGG...hRpump](https://solscan.io/token/PgFtGGquvnv2zEkjG2N2QPvBTBrafuExGYEqahRpump) | 次观察 | Score 76; Tier Early; LP $225.6K; Vol24H $1.47M; 24H +19.84%; V/LP 6.54x; 池数 1; 分项 L12/V15/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 次观察，不直接进攻 |
| [CBUCKS](https://dexscreener.com/solana/b4cp45pgifvm5faxfh6aev8qz3eunqnqgbw7kuc7mhnb) | SOL | [DtcicP...xZpump](https://solscan.io/token/DtcicPCKTKeAh7TDEzTym3hXeoHAoMiBdYJhMYxZpump) | 次观察 | Score 71; Tier Early; LP $291.8K; Vol24H $215.4K; 24H +17.27%; V/LP 0.74x; 池数 1; 分项 L13/V9/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |

### B. 本轮扫描结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| CATE | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | 主观察 | Score 90; Tier Liquid; LP $1.37M; Vol24H $638.9K; 24H +7.60%; V/LP 0.47x; 池数 2; 分项 L20/V12/B22/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| SPCX | SOL | [SPCXxc...5BimGb](https://solscan.io/token/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | 主观察 | Score 86; Tier Liquid; LP $2.37M; Vol24H $3.76M; 24H +3.53%; V/LP 1.59x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [ANSEM](https://dexscreener.com/solana/fnzky6x7entq1er3d225dqyt7ybfka4pskbmqhb8l3cc) | SOL | [9cRCn9...TGpump](https://solscan.io/token/9cRCn9rGT8V2imeM2BaKs13yhMEais3ruM3rPvTGpump) | 主观察 | Score 83; Tier Liquid; LP $777.9K; Vol24H $480.3K; 24H -7.33%; V/LP 0.62x; 池数 1; 分项 L17/V12/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [BPF](https://dexscreener.com/solana/auqgamzwoygpjx9fvtry1i24vywukcxmwrq3zp9symcd) | SOL | [G6wuh4...Mtpump](https://solscan.io/token/G6wuh4ihzeLFtv35r7YX71picr4aga76KphKEMtpump) | 主观察 | Score 78; Tier Early; LP $381.5K; Vol24H $174.5K; 24H +4.29%; V/LP 0.46x; 池数 1; 分项 L15/V9/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [USEF](https://dexscreener.com/solana/5urqw6moinqmdn7t9v895qyhch2ki61uqrqjfjbracd3) | SOL | [JmBAjh...Tupump](https://solscan.io/token/JmBAjhHKp9btzABS5Eudfxbtg2ipqps2JrFzgTupump) | 主观察 | Score 77; Tier Early; LP $351.0K; Vol24H $174.6K; 24H +3.47%; V/LP 0.50x; 池数 1; 分项 L14/V9/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [PUMP](https://dexscreener.com/solana/7q2dqbjtxxp4dqmhec2nsgxwsytq8jaxdygswmag3pfp) | SOL | [9593dF...ysD6A1](https://solscan.io/token/9593dFjsLKKRAaz4LX1eK2DDEgrzfu3idb6yvMysD6A1) | 次观察 | Score 77; Tier Liquid; LP $2.05M; Vol24H $169.8K; 24H -0.25%; V/LP 0.08x; 池数 1; 分项 L20/V8/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，不直接进攻 |
| mihao | SOL | [4CxjZy...8spump](https://solscan.io/token/4CxjZyMNoF1p6eXHXHv1TWpS2X47CuUmLwtGe18spump) | 次观察 | Score 72; Tier Early; LP $313.9K; Vol24H $1.18M; 24H +32.81%; V/LP 3.75x; 池数 2; 分项 L14/V14/B8/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [CLAUDIA](https://dexscreener.com/solana/fe7bpdycs74gqicuf14hwgumtopkv1d9mdyvx5btohfr) | SOL | [2j5SaS...hnW2ZM](https://solscan.io/token/2j5SaS7xy776qCBpyPQbZjyQSAtKiFgrwjfErthnW2ZM) | 次观察 | Score 72; Tier Early; LP $441.3K; Vol24H $807.2K; 24H +17.10%; V/LP 1.83x; 池数 1; 分项 L15/V13/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [JOB](https://dexscreener.com/solana/hauvbmnthcfmg9srxmvz1gaxnpu955hkpdsasc2cx4c8) | SOL | [9Pq7aL...uypump](https://solscan.io/token/9Pq7aLAbhDG2tTnS22cm6kuysZVcZpLFE368HWuypump) | 次观察 | Score 66; Tier Early; LP $148.4K; Vol24H $369.3K; 24H +13.13%; V/LP 2.49x; 池数 1; 分项 L11/V11/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [BRUH](https://dexscreener.com/solana/ehpzesdxtymvwz1iy5nt3lrnjy1xbc1kgqspl1kqnyiv) | SOL | [PgFtGG...hRpump](https://solscan.io/token/PgFtGGquvnv2zEkjG2N2QPvBTBrafuExGYEqahRpump) | 次观察 | Score 66; Tier Early; LP $193.6K; Vol24H $1.08M; 24H -48.71%; V/LP 5.57x; 池数 1; 分项 L12/V14/B8/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [CBUCKS](https://dexscreener.com/solana/b4cp45pgifvm5faxfh6aev8qz3eunqnqgbw7kuc7mhnb) | SOL | [DtcicP...xZpump](https://solscan.io/token/DtcicPCKTKeAh7TDEzTym3hXeoHAoMiBdYJhMYxZpump) | 次观察 | Score 64; Tier Early; LP $312.6K; Vol24H $301.2K; 24H +26.14%; V/LP 0.96x; 池数 1; 分项 L14/V10/B8/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| EVAA | BSC | [0xaa03...a628c1](https://bscscan.com/token/0xaa036928c9c0df07d525b55ea8ee690bb5a628c1) | PVP风险池 | Score 34; Tier Early; LP $221.0K; Vol24H $5.52M; 24H -27.42%; V/LP 24.98x; 池数 1; 分项 L12/V17/B8/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| SpaceXCoin | BSC | [0xdde2...457777](https://bscscan.com/token/0xdde27483de8c958e4d2657d64eb7551717457777) | PVP风险池 | Score 30; Tier Early; LP $142.3K; Vol24H $5.31M; 24H +5509.16%; V/LP 37.29x; 池数 1; 分项 L11/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [Snowball](https://dexscreener.com/solana/aircdeu4yl6hjuina65mtwakzmex7stkzsinmyzhzkt2) | SOL | [9TKbd3...2cpump](https://solscan.io/token/9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump) | PVP风险池 | Score 25; Tier Micro; LP $64.3K; Vol24H $1.88M; 24H +7257.00%; V/LP 29.22x; 池数 7; 分项 L7/V16/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| PAIR | SOL | [32rBxc...Kxpump](https://solscan.io/token/32rBxcFjCFnyqZ41CEPM5AL67X1dcw8w83vZt6Kxpump) | PVP风险池 | Score 19; Tier Micro; LP $15.9K; Vol24H $3.32M; 24H +51.26%; V/LP 208.64x; 池数 1; 分项 L2/V17/B8/Buy8/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### C. PVP风险池明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| EVAA | BSC | [0xaa03...a628c1](https://bscscan.com/token/0xaa036928c9c0df07d525b55ea8ee690bb5a628c1) | 24H未过热但已明显波动；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 34; Tier Early; LP $221.0K; Vol24H $5.52M; 24H -27.42%; V/LP 24.98x; 池数 1; 分项 L12/V17/B8/Buy3/Risk-30 | 只记录热度，不进入主榜 |
| SpaceXCoin | BSC | [0xdde2...457777](https://bscscan.com/token/0xdde27483de8c958e4d2657d64eb7551717457777) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 30; Tier Early; LP $142.3K; Vol24H $5.31M; 24H +5509.16%; V/LP 37.29x; 池数 1; 分项 L11/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [Snowball](https://dexscreener.com/solana/aircdeu4yl6hjuina65mtwakzmex7stkzsinmyzhzkt2) | SOL | [9TKbd3...2cpump](https://solscan.io/token/9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 25; Tier Micro; LP $64.3K; Vol24H $1.88M; 24H +7257.00%; V/LP 29.22x; 池数 7; 分项 L7/V16/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| PAIR | SOL | [32rBxc...Kxpump](https://solscan.io/token/32rBxcFjCFnyqZ41CEPM5AL67X1dcw8w83vZt6Kxpump) | 24H未过热但已明显波动；买卖略偏买入；LP未达主观察门槛；24H成交合格；LP偏薄；Volume/LP极端偏高 | Score 19; Tier Micro; LP $15.9K; Vol24H $3.32M; 24H +51.26%; V/LP 208.64x; 池数 1; 分项 L2/V17/B8/Buy8/Risk-40 | 只记录热度，不进入主榜 |
| [Santaball](https://dexscreener.com/solana/fbjukdyu6dedknkum4djqktz5y6u6939xbwwozdqqfzz) | SOL | [4obGGX...d2pump](https://solscan.io/token/4obGGXRMVyqpWZr12UzyaBdNkgdYwz2GiY8enmd2pump) | 买入笔数占优；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP偏高；年轻币短期暴拉 | Score 14; Tier Micro; LP $59.2K; Vol24H $1.17M; 24H +1751.00%; V/LP 19.74x; 池数 6; 分项 L7/V14/B0/Buy12/Risk-43 | 只记录热度，不进入主榜 |
| [Elonmas](https://dexscreener.com/solana/3hzez3ezzsdtzat12pqmzwii8ury9rknjqumsjqywyt7) | SOL | [6B5X3k...6apump](https://solscan.io/token/6B5X3keXJ4J8LLvswa2mbqMhrRDbt85Jo88sbB6apump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 11; Tier Micro; LP $22.2K; Vol24H $1.94M; 24H +180.00%; V/LP 87.42x; 池数 3; 分项 L3/V16/B0/Buy8/Risk-40 | 只记录热度，不进入主榜 |
| [duk](https://dexscreener.com/solana/4xvrevdhqdfum6ffvtmo7fdmeq7zgwxz1jhj7qva68wx) | SOL | [DG2EJS...qupump](https://solscan.io/token/DG2EJSEtPBge5F7zBCTZG78p27LTCiq8tUkJ39qupump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 10; Tier Micro; LP $34.5K; Vol24H $768.5K; 24H +337.00%; V/LP 22.25x; 池数 1; 分项 L5/V13/B0/Buy8/Risk-40 | 只记录热度，不进入主榜 |
| [DragonRiders](https://dexscreener.com/solana/9s1upzzuzppu1qnlpr7vdn8azxxxbxrayetanzv8psar) | SOL | [5xrT8y...yJJCMh](https://solscan.io/token/5xrT8y2KU2YwzipwCMNxxTc8KAGQd4wjtGTc2WyJJCMh) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高；年轻币短期暴拉；非主流报价池 | Score 0; Tier Micro; LP $35.0K; Vol24H $828.0K; 24H +220.00%; V/LP 23.66x; 池数 5; 分项 L5/V13/B0/Buy8/Risk-68 | 只记录热度，不进入主榜 |

### D. 成熟池观察明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| IDOL | BSC | [0x3b4d...25ab07](https://bscscan.com/token/0x3b4de3c7855c03bb9f50ea252cd2c9fa1125ab07) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限 | Score 72; Tier Liquid; LP $1.01M; Vol24H $6.90M; 24H +6.42%; V/LP 6.81x; 池数 1; 分项 L18/V17/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| SPCXB | BSC | [0xbe9d...3103e1](https://bscscan.com/token/0xbe9d156892e55e7154bcd3cb0fea677f9d3103e1) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限 | Score 71; Tier Liquid; LP $906.1K; Vol24H $2.45M; 24H +2.62%; V/LP 2.70x; 池数 1; 分项 L18/V16/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| AIOT | BSC | [0x55ad...21b4a5](https://bscscan.com/token/0x55ad16bd573b3365f43a9daeb0cc66a73821b4a5) | 24H波动可控；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限 | Score 69; Tier Liquid; LP $3.10M; Vol24H $5.27M; 24H +18.07%; V/LP 1.70x; 池数 1; 分项 L20/V17/B17/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| COLLECT | BSC | [0x4b3d...a087d3](https://bscscan.com/token/0x4b3d30992f003c8167699735f5ab2831b2a087d3) | 24H波动可控；LP达主观察门槛；24H成交合格；Volume/LP未失真；卖出笔数占优；FDV超过早期Alpha主榜上限 | Score 66; Tier Liquid; LP $2.50M; Vol24H $6.88M; 24H +21.25%; V/LP 2.75x; 池数 1; 分项 L20/V17/B17/Buy0/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| [SOL](https://dexscreener.com/bsc/0xbffec96e8f3b5058b1817c14e4380758fada01ef) | BSC | [0x570A...fD43dF](https://bscscan.com/token/0x570A5D26f7765Ecb712C0924E4De545B89fD43dF) | 24H接近横盘；LP达主观察门槛；24H成交合格；Volume/LP未失真；卖出笔数占优；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限 | Score 65; Tier Liquid; LP $1.01M; Vol24H $832.1K; 24H +2.44%; V/LP 0.82x; 池数 1; 分项 L18/V13/B22/Buy0/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| [RAY](https://dexscreener.com/solana/avs9ta4nwdzfpje9ggvnjmvhcqy3v9pgazuz33bfg2ra) | SOL | [4k3Dyj...QrkX6R](https://solscan.io/token/4k3Dyjzvzp8eMZWUXbBCjEvwSkkk59S5iCNLY3QrkX6R) | 24H接近横盘；LP达主观察门槛；24H成交合格；Volume/LP未失真；卖出笔数占优；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 61; Tier Liquid; LP $3.58M; Vol24H $91.7K; 24H -0.97%; V/LP 0.03x; 池数 1; 分项 L20/V7/B22/Buy0/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |

### E. 链上确认/紧急精查表
| Token | 链 | 合约地址 | 是否需要链上确认 | 紧急精查 | 预检状态 | 原因 |
|---|---|---|---|---|---|---|
| CATE | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| SPCX | SOL | [SPCXxc...5BimGb](https://solscan.io/token/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| [ANSEM](https://dexscreener.com/solana/fnzky6x7entq1er3d225dqyt7ybfka4pskbmqhb8l3cc) | SOL | [9cRCn9...TGpump](https://solscan.io/token/9cRCn9rGT8V2imeM2BaKs13yhMEais3ruM3rPvTGpump) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| [BPF](https://dexscreener.com/solana/auqgamzwoygpjx9fvtry1i24vywukcxmwrq3zp9symcd) | SOL | [G6wuh4...Mtpump](https://solscan.io/token/G6wuh4ihzeLFtv35r7YX71picr4aga76KphKEMtpump) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| [USEF](https://dexscreener.com/solana/5urqw6moinqmdn7t9v895qyhch2ki61uqrqjfjbracd3) | SOL | [JmBAjh...Tupump](https://solscan.io/token/JmBAjhHKp9btzABS5Eudfxbtg2ipqps2JrFzgTupump) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| [PUMP](https://dexscreener.com/solana/7q2dqbjtxxp4dqmhec2nsgxwsytq8jaxdygswmag3pfp) | SOL | [9593dF...ysD6A1](https://solscan.io/token/9593dFjsLKKRAaz4LX1eK2DDEgrzfu3idb6yvMysD6A1) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| mihao | SOL | [4CxjZy...8spump](https://solscan.io/token/4CxjZyMNoF1p6eXHXHv1TWpS2X47CuUmLwtGe18spump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [CLAUDIA](https://dexscreener.com/solana/fe7bpdycs74gqicuf14hwgumtopkv1d9mdyvx5btohfr) | SOL | [2j5SaS...hnW2ZM](https://solscan.io/token/2j5SaS7xy776qCBpyPQbZjyQSAtKiFgrwjfErthnW2ZM) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [JOB](https://dexscreener.com/solana/hauvbmnthcfmg9srxmvz1gaxnpu955hkpdsasc2cx4c8) | SOL | [9Pq7aL...uypump](https://solscan.io/token/9Pq7aLAbhDG2tTnS22cm6kuysZVcZpLFE368HWuypump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [BRUH](https://dexscreener.com/solana/ehpzesdxtymvwz1iy5nt3lrnjy1xbc1kgqspl1kqnyiv) | SOL | [PgFtGG...hRpump](https://solscan.io/token/PgFtGGquvnv2zEkjG2N2QPvBTBrafuExGYEqahRpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |

### F. 钱包行为 / AVE命中样本表
| Token | 链 | 合约地址 | 行为状态 | 行为层级 | AVE命中 | 判断 |
|---|---|---|---|---|---:|---|
| CATE | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| SPCX | SOL | [SPCXxc...5BimGb](https://solscan.io/token/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| [ANSEM](https://dexscreener.com/solana/fnzky6x7entq1er3d225dqyt7ybfka4pskbmqhb8l3cc) | SOL | [9cRCn9...TGpump](https://solscan.io/token/9cRCn9rGT8V2imeM2BaKs13yhMEais3ruM3rPvTGpump) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| [BPF](https://dexscreener.com/solana/auqgamzwoygpjx9fvtry1i24vywukcxmwrq3zp9symcd) | SOL | [G6wuh4...Mtpump](https://solscan.io/token/G6wuh4ihzeLFtv35r7YX71picr4aga76KphKEMtpump) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| [USEF](https://dexscreener.com/solana/5urqw6moinqmdn7t9v895qyhch2ki61uqrqjfjbracd3) | SOL | [JmBAjh...Tupump](https://solscan.io/token/JmBAjhHKp9btzABS5Eudfxbtg2ipqps2JrFzgTupump) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |

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
| 成熟池观察 | 6 个 | 成熟资产不占早期Alpha主榜 |
| 合约地址覆盖 | 可用 25，缺失 0 | 地址缺失会阻断BSC RPC/Helius精查，需要优先补齐 |
| LP层级 | Micro 6 / Early 9 / Liquid 10 / Mature 0 | 下一步可以按层级分别设置进攻规则 |
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
| dexscreener_boosts | {'ok': True, 'count': 26, 'expanded': 25} |
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