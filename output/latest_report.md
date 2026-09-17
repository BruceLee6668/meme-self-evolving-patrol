# 自我进化轮巡

**本轮时间 UTC：** 2026-09-17T20:51:50Z
**版本：** 0.5.0-ave-cache-wallet-behavior-prep
**S0 时间锚点：** 2026-06-16T16:15:17+09:00

## 一句话结论
本轮从 121 个合并Token中筛出 3 个主观察候选。v0.5已在v0.4.1基础上增加AVE周缓存真实接口接入框架、Smart Wallet持久保存、wallet_behavior_latest.json，以及BSC Transfer级钱包行为样本。注意：BSC当前是Transfer样本，不等同完整Swap解码。
合约地址可用 25 个，缺失 0 个；缺失地址的候选不能进入后续链上精查。

## 本轮扫描摘要
| 指标 | 数量 |
|---|---:|
| 原始池子记录 | 203 |
| 合并后Token | 121 |
| 输出候选 | 25 |
| 主观察 | 3 |
| 次观察 | 3 |
| PVP风险池 | 8 |
| 成熟池观察 | 5 |
| 低优先观察 | 6 |
| 多池Token | 7 |
| 多池冲突 | 2 |
| Symbol桥接合并 | 2 |
| 合约地址可用 | 25 |
| 合约地址缺失 | 0 |
| Micro层 | 7 |
| Early层 | 9 |
| Liquid层 | 5 |
| Mature层 | 4 |
| 需要链上确认 | 14 |
| 紧急精查候选 | 2 |

## v0.5 数据确认状态
| 项目 | 状态 |
|---|---|
| AVE Smart Wallet周缓存 | active，钱包数 1323，刷新时间 2026-09-14T02:37:35Z，是否过期 否 |
| 链上预检 | 本轮检查 12 个，验证通过 12 个，失败 0 个 |
| Helius状态 | 未配置，SOL使用公共RPC或跳过增强解析 |
| 当前精查层级 | 0.5.0-chain-preflight-plus-wallet-behavior：地址/账户预检 + v0.5钱包行为样本，完整Swap留存仍待下一版 |
| 钱包行为样本 | 本轮检查 3 个，BSC Transfer样本 1 个，SOL签名级 2 个，AVE钱包命中 0 个 |

## 第一部分：生成结果表格

