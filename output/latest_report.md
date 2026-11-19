# 自我进化轮巡

**本轮时间 UTC：** 2026-11-19T08:19:38Z
**版本：** 0.5.0-ave-cache-wallet-behavior-prep
**S0 时间锚点：** 2026-06-16T16:15:17+09:00

## 一句话结论
本轮从 142 个合并Token中筛出 5 个主观察候选。v0.5已在v0.4.1基础上增加AVE周缓存真实接口接入框架、Smart Wallet持久保存、wallet_behavior_latest.json，以及BSC Transfer级钱包行为样本。注意：BSC当前是Transfer样本，不等同完整Swap解码。
合约地址可用 25 个，缺失 0 个；缺失地址的候选不能进入后续链上精查。

## 本轮扫描摘要
| 指标 | 数量 |
|---|---:|
| 原始池子记录 | 273 |
| 合并后Token | 142 |
| 输出候选 | 25 |
| 主观察 | 5 |
| 次观察 | 1 |
| PVP风险池 | 8 |
| 成熟池观察 | 3 |
| 低优先观察 | 8 |
| 多池Token | 8 |
| 多池冲突 | 4 |
| Symbol桥接合并 | 2 |
| 合约地址可用 | 25 |
| 合约地址缺失 | 0 |
| Micro层 | 4 |
| Early层 | 12 |
| Liquid层 | 8 |
| Mature层 | 1 |
| 需要链上确认 | 14 |
| 紧急精查候选 | 2 |

## v0.5 数据确认状态
| 项目 | 状态 |
|---|---|
| AVE Smart Wallet周缓存 | active，钱包数 2748，刷新时间 2026-11-16T04:00:31Z，是否过期 否 |
| 链上预检 | 本轮检查 12 个，验证通过 12 个，失败 0 个 |
| Helius状态 | 未配置，SOL使用公共RPC或跳过增强解析 |
| 当前精查层级 | 0.5.0-chain-preflight-plus-wallet-behavior：地址/账户预检 + v0.5钱包行为样本，完整Swap留存仍待下一版 |
| 钱包行为样本 | 本轮检查 5 个，BSC Transfer样本 2 个，SOL签名级 3 个，AVE钱包命中 0 个 |

## 第一部分：生成结果表格

