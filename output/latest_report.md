# 自我进化轮巡

**本轮时间 UTC：** 2026-07-01T19:46:01Z
**版本：** 0.5.0-ave-cache-wallet-behavior-prep
**S0 时间锚点：** 2026-06-16T16:15:17+09:00

## 一句话结论
本轮从 131 个合并Token中筛出 2 个主观察候选。v0.5已在v0.4.1基础上增加AVE周缓存真实接口接入框架、Smart Wallet持久保存、wallet_behavior_latest.json，以及BSC Transfer级钱包行为样本。注意：BSC当前是Transfer样本，不等同完整Swap解码。
合约地址可用 25 个，缺失 0 个；缺失地址的候选不能进入后续链上精查。

## 本轮扫描摘要
| 指标 | 数量 |
|---|---:|
| 原始池子记录 | 308 |
| 合并后Token | 131 |
| 输出候选 | 25 |
| 主观察 | 2 |
| 次观察 | 5 |
| PVP风险池 | 8 |
| 成熟池观察 | 8 |
| 低优先观察 | 2 |
| 多池Token | 10 |
| 多池冲突 | 4 |
| Symbol桥接合并 | 3 |
| 合约地址可用 | 25 |
| 合约地址缺失 | 0 |
| Micro层 | 5 |
| Early层 | 7 |
| Liquid层 | 9 |
| Mature层 | 4 |
| 需要链上确认 | 17 |
| 紧急精查候选 | 1 |

## v0.5 数据确认状态
| 项目 | 状态 |
|---|---|
| AVE Smart Wallet周缓存 | active，钱包数 406，刷新时间 2026-06-29T02:42:54Z，是否过期 否 |
| 链上预检 | 本轮检查 12 个，验证通过 12 个，失败 0 个 |
| Helius状态 | 未配置，SOL使用公共RPC或跳过增强解析 |
| 当前精查层级 | 0.5.0-chain-preflight-plus-wallet-behavior：地址/账户预检 + v0.5钱包行为样本，完整Swap留存仍待下一版 |
| 钱包行为样本 | 本轮检查 2 个，BSC Transfer样本 1 个，SOL签名级 1 个，AVE钱包命中 0 个 |

## 第一部分：生成结果表格