### A. 上次记录结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| [CATE](https://dexscreener.com/solana/hmzvseemtzhhvznw9uwbag85hctmfnkbhzux16cy7ca3) | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | 主观察 | Score 91; Tier Liquid; LP $2.79M; Vol24H $5.33M; 24H -4.13%; V/LP 1.91x; 池数 2; 分项 L20/V17/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| $BANANA | BSC | [0x3d4f...a9a760](https://bscscan.com/token/0x3d4f0513e8a29669b960f9dbca61861548a9a760) | 主观察 | Score 84; Tier Liquid; LP $4.08M; Vol24H $1.50M; 24H +5.07%; V/LP 0.37x; 池数 1; 分项 L20/V15/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| 4 | BSC | [0x0a43...e14444](https://bscscan.com/token/0x0a43fc31a73013089df59194872ecae4cae14444) | 主观察 | Score 82; Tier Liquid; LP $1.61M; Vol24H $824.1K; 24H +2.93%; V/LP 0.51x; 池数 1; 分项 L20/V13/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [USDF](https://dexscreener.com/solana/9wnusyffb3n74db7zcj9xrv4nf3nr8p689eq5zrow1ez) | SOL | [ireZB2...tQpump](https://solscan.io/token/ireZB2cgtfvFcVQGLYRAzaugVapAzsjgJ1cMetQpump) | 次观察 | Score 71; Tier Early; LP $231.4K; Vol24H $176.8K; 24H +23.82%; V/LP 0.76x; 池数 2; 分项 L13/V9/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [GOAF](https://dexscreener.com/solana/agtlhkrtuasweddsjmmve5cdgpirkatcacavqvbuxf56) | SOL | [Zzph8p...Lcpump](https://solscan.io/token/Zzph8pgSqFBatiyi72Rum7SWKbhks3uyX3qyJLcpump) | 次观察 | Score 68; Tier Early; LP $158.4K; Vol24H $171.9K; 24H +14.09%; V/LP 1.09x; 池数 1; 分项 L11/V8/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [EMBER](https://dexscreener.com/solana/2y6pcqa4fep3jlifdan9jvmw7lsk8f3gwstfy8p7trae) | SOL | [5dvXTZ...k4QEC6](https://solscan.io/token/5dvXTZ5qwgafnHtwu3Ls3QrWx1U4LQsFeCuJgkk4QEC6) | 次观察 | Score 68; Tier Early; LP $353.1K; Vol24H $745.5K; 24H +16.29%; V/LP 2.11x; 池数 1; 分项 L14/V13/B17/Buy3/Risk-3 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [SpaceX Meme](https://dexscreener.com/bsc/0xd0dd21d8dbcf95551647f15aea03e1d275a15632) | BSC | [0x28E6...03167E](https://bscscan.com/token/0x28E69efCF168813113E039341cBA335d1303167E) | 次观察 | Score 64; Tier Micro; LP $95.1K; Vol24H $64.1K; 24H +0.20%; V/LP 0.67x; 池数 1; 分项 L9/V6/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [PAID](https://dexscreener.com/solana/6e3jzltf4tqbwzm3f7a66jf8tfzn6mrqvrbdfgcnwara) | SOL | [98kfF7...zypump](https://solscan.io/token/98kfF7rmsg1QDUEoCqNE7g7M1FdrTt92TEp2CLzypump) | PVP风险池 | Score 44; Tier Early; LP $667.3K; Vol24H $25.55M; 24H +62.15%; V/LP 38.29x; 池数 2; 分项 L17/V17/B8/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [ELON](https://dexscreener.com/solana/6tuhhpysinf41v39kw3jmpvuaxehcabcbhzqqfnwr6xf) | SOL | [GY9mZf...zxpump](https://solscan.io/token/GY9mZfyPpxXxBXBxS2hB2XjhP3kfUsywTvgveozxpump) | PVP风险池 | Score 39; Tier Early; LP $213.1K; Vol24H $7.56M; 24H +31.24%; V/LP 35.49x; 池数 1; 分项 L12/V17/B8/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| priceless | BSC | [0x7d03...a24444](https://bscscan.com/token/0x7d03759e5b41e36899833cb2e008455d69a24444) | PVP风险池 | Score 33; Tier Early; LP $169.6K; Vol24H $4.42M; 24H +28.05%; V/LP 26.09x; 池数 1; 分项 L11/V17/B8/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### B. 本轮扫描结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| [CATE](https://dexscreener.com/solana/hmzvseemtzhhvznw9uwbag85hctmfnkbhzux16cy7ca3) | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | 主观察 | Score 86; Tier Liquid; LP $2.75M; Vol24H $4.68M; 24H -13.91%; V/LP 1.70x; 池数 2; 分项 L20/V17/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| EMBER | SOL | [5dvXTZ...k4QEC6](https://solscan.io/token/5dvXTZ5qwgafnHtwu3Ls3QrWx1U4LQsFeCuJgkk4QEC6) | 主观察 | Score 83; Tier Early; LP $557.1K; Vol24H $856.9K; 24H +1.42%; V/LP 1.54x; 池数 2; 分项 L16/V13/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| 4 | BSC | [0x0a43...e14444](https://bscscan.com/token/0x0a43fc31a73013089df59194872ecae4cae14444) | 主观察 | Score 82; Tier Liquid; LP $1.61M; Vol24H $716.9K; 24H +7.64%; V/LP 0.45x; 池数 1; 分项 L20/V13/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| 蝴蝶人生 | BSC | [0x87ae...a47777](https://bscscan.com/token/0x87ae267002cd1ea0ec86bf3601d4a8ad76a47777) | 次观察 | Score 73; Tier Early; LP $577.8K; Vol24H $5.47M; 24H -6.29%; V/LP 9.47x; 池数 6; 分项 L16/V17/B22/Buy12/Risk-18 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [USDF](https://dexscreener.com/solana/9wnusyffb3n74db7zcj9xrv4nf3nr8p689eq5zrow1ez) | SOL | [ireZB2...tQpump](https://solscan.io/token/ireZB2cgtfvFcVQGLYRAzaugVapAzsjgJ1cMetQpump) | 次观察 | Score 71; Tier Early; LP $233.3K; Vol24H $177.4K; 24H +21.12%; V/LP 0.76x; 池数 2; 分项 L13/V9/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [GOAF](https://dexscreener.com/solana/agtlhkrtuasweddsjmmve5cdgpirkatcacavqvbuxf56) | SOL | [Zzph8p...Lcpump](https://solscan.io/token/Zzph8pgSqFBatiyi72Rum7SWKbhks3uyX3qyJLcpump) | 次观察 | Score 68; Tier Early; LP $157.3K; Vol24H $173.1K; 24H +8.82%; V/LP 1.10x; 池数 1; 分项 L11/V8/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| CNPY | BSC | [0xc69b...90ddd2](https://bscscan.com/token/0xc69b16cf18cea1e5d0bb6a1a9db802097790ddd2) | PVP风险池 | Score 39; Tier Liquid; LP $1.73M; Vol24H $39.47M; 24H +34.78%; V/LP 22.80x; 池数 1; 分项 L20/V17/B8/Buy0/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [WISH](https://dexscreener.com/solana/eqhjvdrgee9q2jecgpemteyj1r9yp9unefvkzueckfzd) | SOL | [4qpraJ...ab5a3U](https://solscan.io/token/4qpraJNwVi8yXn2hx6xxVnsifin1PEhJ8Nv61sab5a3U) | PVP风险池 | Score 25; Tier Micro; LP $50.9K; Vol24H $3.64M; 24H +644.00%; V/LP 71.55x; 池数 1; 分项 L6/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [DONO](https://dexscreener.com/solana/5gibz4fz89tovrn3lejckphcv1w53zldimcmrjnbafpm) | SOL | [9HB7ui...1Wpump](https://solscan.io/token/9HB7uiNQeWTGG1tkuGaMQLhdt9Lg6vmJ4vtLJc1Wpump) | PVP风险池 | Score 22; Tier Micro; LP $35.7K; Vol24H $4.39M; 24H -75.16%; V/LP 123.16x; 池数 1; 分项 L5/V17/B8/Buy8/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [KEVIN](https://dexscreener.com/solana/gignjzirab1l5iyqbqtowl13turtxw5ugdyawhwcjayg) | SOL | [GZik7v...v8A3iE](https://solscan.io/token/GZik7vJSnDAao9tbbcLrMGKfxLu7VCjoAtkDhsv8A3iE) | PVP风险池 | Score 14; Tier Micro; LP $36.1K; Vol24H $6.97M; 24H +229.00%; V/LP 192.91x; 池数 1; 分项 L5/V17/B0/Buy8/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [MEME](https://dexscreener.com/bsc/0x0bac5f3b7898be0c81bfb39c1020640eff889882) | BSC | [0xdA2F...9BfFfF](https://bscscan.com/token/0xdA2F0859b2C1Faa00018DA1E3D078021589BfFfF) | PVP风险池 | Score 6; Tier Micro; LP $33.5K; Vol24H $4.26M; 24H +97.14%; V/LP 127.38x; 池数 3; 分项 L5/V17/B0/Buy3/Risk-43 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [Tilcayo](https://dexscreener.com/solana/asgoadvedl8zjn6kluimsh9m8x2yyaezpsuspvxhj3ly) | SOL | [AyYNfP...s2thto](https://solscan.io/token/AyYNfPtftg2zDP4ZbgcoQMggQtwLh4zpfVVmUJs2thto) | PVP风险池 | Score 4; Tier Early; LP $122.1K; Vol24H $5.17M; 24H +3673.00%; V/LP 42.32x; 池数 1; 分项 L10/V17/B0/Buy8/Risk-55 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [SOLCAT](https://dexscreener.com/solana/9hr6nxw5wsffxnqnqxwzyhrw81uz3ppb7rf9j3i9nmt1) | SOL | [9U1f18...P69bh1](https://solscan.io/token/9U1f18idDeySFnYrurxqT1f5n5nE4g4Uk5LLzP69bh1) | PVP风险池 | Score 4; Tier Early; LP $109.5K; Vol24H $5.02M; 24H +3025.00%; V/LP 45.86x; 池数 1; 分项 L10/V17/B0/Buy8/Risk-55 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [SUUB](https://dexscreener.com/solana/cs8i2jemyyun9e15ca9cq9uxgq2uaml8nklcexkf5gxg) | SOL | [CrrcQs...qPpump](https://solscan.io/token/CrrcQsPD5zNW2hEKhBy5ARP1haGBKAmoqsgD8dqPpump) | PVP风险池 | Score 0; Tier Micro; LP $27.6K; Vol24H $4.86M; 24H +103.00%; V/LP 176.01x; 池数 1; 分项 L4/V17/B0/Buy8/Risk-65 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| BTCB | BSC | [0x7130...3ead9c](https://bscscan.com/token/0x7130d2a12b9bcbfae4f2634d864a1ee1ce3ead9c) | 成熟池观察 | Score 74; Tier Mature; LP $25.94M; Vol24H $12.05M; 24H +0.40%; V/LP 0.46x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-12 | 钱包级数据不可用；当前仅代理指标；资产偏成熟，不按早期吸筹处理；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 成熟池观察，不占用早期Alpha主榜 |

