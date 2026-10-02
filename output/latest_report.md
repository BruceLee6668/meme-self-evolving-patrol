# 自我进化轮巡

**本轮时间 UTC：** 2026-10-02T06:34:37Z
**版本：** 0.5.0-ave-cache-wallet-behavior-prep
**S0 时间锚点：** 2026-06-16T16:15:17+09:00

## 一句话结论
本轮从 140 个合并Token中筛出 5 个主观察候选。v0.5已在v0.4.1基础上增加AVE周缓存真实接口接入框架、Smart Wallet持久保存、wallet_behavior_latest.json，以及BSC Transfer级钱包行为样本。注意：BSC当前是Transfer样本，不等同完整Swap解码。
合约地址可用 25 个，缺失 0 个；缺失地址的候选不能进入后续链上精查。

## 本轮扫描摘要
| 指标 | 数量 |
|---|---:|
| 原始池子记录 | 224 |
| 合并后Token | 140 |
| 输出候选 | 25 |
| 主观察 | 5 |
| 次观察 | 5 |
| PVP风险池 | 8 |
| 成熟池观察 | 2 |
| 低优先观察 | 5 |
| 多池Token | 3 |
| 多池冲突 | 1 |
| Symbol桥接合并 | 1 |
| 合约地址可用 | 25 |
| 合约地址缺失 | 0 |
| Micro层 | 7 |
| Early层 | 10 |
| Liquid层 | 7 |
| Mature层 | 1 |
| 需要链上确认 | 18 |
| 紧急精查候选 | 4 |

## v0.5 数据确认状态
| 项目 | 状态 |
|---|---|
| AVE Smart Wallet周缓存 | active，钱包数 1651，刷新时间 2026-09-28T02:48:12Z，是否过期 否 |
| 链上预检 | 本轮检查 12 个，验证通过 12 个，失败 0 个 |
| Helius状态 | 未配置，SOL使用公共RPC或跳过增强解析 |
| 当前精查层级 | 0.5.0-chain-preflight-plus-wallet-behavior：地址/账户预检 + v0.5钱包行为样本，完整Swap留存仍待下一版 |
| 钱包行为样本 | 本轮检查 6 个，BSC Transfer样本 2 个，SOL签名级 4 个，AVE钱包命中 0 个 |

## 第一部分：生成结果表格