### A. 上次记录结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| ARX | BSC | [0xd5f6...1ca715](https://bscscan.com/token/0xd5f6ef5deabe61e6d5cdb49bfb6f156f2c1ca715) | 主观察 | Score 86; Tier Liquid; LP $1.41M; Vol24H $10.67M; 24H -3.20%; V/LP 7.57x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [SON](https://dexscreener.com/solana/ec9rk1gqmn4d7tjp2efx6m1on1rmxxr5gh4pkswjqskx) | SOL | [ACpzkG...Nppump](https://solscan.io/token/ACpzkGJV3DDU8HXy8yjab7RL9qNmDGym2GwLkzNppump) | 主观察 | Score 80; Tier Early; LP $113.6K; Vol24H $545.9K; 24H -5.50%; V/LP 4.80x; 池数 1; 分项 L10/V12/B22/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [TOESCOIN](https://dexscreener.com/solana/ee3zk9fxp9guair2xerefxf4tsexezffuwetrna2pkcv) | SOL | [6ehEcT...HDpump](https://solscan.io/token/6ehEcTMCc85aNF4x9CWx8HuvWGhxQtvKdhKVf2HDpump) | 次观察 | Score 74; Tier Early; LP $357.3K; Vol24H $2.11M; 24H +28.23%; V/LP 5.91x; 池数 2; 分项 L14/V16/B8/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [CS](https://dexscreener.com/solana/c3hajo5hfxwcgsoxzeqsqzbtfhcdxujb4qna4aqpq6xg) | SOL | [9qwxah...topump](https://solscan.io/token/9qwxahBxcgKyn5X7kZvkN7qxKZg6pkVD8Lo4URtopump) | 次观察 | Score 73; Tier Micro; LP $78.4K; Vol24H $342.7K; 24H +4.60%; V/LP 4.37x; 池数 1; 分项 L8/V11/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [VIN](https://dexscreener.com/bsc/0xde52cff316d8a70256bee647073312c1aa7ee2cf) | BSC | [0x85E4...06a988](https://bscscan.com/token/0x85E43bF8faAF04ceDdcD03d6C07438b72606a988) | 次观察 | Score 73; Tier Liquid; LP $1.14M; Vol24H $894.8K; 24H +59.77%; V/LP 0.78x; 池数 1; 分项 L19/V13/B8/Buy12/Risk-3 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [BULLWIF](https://dexscreener.com/solana/fxfml53napn8w5l7xqgaxachu7akfqo96eztnqjki59m) | SOL | [5npesG...appump](https://solscan.io/token/5npesGsnVhcQbh6oVcsLtn5UKqdgYeipgDKsGaappump) | 次观察 | Score 72; Tier Micro; LP $63.5K; Vol24H $348.2K; 24H +5.20%; V/LP 5.48x; 池数 10; 分项 L7/V11/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [YFSX](https://dexscreener.com/bsc/0x570e2162d9ba3000a088ea1680e21616d177b7c0) | BSC | [0xB7eC...f27388](https://bscscan.com/token/0xB7eC60CF8EF96eD48b119277BC7a954A87f27388) | 次观察 | Score 72; Tier Early; LP $206.1K; Vol24H $194.1K; 24H +7.97%; V/LP 0.94x; 池数 1; 分项 L12/V9/B22/Buy8/Risk-3 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [ㅤ](https://dexscreener.com/solana/pai8kyevjjx7ukbxrrqhvwnpsqu1nqpbsvffddykgt2) | SOL | [FCGtC4...9cNZih](https://solscan.io/token/FCGtC4AXSyLGRfS4rceiFAparP9sikH4DTKSxZ9cNZih) | 次观察 | Score 70; Tier Liquid; LP $2.12M; Vol24H $1.1K; 24H +0.00%; V/LP 0.00x; 池数 2; 分项 L20/V0/B22/Buy12/Risk-8 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [memecoin](https://dexscreener.com/solana/ebpudz8eke1tavcrasmaaegzk3wjveesrxmidmxuyxay) | SOL | [Bb4jR9...d7pump](https://solscan.io/token/Bb4jR951QtVjeFAYFLBYXDSMKjbTDroCLPbFLdd7pump) | 次观察 | Score 67; Tier Early; LP $222.1K; Vol24H $66.9K; 24H -0.22%; V/LP 0.30x; 池数 14; 分项 L12/V6/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [MANIFEST](https://dexscreener.com/solana/2dvbu5h8jcd37gaxajuz4t77hsjjw22lldutzk7gsa43) | SOL | [BCdwQB...ERpump](https://solscan.io/token/BCdwQBAn8dYB5YjTsoB6TdHAWokxv28k2oZUodERpump) | 次观察 | Score 66; Tier Liquid; LP $852.0K; Vol24H $2.09M; 24H +25.71%; V/LP 2.45x; 池数 1; 分项 L18/V16/B8/Buy0/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |

### B. 本轮扫描结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| TOESCOIN | SOL | [6ehEcT...HDpump](https://solscan.io/token/6ehEcTMCc85aNF4x9CWx8HuvWGhxQtvKdhKVf2HDpump) | 主观察 | Score 83; Tier Early; LP $346.5K; Vol24H $2.26M; 24H +14.47%; V/LP 6.52x; 池数 2; 分项 L14/V16/B17/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| ARX | BSC | [0xd5f6...1ca715](https://bscscan.com/token/0xd5f6ef5deabe61e6d5cdb49bfb6f156f2c1ca715) | 主观察 | Score 81; Tier Liquid; LP $1.38M; Vol24H $9.91M; 24H -13.24%; V/LP 7.20x; 池数 1; 分项 L20/V17/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| KINS | SOL | [Tqj8yF...9bpump](https://solscan.io/token/Tqj8yFmagrg7oorpQkVGYR52r96RFTamvWfth9bpump) | 次观察 | Score 73; Tier Early; LP $460.8K; Vol24H $1.20M; 24H +20.52%; V/LP 2.61x; 池数 1; 分项 L15/V14/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [RTM](https://dexscreener.com/solana/ebnuexqpb5wjkxjsfm3ruft7zb7zbxhzgr7ydhyuvuyy) | SOL | [3d1qHS...XCDM6u](https://solscan.io/token/3d1qHSAkQhoN7kN1C6tvpAArCkXWxwYdBng6taXCDM6u) | 次观察 | Score 72; Tier Early; LP $127.6K; Vol24H $926.9K; 24H -0.95%; V/LP 7.27x; 池数 4; 分项 L10/V13/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [ㅤ](https://dexscreener.com/solana/pai8kyevjjx7ukbxrrqhvwnpsqu1nqpbsvffddykgt2) | SOL | [FCGtC4...9cNZih](https://solscan.io/token/FCGtC4AXSyLGRfS4rceiFAparP9sikH4DTKSxZ9cNZih) | 次观察 | Score 70; Tier Liquid; LP $2.12M; Vol24H $1.1K; 24H +0.00%; V/LP 0.00x; 池数 3; 分项 L20/V0/B22/Buy12/Risk-8 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [TripleT](https://dexscreener.com/solana/3kfcgj5r3zshw8htdbzjsrrksrymkvsmfhc4vo4iddxd) | SOL | [J8PSdN...KZpump](https://solscan.io/token/J8PSdNP3QewKq2Z1JJJFDMaqF7KcaiJhR7gbr5KZpump) | 次观察 | Score 66; Tier Early; LP $559.1K; Vol24H $1.31M; 24H +38.36%; V/LP 2.34x; 池数 1; 分项 L16/V15/B8/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [memecoin](https://dexscreener.com/solana/ebpudz8eke1tavcrasmaaegzk3wjveesrxmidmxuyxay) | SOL | [Bb4jR9...d7pump](https://solscan.io/token/Bb4jR951QtVjeFAYFLBYXDSMKjbTDroCLPbFLdd7pump) | 次观察 | Score 66; Tier Early; LP $223.5K; Vol24H $58.7K; 24H +0.03%; V/LP 0.26x; 池数 13; 分项 L12/V5/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| BASED | BSC | [0x1d28...958e4d](https://bscscan.com/token/0x1d28d989f9e3ccb8b15d0cec601734514f958e4d) | PVP风险池 | Score 42; Tier Liquid; LP $1.42M; Vol24H $39.54M; 24H +28.49%; V/LP 27.90x; 池数 1; 分项 L20/V17/B8/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| NES | BSC | [0x3131...ac3fb5](https://bscscan.com/token/0x3131f6b80c26936ab03f7d9d29eb4ddf36ac3fb5) | PVP风险池 | Score 39; Tier Liquid; LP $1.34M; Vol24H $95.10M; 24H +19.13%; V/LP 70.92x; 池数 1; 分项 L20/V17/B17/Buy3/Risk-42 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [OCCAM](https://dexscreener.com/solana/6tbpwlernnkeswwwt6rwa5lxjfekpuvfkzyrgmckuess) | SOL | [41y7bE...2gpump](https://solscan.io/token/41y7bEjuidUJTZJ7mbfqzKjNcBiecYvjnyPwCb2gpump) | PVP风险池 | Score 30; Tier Early; LP $158.3K; Vol24H $10.63M; 24H +632.00%; V/LP 67.11x; 池数 1; 分项 L11/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [world](https://dexscreener.com/solana/ewrxs61yb2swiangqcbg9vgerkwdz3fxxwtyz2kfvbm8) | SOL | [FMqh9m...aJpump](https://solscan.io/token/FMqh9mqR6drPZqqW6wPqLHxX4rqNDWGhYLaMfoaJpump) | PVP风险池 | Score 27; Tier Early; LP $288.0K; Vol24H $7.72M; 24H +119.00%; V/LP 26.82x; 池数 2; 分项 L13/V17/B0/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [Horseradish](https://dexscreener.com/solana/2pcbimrflvuklgb394xmmfrcb82bu7utluphs8wbw6vz) | SOL | [GAefbs...xFpump](https://solscan.io/token/GAefbsZef5zGjacXf65ioie8gzHEnS9xzSWNZsxFpump) | PVP风险池 | Score 14; Tier Micro; LP $32.0K; Vol24H $2.69M; 24H +372.00%; V/LP 83.95x; 池数 2; 分项 L5/V17/B0/Buy8/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| FABLE | SOL | [498DeY...DDpump](https://solscan.io/token/498DeYRS7AtLdE5wbwXbpFtinMTDTJxuvfXMraDDpump) | PVP风险池 | Score 13; Tier Micro; LP $31.7K; Vol24H $2.01M; 24H +350.51%; V/LP 63.54x; 池数 2; 分项 L5/V16/B0/Buy8/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [FROGBULL](https://dexscreener.com/solana/gkgwpmtt7jcwzf4pxtzqq4zjcryeppz2mmj4y3xegzrb) | SOL | [BDbNwA...p6pump](https://solscan.io/token/BDbNwA95183CdqUhx2P6R3fWXbefubVbx2wNnCp6pump) | PVP风险池 | Score 11; Tier Micro; LP $76.0K; Vol24H $1.18M; 24H +2992.00%; V/LP 15.47x; 池数 1; 分项 L8/V14/B0/Buy8/Risk-43 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| ZAYED | SOL | [6XUkLa...THpump](https://solscan.io/token/6XUkLa8fbTzRUkGotni7UtkG4EHtUFe8qPhJU5THpump) | PVP风险池 | Score 6; Tier Micro; LP $7.1K; Vol24H $1.11M; 24H -98.22%; V/LP 154.96x; 池数 1; 分项 L0/V14/B0/Buy8/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### C. PVP风险池明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| BASED | BSC | [0x1d28...958e4d](https://bscscan.com/token/0x1d28d989f9e3ccb8b15d0cec601734514f958e4d) | 24H未过热但已明显波动；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 42; Tier Liquid; LP $1.42M; Vol24H $39.54M; 24H +28.49%; V/LP 27.90x; 池数 1; 分项 L20/V17/B8/Buy3/Risk-30 | 只记录热度，不进入主榜 |
| NES | BSC | [0x3131...ac3fb5](https://bscscan.com/token/0x3131f6b80c26936ab03f7d9d29eb4ddf36ac3fb5) | 24H波动可控；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP极端偏高；FDV超过早期Alpha主榜上限；成熟大市值 | Score 39; Tier Liquid; LP $1.34M; Vol24H $95.10M; 24H +19.13%; V/LP 70.92x; 池数 1; 分项 L20/V17/B17/Buy3/Risk-42 | 只记录热度，不进入主榜 |
| [OCCAM](https://dexscreener.com/solana/6tbpwlernnkeswwwt6rwa5lxjfekpuvfkzyrgmckuess) | SOL | [41y7bE...2gpump](https://solscan.io/token/41y7bEjuidUJTZJ7mbfqzKjNcBiecYvjnyPwCb2gpump) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 30; Tier Early; LP $158.3K; Vol24H $10.63M; 24H +632.00%; V/LP 67.11x; 池数 1; 分项 L11/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [world](https://dexscreener.com/solana/ewrxs61yb2swiangqcbg9vgerkwdz3fxxwtyz2kfvbm8) | SOL | [FMqh9m...aJpump](https://solscan.io/token/FMqh9mqR6drPZqqW6wPqLHxX4rqNDWGhYLaMfoaJpump) | 买卖基本均衡；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 27; Tier Early; LP $288.0K; Vol24H $7.72M; 24H +119.00%; V/LP 26.82x; 池数 2; 分项 L13/V17/B0/Buy3/Risk-30 | 只记录热度，不进入主榜 |
| [Horseradish](https://dexscreener.com/solana/2pcbimrflvuklgb394xmmfrcb82bu7utluphs8wbw6vz) | SOL | [GAefbs...xFpump](https://solscan.io/token/GAefbsZef5zGjacXf65ioie8gzHEnS9xzSWNZsxFpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 14; Tier Micro; LP $32.0K; Vol24H $2.69M; 24H +372.00%; V/LP 83.95x; 池数 2; 分项 L5/V17/B0/Buy8/Risk-40 | 只记录热度，不进入主榜 |
| FABLE | SOL | [498DeY...DDpump](https://solscan.io/token/498DeYRS7AtLdE5wbwXbpFtinMTDTJxuvfXMraDDpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 13; Tier Micro; LP $31.7K; Vol24H $2.01M; 24H +350.51%; V/LP 63.54x; 池数 2; 分项 L5/V16/B0/Buy8/Risk-40 | 只记录热度，不进入主榜 |
| [FROGBULL](https://dexscreener.com/solana/gkgwpmtt7jcwzf4pxtzqq4zjcryeppz2mmj4y3xegzrb) | SOL | [BDbNwA...p6pump](https://solscan.io/token/BDbNwA95183CdqUhx2P6R3fWXbefubVbx2wNnCp6pump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP偏高；年轻币短期暴拉 | Score 11; Tier Micro; LP $76.0K; Vol24H $1.18M; 24H +2992.00%; V/LP 15.47x; 池数 1; 分项 L8/V14/B0/Buy8/Risk-43 | 只记录热度，不进入主榜 |
| ZAYED | SOL | [6XUkLa...THpump](https://solscan.io/token/6XUkLa8fbTzRUkGotni7UtkG4EHtUFe8qPhJU5THpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 6; Tier Micro; LP $7.1K; Vol24H $1.11M; 24H -98.22%; V/LP 154.96x; 池数 1; 分项 L0/V14/B0/Buy8/Risk-40 | 只记录热度，不进入主榜 |

### D. 成熟池观察明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| [ANSEM](https://dexscreener.com/solana/evefweghf7reov3wthjdxgx3owabua7wehehcuhpb1h) | SOL | [9cRCn9...TGpump](https://solscan.io/token/9cRCn9rGT8V2imeM2BaKs13yhMEais3ruM3rPvTGpump) | 24H波动可控；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；非主流报价池；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 71; Tier Mature; LP $15.11M; Vol24H $20.77M; 24H +14.29%; V/LP 1.37x; 池数 3; 分项 L20/V17/B17/Buy8/Risk-15 | 成熟池观察，不占用早期Alpha主榜 |
| [RAY](https://dexscreener.com/solana/2axxcn6on9bbt5owwmth53c7qhuxvhleu718kqt8rvy2) | SOL | [4k3Dyj...QrkX6R](https://solscan.io/token/4k3Dyjzvzp8eMZWUXbBCjEvwSkkk59S5iCNLY3QrkX6R) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 71; Tier Liquid; LP $1.12M; Vol24H $1.48M; 24H +4.17%; V/LP 1.32x; 池数 2; 分项 L19/V15/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| [JUP](https://dexscreener.com/solana/3xngdc58axytrj64stqz5trdqwvtwhlr888irbbwznee) | SOL | [JUPyiw...NsDvCN](https://solscan.io/token/JUPyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；非主流报价池；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 71; Tier Mature; LP $157.69M; Vol24H $276.77M; 24H -1.98%; V/LP 1.76x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-15 | 成熟池观察，不占用早期Alpha主榜 |
| [Bonk](https://dexscreener.com/solana/2hxctgnfeqfnsxv8d7ztybebeaowmwwvedqq8v3obyas) | SOL | [DezXAZ...pPB263](https://solscan.io/token/DezXAZ8z7PnrnRJjz3wXBoRgixCa6xjnB7YaB1pPB263) | 24H接近横盘；LP达主观察门槛；24H成交合格；Volume/LP未失真；卖出笔数占优；非主流报价池；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 68; Tier Mature; LP $109.69M; Vol24H $177.10M; 24H +0.50%; V/LP 1.61x; 池数 1; 分项 L20/V17/B22/Buy0/Risk-15 | 成熟池观察，不占用早期Alpha主榜 |
| BTW | BSC | [0x4440...35acaa](https://bscscan.com/token/0x444045b0ee1ee319a660a5e3d604ca0ffa35acaa) | 24H波动可控；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 68; Tier Liquid; LP $1.27M; Vol24H $4.23M; 24H +23.51%; V/LP 3.33x; 池数 1; 分项 L19/V17/B17/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| [PUMP](https://dexscreener.com/solana/4c8kctyztmtzwv83y5actpvt2axyyu2t9zhhdotfgnno) | SOL | [pumpCm...7H9Dfn](https://solscan.io/token/pumpCmXqMfrsAkQ5r49WcJnRayYRqmXz6ae8H7H9Dfn) | 24H波动可控；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；非主流报价池；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 66; Tier Mature; LP $63.07M; Vol24H $165.44M; 24H -11.07%; V/LP 2.62x; 池数 1; 分项 L20/V17/B17/Buy3/Risk-15 | 成熟池观察，不占用早期Alpha主榜 |
| [MET](https://dexscreener.com/solana/5hbf9jp8k5zdrzp9pokpypfqobse5mgcmw6nqodurgcd) | SOL | [METvsv...n6mWQL](https://solscan.io/token/METvsvVRapdj9cFLzq4Tr43xK4tAjQfwX76z3n6mWQL) | 24H波动可控；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 62; Tier Liquid; LP $801.5K; Vol24H $895.4K; 24H +12.51%; V/LP 1.12x; 池数 1; 分项 L17/V13/B17/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| [mɔ](https://dexscreener.com/solana/ceuutv2xuirspbpu7tmyjqedz11zgr8shhvtpgm6az5z) | SOL | [7jdJEm...TiA4it](https://solscan.io/token/7jdJEmvsZX6MGx2MziseZ3YZ5Mnp8iG3tuo2hJTiA4it) | 24H接近横盘；买入笔数占优；LP达主观察门槛；Volume/LP未失真；24H成交不足；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限 | Score 58; Tier Liquid; LP $3.70M; Vol24H $1.0K; 24H +0.00%; V/LP 0.00x; 池数 3; 分项 L20/V0/B22/Buy12/Risk-20 | 成熟池观察，不占用早期Alpha主榜 |

### E. 链上确认/紧急精查表
| Token | 链 | 合约地址 | 是否需要链上确认 | 紧急精查 | 预检状态 | 原因 |
|---|---|---|---|---|---|---|
| TOESCOIN | SOL | [6ehEcT...HDpump](https://solscan.io/token/6ehEcTMCc85aNF4x9CWx8HuvWGhxQtvKdhKVf2HDpump) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| ARX | BSC | [0xd5f6...1ca715](https://bscscan.com/token/0xd5f6ef5deabe61e6d5cdb49bfb6f156f2c1ca715) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| KINS | SOL | [Tqj8yF...9bpump](https://solscan.io/token/Tqj8yFmagrg7oorpQkVGYR52r96RFTamvWfth9bpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [RTM](https://dexscreener.com/solana/ebnuexqpb5wjkxjsfm3ruft7zb7zbxhzgr7ydhyuvuyy) | SOL | [3d1qHS...XCDM6u](https://solscan.io/token/3d1qHSAkQhoN7kN1C6tvpAArCkXWxwYdBng6taXCDM6u) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [ANSEM](https://dexscreener.com/solana/evefweghf7reov3wthjdxgx3owabua7wehehcuhpb1h) | SOL | [9cRCn9...TGpump](https://solscan.io/token/9cRCn9rGT8V2imeM2BaKs13yhMEais3ruM3rPvTGpump) | 是 | 否 | verified / address_preflight_v0.4 | 多池数据冲突，需链上/聚合源复核 |
| [ㅤ](https://dexscreener.com/solana/pai8kyevjjx7ukbxrrqhvwnpsqu1nqpbsvffddykgt2) | SOL | [FCGtC4...9cNZih](https://solscan.io/token/FCGtC4AXSyLGRfS4rceiFAparP9sikH4DTKSxZ9cNZih) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；多池数据冲突，需链上/聚合源复核 |
| [TripleT](https://dexscreener.com/solana/3kfcgj5r3zshw8htdbzjsrrksrymkvsmfhc4vo4iddxd) | SOL | [J8PSdN...KZpump](https://solscan.io/token/J8PSdNP3QewKq2Z1JJJFDMaqF7KcaiJhR7gbr5KZpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [memecoin](https://dexscreener.com/solana/ebpudz8eke1tavcrasmaaegzk3wjveesrxmidmxuyxay) | SOL | [Bb4jR9...d7pump](https://solscan.io/token/Bb4jR951QtVjeFAYFLBYXDSMKjbTDroCLPbFLdd7pump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；多池数据冲突，需链上/聚合源复核 |
| [mɔ](https://dexscreener.com/solana/ceuutv2xuirspbpu7tmyjqedz11zgr8shhvtpgm6az5z) | SOL | [7jdJEm...TiA4it](https://solscan.io/token/7jdJEmvsZX6MGx2MziseZ3YZ5Mnp8iG3tuo2hJTiA4it) | 是 | 否 | verified / address_preflight_v0.4 | 多池数据冲突，需链上/聚合源复核 |
| BASED | BSC | [0x1d28...958e4d](https://bscscan.com/token/0x1d28d989f9e3ccb8b15d0cec601734514f958e4d) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |

### F. 钱包行为 / AVE命中样本表
| Token | 链 | 合约地址 | 行为状态 | 行为层级 | AVE命中 | 判断 |
|---|---|---|---|---|---:|---|
| TOESCOIN | SOL | [6ehEcT...HDpump](https://solscan.io/token/6ehEcTMCc85aNF4x9CWx8HuvWGhxQtvKdhKVf2HDpump) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| ARX | BSC | [0xd5f6...1ca715](https://bscscan.com/token/0xd5f6ef5deabe61e6d5cdb49bfb6f156f2c1ca715) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |

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
| 成熟池观察 | 8 个 | 成熟资产不占早期Alpha主榜 |
| 合约地址覆盖 | 可用 25，缺失 0 | 地址缺失会阻断BSC RPC/Helius精查，需要优先补齐 |
| LP层级 | Micro 5 / Early 7 / Liquid 9 / Mature 4 | 下一步可以按层级分别设置进攻规则 |
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