### C. PVP风险池明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| CNPY | BSC | [0xc69b...90ddd2](https://bscscan.com/token/0xc69b16cf18cea1e5d0bb6a1a9db802097790ddd2) | 24H未过热但已明显波动；LP达主观察门槛；24H成交合格；卖出笔数占优；Volume/LP极端偏高 | Score 39; Tier Liquid; LP $1.73M; Vol24H $39.47M; 24H +34.78%; V/LP 22.80x; 池数 1; 分项 L20/V17/B8/Buy0/Risk-30 | 只记录热度，不进入主榜 |
| [WISH](https://dexscreener.com/solana/eqhjvdrgee9q2jecgpemteyj1r9yp9unefvkzueckfzd) | SOL | [4qpraJ...ab5a3U](https://solscan.io/token/4qpraJNwVi8yXn2hx6xxVnsifin1PEhJ8Nv61sab5a3U) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 25; Tier Micro; LP $50.9K; Vol24H $3.64M; 24H +644.00%; V/LP 71.55x; 池数 1; 分项 L6/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [DONO](https://dexscreener.com/solana/5gibz4fz89tovrn3lejckphcv1w53zldimcmrjnbafpm) | SOL | [9HB7ui...1Wpump](https://solscan.io/token/9HB7uiNQeWTGG1tkuGaMQLhdt9Lg6vmJ4vtLJc1Wpump) | 24H未过热但已明显波动；买卖略偏买入；LP未达主观察门槛；24H成交合格；LP偏薄；Volume/LP极端偏高 | Score 22; Tier Micro; LP $35.7K; Vol24H $4.39M; 24H -75.16%; V/LP 123.16x; 池数 1; 分项 L5/V17/B8/Buy8/Risk-40 | 只记录热度，不进入主榜 |
| [KEVIN](https://dexscreener.com/solana/gignjzirab1l5iyqbqtowl13turtxw5ugdyawhwcjayg) | SOL | [GZik7v...v8A3iE](https://solscan.io/token/GZik7vJSnDAao9tbbcLrMGKfxLu7VCjoAtkDhsv8A3iE) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 14; Tier Micro; LP $36.1K; Vol24H $6.97M; 24H +229.00%; V/LP 192.91x; 池数 1; 分项 L5/V17/B0/Buy8/Risk-40 | 只记录热度，不进入主榜 |
| [MEME](https://dexscreener.com/bsc/0x0bac5f3b7898be0c81bfb39c1020640eff889882) | BSC | [0xdA2F...9BfFfF](https://bscscan.com/token/0xdA2F0859b2C1Faa00018DA1E3D078021589BfFfF) | 买卖基本均衡；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高；非主流报价池 | Score 6; Tier Micro; LP $33.5K; Vol24H $4.26M; 24H +97.14%; V/LP 127.38x; 池数 3; 分项 L5/V17/B0/Buy3/Risk-43 | 只记录热度，不进入主榜 |
| [Tilcayo](https://dexscreener.com/solana/asgoadvedl8zjn6kluimsh9m8x2yyaezpsuspvxhj3ly) | SOL | [AyYNfP...s2thto](https://solscan.io/token/AyYNfPtftg2zDP4ZbgcoQMggQtwLh4zpfVVmUJs2thto) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高；年轻币短期暴拉 | Score 4; Tier Early; LP $122.1K; Vol24H $5.17M; 24H +3673.00%; V/LP 42.32x; 池数 1; 分项 L10/V17/B0/Buy8/Risk-55 | 只记录热度，不进入主榜 |
| [SOLCAT](https://dexscreener.com/solana/9hr6nxw5wsffxnqnqxwzyhrw81uz3ppb7rf9j3i9nmt1) | SOL | [9U1f18...P69bh1](https://solscan.io/token/9U1f18idDeySFnYrurxqT1f5n5nE4g4Uk5LLzP69bh1) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高；年轻币短期暴拉 | Score 4; Tier Early; LP $109.5K; Vol24H $5.02M; 24H +3025.00%; V/LP 45.86x; 池数 1; 分项 L10/V17/B0/Buy8/Risk-55 | 只记录热度，不进入主榜 |
| [SUUB](https://dexscreener.com/solana/cs8i2jemyyun9e15ca9cq9uxgq2uaml8nklcexkf5gxg) | SOL | [CrrcQs...qPpump](https://solscan.io/token/CrrcQsPD5zNW2hEKhBy5ARP1haGBKAmoqsgD8dqPpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高；年轻币短期暴拉 | Score 0; Tier Micro; LP $27.6K; Vol24H $4.86M; 24H +103.00%; V/LP 176.01x; 池数 1; 分项 L4/V17/B0/Buy8/Risk-65 | 只记录热度，不进入主榜 |

### D. 成熟池观察明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| BTCB | BSC | [0x7130...3ead9c](https://bscscan.com/token/0x7130d2a12b9bcbfae4f2634d864a1ee1ce3ead9c) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 74; Tier Mature; LP $25.94M; Vol24H $12.05M; 24H +0.40%; V/LP 0.46x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| STONK | SOL | [6GmAFS...MpUNgx](https://solscan.io/token/6GmAFSYs4gk3FDao5FzzySQpPZaWsa4rUJHacpMpUNgx) | 24H波动可控；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 74; Tier Mature; LP $6.74M; Vol24H $4.40M; 24H +22.08%; V/LP 0.65x; 池数 2; 分项 L20/V17/B17/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| USELESS | SOL | [Dz9mQ9...8Mbonk](https://solscan.io/token/Dz9mQ9NzkBcCsuGPFJ3r1bS4wgqKMHBPiVuniW8Mbonk) | 24H波动可控；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 74; Tier Mature; LP $5.06M; Vol24H $2.86M; 24H +13.86%; V/LP 0.56x; 池数 1; 分项 L20/V17/B17/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| [ANSEM](https://dexscreener.com/solana/fnzky6x7entq1er3d225dqyt7ybfka4pskbmqhb8l3cc) | SOL | [9cRCn9...TGpump](https://solscan.io/token/9cRCn9rGT8V2imeM2BaKs13yhMEais3ruM3rPvTGpump) | 24H波动可控；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 73; Tier Liquid; LP $2.18M; Vol24H $2.10M; 24H +9.58%; V/LP 0.96x; 池数 1; 分项 L20/V16/B17/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| ZCAT | SOL | [HcRLc9...qiDeJR](https://solscan.io/token/HcRLc9VDgjLeK154xDawfb1dmVJ98DoSqcwTHGqiDeJR) | 24H未过热但已明显波动；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 59; Tier Liquid; LP $1.63M; Vol24H $2.39M; 24H +36.51%; V/LP 1.47x; 池数 1; 分项 L20/V16/B8/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |

### E. 链上确认/紧急精查表
| Token | 链 | 合约地址 | 是否需要链上确认 | 紧急精查 | 预检状态 | 原因 |
|---|---|---|---|---|---|---|
| [CATE](https://dexscreener.com/solana/hmzvseemtzhhvznw9uwbag85hctmfnkbhzux16cy7ca3) | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| EMBER | SOL | [5dvXTZ...k4QEC6](https://solscan.io/token/5dvXTZ5qwgafnHtwu3Ls3QrWx1U4LQsFeCuJgkk4QEC6) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| 4 | BSC | [0x0a43...e14444](https://bscscan.com/token/0x0a43fc31a73013089df59194872ecae4cae14444) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| 蝴蝶人生 | BSC | [0x87ae...a47777](https://bscscan.com/token/0x87ae267002cd1ea0ec86bf3601d4a8ad76a47777) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；多池数据冲突，需链上/聚合源复核 |
| [USDF](https://dexscreener.com/solana/9wnusyffb3n74db7zcj9xrv4nf3nr8p689eq5zrow1ez) | SOL | [ireZB2...tQpump](https://solscan.io/token/ireZB2cgtfvFcVQGLYRAzaugVapAzsjgJ1cMetQpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；多池数据冲突，需链上/聚合源复核 |
| [GOAF](https://dexscreener.com/solana/agtlhkrtuasweddsjmmve5cdgpirkatcacavqvbuxf56) | SOL | [Zzph8p...Lcpump](https://solscan.io/token/Zzph8pgSqFBatiyi72Rum7SWKbhks3uyX3qyJLcpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| CNPY | BSC | [0xc69b...90ddd2](https://bscscan.com/token/0xc69b16cf18cea1e5d0bb6a1a9db802097790ddd2) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| [WISH](https://dexscreener.com/solana/eqhjvdrgee9q2jecgpemteyj1r9yp9unefvkzueckfzd) | SOL | [4qpraJ...ab5a3U](https://solscan.io/token/4qpraJNwVi8yXn2hx6xxVnsifin1PEhJ8Nv61sab5a3U) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| [DONO](https://dexscreener.com/solana/5gibz4fz89tovrn3lejckphcv1w53zldimcmrjnbafpm) | SOL | [9HB7ui...1Wpump](https://solscan.io/token/9HB7uiNQeWTGG1tkuGaMQLhdt9Lg6vmJ4vtLJc1Wpump) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| [KEVIN](https://dexscreener.com/solana/gignjzirab1l5iyqbqtowl13turtxw5ugdyawhwcjayg) | SOL | [GZik7v...v8A3iE](https://solscan.io/token/GZik7vJSnDAao9tbbcLrMGKfxLu7VCjoAtkDhsv8A3iE) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |

### F. 钱包行为 / AVE命中样本表
| Token | 链 | 合约地址 | 行为状态 | 行为层级 | AVE命中 | 判断 |
|---|---|---|---|---|---:|---|
| [CATE](https://dexscreener.com/solana/hmzvseemtzhhvznw9uwbag85hctmfnkbhzux16cy7ca3) | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| EMBER | SOL | [5dvXTZ...k4QEC6](https://solscan.io/token/5dvXTZ5qwgafnHtwu3Ls3QrWx1U4LQsFeCuJgkk4QEC6) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| 4 | BSC | [0x0a43...e14444](https://bscscan.com/token/0x0a43fc31a73013089df59194872ecae4cae14444) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |

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
| 成熟池观察 | 5 个 | 成熟资产不占早期Alpha主榜 |
| 合约地址覆盖 | 可用 25，缺失 0 | 地址缺失会阻断BSC RPC/Helius精查，需要优先补齐 |
| LP层级 | Micro 7 / Early 9 / Liquid 5 / Mature 4 | 下一步可以按层级分别设置进攻规则 |
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
| dexscreener_search | {'ok': True, 'count': 337} |
| geckoterminal_bsc_trending | {'ok': True, 'count': 20} |
| geckoterminal_solana_trending | {'ok': True, 'count': 20} |

## 数据限制
- This v0.4 scan uses free public sources plus lightweight chain address/account preflight when enabled.
- AVE Smart Money weekly cache structure is connected; real AVE API refresh is handled by the weekly workflow/cache file.
- S0 exact historical replay is not implemented yet; candidates are marked with current metrics only.
- Wallet-level buy/sell retention is not implemented yet; v0.4 only preflights token contract/account existence.
- v0.4 adds chain preflight status and Smart Wallet cache status on top of contract-address output, liquidity tiers, visible PVP/mature detail tables, and chain-verify flags.
- Contract addresses are extracted from DEXScreener baseToken or GeckoTerminal relationships when available; missing addresses are explicitly marked unavailable.