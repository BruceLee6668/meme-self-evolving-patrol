# 自我进化轮巡

**本轮时间 UTC：** 2026-10-20T13:13:04Z
**版本：** 0.5.0-ave-cache-wallet-behavior-prep
**S0 时间锚点：** 2026-06-16T16:15:17+09:00

## 一句话结论
本轮从 142 个合并Token中筛出 1 个主观察候选。v0.5已在v0.4.1基础上增加AVE周缓存真实接口接入框架、Smart Wallet持久保存、wallet_behavior_latest.json，以及BSC Transfer级钱包行为样本。注意：BSC当前是Transfer样本，不等同完整Swap解码。
合约地址可用 25 个，缺失 0 个；缺失地址的候选不能进入后续链上精查。

## 本轮扫描摘要
| 指标 | 数量 |
|---|---:|
| 原始池子记录 | 244 |
| 合并后Token | 142 |
| 输出候选 | 25 |
| 主观察 | 1 |
| 次观察 | 6 |
| PVP风险池 | 8 |
| 成熟池观察 | 7 |
| 低优先观察 | 3 |
| 多池Token | 10 |
| 多池冲突 | 2 |
| Symbol桥接合并 | 1 |
| 合约地址可用 | 25 |
| 合约地址缺失 | 0 |
| Micro层 | 8 |
| Early层 | 7 |
| Liquid层 | 9 |
| Mature层 | 1 |
| 需要链上确认 | 16 |
| 紧急精查候选 | 0 |

## v0.5 数据确认状态
| 项目 | 状态 |
|---|---|
| AVE Smart Wallet周缓存 | active，钱包数 2069，刷新时间 2026-10-19T02:35:21Z，是否过期 否 |
| 链上预检 | 本轮检查 12 个，验证通过 12 个，失败 0 个 |
| Helius状态 | 未配置，SOL使用公共RPC或跳过增强解析 |
| 当前精查层级 | 0.5.0-chain-preflight-plus-wallet-behavior：地址/账户预检 + v0.5钱包行为样本，完整Swap留存仍待下一版 |
| 钱包行为样本 | 本轮检查 1 个，BSC Transfer样本 1 个，SOL签名级 0 个，AVE钱包命中 0 个 |

## 第一部分：生成结果表格