### A. 上次记录结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| SI | SOL | [DEW9dS...i98WDP](https://solscan.io/token/DEW9dSN6QpWyNthphCpMmAbZP1Q4cEKR9xQXAri98WDP) | 主观察 | Score 88; Tier Liquid; LP $873.2K; Vol24H $1.82M; 24H -3.07%; V/LP 2.08x; 池数 4; 分项 L18/V16/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [OTC](https://dexscreener.com/solana/da4pm4xsdy4m9v4cgakkbvh1pw1ysctqqa5nekghukpt) | SOL | [MukLDt...udpump](https://solscan.io/token/MukLDtJ8Cx9DxLbeyLRSWPSposTMWuwHANbuaudpump) | 主观察 | Score 87; Tier Early; LP $715.5K; Vol24H $2.63M; 24H +21.06%; V/LP 3.68x; 池数 1; 分项 L17/V17/B17/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [CATE](https://dexscreener.com/solana/hmzvseemtzhhvznw9uwbag85hctmfnkbhzux16cy7ca3) | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | 主观察 | Score 86; Tier Liquid; LP $3.31M; Vol24H $4.86M; 24H +18.56%; V/LP 1.47x; 池数 1; 分项 L20/V17/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| BOB | BSC | [0x5136...e1560e](https://bscscan.com/token/0x51363f073b1e4920fda7aa9e9d84ba97ede1560e) | 主观察 | Score 84; Tier Liquid; LP $1.21M; Vol24H $1.96M; 24H -20.71%; V/LP 1.62x; 池数 1; 分项 L19/V16/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| BREW | BSC | [0xfa6d...3f2159](https://bscscan.com/token/0xfa6d9b504848606eb9aec04ccc161d169b3f2159) | 主观察 | Score 83; Tier Early; LP $688.2K; Vol24H $616.8K; 24H -7.78%; V/LP 0.90x; 池数 1; 分项 L17/V12/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| WKC | BSC | [0x6ec9...128edb](https://bscscan.com/token/0x6ec90334d89dbdc89e08a133271be3d104128edb) | 次观察 | Score 80; Tier Liquid; LP $1.12M; Vol24H $99.1K; 24H -2.99%; V/LP 0.09x; 池数 1; 分项 L19/V7/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 次观察，不直接进攻 |
| [WAIF](https://dexscreener.com/solana/2panrxhfn7za3k3akvhiwej6cmrncsnfrzqmzwnvtz1j) | SOL | [wYGJoo...3Tpump](https://solscan.io/token/wYGJooYPKykXrCUrkDTmxoL4McN2VwyYP2Gvz3Tpump) | 次观察 | Score 71; Tier Early; LP $224.8K; Vol24H $250.6K; 24H +23.42%; V/LP 1.11x; 池数 1; 分项 L12/V10/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [e/acc](https://dexscreener.com/solana/4jankfddd5fftk5pxdj3pptwjutefswqejzjcgkq9kww) | SOL | [CbcyNo...kzpKoU](https://solscan.io/token/CbcyNo7m1amFWqEQm2m4PLv1UNvpcL3C1Ujm6AkzpKoU) | 次观察 | Score 70; Tier Early; LP $714.1K; Vol24H $11.09M; 24H -2.62%; V/LP 15.53x; 池数 3; 分项 L17/V17/B22/Buy8/Risk-18 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [USDF](https://dexscreener.com/solana/aqp9ekhgp1u35usbdayglpgnvzuyezlshfxfzkw3cye9) | SOL | [7MuvW6...Ropump](https://solscan.io/token/7MuvW6G2pDTGSjzpjqeDYigUsXqqd6TmEzLgvRRopump) | 次观察 | Score 68; Tier Micro; LP $79.5K; Vol24H $64.7K; 24H +7.27%; V/LP 0.81x; 池数 2; 分项 L8/V6/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| THESIS | BSC | [0x4519...dd7777](https://bscscan.com/token/0x4519cacc591aecc5f8476bebee43b11ffedd7777) | 次观察 | Score 66; Tier Micro; LP $88.5K; Vol24H $413.5K; 24H -2.06%; V/LP 4.67x; 池数 1; 分项 L9/V11/B22/Buy0/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |

### B. 本轮扫描结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| [OTC](https://dexscreener.com/solana/da4pm4xsdy4m9v4cgakkbvh1pw1ysctqqa5nekghukpt) | SOL | [MukLDt...udpump](https://solscan.io/token/MukLDtJ8Cx9DxLbeyLRSWPSposTMWuwHANbuaudpump) | 主观察 | Score 86; Tier Early; LP $685.9K; Vol24H $2.50M; 24H +10.01%; V/LP 3.64x; 池数 1; 分项 L17/V16/B17/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [CATE](https://dexscreener.com/solana/hmzvseemtzhhvznw9uwbag85hctmfnkbhzux16cy7ca3) | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | 主观察 | Score 86; Tier Liquid; LP $3.30M; Vol24H $5.15M; 24H +13.48%; V/LP 1.56x; 池数 1; 分项 L20/V17/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [PAID](https://dexscreener.com/solana/6e3jzltf4tqbwzm3f7a66jf8tfzn6mrqvrbdfgcnwara) | SOL | [98kfF7...zypump](https://solscan.io/token/98kfF7rmsg1QDUEoCqNE7g7M1FdrTt92TEp2CLzypump) | 主观察 | Score 82; Tier Liquid; LP $755.2K; Vol24H $2.25M; 24H +1.93%; V/LP 2.98x; 池数 1; 分项 L17/V16/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| BOB | BSC | [0x5136...e1560e](https://bscscan.com/token/0x51363f073b1e4920fda7aa9e9d84ba97ede1560e) | 主观察 | Score 82; Tier Liquid; LP $1.18M; Vol24H $1.12M; 24H -10.01%; V/LP 0.95x; 池数 1; 分项 L19/V14/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| SI | SOL | [DEW9dS...i98WDP](https://solscan.io/token/DEW9dSN6QpWyNthphCpMmAbZP1Q4cEKR9xQXAri98WDP) | 主观察 | Score 81; Tier Liquid; LP $783.4K; Vol24H $1.60M; 24H -22.96%; V/LP 2.05x; 池数 4; 分项 L17/V15/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| APM | BSC | [0x72a2...a0921e](https://bscscan.com/token/0x72a22faa6a522c81a8f5d508381e18af3da0921e) | 次观察 | Score 81; Tier Liquid; LP $1.58M; Vol24H $5.26M; 24H +19.47%; V/LP 3.32x; 池数 1; 分项 L20/V17/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 次观察，不直接进攻 |
| BREW | BSC | [0xfa6d...3f2159](https://bscscan.com/token/0xfa6d9b504848606eb9aec04ccc161d169b3f2159) | 次观察 | Score 76; Tier Liquid; LP $805.7K; Vol24H $991.5K; 24H +9.64%; V/LP 1.23x; 池数 1; 分项 L18/V14/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，不直接进攻 |
| [WAIF](https://dexscreener.com/solana/2panrxhfn7za3k3akvhiwej6cmrncsnfrzqmzwnvtz1j) | SOL | [wYGJoo...3Tpump](https://solscan.io/token/wYGJooYPKykXrCUrkDTmxoL4McN2VwyYP2Gvz3Tpump) | 次观察 | Score 72; Tier Early; LP $235.9K; Vol24H $252.8K; 24H +22.53%; V/LP 1.07x; 池数 1; 分项 L13/V10/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [Pinata](https://dexscreener.com/solana/braoezs1zhzdqwqwkwnh3z4ouylxvlcvglpfhhbvzcht) | SOL | [Edpcd9...vopump](https://solscan.io/token/Edpcd9aYh6BVRKV5hYrgnEuJ3MHAFcdnHtSL9yvopump) | 次观察 | Score 69; Tier Micro; LP $50.5K; Vol24H $309.1K; 24H +9.90%; V/LP 6.12x; 池数 1; 分项 L6/V10/B17/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [EMBER](https://dexscreener.com/solana/2y6pcqa4fep3jlifdan9jvmw7lsk8f3gwstfy8p7trae) | SOL | [5dvXTZ...k4QEC6](https://solscan.io/token/5dvXTZ5qwgafnHtwu3Ls3QrWx1U4LQsFeCuJgkk4QEC6) | 次观察 | Score 65; Tier Early; LP $346.4K; Vol24H $324.5K; 24H +20.91%; V/LP 0.94x; 池数 1; 分项 L14/V10/B17/Buy3/Risk-3 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| ct | BSC | [0x0a09...867f46](https://bscscan.com/token/0x0a092e544da31150b439a1aaa1a3a2214a867f46) | PVP风险池 | Score 42; Tier Liquid; LP $1.90M; Vol24H $119.09M; 24H +26.44%; V/LP 62.78x; 池数 1; 分项 L20/V17/B8/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| Nailoong | BSC | [0xb936...aa7777](https://bscscan.com/token/0xb936cab857514bb917431cc8e2b7f1da5caa7777) | PVP风险池 | Score 29; Tier Early; LP $133.3K; Vol24H $7.33M; 24H +4761.17%; V/LP 54.96x; 池数 1; 分项 L10/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| MEME | SOL | [FFrRBP...8zpump](https://solscan.io/token/FFrRBPP9yWtSqnKjXXM9C77MBdLztfdgSnRE858zpump) | PVP风险池 | Score 29; Tier Micro; LP $20.8K; Vol24H $4.32M; 24H -5.78%; V/LP 207.88x; 池数 3; 分项 L3/V17/B22/Buy3/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [Jane](https://dexscreener.com/solana/31ectc8w3vcx7bifwk2o5ax41fpi2uyhcehcy2gd3h5h) | SOL | [9pJWJd...Yw9ZMr](https://solscan.io/token/9pJWJdpPebyANys45eetpemLJo8yTz4n5B9zbpYw9ZMr) | PVP风险池 | Score 28; Tier Micro; LP $97.4K; Vol24H $10.18M; 24H +1474.00%; V/LP 104.54x; 池数 2; 分项 L9/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [SAPLING](https://dexscreener.com/solana/6ejg4ayjm3mk1t2zbkjbj43df3s7rbmpc9mgo526k51g) | SOL | [BZFYNP...BbB96W](https://solscan.io/token/BZFYNPeQAEW3HWQ4DNsTVahC1n4ZjTgn6jB2nnBbB96W) | PVP风险池 | Score 28; Tier Early; LP $215.2K; Vol24H $4.61M; 24H +1898.00%; V/LP 21.43x; 池数 1; 分项 L12/V17/B0/Buy8/Risk-33 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### C. PVP风险池明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| ct | BSC | [0x0a09...867f46](https://bscscan.com/token/0x0a092e544da31150b439a1aaa1a3a2214a867f46) | 24H未过热但已明显波动；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 42; Tier Liquid; LP $1.90M; Vol24H $119.09M; 24H +26.44%; V/LP 62.78x; 池数 1; 分项 L20/V17/B8/Buy3/Risk-30 | 只记录热度，不进入主榜 |
| Nailoong | BSC | [0xb936...aa7777](https://bscscan.com/token/0xb936cab857514bb917431cc8e2b7f1da5caa7777) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 29; Tier Early; LP $133.3K; Vol24H $7.33M; 24H +4761.17%; V/LP 54.96x; 池数 1; 分项 L10/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| MEME | SOL | [FFrRBP...8zpump](https://solscan.io/token/FFrRBPP9yWtSqnKjXXM9C77MBdLztfdgSnRE858zpump) | 24H接近横盘；买卖基本均衡；LP未达主观察门槛；24H成交合格；LP偏薄；Volume/LP极端偏高 | Score 29; Tier Micro; LP $20.8K; Vol24H $4.32M; 24H -5.78%; V/LP 207.88x; 池数 3; 分项 L3/V17/B22/Buy3/Risk-40 | 只记录热度，不进入主榜 |
| [Jane](https://dexscreener.com/solana/31ectc8w3vcx7bifwk2o5ax41fpi2uyhcehcy2gd3h5h) | SOL | [9pJWJd...Yw9ZMr](https://solscan.io/token/9pJWJdpPebyANys45eetpemLJo8yTz4n5B9zbpYw9ZMr) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 28; Tier Micro; LP $97.4K; Vol24H $10.18M; 24H +1474.00%; V/LP 104.54x; 池数 2; 分项 L9/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [SAPLING](https://dexscreener.com/solana/6ejg4ayjm3mk1t2zbkjbj43df3s7rbmpc9mgo526k51g) | SOL | [BZFYNP...BbB96W](https://solscan.io/token/BZFYNPeQAEW3HWQ4DNsTVahC1n4ZjTgn6jB2nnBbB96W) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高；非主流报价池 | Score 28; Tier Early; LP $215.2K; Vol24H $4.61M; 24H +1898.00%; V/LP 21.43x; 池数 1; 分项 L12/V17/B0/Buy8/Risk-33 | 只记录热度，不进入主榜 |
| [Ansemmas](https://dexscreener.com/solana/6qirp44q2t8b1cfbgmnqexcldqhfqmncfaffpkg4n156) | SOL | [HXxJda...AAMASS](https://solscan.io/token/HXxJdaQbrYRvwTAM8M8mUPyoRPvmyuUbPFBRkiAAMASS) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 26; Tier Micro; LP $64.3K; Vol24H $4.52M; 24H +710.00%; V/LP 70.33x; 池数 1; 分项 L7/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [COCKROACH](https://dexscreener.com/solana/5d1mwaczebhe96bx8zn3jqgjwpubjqf7vcbmmhr5gskb) | SOL | [H4KUxs...r6nyJc](https://solscan.io/token/H4KUxsEgCp2yDpFvyDuGM5k6XevSKKrrKUxZ3Zr6nyJc) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高；非主流报价池 | Score 26; Tier Early; LP $134.5K; Vol24H $3.78M; 24H +280.00%; V/LP 28.12x; 池数 1; 分项 L10/V17/B0/Buy8/Risk-33 | 只记录热度，不进入主榜 |
| [www](https://dexscreener.com/solana/cr469kh7ocptqk5yademjvpbwx1dixxlioopfjn23jsg) | SOL | [GAwhcp...3Q9S9H](https://solscan.io/token/GAwhcphCqCv5bKHmCiN4VDdNWfbXJL4npmkc8L3Q9S9H) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高；年轻币短期暴拉 | Score 6; Tier Early; LP $208.3K; Vol24H $13.81M; 24H +6678.00%; V/LP 66.31x; 池数 1; 分项 L12/V17/B0/Buy8/Risk-55 | 只记录热度，不进入主榜 |

### D. 成熟池观察明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| ARK | BSC | [0xcae1...618b9d](https://bscscan.com/token/0xcae117ca6bc8a341d2e7207f30e180f0e5618b9d) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 74; Tier Mature; LP $58.03M; Vol24H $3.38M; 24H +0.45%; V/LP 0.06x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| MarsCoin | BSC | [0xfe18...5c7777](https://bscscan.com/token/0xfe189e97832da1573e4e4ff034f4ffc3a15c7777) | 24H波动可控；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 68; Tier Early; LP $436.5K; Vol24H $2.24M; 24H -9.57%; V/LP 5.13x; 池数 1; 分项 L15/V16/B17/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |

### E. 链上确认/紧急精查表
| Token | 链 | 合约地址 | 是否需要链上确认 | 紧急精查 | 预检状态 | 原因 |
|---|---|---|---|---|---|---|
| [OTC](https://dexscreener.com/solana/da4pm4xsdy4m9v4cgakkbvh1pw1ysctqqa5nekghukpt) | SOL | [MukLDt...udpump](https://solscan.io/token/MukLDtJ8Cx9DxLbeyLRSWPSposTMWuwHANbuaudpump) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| [CATE](https://dexscreener.com/solana/hmzvseemtzhhvznw9uwbag85hctmfnkbhzux16cy7ca3) | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| BOB | BSC | [0x5136...e1560e](https://bscscan.com/token/0x51363f073b1e4920fda7aa9e9d84ba97ede1560e) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| APM | BSC | [0x72a2...a0921e](https://bscscan.com/token/0x72a22faa6a522c81a8f5d508381e18af3da0921e) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| [PAID](https://dexscreener.com/solana/6e3jzltf4tqbwzm3f7a66jf8tfzn6mrqvrbdfgcnwara) | SOL | [98kfF7...zypump](https://solscan.io/token/98kfF7rmsg1QDUEoCqNE7g7M1FdrTt92TEp2CLzypump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| SI | SOL | [DEW9dS...i98WDP](https://solscan.io/token/DEW9dSN6QpWyNthphCpMmAbZP1Q4cEKR9xQXAri98WDP) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；多池数据冲突，需链上/聚合源复核 |
| BREW | BSC | [0xfa6d...3f2159](https://bscscan.com/token/0xfa6d9b504848606eb9aec04ccc161d169b3f2159) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [WAIF](https://dexscreener.com/solana/2panrxhfn7za3k3akvhiwej6cmrncsnfrzqmzwnvtz1j) | SOL | [wYGJoo...3Tpump](https://solscan.io/token/wYGJooYPKykXrCUrkDTmxoL4McN2VwyYP2Gvz3Tpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [Pinata](https://dexscreener.com/solana/braoezs1zhzdqwqwkwnh3z4ouylxvlcvglpfhhbvzcht) | SOL | [Edpcd9...vopump](https://solscan.io/token/Edpcd9aYh6BVRKV5hYrgnEuJ3MHAFcdnHtSL9yvopump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [EMBER](https://dexscreener.com/solana/2y6pcqa4fep3jlifdan9jvmw7lsk8f3gwstfy8p7trae) | SOL | [5dvXTZ...k4QEC6](https://solscan.io/token/5dvXTZ5qwgafnHtwu3Ls3QrWx1U4LQsFeCuJgkk4QEC6) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |

### F. 钱包行为 / AVE命中样本表
| Token | 链 | 合约地址 | 行为状态 | 行为层级 | AVE命中 | 判断 |
|---|---|---|---|---|---:|---|
| [OTC](https://dexscreener.com/solana/da4pm4xsdy4m9v4cgakkbvh1pw1ysctqqa5nekghukpt) | SOL | [MukLDt...udpump](https://solscan.io/token/MukLDtJ8Cx9DxLbeyLRSWPSposTMWuwHANbuaudpump) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| [CATE](https://dexscreener.com/solana/hmzvseemtzhhvznw9uwbag85hctmfnkbhzux16cy7ca3) | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| BOB | BSC | [0x5136...e1560e](https://bscscan.com/token/0x51363f073b1e4920fda7aa9e9d84ba97ede1560e) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| APM | BSC | [0x72a2...a0921e](https://bscscan.com/token/0x72a22faa6a522c81a8f5d508381e18af3da0921e) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| [PAID](https://dexscreener.com/solana/6e3jzltf4tqbwzm3f7a66jf8tfzn6mrqvrbdfgcnwara) | SOL | [98kfF7...zypump](https://solscan.io/token/98kfF7rmsg1QDUEoCqNE7g7M1FdrTt92TEp2CLzypump) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| SI | SOL | [DEW9dS...i98WDP](https://solscan.io/token/DEW9dSN6QpWyNthphCpMmAbZP1Q4cEKR9xQXAri98WDP) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |

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
| LP层级 | Micro 7 / Early 10 / Liquid 7 / Mature 1 | 下一步可以按层级分别设置进攻规则 |
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