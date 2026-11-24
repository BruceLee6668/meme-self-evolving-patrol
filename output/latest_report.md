# 自我进化轮巡

**本轮时间 UTC：** 2026-11-24T06:40:56Z
**版本：** 0.5.0-ave-cache-wallet-behavior-prep
**S0 时间锚点：** 2026-06-16T16:15:17+09:00

## 一句话结论
本轮从 131 个合并Token中筛出 5 个主观察候选。v0.5已在v0.4.1基础上增加AVE周缓存真实接口接入框架、Smart Wallet持久保存、wallet_behavior_latest.json，以及BSC Transfer级钱包行为样本。注意：BSC当前是Transfer样本，不等同完整Swap解码。
合约地址可用 25 个，缺失 0 个；缺失地址的候选不能进入后续链上精查。

## 本轮扫描摘要
| 指标 | 数量 |
|---|---:|
| 原始池子记录 | 211 |
| 合并后Token | 131 |
| 输出候选 | 25 |
| 主观察 | 5 |
| 次观察 | 6 |
| PVP风险池 | 8 |
| 成熟池观察 | 6 |
| 低优先观察 | 0 |
| 多池Token | 8 |
| 多池冲突 | 2 |
| Symbol桥接合并 | 2 |
| 合约地址可用 | 25 |
| 合约地址缺失 | 0 |
| Micro层 | 4 |
| Early层 | 12 |
| Liquid层 | 8 |
| Mature层 | 1 |
| 需要链上确认 | 19 |
| 紧急精查候选 | 7 |

## v0.5 数据确认状态
| 项目 | 状态 |
|---|---|
| AVE Smart Wallet周缓存 | active，钱包数 2927，刷新时间 2026-11-23T04:56:43Z，是否过期 否 |
| 链上预检 | 本轮检查 12 个，验证通过 12 个，失败 0 个 |
| Helius状态 | 未配置，SOL使用公共RPC或跳过增强解析 |
| 当前精查层级 | 0.5.0-chain-preflight-plus-wallet-behavior：地址/账户预检 + v0.5钱包行为样本，完整Swap留存仍待下一版 |
| 钱包行为样本 | 本轮检查 7 个，BSC Transfer样本 1 个，SOL签名级 6 个，AVE钱包命中 0 个 |

## 第一部分：生成结果表格