### A. 上次记录结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| 龙虾 | BSC | [0xeccb...7e4444](https://bscscan.com/token/0xeccbb861c0dda7efd964010085488b69317e4444) | 主观察 | Score 84; Tier Liquid; LP $1.46M; Vol24H $1.39M; 24H -2.62%; V/LP 0.95x; 池数 19; 分项 L20/V15/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| TART | BSC | [0x7ab8...750314](https://bscscan.com/token/0x7ab8d02cbb51ff7223fde700eaaa2a91bf750314) | 主观察 | Score 83; Tier Liquid; LP $801.1K; Vol24H $663.1K; 24H +11.26%; V/LP 0.83x; 池数 1; 分项 L17/V13/B17/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| EWYB | BSC | [0xbe82...2e2cb8](https://bscscan.com/token/0xbe82f76637dba2c114c41df856c2c51e522e2cb8) | 主观察 | Score 76; Tier Early; LP $227.5K; Vol24H $1.78M; 24H -3.46%; V/LP 7.82x; 池数 1; 分项 L12/V15/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [CBUCKS](https://dexscreener.com/solana/b4cp45pgifvm5faxfh6aev8qz3eunqnqgbw7kuc7mhnb) | SOL | [DtcicP...xZpump](https://solscan.io/token/DtcicPCKTKeAh7TDEzTym3hXeoHAoMiBdYJhMYxZpump) | 次观察 | Score 73; Tier Early; LP $112.3K; Vol24H $240.7K; 24H -2.37%; V/LP 2.14x; 池数 2; 分项 L10/V9/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [NODF](https://dexscreener.com/solana/bnchf8gcxgkxswbpkue5d8rhgfb31qgt7dbavmpy7riv) | SOL | [qTFyfJ...aXpump](https://solscan.io/token/qTFyfJiSQhMooT6LzybsWHjMXSGWsdkY3w8C9aXpump) | 次观察 | Score 73; Tier Early; LP $390.5K; Vol24H $183.9K; 24H +10.15%; V/LP 0.47x; 池数 1; 分项 L15/V9/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| MarsCoin | BSC | [0xfe18...5c7777](https://bscscan.com/token/0xfe189e97832da1573e4e4ff034f4ffc3a15c7777) | 次观察 | Score 73; Tier Early; LP $211.1K; Vol24H $614.6K; 24H +1.23%; V/LP 2.91x; 池数 1; 分项 L12/V12/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| AGT | BSC | [0x5dbd...cae274](https://bscscan.com/token/0x5dbde81fce337ff4bcaaee4ca3466c00aecae274) | PVP风险池 | Score 39; Tier Liquid; LP $2.81M; Vol24H $66.47M; 24H -18.95%; V/LP 23.68x; 池数 1; 分项 L20/V17/B17/Buy3/Risk-42 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| DNA | BSC | [0xa991...c5cf7b](https://bscscan.com/token/0xa991f61940095aea0724ef54077223b048c5cf7b) | PVP风险池 | Score 39; Tier Liquid; LP $1.74M; Vol24H $66.06M; 24H -15.47%; V/LP 37.98x; 池数 1; 分项 L20/V17/B17/Buy3/Risk-42 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| startupSI | SOL | [EKosQw...KDpump](https://solscan.io/token/EKosQw4oJFbXmeJ4qRnbH1quGFRTc3Eok6nwnFKDpump) | PVP风险池 | Score 37; Tier Early; LP $338.6K; Vol24H $13.34M; 24H +81.36%; V/LP 39.40x; 池数 2; 分项 L14/V17/B0/Buy12/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [UHI](https://dexscreener.com/solana/3ensvqnhuhtqzmbxpdg4pkxwbbnzjvfcz2yycfxc9qnh) | SOL | [FGkCj2...Hepump](https://solscan.io/token/FGkCj28xhabWTYg9QyzACvs4NsN6LUyesP6EwiHepump) | PVP风险池 | Score 34; Tier Micro; LP $62.8K; Vol24H $5.00M; 24H +65.71%; V/LP 79.53x; 池数 2; 分项 L7/V17/B8/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### B. 本轮扫描结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| COLLECT | BSC | [0x4b3d...a087d3](https://bscscan.com/token/0x4b3d30992f003c8167699735f5ab2831b2a087d3) | 主观察 | Score 86; Tier Liquid; LP $2.36M; Vol24H $5.45M; 24H +7.75%; V/LP 2.31x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [DAWG](https://dexscreener.com/bsc/0x9e83be1267e9a6d43bb7f3a8c0dc3c092ccae63e) | BSC | [0x7D04...237777](https://bscscan.com/token/0x7D0443CdDFc8E11AF105F4fE44Dd28c630237777) | 次观察 | Score 75; Tier Early; LP $198.3K; Vol24H $313.9K; 24H -11.49%; V/LP 1.58x; 池数 1; 分项 L12/V10/B17/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [SI276](https://dexscreener.com/solana/12jc1dzjpzbcdakum4brakh9jcfry2tlg1ffgsl4ftcg) | SOL | [HMYd9t...6upump](https://solscan.io/token/HMYd9tosnUXuNHmq7pXmoePRVBLBBjA3JBfydq6upump) | 次观察 | Score 75; Tier Micro; LP $84.0K; Vol24H $193.5K; 24H +4.16%; V/LP 2.30x; 池数 2; 分项 L8/V9/B22/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| TART | BSC | [0x7ab8...750314](https://bscscan.com/token/0x7ab8d02cbb51ff7223fde700eaaa2a91bf750314) | 次观察 | Score 75; Tier Liquid; LP $852.4K; Vol24H $881.2K; 24H +26.54%; V/LP 1.03x; 池数 5; 分项 L18/V13/B8/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [CBUCKS](https://dexscreener.com/solana/b4cp45pgifvm5faxfh6aev8qz3eunqnqgbw7kuc7mhnb) | SOL | [DtcicP...xZpump](https://solscan.io/token/DtcicPCKTKeAh7TDEzTym3hXeoHAoMiBdYJhMYxZpump) | 次观察 | Score 73; Tier Early; LP $109.8K; Vol24H $241.9K; 24H -6.42%; V/LP 2.20x; 池数 2; 分项 L10/V9/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [NODF](https://dexscreener.com/solana/bnchf8gcxgkxswbpkue5d8rhgfb31qgt7dbavmpy7riv) | SOL | [qTFyfJ...aXpump](https://solscan.io/token/qTFyfJiSQhMooT6LzybsWHjMXSGWsdkY3w8C9aXpump) | 次观察 | Score 73; Tier Early; LP $394.4K; Vol24H $181.3K; 24H +9.67%; V/LP 0.46x; 池数 1; 分项 L15/V9/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [texcat](https://dexscreener.com/solana/czcfvsc2hqvf1zwu6ya2vrf7g29anu4nnrhw7jvvd3vw) | SOL | [BdXfLf...Uc2S5t](https://solscan.io/token/BdXfLfcbDE8YvpbvvmmGTduqcDesaQVUm5xLxgUc2S5t) | 次观察 | Score 64; Tier Micro; LP $63.3K; Vol24H $139.5K; 24H +19.92%; V/LP 2.20x; 池数 2; 分项 L7/V8/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| DNA | BSC | [0xa991...c5cf7b](https://bscscan.com/token/0xa991f61940095aea0724ef54077223b048c5cf7b) | PVP风险池 | Score 44; Tier Liquid; LP $1.75M; Vol24H $83.19M; 24H -5.24%; V/LP 47.58x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-42 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| BORLY | SOL | [ECFmFa...Aspump](https://solscan.io/token/ECFmFaHyJ8krXErN1QAxqUq97xCFUWYv9Ax5j2Aspump) | PVP风险池 | Score 32; Tier Micro; LP $94.3K; Vol24H $4.29M; 24H +185.94%; V/LP 45.53x; 池数 1; 分项 L9/V17/B0/Buy12/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [startupSI](https://dexscreener.com/solana/ascpffyzxmnhhfhqqwawtcrmasguzcjtwyu6os6cqd2r) | SOL | [EKosQw...KDpump](https://solscan.io/token/EKosQw4oJFbXmeJ4qRnbH1quGFRTc3Eok6nwnFKDpump) | PVP风险池 | Score 31; Tier Micro; LP $70.7K; Vol24H $14.09M; 24H -94.28%; V/LP 199.25x; 池数 2; 分项 L8/V17/B0/Buy12/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [Pokémon](https://dexscreener.com/solana/cxyug8pvwbbkw41mlaq7j87ft3drydjzv2a5pgwb31an) | SOL | [D42TjM...hJXvb1](https://solscan.io/token/D42TjMjz5H7toPu5md5KBXreZkCSdZMEfLQwmBhJXvb1) | PVP风险池 | Score 27; Tier Early; LP $141.7K; Vol24H $3.63M; 24H +12122.00%; V/LP 25.64x; 池数 1; 分项 L11/V17/B0/Buy8/Risk-33 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [COLLECTOOOR](https://dexscreener.com/solana/9yf6szskpr7yeshde3mqp4acxgynricdrxpxr9gfye27) | SOL | [ESnW5Z...Rmpump](https://solscan.io/token/ESnW5ZbLmoEAg2QEMxnMsY9R3aS8Kw58HJacYURmpump) | PVP风险池 | Score 26; Tier Micro; LP $62.3K; Vol24H $4.67M; 24H +447.00%; V/LP 75.06x; 池数 2; 分项 L7/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| COMPUTE | SOL | [GWe3TN...FLpump](https://solscan.io/token/GWe3TNg1UPxeaSazxK8U49PDAqXCaX9Jc8zbttFLpump) | PVP风险池 | Score 26; Tier Micro; LP $56.6K; Vol24H $2.71M; 24H +202.50%; V/LP 47.93x; 池数 2; 分项 L7/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| UHI | SOL | [FGkCj2...Hepump](https://solscan.io/token/FGkCj28xhabWTYg9QyzACvs4NsN6LUyesP6EwiHepump) | PVP风险池 | Score 23; Tier Micro; LP $48.9K; Vol24H $2.55M; 24H -77.90%; V/LP 52.19x; 池数 2; 分项 L6/V17/B8/Buy8/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [Kim](https://dexscreener.com/solana/2sa5714m6bst4zdpxs5trfppeaz1pcamdyhggatfrazw) | SOL | [ESABfJ...ojpump](https://solscan.io/token/ESABfJpt9cocXgWX7HF8WwSXrcv785oyaA8imwojpump) | PVP风险池 | Score 13; Tier Micro; LP $27.6K; Vol24H $2.92M; 24H +145.00%; V/LP 105.72x; 池数 1; 分项 L4/V17/B0/Buy8/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### C. PVP风险池明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| DNA | BSC | [0xa991...c5cf7b](https://bscscan.com/token/0xa991f61940095aea0724ef54077223b048c5cf7b) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP极端偏高；FDV超过早期Alpha主榜上限；成熟大市值 | Score 44; Tier Liquid; LP $1.75M; Vol24H $83.19M; 24H -5.24%; V/LP 47.58x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-42 | 只记录热度，不进入主榜 |
| BORLY | SOL | [ECFmFa...Aspump](https://solscan.io/token/ECFmFaHyJ8krXErN1QAxqUq97xCFUWYv9Ax5j2Aspump) | 买入笔数占优；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 32; Tier Micro; LP $94.3K; Vol24H $4.29M; 24H +185.94%; V/LP 45.53x; 池数 1; 分项 L9/V17/B0/Buy12/Risk-30 | 只记录热度，不进入主榜 |
| [startupSI](https://dexscreener.com/solana/ascpffyzxmnhhfhqqwawtcrmasguzcjtwyu6os6cqd2r) | SOL | [EKosQw...KDpump](https://solscan.io/token/EKosQw4oJFbXmeJ4qRnbH1quGFRTc3Eok6nwnFKDpump) | 买入笔数占优；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 31; Tier Micro; LP $70.7K; Vol24H $14.09M; 24H -94.28%; V/LP 199.25x; 池数 2; 分项 L8/V17/B0/Buy12/Risk-30 | 只记录热度，不进入主榜 |
| [Pokémon](https://dexscreener.com/solana/cxyug8pvwbbkw41mlaq7j87ft3drydjzv2a5pgwb31an) | SOL | [D42TjM...hJXvb1](https://solscan.io/token/D42TjMjz5H7toPu5md5KBXreZkCSdZMEfLQwmBhJXvb1) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高；非主流报价池 | Score 27; Tier Early; LP $141.7K; Vol24H $3.63M; 24H +12122.00%; V/LP 25.64x; 池数 1; 分项 L11/V17/B0/Buy8/Risk-33 | 只记录热度，不进入主榜 |
| [COLLECTOOOR](https://dexscreener.com/solana/9yf6szskpr7yeshde3mqp4acxgynricdrxpxr9gfye27) | SOL | [ESnW5Z...Rmpump](https://solscan.io/token/ESnW5ZbLmoEAg2QEMxnMsY9R3aS8Kw58HJacYURmpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 26; Tier Micro; LP $62.3K; Vol24H $4.67M; 24H +447.00%; V/LP 75.06x; 池数 2; 分项 L7/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| COMPUTE | SOL | [GWe3TN...FLpump](https://solscan.io/token/GWe3TNg1UPxeaSazxK8U49PDAqXCaX9Jc8zbttFLpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 26; Tier Micro; LP $56.6K; Vol24H $2.71M; 24H +202.50%; V/LP 47.93x; 池数 2; 分项 L7/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| UHI | SOL | [FGkCj2...Hepump](https://solscan.io/token/FGkCj28xhabWTYg9QyzACvs4NsN6LUyesP6EwiHepump) | 24H未过热但已明显波动；买卖略偏买入；LP未达主观察门槛；24H成交合格；LP偏薄；Volume/LP极端偏高 | Score 23; Tier Micro; LP $48.9K; Vol24H $2.55M; 24H -77.90%; V/LP 52.19x; 池数 2; 分项 L6/V17/B8/Buy8/Risk-40 | 只记录热度，不进入主榜 |
| [Kim](https://dexscreener.com/solana/2sa5714m6bst4zdpxs5trfppeaz1pcamdyhggatfrazw) | SOL | [ESABfJ...ojpump](https://solscan.io/token/ESABfJpt9cocXgWX7HF8WwSXrcv785oyaA8imwojpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 13; Tier Micro; LP $27.6K; Vol24H $2.92M; 24H +145.00%; V/LP 105.72x; 池数 1; 分项 L4/V17/B0/Buy8/Risk-40 | 只记录热度，不进入主榜 |

### D. 成熟池观察明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| [RAY](https://dexscreener.com/solana/2axxcn6on9bbt5owwmth53c7qhuxvhleu718kqt8rvy2) | SOL | [4k3Dyj...QrkX6R](https://solscan.io/token/4k3Dyjzvzp8eMZWUXbBCjEvwSkkk59S5iCNLY3QrkX6R) | 24H接近横盘；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 79; Tier Liquid; LP $2.27M; Vol24H $3.13M; 24H -1.55%; V/LP 1.38x; 池数 1; 分项 L20/V17/B22/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| AKE | BSC | [0x2c3a...12f7db](https://bscscan.com/token/0x2c3a8ee94ddd97244a93bc48298f97d2c412f7db) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 74; Tier Liquid; LP $2.60M; Vol24H $4.33M; 24H +1.04%; V/LP 1.66x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| CARDS | SOL | [CARDSc...dKxYjp](https://solscan.io/token/CARDSccUMFKoPRZxt5vt3ksUbxEFEcnZ3H2pd3dKxYjp) | 24H波动可控；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 74; Tier Liquid; LP $4.45M; Vol24H $13.67M; 24H +15.36%; V/LP 3.07x; 池数 1; 分项 L20/V17/B17/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| ARK | BSC | [0xcae1...618b9d](https://bscscan.com/token/0xcae117ca6bc8a341d2e7207f30e180f0e5618b9d) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 73; Tier Mature; LP $57.79M; Vol24H $2.21M; 24H -0.68%; V/LP 0.04x; 池数 1; 分项 L20/V16/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| Q | BSC | [0xc07e...690589](https://bscscan.com/token/0xc07e1300dc138601fa6b0b59f8d0fa477e690589) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 70; Tier Liquid; LP $1.47M; Vol24H $684.3K; 24H +5.26%; V/LP 0.47x; 池数 1; 分项 L20/V13/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| STONK | SOL | [6GmAFS...MpUNgx](https://solscan.io/token/6GmAFSYs4gk3FDao5FzzySQpPZaWsa4rUJHacpMpUNgx) | 24H接近横盘；LP达主观察门槛；24H成交合格；Volume/LP未失真；卖出笔数占优；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限 | Score 68; Tier Liquid; LP $1.83M; Vol24H $1.03M; 24H -7.79%; V/LP 0.57x; 池数 1; 分项 L20/V14/B22/Buy0/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| [UDTF](https://dexscreener.com/solana/5dnezejxysaoxddkhdzye3zeftqg6dzfsbcq4naqvcxl) | SOL | [AwpzNp...W2pump](https://solscan.io/token/AwpzNpDnUuMqgZVB9Q2trhWpx6ZragdWgS95UNW2pump) | 24H未过热但已明显波动；买入笔数占优；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 63; Tier Liquid; LP $1.47M; Vol24H $353.3K; 24H +26.02%; V/LP 0.24x; 池数 2; 分项 L20/V11/B8/Buy12/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |

### E. 链上确认/紧急精查表
| Token | 链 | 合约地址 | 是否需要链上确认 | 紧急精查 | 预检状态 | 原因 |
|---|---|---|---|---|---|---|
| COLLECT | BSC | [0x4b3d...a087d3](https://bscscan.com/token/0x4b3d30992f003c8167699735f5ab2831b2a087d3) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [DAWG](https://dexscreener.com/bsc/0x9e83be1267e9a6d43bb7f3a8c0dc3c092ccae63e) | BSC | [0x7D04...237777](https://bscscan.com/token/0x7D0443CdDFc8E11AF105F4fE44Dd28c630237777) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [SI276](https://dexscreener.com/solana/12jc1dzjpzbcdakum4brakh9jcfry2tlg1ffgsl4ftcg) | SOL | [HMYd9t...6upump](https://solscan.io/token/HMYd9tosnUXuNHmq7pXmoePRVBLBBjA3JBfydq6upump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；多池数据冲突，需链上/聚合源复核 |
| TART | BSC | [0x7ab8...750314](https://bscscan.com/token/0x7ab8d02cbb51ff7223fde700eaaa2a91bf750314) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [CBUCKS](https://dexscreener.com/solana/b4cp45pgifvm5faxfh6aev8qz3eunqnqgbw7kuc7mhnb) | SOL | [DtcicP...xZpump](https://solscan.io/token/DtcicPCKTKeAh7TDEzTym3hXeoHAoMiBdYJhMYxZpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [NODF](https://dexscreener.com/solana/bnchf8gcxgkxswbpkue5d8rhgfb31qgt7dbavmpy7riv) | SOL | [qTFyfJ...aXpump](https://solscan.io/token/qTFyfJiSQhMooT6LzybsWHjMXSGWsdkY3w8C9aXpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [texcat](https://dexscreener.com/solana/czcfvsc2hqvf1zwu6ya2vrf7g29anu4nnrhw7jvvd3vw) | SOL | [BdXfLf...Uc2S5t](https://solscan.io/token/BdXfLfcbDE8YvpbvvmmGTduqcDesaQVUm5xLxgUc2S5t) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [UDTF](https://dexscreener.com/solana/5dnezejxysaoxddkhdzye3zeftqg6dzfsbcq4naqvcxl) | SOL | [AwpzNp...W2pump](https://solscan.io/token/AwpzNpDnUuMqgZVB9Q2trhWpx6ZragdWgS95UNW2pump) | 是 | 否 | verified / address_preflight_v0.4 | 多池数据冲突，需链上/聚合源复核 |
| DNA | BSC | [0xa991...c5cf7b](https://bscscan.com/token/0xa991f61940095aea0724ef54077223b048c5cf7b) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| BORLY | SOL | [ECFmFa...Aspump](https://solscan.io/token/ECFmFaHyJ8krXErN1QAxqUq97xCFUWYv9Ax5j2Aspump) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |

### F. 钱包行为 / AVE命中样本表
| Token | 链 | 合约地址 | 行为状态 | 行为层级 | AVE命中 | 判断 |
|---|---|---|---|---|---:|---|
| COLLECT | BSC | [0x4b3d...a087d3](https://bscscan.com/token/0x4b3d30992f003c8167699735f5ab2831b2a087d3) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |

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
| 主观察候选 | 1 个 | 主榜继续稀缺，但必须结合合约地址进入链上确认 |
| PVP风险池 | 8 个 | v0.3已单独展示明细，便于判断噪声来源 |
| 成熟池观察 | 7 个 | 成熟资产不占早期Alpha主榜 |
| 合约地址覆盖 | 可用 25，缺失 0 | 地址缺失会阻断BSC RPC/Helius精查，需要优先补齐 |
| LP层级 | Micro 8 / Early 7 / Liquid 9 / Mature 1 | 下一步可以按层级分别设置进攻规则 |
| S0对比 | 尚未做精确历史回放 | 后续用GeckoTerminal OHLCV / 链上数据补齐 |
| 链上确认 | v0.5执行地址/账户预检 + BSC Transfer级钱包行为样本 | 可以初步看到活跃钱包/缓存命中，但仍不能替代完整Swap留存判断 |
| Smart Money | AVE周缓存 + 代理指标 | 无具体钱包映射前，不允许标记真实吸筹 |

### C. 本轮优化调整表
| 调整项 | 触发原因 | 对下轮筛选影响 |
|---|---|---|
| chain_verify_pipeline | 观察池候选需要链上Swap、钱包留存和大额买卖确认；v0.4.1已生成确认标记并强制落地chain_verify_latest.json | 下轮报告继续输出链上确认/紧急精查表，为接BSC RPC/Helius做准备 |
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
| dexscreener_search | {'ok': True, 'count': 332} |
| geckoterminal_bsc_trending | {'ok': True, 'count': 20} |
| geckoterminal_solana_trending | {'ok': True, 'count': 20} |

## 数据限制
- This v0.4 scan uses free public sources plus lightweight chain address/account preflight when enabled.
- AVE Smart Money weekly cache structure is connected; real AVE API refresh is handled by the weekly workflow/cache file.
- S0 exact historical replay is not implemented yet; candidates are marked with current metrics only.
- Wallet-level buy/sell retention is not implemented yet; v0.4 only preflights token contract/account existence.
- v0.4 adds chain preflight status and Smart Wallet cache status on top of contract-address output, liquidity tiers, visible PVP/mature detail tables, and chain-verify flags.
- Contract addresses are extracted from DEXScreener baseToken or GeckoTerminal relationships when available; missing addresses are explicitly marked unavailable.