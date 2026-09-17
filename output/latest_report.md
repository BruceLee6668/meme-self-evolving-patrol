# 自我进化轮巡

**本轮时间 UTC：** 2026-09-17T17:30:46Z
**版本：** 0.5.0-ave-cache-wallet-behavior-prep
**S0 时间锚点：** 2026-06-16T16:15:17+09:00

## 一句话结论
本轮从 129 个合并Token中筛出 3 个主观察候选。v0.5已在v0.4.1基础上增加AVE周缓存真实接口接入框架、Smart Wallet持久保存、wallet_behavior_latest.json，以及BSC Transfer级钱包行为样本。注意：BSC当前是Transfer样本，不等同完整Swap解码。
合约地址可用 25 个，缺失 0 个；缺失地址的候选不能进入后续链上精查。

## 本轮扫描摘要
| 指标 | 数量 |
|---|---:|
| 原始池子记录 | 208 |
| 合并后Token | 129 |
| 输出候选 | 25 |
| 主观察 | 3 |
| 次观察 | 4 |
| PVP风险池 | 8 |
| 成熟池观察 | 6 |
| 低优先观察 | 4 |
| 多池Token | 7 |
| 多池冲突 | 2 |
| Symbol桥接合并 | 2 |
| 合约地址可用 | 25 |
| 合约地址缺失 | 0 |
| Micro层 | 7 |
| Early层 | 9 |
| Liquid层 | 6 |
| Mature层 | 3 |
| 需要链上确认 | 16 |
| 紧急精查候选 | 1 |

## v0.5 数据确认状态
| 项目 | 状态 |
|---|---|
| AVE Smart Wallet周缓存 | active，钱包数 1323，刷新时间 2026-09-14T02:37:35Z，是否过期 否 |
| 链上预检 | 本轮检查 12 个，验证通过 12 个，失败 0 个 |
| Helius状态 | 未配置，SOL使用公共RPC或跳过增强解析 |
| 当前精查层级 | 0.5.0-chain-preflight-plus-wallet-behavior：地址/账户预检 + v0.5钱包行为样本，完整Swap留存仍待下一版 |
| 钱包行为样本 | 本轮检查 3 个，BSC Transfer样本 2 个，SOL签名级 1 个，AVE钱包命中 0 个 |

## 第一部分：生成结果表格