### A. 上次记录结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| $BANANA | BSC | [0x3d4f...a9a760](https://bscscan.com/token/0x3d4f0513e8a29669b960f9dbca61861548a9a760) | 主观察 | Score 86; Tier Liquid; LP $3.04M; Vol24H $10.79M; 24H -2.99%; V/LP 3.55x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| CATE | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | 主观察 | Score 81; Tier Liquid; LP $1.31M; Vol24H $708.4K; 24H -12.71%; V/LP 0.54x; 池数 2; 分项 L19/V13/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| JCT | BSC | [0xea37...b17707](https://bscscan.com/token/0xea37a8de1de2d9d10772eeb569e28bfa5cb17707) | 主观察 | Score 81; Tier Early; LP $588.6K; Vol24H $2.15M; 24H -1.59%; V/LP 3.64x; 池数 1; 分项 L16/V16/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [PUMP](https://dexscreener.com/solana/7q2dqbjtxxp4dqmhec2nsgxwsytq8jaxdygswmag3pfp) | SOL | [9593dF...ysD6A1](https://solscan.io/token/9593dFjsLKKRAaz4LX1eK2DDEgrzfu3idb6yvMysD6A1) | 主观察 | Score 77; Tier Liquid; LP $2.05M; Vol24H $159.5K; 24H -0.25%; V/LP 0.08x; 池数 3; 分项 L20/V8/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| pippin | SOL | [Dfh5Dz...mApump](https://solscan.io/token/Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump) | 主观察 | Score 77; Tier Liquid; LP $3.43M; Vol24H $14.20M; 24H +68.24%; V/LP 4.14x; 池数 1; 分项 L20/V17/B8/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| JAGENT | BSC | [0x8e64...e4ae15](https://bscscan.com/token/0x8e6442663a4f8c50b6132c68d42a30e7dfe4ae15) | 次观察 | Score 76; Tier Liquid; LP $3.74M; Vol24H $1.55M; 24H +9.76%; V/LP 0.42x; 池数 1; 分项 L20/V15/B17/Buy0/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，不直接进攻 |
| [CLAUDIA](https://dexscreener.com/solana/fe7bpdycs74gqicuf14hwgumtopkv1d9mdyvx5btohfr) | SOL | [2j5SaS...hnW2ZM](https://solscan.io/token/2j5SaS7xy776qCBpyPQbZjyQSAtKiFgrwjfErthnW2ZM) | 次观察 | Score 73; Tier Early; LP $370.1K; Vol24H $1.72M; 24H +17.49%; V/LP 4.65x; 池数 2; 分项 L14/V15/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| Max | SOL | [5qaP7o...aTpump](https://solscan.io/token/5qaP7oKUqKffwwo5DaEqDoTtsBLMpdbQTxEkCDaTpump) | 次观察 | Score 72; Tier Early; LP $138.0K; Vol24H $716.7K; 24H +4.03%; V/LP 5.19x; 池数 1; 分项 L10/V13/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [GATO](https://dexscreener.com/solana/5e3dxlxgwmtdcoka51wyyakttjfzbwqcoyuhbui5gt2m) | SOL | [HsprHx...k6pump](https://solscan.io/token/HsprHxBRgiVaQdRf3TnKNuZZtaX9JUSPgMFdAkk6pump) | 次观察 | Score 67; Tier Early; LP $214.8K; Vol24H $1.42M; 24H -28.93%; V/LP 6.62x; 池数 1; 分项 L12/V15/B8/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| :3 | SOL | [FSkyjf...Nppump](https://solscan.io/token/FSkyjfqB26u6c2GSgpACrjbxp9yQAR8rutxprVNppump) | PVP风险池 | Score 33; Tier Micro; LP $67.0K; Vol24H $1.74M; 24H -33.91%; V/LP 25.92x; 池数 2; 分项 L8/V15/B8/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### B. 本轮扫描结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| pippin | SOL | [Dfh5Dz...mApump](https://solscan.io/token/Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump) | 主观察 | Score 86; Tier Liquid; LP $3.26M; Vol24H $13.06M; 24H -5.26%; V/LP 4.00x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| CLAUDIA | SOL | [2j5SaS...hnW2ZM](https://solscan.io/token/2j5SaS7xy776qCBpyPQbZjyQSAtKiFgrwjfErthnW2ZM) | 主观察 | Score 85; Tier Early; LP $381.2K; Vol24H $1.84M; 24H +5.53%; V/LP 4.82x; 池数 2; 分项 L15/V16/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| BASED | BSC | [0x1d28...958e4d](https://bscscan.com/token/0x1d28d989f9e3ccb8b15d0cec601734514f958e4d) | 主观察 | Score 84; Tier Liquid; LP $840.6K; Vol24H $3.03M; 24H +6.78%; V/LP 3.60x; 池数 1; 分项 L18/V17/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| JCT | BSC | [0xea37...b17707](https://bscscan.com/token/0xea37a8de1de2d9d10772eeb569e28bfa5cb17707) | 主观察 | Score 81; Tier Early; LP $598.2K; Vol24H $2.06M; 24H +2.74%; V/LP 3.45x; 池数 1; 分项 L16/V16/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [PUMP](https://dexscreener.com/solana/7q2dqbjtxxp4dqmhec2nsgxwsytq8jaxdygswmag3pfp) | SOL | [9593dF...ysD6A1](https://solscan.io/token/9593dFjsLKKRAaz4LX1eK2DDEgrzfu3idb6yvMysD6A1) | 主观察 | Score 76; Tier Liquid; LP $2.05M; Vol24H $109.4K; 24H -0.20%; V/LP 0.05x; 池数 3; 分项 L20/V7/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| JAGENT | BSC | [0x8e64...e4ae15](https://bscscan.com/token/0x8e6442663a4f8c50b6132c68d42a30e7dfe4ae15) | 次观察 | Score 68; Tier Liquid; LP $4.07M; Vol24H $2.48M; 24H +32.62%; V/LP 0.61x; 池数 1; 分项 L20/V16/B8/Buy0/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| TTWO | SOL | [TTWofw...vQFbKo](https://solscan.io/token/TTWofwAge91oFhZs7kpQdyrVRkmevgM88xijGvQFbKo) | PVP风险池 | Score 57; Tier Early; LP $580.4K; Vol24H $98.93M; 24H +5.27%; V/LP 170.45x; 池数 1; 分项 L16/V17/B22/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| PIEVERSE | BSC | [0x0e63...0225a9](https://bscscan.com/token/0x0e63b9c287e32a05e6b9ab8ee8df88a2760225a9) | PVP风险池 | Score 36; Tier Liquid; LP $2.75M; Vol24H $65.71M; 24H +18.76%; V/LP 23.94x; 池数 1; 分项 L20/V17/B17/Buy0/Risk-42 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [GTASZN](https://dexscreener.com/solana/c3ai5bk7q9jttvcbwqeexsta99bmmlcnvyasdd7mnqbt) | SOL | [A4jXnW...TVpump](https://solscan.io/token/A4jXnWk1rDRDth6HmDASi45c89n1AguTHivAQPTVpump) | PVP风险池 | Score 32; Tier Micro; LP $96.5K; Vol24H $4.09M; 24H +1383.00%; V/LP 42.35x; 池数 5; 分项 L9/V17/B0/Buy12/Risk-30 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [DCTY](https://dexscreener.com/solana/dchxq4qfppnpedfzlniwvphrvuufgfqedlaazbizhuwf) | SOL | [9hjBLB...f4pump](https://solscan.io/token/9hjBLBrc7WZW2H8UQvBAvG5WiTZotXUv2Bdcn4f4pump) | PVP风险池 | Score 31; Tier Early; LP $432.2K; Vol24H $45.80M; 24H +17906.00%; V/LP 105.97x; 池数 5; 分项 L15/V17/B0/Buy8/Risk-33 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [DacityCoin](https://dexscreener.com/solana/7te1wxcfeqjklghxfvxscngztqunoz9fxbn7kkjrkner) | SOL | [DKYcjo...Xdpump](https://solscan.io/token/DKYcjobF7HPtL9RyQBRdeRQ2iWvizpfbgWwPWNXdpump) | PVP风险池 | Score 28; Tier Early; LP $187.8K; Vol24H $8.87M; 24H -81.55%; V/LP 47.23x; 池数 2; 分项 L12/V17/B0/Buy8/Risk-33 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [BUCKME](https://dexscreener.com/solana/h529gpab6vkq5scwypjwmgb9njhf4udpmlwx6j6gkga8) | SOL | [DEgAkP...R2pump](https://solscan.io/token/DEgAkPNxz3dtMsesD2FDkNA2S6sch5YWfGUDT7R2pump) | PVP风险池 | Score 24; Tier Micro; LP $20.6K; Vol24H $2.67M; 24H -12.11%; V/LP 129.69x; 池数 3; 分项 L3/V17/B17/Buy3/Risk-40 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| GTA6 | SOL | [4kjruq...pQzDnz](https://solscan.io/token/4kjruqGHDsSqkMdFfCjV7Vb62HPFhtXyWc2t6JpQzDnz) | PVP风险池 | Score 22; Tier Micro; LP $33.6K; Vol24H $7.13M; 24H -71.84%; V/LP 212.01x; 池数 1; 分项 L5/V17/B8/Buy8/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [Apocrycoin](https://dexscreener.com/solana/31zwgjenwbxd2nknfmhtbaffegtmviijvx3niqvb9cn9) | SOL | [79rE2a...fhpump](https://solscan.io/token/79rE2ac8JhN3U12QLhymgDmCTiwBN1d4maTcK1fhpump) | PVP风险池 | Score 11; Tier Micro; LP $37.4K; Vol24H $4.45M; 24H +213.00%; V/LP 118.86x; 池数 1; 分项 L5/V17/B0/Buy8/Risk-43 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [USDC](https://dexscreener.com/solana/djntgubgeqiucwe8f981m2c3zghzt2xld8f2sqdz6rsz) | SOL | [EPjFWd...yTDt1v](https://solscan.io/token/EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v) | 成熟池观察 | Score 74; Tier Liquid; LP $2.36M; Vol24H $9.88M; 24H +0.14%; V/LP 4.19x; 池数 5; 分项 L20/V17/B22/Buy3/Risk-12 | 钱包级数据不可用；当前仅代理指标；资产偏成熟，不按早期吸筹处理；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 成熟池观察，不占用早期Alpha主榜 |

### C. PVP风险池明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| TTWO | SOL | [TTWofw...vQFbKo](https://solscan.io/token/TTWofwAge91oFhZs7kpQdyrVRkmevgM88xijGvQFbKo) | 24H接近横盘；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 57; Tier Early; LP $580.4K; Vol24H $98.93M; 24H +5.27%; V/LP 170.45x; 池数 1; 分项 L16/V17/B22/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| PIEVERSE | BSC | [0x0e63...0225a9](https://bscscan.com/token/0x0e63b9c287e32a05e6b9ab8ee8df88a2760225a9) | 24H波动可控；LP达主观察门槛；24H成交合格；卖出笔数占优；Volume/LP极端偏高；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 36; Tier Liquid; LP $2.75M; Vol24H $65.71M; 24H +18.76%; V/LP 23.94x; 池数 1; 分项 L20/V17/B17/Buy0/Risk-42 | 只记录热度，不进入主榜 |
| [GTASZN](https://dexscreener.com/solana/c3ai5bk7q9jttvcbwqeexsta99bmmlcnvyasdd7mnqbt) | SOL | [A4jXnW...TVpump](https://solscan.io/token/A4jXnWk1rDRDth6HmDASi45c89n1AguTHivAQPTVpump) | 买入笔数占优；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 32; Tier Micro; LP $96.5K; Vol24H $4.09M; 24H +1383.00%; V/LP 42.35x; 池数 5; 分项 L9/V17/B0/Buy12/Risk-30 | 只记录热度，不进入主榜 |
| [DCTY](https://dexscreener.com/solana/dchxq4qfppnpedfzlniwvphrvuufgfqedlaazbizhuwf) | SOL | [9hjBLB...f4pump](https://solscan.io/token/9hjBLBrc7WZW2H8UQvBAvG5WiTZotXUv2Bdcn4f4pump) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高；非主流报价池 | Score 31; Tier Early; LP $432.2K; Vol24H $45.80M; 24H +17906.00%; V/LP 105.97x; 池数 5; 分项 L15/V17/B0/Buy8/Risk-33 | 只记录热度，不进入主榜 |
| [DacityCoin](https://dexscreener.com/solana/7te1wxcfeqjklghxfvxscngztqunoz9fxbn7kkjrkner) | SOL | [DKYcjo...Xdpump](https://solscan.io/token/DKYcjobF7HPtL9RyQBRdeRQ2iWvizpfbgWwPWNXdpump) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高；非主流报价池 | Score 28; Tier Early; LP $187.8K; Vol24H $8.87M; 24H -81.55%; V/LP 47.23x; 池数 2; 分项 L12/V17/B0/Buy8/Risk-33 | 只记录热度，不进入主榜 |
| [BUCKME](https://dexscreener.com/solana/h529gpab6vkq5scwypjwmgb9njhf4udpmlwx6j6gkga8) | SOL | [DEgAkP...R2pump](https://solscan.io/token/DEgAkPNxz3dtMsesD2FDkNA2S6sch5YWfGUDT7R2pump) | 24H波动可控；买卖基本均衡；LP未达主观察门槛；24H成交合格；LP偏薄；Volume/LP极端偏高 | Score 24; Tier Micro; LP $20.6K; Vol24H $2.67M; 24H -12.11%; V/LP 129.69x; 池数 3; 分项 L3/V17/B17/Buy3/Risk-40 | 只记录热度，不进入主榜 |
| GTA6 | SOL | [4kjruq...pQzDnz](https://solscan.io/token/4kjruqGHDsSqkMdFfCjV7Vb62HPFhtXyWc2t6JpQzDnz) | 24H未过热但已明显波动；买卖略偏买入；LP未达主观察门槛；24H成交合格；LP偏薄；Volume/LP极端偏高 | Score 22; Tier Micro; LP $33.6K; Vol24H $7.13M; 24H -71.84%; V/LP 212.01x; 池数 1; 分项 L5/V17/B8/Buy8/Risk-40 | 只记录热度，不进入主榜 |
| [Apocrycoin](https://dexscreener.com/solana/31zwgjenwbxd2nknfmhtbaffegtmviijvx3niqvb9cn9) | SOL | [79rE2a...fhpump](https://solscan.io/token/79rE2ac8JhN3U12QLhymgDmCTiwBN1d4maTcK1fhpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高；非主流报价池 | Score 11; Tier Micro; LP $37.4K; Vol24H $4.45M; 24H +213.00%; V/LP 118.86x; 池数 1; 分项 L5/V17/B0/Buy8/Risk-43 | 只记录热度，不进入主榜 |

### D. 成熟池观察明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| [USDC](https://dexscreener.com/solana/djntgubgeqiucwe8f981m2c3zghzt2xld8f2sqdz6rsz) | SOL | [EPjFWd...yTDt1v](https://solscan.io/token/EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 74; Tier Liquid; LP $2.36M; Vol24H $9.88M; 24H +0.14%; V/LP 4.19x; 池数 5; 分项 L20/V17/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| ARK | BSC | [0xcae1...618b9d](https://bscscan.com/token/0xcae117ca6bc8a341d2e7207f30e180f0e5618b9d) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 74; Tier Mature; LP $58.69M; Vol24H $6.08M; 24H +0.63%; V/LP 0.10x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| ARIA | BSC | [0x5d3a...555238](https://bscscan.com/token/0x5d3a12c42e5372b2cc3264ab3cdcf660a1555238) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；成熟大市值 | Score 74; Tier Liquid; LP $2.10M; Vol24H $9.42M; 24H +5.79%; V/LP 4.47x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |

### E. 链上确认/紧急精查表
| Token | 链 | 合约地址 | 是否需要链上确认 | 紧急精查 | 预检状态 | 原因 |
|---|---|---|---|---|---|---|
| pippin | SOL | [Dfh5Dz...mApump](https://solscan.io/token/Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| CLAUDIA | SOL | [2j5SaS...hnW2ZM](https://solscan.io/token/2j5SaS7xy776qCBpyPQbZjyQSAtKiFgrwjfErthnW2ZM) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| BASED | BSC | [0x1d28...958e4d](https://bscscan.com/token/0x1d28d989f9e3ccb8b15d0cec601734514f958e4d) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| JCT | BSC | [0xea37...b17707](https://bscscan.com/token/0xea37a8de1de2d9d10772eeb569e28bfa5cb17707) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [PUMP](https://dexscreener.com/solana/7q2dqbjtxxp4dqmhec2nsgxwsytq8jaxdygswmag3pfp) | SOL | [9593dF...ysD6A1](https://solscan.io/token/9593dFjsLKKRAaz4LX1eK2DDEgrzfu3idb6yvMysD6A1) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；多池数据冲突，需链上/聚合源复核 |
| JAGENT | BSC | [0x8e64...e4ae15](https://bscscan.com/token/0x8e6442663a4f8c50b6132c68d42a30e7dfe4ae15) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| TTWO | SOL | [TTWofw...vQFbKo](https://solscan.io/token/TTWofwAge91oFhZs7kpQdyrVRkmevgM88xijGvQFbKo) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| PIEVERSE | BSC | [0x0e63...0225a9](https://bscscan.com/token/0x0e63b9c287e32a05e6b9ab8ee8df88a2760225a9) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| [GTASZN](https://dexscreener.com/solana/c3ai5bk7q9jttvcbwqeexsta99bmmlcnvyasdd7mnqbt) | SOL | [A4jXnW...TVpump](https://solscan.io/token/A4jXnWk1rDRDth6HmDASi45c89n1AguTHivAQPTVpump) | 是 | 否 | verified / address_preflight_v0.4 | 多池数据冲突，需链上/聚合源复核；PVP候选仅记录，非紧急精查 |
| [DCTY](https://dexscreener.com/solana/dchxq4qfppnpedfzlniwvphrvuufgfqedlaazbizhuwf) | SOL | [9hjBLB...f4pump](https://solscan.io/token/9hjBLBrc7WZW2H8UQvBAvG5WiTZotXUv2Bdcn4f4pump) | 是 | 否 | verified / address_preflight_v0.4 | 多池数据冲突，需链上/聚合源复核；PVP候选仅记录，非紧急精查 |

### F. 钱包行为 / AVE命中样本表
| Token | 链 | 合约地址 | 行为状态 | 行为层级 | AVE命中 | 判断 |
|---|---|---|---|---|---:|---|
| pippin | SOL | [Dfh5Dz...mApump](https://solscan.io/token/Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| CLAUDIA | SOL | [2j5SaS...hnW2ZM](https://solscan.io/token/2j5SaS7xy776qCBpyPQbZjyQSAtKiFgrwjfErthnW2ZM) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| BASED | BSC | [0x1d28...958e4d](https://bscscan.com/token/0x1d28d989f9e3ccb8b15d0cec601734514f958e4d) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| JCT | BSC | [0xea37...b17707](https://bscscan.com/token/0xea37a8de1de2d9d10772eeb569e28bfa5cb17707) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
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
| 主观察候选 | 5 个 | 主榜继续稀缺，但必须结合合约地址进入链上确认 |
| PVP风险池 | 8 个 | v0.3已单独展示明细，便于判断噪声来源 |
| 成熟池观察 | 3 个 | 成熟资产不占早期Alpha主榜 |
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