### A. 上次记录结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| CATE | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | 主观察 | Score 90; Tier Liquid; LP $1.31M; Vol24H $869.2K; 24H -4.26%; V/LP 0.66x; 池数 2; 分项 L19/V13/B22/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| mubarak | BSC | [0x5c85...6b46f6](https://bscscan.com/token/0x5c85d6c6825ab4032337f11ee92a72df936b46f6) | 主观察 | Score 86; Tier Liquid; LP $1.81M; Vol24H $2.76M; 24H +24.10%; V/LP 1.52x; 池数 1; 分项 L20/V17/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [TROLL](https://dexscreener.com/solana/4w2cysotx6czaugmmwg13hdpy4qemg2czekyeqyk9ama) | SOL | [5UUH9R...TBhgH2](https://solscan.io/token/5UUH9RTDiSpq6HKS6bp4NdU9PNJpXRXuiw6ShBTBhgH2) | 主观察 | Score 85; Tier Liquid; LP $1.83M; Vol24H $429.7K; 24H +2.21%; V/LP 0.23x; 池数 1; 分项 L20/V11/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| mihao | SOL | [4CxjZy...8spump](https://solscan.io/token/4CxjZyMNoF1p6eXHXHv1TWpS2X47CuUmLwtGe18spump) | 主观察 | Score 82; Tier Early; LP $348.0K; Vol24H $1.21M; 24H +0.18%; V/LP 3.48x; 池数 2; 分项 L14/V14/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| SI | SOL | [DEW9dS...i98WDP](https://solscan.io/token/DEW9dSN6QpWyNthphCpMmAbZP1Q4cEKR9xQXAri98WDP) | 主观察 | Score 81; Tier Early; LP $350.8K; Vol24H $896.0K; 24H +0.12%; V/LP 2.55x; 池数 2; 分项 L14/V13/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| CLAUDIA | SOL | [2j5SaS...hnW2ZM](https://solscan.io/token/2j5SaS7xy776qCBpyPQbZjyQSAtKiFgrwjfErthnW2ZM) | 次观察 | Score 78; Tier Early; LP $445.7K; Vol24H $1.03M; 24H -17.19%; V/LP 2.31x; 池数 2; 分项 L15/V14/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 次观察，不直接进攻 |
| [GATO](https://dexscreener.com/solana/5e3dxlxgwmtdcoka51wyyakttjfzbwqcoyuhbui5gt2m) | SOL | [HsprHx...k6pump](https://solscan.io/token/HsprHxBRgiVaQdRf3TnKNuZZtaX9JUSPgMFdAkk6pump) | 次观察 | Score 67; Tier Early; LP $145.1K; Vol24H $117.4K; 24H -3.60%; V/LP 0.81x; 池数 1; 分项 L11/V7/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| IDOL | BSC | [0x3b4d...25ab07](https://bscscan.com/token/0x3b4de3c7855c03bb9f50ea252cd2c9fa1125ab07) | 次观察 | Score 66; Tier Liquid; LP $968.9K; Vol24H $11.63M; 24H +5.16%; V/LP 12.01x; 池数 1; 分项 L18/V17/B22/Buy3/Risk-18 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [CBUCKS](https://dexscreener.com/solana/b4cp45pgifvm5faxfh6aev8qz3eunqnqgbw7kuc7mhnb) | SOL | [DtcicP...xZpump](https://solscan.io/token/DtcicPCKTKeAh7TDEzTym3hXeoHAoMiBdYJhMYxZpump) | 次观察 | Score 64; Tier Early; LP $234.6K; Vol24H $102.5K; 24H +12.88%; V/LP 0.44x; 池数 1; 分项 L13/V7/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [UCASH](https://dexscreener.com/solana/4h7r5jzaq6pgnjfud12aeuqjrqygwz2yhpsra6sh1rxt) | SOL | [7cFiqd...sspump](https://solscan.io/token/7cFiqdT46zs7ooHWLFiLSaSQKLMibtokh9dBinsspump) | PVP风险池 | Score 54; Tier Micro; LP $91.4K; Vol24H $4.89M; 24H -2.00%; V/LP 53.45x; 池数 1; 分项 L9/V17/B22/Buy12/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### B. 本轮扫描结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| CATE | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | 主观察 | Score 86; Tier Liquid; LP $1.32M; Vol24H $842.5K; 24H -7.02%; V/LP 0.64x; 池数 2; 分项 L19/V13/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| mubarak | BSC | [0x5c85...6b46f6](https://bscscan.com/token/0x5c85d6c6825ab4032337f11ee92a72df936b46f6) | 主观察 | Score 86; Tier Liquid; LP $1.76M; Vol24H $3.28M; 24H +16.57%; V/LP 1.87x; 池数 1; 分项 L20/V17/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| NVDA | SOL | [NVDAVu...KFxNjv](https://solscan.io/token/NVDAVuiB7hwd3m5Wa1JuHNovPaPG6BH1QNztbKFxNjv) | 主观察 | Score 83; Tier Early; LP $712.7K; Vol24H $5.42M; 24H +21.61%; V/LP 7.61x; 池数 1; 分项 L17/V17/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [TROLL](https://dexscreener.com/solana/4w2cysotx6czaugmmwg13hdpy4qemg2czekyeqyk9ama) | SOL | [5UUH9R...TBhgH2](https://solscan.io/token/5UUH9RTDiSpq6HKS6bp4NdU9PNJpXRXuiw6ShBTBhgH2) | 主观察 | Score 82; Tier Liquid; LP $1.78M; Vol24H $808.4K; 24H -8.75%; V/LP 0.45x; 池数 1; 分项 L20/V13/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| SI | SOL | [DEW9dS...i98WDP](https://solscan.io/token/DEW9dSN6QpWyNthphCpMmAbZP1Q4cEKR9xQXAri98WDP) | 主观察 | Score 81; Tier Early; LP $333.6K; Vol24H $695.0K; 24H -1.25%; V/LP 2.08x; 池数 1; 分项 L14/V13/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [BPF](https://dexscreener.com/solana/auqgamzwoygpjx9fvtry1i24vywukcxmwrq3zp9symcd) | SOL | [G6wuh4...Mtpump](https://solscan.io/token/G6wuh4ihzeLFtv35r7YX71picr4aga76KphKEMtpump) | 次观察 | Score 77; Tier Early; LP $352.8K; Vol24H $176.9K; 24H +7.70%; V/LP 0.50x; 池数 1; 分项 L14/V9/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 次观察，不直接进攻 |
| [USEF](https://dexscreener.com/solana/5urqw6moinqmdn7t9v895qyhch2ki61uqrqjfjbracd3) | SOL | [JmBAjh...Tupump](https://solscan.io/token/JmBAjhHKp9btzABS5Eudfxbtg2ipqps2JrFzgTupump) | 次观察 | Score 77; Tier Early; LP $326.1K; Vol24H $176.1K; 24H +7.53%; V/LP 0.54x; 池数 1; 分项 L14/V9/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 次观察，不直接进攻 |
| [mihao](https://dexscreener.com/solana/ho1asg6wgh1ffxdehrk2f4ggt1hoxo9s5jclmdqeyebz) | SOL | [4CxjZy...8spump](https://solscan.io/token/4CxjZyMNoF1p6eXHXHv1TWpS2X47CuUmLwtGe18spump) | 次观察 | Score 72; Tier Early; LP $320.6K; Vol24H $1.16M; 24H -13.78%; V/LP 3.63x; 池数 2; 分项 L14/V14/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [CLAUDIA](https://dexscreener.com/solana/fe7bpdycs74gqicuf14hwgumtopkv1d9mdyvx5btohfr) | SOL | [2j5SaS...hnW2ZM](https://solscan.io/token/2j5SaS7xy776qCBpyPQbZjyQSAtKiFgrwjfErthnW2ZM) | 次观察 | Score 72; Tier Early; LP $441.1K; Vol24H $756.7K; 24H -15.23%; V/LP 1.72x; 池数 2; 分项 L15/V13/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [HOGE](https://dexscreener.com/solana/7cnc9ggegzeffk8flxiyuhdtmeefpqzond56u1mxhnor) | SOL | [FVzqGq...fopump](https://solscan.io/token/FVzqGqRmr4UH1Fif6dewmwbJ1p4YUZCu8dcw4Efopump) | 次观察 | Score 65; Tier Early; LP $113.1K; Vol24H $409.0K; 24H +15.98%; V/LP 3.61x; 池数 1; 分项 L10/V11/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [EXFIL](https://dexscreener.com/solana/2zpfdgd48k7b2u9yqz4hjspaptovu9uiebfqyxeoexkv) | SOL | [6FhVPc...y6pump](https://solscan.io/token/6FhVPctYg363pQbs4iSvqyHe2cJzfsvFD96gePy6pump) | 次观察 | Score 64; Tier Early; LP $115.7K; Vol24H $60.4K; 24H -2.31%; V/LP 0.52x; 池数 1; 分项 L10/V5/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| EVAA | BSC | [0xaa03...a628c1](https://bscscan.com/token/0xaa036928c9c0df07d525b55ea8ee690bb5a628c1) | PVP风险池 | Score 44; Tier Early; LP $240.5K; Vol24H $7.19M; 24H -18.91%; V/LP 29.92x; 池数 1; 分项 L13/V17/B17/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [JENSEN](https://dexscreener.com/solana/dqpqkbbqr3wmty5ryjoq3nzrrzwbh7h9x2gj7osn9mhh) | SOL | [HKiMA2...fmpump](https://solscan.io/token/HKiMA2mKQHU2cjfZ4Kbmru5GBGCauSNqPtpu8cfmpump) | PVP风险池 | Score 29; Tier Micro; LP $52.0K; Vol24H $2.37M; 24H +453.00%; V/LP 45.62x; 池数 8; 分项 L7/V16/B0/Buy12/Risk-30 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [COPIUM](https://dexscreener.com/solana/8rjw3dbbzfzkyf5tinesjqpyjtepzg8dz7dnb2sebupp) | SOL | [BAKsQr...q7pump](https://solscan.io/token/BAKsQrynzwadyACDMsg3J5R8a4CTvj1u7kEYyjq7pump) | PVP风险池 | Score 27; Tier Micro; LP $63.6K; Vol24H $1.36M; 24H +31.73%; V/LP 21.34x; 池数 1; 分项 L7/V15/B8/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [UCASH](https://dexscreener.com/solana/4h7r5jzaq6pgnjfud12aeuqjrqygwz2yhpsra6sh1rxt) | SOL | [7cFiqd...sspump](https://solscan.io/token/7cFiqdT46zs7ooHWLFiLSaSQKLMibtokh9dBinsspump) | PVP风险池 | Score 18; Tier Micro; LP $34.0K; Vol24H $4.98M; 24H -83.27%; V/LP 146.30x; 池数 2; 分项 L5/V17/B0/Buy12/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### C. PVP风险池明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| EVAA | BSC | [0xaa03...a628c1](https://bscscan.com/token/0xaa036928c9c0df07d525b55ea8ee690bb5a628c1) | 24H波动可控；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 44; Tier Early; LP $240.5K; Vol24H $7.19M; 24H -18.91%; V/LP 29.92x; 池数 1; 分项 L13/V17/B17/Buy3/Risk-30 | 只记录热度，不进入主榜 |
| [JENSEN](https://dexscreener.com/solana/dqpqkbbqr3wmty5ryjoq3nzrrzwbh7h9x2gj7osn9mhh) | SOL | [HKiMA2...fmpump](https://solscan.io/token/HKiMA2mKQHU2cjfZ4Kbmru5GBGCauSNqPtpu8cfmpump) | 买入笔数占优；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 29; Tier Micro; LP $52.0K; Vol24H $2.37M; 24H +453.00%; V/LP 45.62x; 池数 8; 分项 L7/V16/B0/Buy12/Risk-30 | 只记录热度，不进入主榜 |
| [COPIUM](https://dexscreener.com/solana/8rjw3dbbzfzkyf5tinesjqpyjtepzg8dz7dnb2sebupp) | SOL | [BAKsQr...q7pump](https://solscan.io/token/BAKsQrynzwadyACDMsg3J5R8a4CTvj1u7kEYyjq7pump) | 24H未过热但已明显波动；买卖基本均衡；LP未达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 27; Tier Micro; LP $63.6K; Vol24H $1.36M; 24H +31.73%; V/LP 21.34x; 池数 1; 分项 L7/V15/B8/Buy3/Risk-30 | 只记录热度，不进入主榜 |
| [UCASH](https://dexscreener.com/solana/4h7r5jzaq6pgnjfud12aeuqjrqygwz2yhpsra6sh1rxt) | SOL | [7cFiqd...sspump](https://solscan.io/token/7cFiqdT46zs7ooHWLFiLSaSQKLMibtokh9dBinsspump) | 买入笔数占优；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 18; Tier Micro; LP $34.0K; Vol24H $4.98M; 24H -83.27%; V/LP 146.30x; 池数 2; 分项 L5/V17/B0/Buy12/Risk-40 | 只记录热度，不进入主榜 |
| [GROKIA](https://dexscreener.com/solana/cpfb8ptvj8uzu55nkj6sx4kmv6zve7j2t3c22mlgcvgg) | SOL | [3cL47o...dXpump](https://solscan.io/token/3cL47ohWa2HApLYKtqPsqkjaxJ6HLvT5Ri1KvWdXpump) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP偏高；年轻币短期暴拉 | Score 15; Tier Early; LP $133.0K; Vol24H $2.07M; 24H +2729.00%; V/LP 15.56x; 池数 1; 分项 L10/V16/B0/Buy8/Risk-43 | 只记录热度，不进入主榜 |
| [JIMMY](https://dexscreener.com/solana/fnhwfv49ywctgcdtyf34avn8bixxcgxukqlctkrkp1gq) | SOL | [38M2z4...Nipump](https://solscan.io/token/38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 14; Tier Micro; LP $48.2K; Vol24H $2.09M; 24H +1162.00%; V/LP 43.38x; 池数 2; 分项 L6/V16/B0/Buy8/Risk-40 | 只记录热度，不进入主榜 |
| [JENSEN](https://dexscreener.com/bsc/0x32bb631bf965dd9fdeecbd99f1da0d2d1daab227) | BSC | [0xf22d...5112e2](https://bscscan.com/token/0xf22deE3117c836Ef2A5728a00AFc00D34F5112e2) | 买入笔数占优；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高；年轻币短期暴拉 | Score 12; Tier Early; LP $361.1K; Vol24H $13.13M; 24H +25860.00%; V/LP 36.36x; 池数 1; 分项 L14/V17/B0/Buy12/Risk-55 | 只记录热度，不进入主榜 |
| [DONJENSEN](https://dexscreener.com/solana/7v3yununayz6kwbaxjsd3txnk2wt92q18zjib677nnso) | SOL | [5LDows...1bpump](https://solscan.io/token/5LDowscYVD3a6ZS4m8gCqG5nU16eLTwRXhciFi1bpump) | 买卖基本均衡；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP偏高；年轻币短期暴拉 | Score 7; Tier Early; LP $101.3K; Vol24H $1.03M; 24H +5377.00%; V/LP 10.12x; 池数 5; 分项 L9/V14/B0/Buy3/Risk-43 | 只记录热度，不进入主榜 |

### D. 成熟池观察明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| [RAY](https://dexscreener.com/solana/2axxcn6on9bbt5owwmth53c7qhuxvhleu718kqt8rvy2) | SOL | [4k3Dyj...QrkX6R](https://solscan.io/token/4k3Dyjzvzp8eMZWUXbBCjEvwSkkk59S5iCNLY3QrkX6R) | 24H接近横盘；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 79; Tier Liquid; LP $1.43M; Vol24H $2.61M; 24H +2.22%; V/LP 1.83x; 池数 1; 分项 L20/V17/B22/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| ARIA | BSC | [0x5d3a...555238](https://bscscan.com/token/0x5d3a12c42e5372b2cc3264ab3cdcf660a1555238) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；成熟大市值 | Score 74; Tier Liquid; LP $2.20M; Vol24H $14.66M; 24H +7.06%; V/LP 6.68x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| Q | BSC | [0xc07e...690589](https://bscscan.com/token/0xc07e1300dc138601fa6b0b59f8d0fa477e690589) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 73; Tier Liquid; LP $1.06M; Vol24H $2.82M; 24H -3.07%; V/LP 2.67x; 池数 1; 分项 L19/V17/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| TRUMP | SOL | [6p6xgH...jfGiPN](https://solscan.io/token/6p6xgHyF7AeE6TZkSmFsko444wqoP15icUSqi2jfGiPN) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 73; Tier Liquid; LP $3.80M; Vol24H $2.29M; 24H -3.65%; V/LP 0.60x; 池数 1; 分项 L20/V16/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| [SOL](https://dexscreener.com/bsc/0xbffec96e8f3b5058b1817c14e4380758fada01ef) | BSC | [0x570A...fD43dF](https://bscscan.com/token/0x570A5D26f7765Ecb712C0924E4De545B89fD43dF) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限 | Score 71; Tier Liquid; LP $994.8K; Vol24H $1.97M; 24H -0.12%; V/LP 1.98x; 池数 1; 分项 L18/V16/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| PUMP | SOL | [pumpCm...7H9Dfn](https://solscan.io/token/pumpCmXqMfrsAkQ5r49WcJnRayYRqmXz6ae8H7H9Dfn) | 24H接近横盘；LP达主观察门槛；24H成交合格；Volume/LP未失真；卖出笔数占优；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 71; Tier Mature; LP $18.04M; Vol24H $4.00M; 24H -2.63%; V/LP 0.22x; 池数 2; 分项 L20/V17/B22/Buy0/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |

### E. 链上确认/紧急精查表
| Token | 链 | 合约地址 | 是否需要链上确认 | 紧急精查 | 预检状态 | 原因 |
|---|---|---|---|---|---|---|
| CATE | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| mubarak | BSC | [0x5c85...6b46f6](https://bscscan.com/token/0x5c85d6c6825ab4032337f11ee92a72df936b46f6) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| NVDA | SOL | [NVDAVu...KFxNjv](https://solscan.io/token/NVDAVuiB7hwd3m5Wa1JuHNovPaPG6BH1QNztbKFxNjv) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| [TROLL](https://dexscreener.com/solana/4w2cysotx6czaugmmwg13hdpy4qemg2czekyeqyk9ama) | SOL | [5UUH9R...TBhgH2](https://solscan.io/token/5UUH9RTDiSpq6HKS6bp4NdU9PNJpXRXuiw6ShBTBhgH2) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| SI | SOL | [DEW9dS...i98WDP](https://solscan.io/token/DEW9dSN6QpWyNthphCpMmAbZP1Q4cEKR9xQXAri98WDP) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| [BPF](https://dexscreener.com/solana/auqgamzwoygpjx9fvtry1i24vywukcxmwrq3zp9symcd) | SOL | [G6wuh4...Mtpump](https://solscan.io/token/G6wuh4ihzeLFtv35r7YX71picr4aga76KphKEMtpump) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| [USEF](https://dexscreener.com/solana/5urqw6moinqmdn7t9v895qyhch2ki61uqrqjfjbracd3) | SOL | [JmBAjh...Tupump](https://solscan.io/token/JmBAjhHKp9btzABS5Eudfxbtg2ipqps2JrFzgTupump) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| [mihao](https://dexscreener.com/solana/ho1asg6wgh1ffxdehrk2f4ggt1hoxo9s5jclmdqeyebz) | SOL | [4CxjZy...8spump](https://solscan.io/token/4CxjZyMNoF1p6eXHXHv1TWpS2X47CuUmLwtGe18spump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [CLAUDIA](https://dexscreener.com/solana/fe7bpdycs74gqicuf14hwgumtopkv1d9mdyvx5btohfr) | SOL | [2j5SaS...hnW2ZM](https://solscan.io/token/2j5SaS7xy776qCBpyPQbZjyQSAtKiFgrwjfErthnW2ZM) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [HOGE](https://dexscreener.com/solana/7cnc9ggegzeffk8flxiyuhdtmeefpqzond56u1mxhnor) | SOL | [FVzqGq...fopump](https://solscan.io/token/FVzqGqRmr4UH1Fif6dewmwbJ1p4YUZCu8dcw4Efopump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |

### F. 钱包行为 / AVE命中样本表
| Token | 链 | 合约地址 | 行为状态 | 行为层级 | AVE命中 | 判断 |
|---|---|---|---|---|---:|---|
| CATE | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| mubarak | BSC | [0x5c85...6b46f6](https://bscscan.com/token/0x5c85d6c6825ab4032337f11ee92a72df936b46f6) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| NVDA | SOL | [NVDAVu...KFxNjv](https://solscan.io/token/NVDAVuiB7hwd3m5Wa1JuHNovPaPG6BH1QNztbKFxNjv) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| [TROLL](https://dexscreener.com/solana/4w2cysotx6czaugmmwg13hdpy4qemg2czekyeqyk9ama) | SOL | [5UUH9R...TBhgH2](https://solscan.io/token/5UUH9RTDiSpq6HKS6bp4NdU9PNJpXRXuiw6ShBTBhgH2) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| SI | SOL | [DEW9dS...i98WDP](https://solscan.io/token/DEW9dSN6QpWyNthphCpMmAbZP1Q4cEKR9xQXAri98WDP) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
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
| dexscreener_boosts | {'ok': True, 'count': 20, 'expanded': 20} |
| dexscreener_search | {'ok': True, 'count': 333} |
| geckoterminal_bsc_trending | {'ok': True, 'count': 20} |
| geckoterminal_solana_trending | {'ok': True, 'count': 20} |

## 数据限制
- This v0.4 scan uses free public sources plus lightweight chain address/account preflight when enabled.
- AVE Smart Money weekly cache structure is connected; real AVE API refresh is handled by the weekly workflow/cache file.
- S0 exact historical replay is not implemented yet; candidates are marked with current metrics only.
- Wallet-level buy/sell retention is not implemented yet; v0.4 only preflights token contract/account existence.
- v0.4 adds chain preflight status and Smart Wallet cache status on top of contract-address output, liquidity tiers, visible PVP/mature detail tables, and chain-verify flags.
- Contract addresses are extracted from DEXScreener baseToken or GeckoTerminal relationships when available; missing addresses are explicitly marked unavailable.