### A. 上次记录结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| [CATE](https://dexscreener.com/solana/hmzvseemtzhhvznw9uwbag85hctmfnkbhzux16cy7ca3) | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | 主观察 | Score 91; Tier Liquid; LP $2.77M; Vol24H $5.62M; 24H -6.47%; V/LP 2.03x; 池数 2; 分项 L20/V17/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| $BANANA | BSC | [0x3d4f...a9a760](https://bscscan.com/token/0x3d4f0513e8a29669b960f9dbca61861548a9a760) | 主观察 | Score 84; Tier Liquid; LP $4.04M; Vol24H $1.54M; 24H +1.78%; V/LP 0.38x; 池数 1; 分项 L20/V15/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| AIN | BSC | [0x9558...84f4a3](https://bscscan.com/token/0x9558a9254890b2a8b057a789f413631b9084f4a3) | 主观察 | Score 81; Tier Liquid; LP $1.10M; Vol24H $690.3K; 24H -4.67%; V/LP 0.63x; 池数 1; 分项 L19/V13/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| 蝴蝶人生 | BSC | [0x87ae...a47777](https://bscscan.com/token/0x87ae267002cd1ea0ec86bf3601d4a8ad76a47777) | 主观察 | Score 78; Tier Early; LP $676.8K; Vol24H $5.24M; 24H +72.42%; V/LP 7.74x; 池数 9; 分项 L17/V17/B8/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| biketyson | SOL | [CbyTNf...Pwpump](https://solscan.io/token/CbyTNf7UPzvewHh4Zp6umogM2RWahhmGRJWLJnPwpump) | 次观察 | Score 68; Tier Early; LP $205.4K; Vol24H $540.5K; 24H -12.84%; V/LP 2.63x; 池数 2; 分项 L12/V12/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [RAYCAT](https://dexscreener.com/solana/987vwvjz5frjwcy9zwc2trugl8fbmt1af4purt7xjpjd) | SOL | [CFNRDa...jNupFL](https://solscan.io/token/CFNRDaxFcvRwRSNnA5cHrCCr6AHhk9dNkHWpRUjNupFL) | 次观察 | Score 65; Tier Early; LP $460.1K; Vol24H $760.2K; 24H +42.29%; V/LP 1.65x; 池数 1; 分项 L15/V13/B8/Buy8/Risk-3 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| CNPY | BSC | [0xc69b...90ddd2](https://bscscan.com/token/0xc69b16cf18cea1e5d0bb6a1a9db802097790ddd2) | 次观察 | Score 65; Tier Liquid; LP $1.60M; Vol24H $28.98M; 24H -0.17%; V/LP 18.14x; 池数 1; 分项 L20/V17/B22/Buy0/Risk-18 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [SpaceX Meme](https://dexscreener.com/bsc/0xd0dd21d8dbcf95551647f15aea03e1d275a15632) | BSC | [0x28E6...03167E](https://bscscan.com/token/0x28E69efCF168813113E039341cBA335d1303167E) | 次观察 | Score 64; Tier Micro; LP $95.5K; Vol24H $63.8K; 24H +2.90%; V/LP 0.67x; 池数 1; 分项 L9/V6/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [ELON](https://dexscreener.com/solana/6tuhhpysinf41v39kw3jmpvuaxehcabcbhzqqfnwr6xf) | SOL | [GY9mZf...zxpump](https://solscan.io/token/GY9mZfyPpxXxBXBxS2hB2XjhP3kfUsywTvgveozxpump) | PVP风险池 | Score 39; Tier Early; LP $193.8K; Vol24H $8.20M; 24H +65.02%; V/LP 42.30x; 池数 1; 分项 L12/V17/B8/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [lockinu](https://dexscreener.com/solana/f8slh2bav3mcr7vqorzdpcmzvave3sjoveeese3ovgmh) | SOL | [7GPGqs...EHpump](https://solscan.io/token/7GPGqsfVK1gG88GuVEetrsVyDiikABTsj9B9aHEHpump) | PVP风险池 | Score 34; Tier Micro; LP $51.8K; Vol24H $3.49M; 24H -65.47%; V/LP 67.34x; 池数 1; 分项 L7/V17/B8/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### B. 本轮扫描结果表
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
| [WISH](https://dexscreener.com/solana/eqhjvdrgee9q2jecgpemteyj1r9yp9unefvkzueckfzd) | SOL | [4qpraJ...ab5a3U](https://solscan.io/token/4qpraJNwVi8yXn2hx6xxVnsifin1PEhJ8Nv61sab5a3U) | PVP风险池 | Score 25; Tier Micro; LP $50.2K; Vol24H $3.54M; 24H +625.00%; V/LP 70.55x; 池数 1; 分项 L6/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [PAIDDOGE](https://dexscreener.com/solana/bs7ad8ehzb4njfcsnewodg2yulxrvdnplu4wgkjj2sqj) | SOL | [52qkNp...Kqpump](https://solscan.io/token/52qkNpgTHcjuDYhKVcg6rJS4uYYtJHpDRcJoSdKqpump) | PVP风险池 | Score 21; Tier Micro; LP $27.3K; Vol24H $5.36M; 24H -30.22%; V/LP 196.31x; 池数 1; 分项 L4/V17/B8/Buy8/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [KEVIN](https://dexscreener.com/solana/gignjzirab1l5iyqbqtowl13turtxw5ugdyawhwcjayg) | SOL | [GZik7v...v8A3iE](https://solscan.io/token/GZik7vJSnDAao9tbbcLrMGKfxLu7VCjoAtkDhsv8A3iE) | PVP风险池 | Score 15; Tier Micro; LP $45.5K; Vol24H $6.89M; 24H +412.00%; V/LP 151.47x; 池数 1; 分项 L6/V17/B0/Buy8/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [DONO](https://dexscreener.com/solana/5gibz4fz89tovrn3lejckphcv1w53zldimcmrjnbafpm) | SOL | [9HB7ui...1Wpump](https://solscan.io/token/9HB7uiNQeWTGG1tkuGaMQLhdt9Lg6vmJ4vtLJc1Wpump) | PVP风险池 | Score 15; Tier Micro; LP $47.3K; Vol24H $5.62M; 24H +461.00%; V/LP 118.93x; 池数 1; 分项 L6/V17/B0/Buy8/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [MEME](https://dexscreener.com/bsc/0x0bac5f3b7898be0c81bfb39c1020640eff889882) | BSC | [0xdA2F...9BfFfF](https://bscscan.com/token/0xdA2F0859b2C1Faa00018DA1E3D078021589BfFfF) | PVP风险池 | Score 6; Tier Micro; LP $39.3K; Vol24H $4.22M; 24H +173.00%; V/LP 107.52x; 池数 3; 分项 L5/V17/B0/Buy3/Risk-43 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### C. PVP风险池明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| [PAID](https://dexscreener.com/solana/6e3jzltf4tqbwzm3f7a66jf8tfzn6mrqvrbdfgcnwara) | SOL | [98kfF7...zypump](https://solscan.io/token/98kfF7rmsg1QDUEoCqNE7g7M1FdrTt92TEp2CLzypump) | 24H未过热但已明显波动；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 44; Tier Early; LP $667.3K; Vol24H $25.55M; 24H +62.15%; V/LP 38.29x; 池数 2; 分项 L17/V17/B8/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [ELON](https://dexscreener.com/solana/6tuhhpysinf41v39kw3jmpvuaxehcabcbhzqqfnwr6xf) | SOL | [GY9mZf...zxpump](https://solscan.io/token/GY9mZfyPpxXxBXBxS2hB2XjhP3kfUsywTvgveozxpump) | 24H未过热但已明显波动；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 39; Tier Early; LP $213.1K; Vol24H $7.56M; 24H +31.24%; V/LP 35.49x; 池数 1; 分项 L12/V17/B8/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| priceless | BSC | [0x7d03...a24444](https://bscscan.com/token/0x7d03759e5b41e36899833cb2e008455d69a24444) | 24H未过热但已明显波动；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 33; Tier Early; LP $169.6K; Vol24H $4.42M; 24H +28.05%; V/LP 26.09x; 池数 1; 分项 L11/V17/B8/Buy3/Risk-30 | 只记录热度，不进入主榜 |
| [WISH](https://dexscreener.com/solana/eqhjvdrgee9q2jecgpemteyj1r9yp9unefvkzueckfzd) | SOL | [4qpraJ...ab5a3U](https://solscan.io/token/4qpraJNwVi8yXn2hx6xxVnsifin1PEhJ8Nv61sab5a3U) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 25; Tier Micro; LP $50.2K; Vol24H $3.54M; 24H +625.00%; V/LP 70.55x; 池数 1; 分项 L6/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [PAIDDOGE](https://dexscreener.com/solana/bs7ad8ehzb4njfcsnewodg2yulxrvdnplu4wgkjj2sqj) | SOL | [52qkNp...Kqpump](https://solscan.io/token/52qkNpgTHcjuDYhKVcg6rJS4uYYtJHpDRcJoSdKqpump) | 24H未过热但已明显波动；买卖略偏买入；LP未达主观察门槛；24H成交合格；LP偏薄；Volume/LP极端偏高 | Score 21; Tier Micro; LP $27.3K; Vol24H $5.36M; 24H -30.22%; V/LP 196.31x; 池数 1; 分项 L4/V17/B8/Buy8/Risk-40 | 只记录热度，不进入主榜 |
| [KEVIN](https://dexscreener.com/solana/gignjzirab1l5iyqbqtowl13turtxw5ugdyawhwcjayg) | SOL | [GZik7v...v8A3iE](https://solscan.io/token/GZik7vJSnDAao9tbbcLrMGKfxLu7VCjoAtkDhsv8A3iE) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 15; Tier Micro; LP $45.5K; Vol24H $6.89M; 24H +412.00%; V/LP 151.47x; 池数 1; 分项 L6/V17/B0/Buy8/Risk-40 | 只记录热度，不进入主榜 |
| [DONO](https://dexscreener.com/solana/5gibz4fz89tovrn3lejckphcv1w53zldimcmrjnbafpm) | SOL | [9HB7ui...1Wpump](https://solscan.io/token/9HB7uiNQeWTGG1tkuGaMQLhdt9Lg6vmJ4vtLJc1Wpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 15; Tier Micro; LP $47.3K; Vol24H $5.62M; 24H +461.00%; V/LP 118.93x; 池数 1; 分项 L6/V17/B0/Buy8/Risk-40 | 只记录热度，不进入主榜 |
| [MEME](https://dexscreener.com/bsc/0x0bac5f3b7898be0c81bfb39c1020640eff889882) | BSC | [0xdA2F...9BfFfF](https://bscscan.com/token/0xdA2F0859b2C1Faa00018DA1E3D078021589BfFfF) | 买卖基本均衡；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高；非主流报价池 | Score 6; Tier Micro; LP $39.3K; Vol24H $4.22M; 24H +173.00%; V/LP 107.52x; 池数 3; 分项 L5/V17/B0/Buy3/Risk-43 | 只记录热度，不进入主榜 |

### D. 成熟池观察明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| BTCB | BSC | [0x7130...3ead9c](https://bscscan.com/token/0x7130d2a12b9bcbfae4f2634d864a1ee1ce3ead9c) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 74; Tier Mature; LP $25.98M; Vol24H $13.35M; 24H +1.52%; V/LP 0.51x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| [ANSEM](https://dexscreener.com/solana/fnzky6x7entq1er3d225dqyt7ybfka4pskbmqhb8l3cc) | SOL | [9cRCn9...TGpump](https://solscan.io/token/9cRCn9rGT8V2imeM2BaKs13yhMEais3ruM3rPvTGpump) | 24H波动可控；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 73; Tier Liquid; LP $2.16M; Vol24H $1.86M; 24H +9.46%; V/LP 0.86x; 池数 1; 分项 L20/V16/B17/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| USELESS | SOL | [Dz9mQ9...8Mbonk](https://solscan.io/token/Dz9mQ9NzkBcCsuGPFJ3r1bS4wgqKMHBPiVuniW8Mbonk) | 24H波动可控；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 73; Tier Mature; LP $5.03M; Vol24H $2.44M; 24H +14.29%; V/LP 0.48x; 池数 1; 分项 L20/V16/B17/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| [RAY](https://dexscreener.com/solana/2axxcn6on9bbt5owwmth53c7qhuxvhleu718kqt8rvy2) | SOL | [4k3Dyj...QrkX6R](https://solscan.io/token/4k3Dyjzvzp8eMZWUXbBCjEvwSkkk59S5iCNLY3QrkX6R) | 24H波动可控；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 69; Tier Liquid; LP $2.80M; Vol24H $10.99M; 24H +11.04%; V/LP 3.93x; 池数 1; 分项 L20/V17/B17/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| STONK | SOL | [6GmAFS...MpUNgx](https://solscan.io/token/6GmAFSYs4gk3FDao5FzzySQpPZaWsa4rUJHacpMpUNgx) | 24H未过热但已明显波动；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 65; Tier Mature; LP $6.63M; Vol24H $3.45M; 24H +46.05%; V/LP 0.52x; 池数 2; 分项 L20/V17/B8/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| ZCAT | SOL | [HcRLc9...qiDeJR](https://solscan.io/token/HcRLc9VDgjLeK154xDawfb1dmVJ98DoSqcwTHGqiDeJR) | 24H未过热但已明显波动；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 59; Tier Liquid; LP $1.68M; Vol24H $1.96M; 24H +47.22%; V/LP 1.17x; 池数 1; 分项 L20/V16/B8/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |

### E. 链上确认/紧急精查表
| Token | 链 | 合约地址 | 是否需要链上确认 | 紧急精查 | 预检状态 | 原因 |
|---|---|---|---|---|---|---|
| [CATE](https://dexscreener.com/solana/hmzvseemtzhhvznw9uwbag85hctmfnkbhzux16cy7ca3) | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| $BANANA | BSC | [0x3d4f...a9a760](https://bscscan.com/token/0x3d4f0513e8a29669b960f9dbca61861548a9a760) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| 4 | BSC | [0x0a43...e14444](https://bscscan.com/token/0x0a43fc31a73013089df59194872ecae4cae14444) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [USDF](https://dexscreener.com/solana/9wnusyffb3n74db7zcj9xrv4nf3nr8p689eq5zrow1ez) | SOL | [ireZB2...tQpump](https://solscan.io/token/ireZB2cgtfvFcVQGLYRAzaugVapAzsjgJ1cMetQpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；多池数据冲突，需链上/聚合源复核 |
| [GOAF](https://dexscreener.com/solana/agtlhkrtuasweddsjmmve5cdgpirkatcacavqvbuxf56) | SOL | [Zzph8p...Lcpump](https://solscan.io/token/Zzph8pgSqFBatiyi72Rum7SWKbhks3uyX3qyJLcpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [EMBER](https://dexscreener.com/solana/2y6pcqa4fep3jlifdan9jvmw7lsk8f3gwstfy8p7trae) | SOL | [5dvXTZ...k4QEC6](https://solscan.io/token/5dvXTZ5qwgafnHtwu3Ls3QrWx1U4LQsFeCuJgkk4QEC6) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [SpaceX Meme](https://dexscreener.com/bsc/0xd0dd21d8dbcf95551647f15aea03e1d275a15632) | BSC | [0x28E6...03167E](https://bscscan.com/token/0x28E69efCF168813113E039341cBA335d1303167E) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| 蝴蝶人生 | BSC | [0x87ae...a47777](https://bscscan.com/token/0x87ae267002cd1ea0ec86bf3601d4a8ad76a47777) | 是 | 否 | verified / address_preflight_v0.4 | 多池数据冲突，需链上/聚合源复核 |
| [PAID](https://dexscreener.com/solana/6e3jzltf4tqbwzm3f7a66jf8tfzn6mrqvrbdfgcnwara) | SOL | [98kfF7...zypump](https://solscan.io/token/98kfF7rmsg1QDUEoCqNE7g7M1FdrTt92TEp2CLzypump) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| [ELON](https://dexscreener.com/solana/6tuhhpysinf41v39kw3jmpvuaxehcabcbhzqqfnwr6xf) | SOL | [GY9mZf...zxpump](https://solscan.io/token/GY9mZfyPpxXxBXBxS2hB2XjhP3kfUsywTvgveozxpump) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |

### F. 钱包行为 / AVE命中样本表
| Token | 链 | 合约地址 | 行为状态 | 行为层级 | AVE命中 | 判断 |
|---|---|---|---|---|---:|---|
| [CATE](https://dexscreener.com/solana/hmzvseemtzhhvznw9uwbag85hctmfnkbhzux16cy7ca3) | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| $BANANA | BSC | [0x3d4f...a9a760](https://bscscan.com/token/0x3d4f0513e8a29669b960f9dbca61861548a9a760) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
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
| 成熟池观察 | 6 个 | 成熟资产不占早期Alpha主榜 |
| 合约地址覆盖 | 可用 25，缺失 0 | 地址缺失会阻断BSC RPC/Helius精查，需要优先补齐 |
| LP层级 | Micro 7 / Early 9 / Liquid 6 / Mature 3 | 下一步可以按层级分别设置进攻规则 |
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