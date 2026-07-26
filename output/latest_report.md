# 自我进化轮巡

**本轮时间 UTC：** 2026-07-26T15:00:07Z
**版本：** 0.5.0-ave-cache-wallet-behavior-prep
**S0 时间锚点：** 2026-06-16T16:15:17+09:00

## 一句话结论
本轮从 108 个合并Token中筛出 1 个主观察候选。v0.5已在v0.4.1基础上增加AVE周缓存真实接口接入框架、Smart Wallet持久保存、wallet_behavior_latest.json，以及BSC Transfer级钱包行为样本。注意：BSC当前是Transfer样本，不等同完整Swap解码。
合约地址可用 25 个，缺失 0 个；缺失地址的候选不能进入后续链上精查。

## 本轮扫描摘要
| 指标 | 数量 |
|---|---:|
| 原始池子记录 | 239 |
| 合并后Token | 108 |
| 输出候选 | 25 |
| 主观察 | 1 |
| 次观察 | 3 |
| PVP风险池 | 8 |
| 成熟池观察 | 7 |
| 低优先观察 | 5 |
| 多池Token | 14 |
| 多池冲突 | 3 |
| Symbol桥接合并 | 1 |
| 合约地址可用 | 25 |
| 合约地址缺失 | 0 |
| Micro层 | 11 |
| Early层 | 3 |
| Liquid层 | 8 |
| Mature层 | 3 |
| 需要链上确认 | 12 |
| 紧急精查候选 | 1 |

## v0.5 数据确认状态
| 项目 | 状态 |
|---|---|
| AVE Smart Wallet周缓存 | active，钱包数 732，刷新时间 2026-07-20T02:12:03Z，是否过期 否 |
| 链上预检 | 本轮检查 12 个，验证通过 12 个，失败 0 个 |
| Helius状态 | 未配置，SOL使用公共RPC或跳过增强解析 |
| 当前精查层级 | 0.5.0-chain-preflight-plus-wallet-behavior：地址/账户预检 + v0.5钱包行为样本，完整Swap留存仍待下一版 |
| 钱包行为样本 | 本轮检查 1 个，BSC Transfer样本 1 个，SOL签名级 0 个，AVE钱包命中 0 个 |

## 第一部分：生成结果表格

### A. 上次记录结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| QQQB | BSC | [0x2058...11efc7](https://bscscan.com/token/0x205812cdbed920aff76c6580abd681a46d11efc7) | 主观察 | Score 91; Tier Liquid; LP $2.64M; Vol24H $20.51M; 24H +0.84%; V/LP 7.77x; 池数 1; 分项 L20/V17/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| AA | BSC | [0x01bf...0f6936](https://bscscan.com/token/0x01bf3d77cd08b19bf3f2309972123a2cca0f6936) | 主观察 | Score 78; Tier Liquid; LP $927.6K; Vol24H $2.33M; 24H -16.36%; V/LP 2.52x; 池数 1; 分项 L18/V16/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [HBULL](https://dexscreener.com/solana/edx18gjcdijqslaja2pp5c2vma3btrrx4utxkejufrtq) | SOL | [7V6Sk6...k9pump](https://solscan.io/token/7V6Sk63y8Rr1MvcN5mYNp61wgFhy4EeQg5gUASk9pump) | 次观察 | Score 73; Tier Early; LP $123.9K; Vol24H $990.9K; 24H +22.89%; V/LP 8.00x; 池数 5; 分项 L10/V14/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [Jimothy](https://dexscreener.com/solana/5pghkctym6odbhgo2tkmst2ajmjsb2uzbqrkkn4zuft5) | SOL | [Ge87Et...xTpump](https://solscan.io/token/Ge87EtsjwRQbHaqQmKRno69RFTwh9bfSsm99XNxTpump) | 次观察 | Score 64; Tier Early; LP $508.8K; Vol24H $4.67M; 24H -22.11%; V/LP 9.19x; 池数 1; 分项 L16/V17/B17/Buy8/Risk-18 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [Cupsey](https://dexscreener.com/solana/dpzkojvewah1wpchd3gwkeegm7g2mxkbw48urniagbvx) | SOL | [6NwarB...9vpump](https://solscan.io/token/6NwarBvDkXhByqVp2Qkq5i9XbtA2B3Bwe8SWGu9vpump) | 次观察 | Score 64; Tier Early; LP $313.7K; Vol24H $1.37M; 24H -37.18%; V/LP 4.36x; 池数 1; 分项 L14/V15/B8/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [RAKO](https://dexscreener.com/solana/hmvaoct9ag9jpmxvke8nbg2ieomreezs3yb3bgna49fa) | SOL | [5sd8bK...Xipump](https://solscan.io/token/5sd8bKraewJNHFg72scxxYXNeLCASVct1gxqi3Xipump) | PVP风险池 | Score 31; Tier Micro; LP $60.5K; Vol24H $1.24M; 24H +48.76%; V/LP 20.51x; 池数 2; 分项 L7/V14/B8/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [sharkdog](https://dexscreener.com/solana/4rm2wys8vafjf345tf9ckhqnjyf6ttskljiygdifwkmv) | SOL | [8gEtFe...2v5qFn](https://solscan.io/token/8gEtFeKeRt1QREkU51dRih9pQ39PyYpRRZTyLg2v5qFn) | PVP风险池 | Score 26; Tier Micro; LP $59.6K; Vol24H $4.44M; 24H +718.00%; V/LP 74.50x; 池数 2; 分项 L7/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [Cupsey2028](https://dexscreener.com/solana/79z4t9byfgv5ghcay26cqxzbkuchrjm4jez1pgdb52wh) | SOL | [7LRpii...YWpump](https://solscan.io/token/7LRpiiDzNVRdxfatA5T1iGvQmPUP46pMkpfGnqYWpump) | PVP风险池 | Score 17; Tier Micro; LP $30.0K; Vol24H $5.77M; 24H +127.00%; V/LP 192.42x; 池数 2; 分项 L4/V17/B0/Buy12/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [Tiana](https://dexscreener.com/solana/4agoaezcnghm48te9jvw6kysjzsmxejyecyprfzom4gd) | SOL | [MeDy6n...m3pump](https://solscan.io/token/MeDy6nEaqwRs6g8bDuthTrMJfV8WEQDHA7bSHm3pump) | PVP风险池 | Score 14; Tier Micro; LP $43.9K; Vol24H $1.84M; 24H +885.00%; V/LP 41.98x; 池数 2; 分项 L6/V16/B0/Buy8/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| Ferret | SOL | [HXuiny...tJpump](https://solscan.io/token/HXuinymFnfjaiM4LkaFDLvvQ4a1WL5qoupdyUGtJpump) | PVP风险池 | Score 13; Tier Micro; LP $33.7K; Vol24H $2.25M; 24H +543.44%; V/LP 66.68x; 池数 2; 分项 L5/V16/B0/Buy8/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### B. 本轮扫描结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| AA | BSC | [0x01bf...0f6936](https://bscscan.com/token/0x01bf3d77cd08b19bf3f2309972123a2cca0f6936) | 主观察 | Score 78; Tier Liquid; LP $928.0K; Vol24H $2.06M; 24H -14.91%; V/LP 2.22x; 池数 1; 分项 L18/V16/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [Cupsey](https://dexscreener.com/solana/dpzkojvewah1wpchd3gwkeegm7g2mxkbw48urniagbvx) | SOL | [6NwarB...9vpump](https://solscan.io/token/6NwarBvDkXhByqVp2Qkq5i9XbtA2B3Bwe8SWGu9vpump) | 次观察 | Score 72; Tier Early; LP $318.9K; Vol24H $1.18M; 24H -19.13%; V/LP 3.69x; 池数 2; 分项 L14/V14/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| ESPORTS | BSC | [0xf39e...508e48](https://bscscan.com/token/0xf39e4b21c84e737df08e2c3b32541d856f508e48) | 次观察 | Score 71; Tier Liquid; LP $1.04M; Vol24H $7.44M; 24H -32.11%; V/LP 7.13x; 池数 2; 分项 L19/V17/B8/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [Jimothy](https://dexscreener.com/solana/5pghkctym6odbhgo2tkmst2ajmjsb2uzbqrkkn4zuft5) | SOL | [Ge87Et...xTpump](https://solscan.io/token/Ge87EtsjwRQbHaqQmKRno69RFTwh9bfSsm99XNxTpump) | 次观察 | Score 64; Tier Early; LP $542.8K; Vol24H $4.44M; 24H -21.69%; V/LP 8.19x; 池数 1; 分项 L16/V17/B17/Buy8/Risk-18 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| sharkdog | SOL | [8gEtFe...2v5qFn](https://solscan.io/token/8gEtFeKeRt1QREkU51dRih9pQ39PyYpRRZTyLg2v5qFn) | PVP风险池 | Score 26; Tier Micro; LP $60.5K; Vol24H $4.22M; 24H +128.17%; V/LP 69.76x; 池数 2; 分项 L7/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| Cupsey2028 | SOL | [7LRpii...YWpump](https://solscan.io/token/7LRpiiDzNVRdxfatA5T1iGvQmPUP46pMkpfGnqYWpump) | PVP风险池 | Score 25; Tier Micro; LP $25.1K; Vol24H $6.08M; 24H -45.39%; V/LP 242.38x; 池数 2; 分项 L4/V17/B8/Buy12/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [Tiana](https://dexscreener.com/solana/4agoaezcnghm48te9jvw6kysjzsmxejyecyprfzom4gd) | SOL | [MeDy6n...m3pump](https://solscan.io/token/MeDy6nEaqwRs6g8bDuthTrMJfV8WEQDHA7bSHm3pump) | PVP风险池 | Score 25; Tier Micro; LP $54.1K; Vol24H $1.96M; 24H +1362.00%; V/LP 36.30x; 池数 2; 分项 L7/V16/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [BullPad](https://dexscreener.com/solana/8xhumrdufgyaavn4rp27cpowpzcmnkc33ymtxt6wjmye) | SOL | [BcbuAE...xQpump](https://solscan.io/token/BcbuAEmVwQ4QWBNn1KQxcsJnpH39LGE76apE6XxQpump) | PVP风险池 | Score 24; Tier Micro; LP $14.0K; Vol24H $1.25M; 24H +20.68%; V/LP 89.31x; 池数 5; 分项 L1/V14/B17/Buy8/Risk-40 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| Ferret | SOL | [HXuiny...tJpump](https://solscan.io/token/HXuinymFnfjaiM4LkaFDLvvQ4a1WL5qoupdyUGtJpump) | PVP风险池 | Score 13; Tier Micro; LP $32.4K; Vol24H $2.30M; 24H +497.63%; V/LP 70.92x; 池数 2; 分项 L5/V16/B0/Buy8/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [Cog](https://dexscreener.com/solana/b9ytardjvsmfujzzimy92bfj6lmm2wynzhzz4anlmczj) | SOL | [7rSpKg...d9pump](https://solscan.io/token/7rSpKgASuXN5hfw3jsKNZN6ysNCR1Eixb2PD2Nd9pump) | PVP风险池 | Score 11; Tier Micro; LP $23.5K; Vol24H $2.07M; 24H +193.00%; V/LP 88.31x; 池数 16; 分项 L3/V16/B0/Buy8/Risk-40 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [waddles](https://dexscreener.com/solana/ennzvzyjgr6bb9ixzmrkptgwkp5dawh4usjcsusyfsgx) | SOL | [38iSF6...Srpump](https://solscan.io/token/38iSF6E33YPABapMELpnMPR6aJGQpT3aGjk9wCSrpump) | PVP风险池 | Score 11; Tier Micro; LP $25.8K; Vol24H $1.81M; 24H +257.00%; V/LP 70.34x; 池数 3; 分项 L4/V15/B0/Buy8/Risk-40 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| Neném | SOL | [GPJZWS...7Tpump](https://solscan.io/token/GPJZWSVZpYsRxuzhv1DKDGTmawPgSxUSd6fpja7Tpump) | PVP风险池 | Score 7; Tier Micro; LP $3.7K; Vol24H $1.67M; 24H -99.32%; V/LP 449.94x; 池数 1; 分项 L0/V15/B0/Buy8/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| LAB | BSC | [0x7ec4...25593a](https://bscscan.com/token/0x7ec43cf65f1663f820427c62a5780b8f2e25593a) | 成熟池观察 | Score 74; Tier Liquid; LP $1.47M; Vol24H $4.45M; 24H +7.01%; V/LP 3.03x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-12 | 钱包级数据不可用；当前仅代理指标；资产偏成熟，不按早期吸筹处理；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 成熟池观察，不占用早期Alpha主榜 |
| ZAMA | BSC | [0x6907...87519f](https://bscscan.com/token/0x6907a5986c4950bdaf2f81828ec0737ce787519f) | 成熟池观察 | Score 74; Tier Liquid; LP $1.34M; Vol24H $5.68M; 24H -2.57%; V/LP 4.25x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-12 | 钱包级数据不可用；当前仅代理指标；资产偏成熟，不按早期吸筹处理；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 成熟池观察，不占用早期Alpha主榜 |
| [ANSEM](https://dexscreener.com/solana/fnzky6x7entq1er3d225dqyt7ybfka4pskbmqhb8l3cc) | SOL | [9cRCn9...TGpump](https://solscan.io/token/9cRCn9rGT8V2imeM2BaKs13yhMEais3ruM3rPvTGpump) | 成熟池观察 | Score 73; Tier Liquid; LP $2.00M; Vol24H $2.39M; 24H +9.80%; V/LP 1.20x; 池数 2; 分项 L20/V16/B17/Buy8/Risk-12 | 钱包级数据不可用；当前仅代理指标；资产偏成熟，不按早期吸筹处理；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 成熟池观察，不占用早期Alpha主榜 |

### C. PVP风险池明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| sharkdog | SOL | [8gEtFe...2v5qFn](https://solscan.io/token/8gEtFeKeRt1QREkU51dRih9pQ39PyYpRRZTyLg2v5qFn) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 26; Tier Micro; LP $60.5K; Vol24H $4.22M; 24H +128.17%; V/LP 69.76x; 池数 2; 分项 L7/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| Cupsey2028 | SOL | [7LRpii...YWpump](https://solscan.io/token/7LRpiiDzNVRdxfatA5T1iGvQmPUP46pMkpfGnqYWpump) | 24H未过热但已明显波动；买入笔数占优；LP未达主观察门槛；24H成交合格；LP偏薄；Volume/LP极端偏高 | Score 25; Tier Micro; LP $25.1K; Vol24H $6.08M; 24H -45.39%; V/LP 242.38x; 池数 2; 分项 L4/V17/B8/Buy12/Risk-40 | 只记录热度，不进入主榜 |
| [Tiana](https://dexscreener.com/solana/4agoaezcnghm48te9jvw6kysjzsmxejyecyprfzom4gd) | SOL | [MeDy6n...m3pump](https://solscan.io/token/MeDy6nEaqwRs6g8bDuthTrMJfV8WEQDHA7bSHm3pump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 25; Tier Micro; LP $54.1K; Vol24H $1.96M; 24H +1362.00%; V/LP 36.30x; 池数 2; 分项 L7/V16/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [BullPad](https://dexscreener.com/solana/8xhumrdufgyaavn4rp27cpowpzcmnkc33ymtxt6wjmye) | SOL | [BcbuAE...xQpump](https://solscan.io/token/BcbuAEmVwQ4QWBNn1KQxcsJnpH39LGE76apE6XxQpump) | 24H波动可控；买卖略偏买入；LP未达主观察门槛；24H成交合格；LP偏薄；Volume/LP极端偏高 | Score 24; Tier Micro; LP $14.0K; Vol24H $1.25M; 24H +20.68%; V/LP 89.31x; 池数 5; 分项 L1/V14/B17/Buy8/Risk-40 | 只记录热度，不进入主榜 |
| Ferret | SOL | [HXuiny...tJpump](https://solscan.io/token/HXuinymFnfjaiM4LkaFDLvvQ4a1WL5qoupdyUGtJpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 13; Tier Micro; LP $32.4K; Vol24H $2.30M; 24H +497.63%; V/LP 70.92x; 池数 2; 分项 L5/V16/B0/Buy8/Risk-40 | 只记录热度，不进入主榜 |
| [Cog](https://dexscreener.com/solana/b9ytardjvsmfujzzimy92bfj6lmm2wynzhzz4anlmczj) | SOL | [7rSpKg...d9pump](https://solscan.io/token/7rSpKgASuXN5hfw3jsKNZN6ysNCR1Eixb2PD2Nd9pump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 11; Tier Micro; LP $23.5K; Vol24H $2.07M; 24H +193.00%; V/LP 88.31x; 池数 16; 分项 L3/V16/B0/Buy8/Risk-40 | 只记录热度，不进入主榜 |
| [waddles](https://dexscreener.com/solana/ennzvzyjgr6bb9ixzmrkptgwkp5dawh4usjcsusyfsgx) | SOL | [38iSF6...Srpump](https://solscan.io/token/38iSF6E33YPABapMELpnMPR6aJGQpT3aGjk9wCSrpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 11; Tier Micro; LP $25.8K; Vol24H $1.81M; 24H +257.00%; V/LP 70.34x; 池数 3; 分项 L4/V15/B0/Buy8/Risk-40 | 只记录热度，不进入主榜 |
| Neném | SOL | [GPJZWS...7Tpump](https://solscan.io/token/GPJZWSVZpYsRxuzhv1DKDGTmawPgSxUSd6fpja7Tpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 7; Tier Micro; LP $3.7K; Vol24H $1.67M; 24H -99.32%; V/LP 449.94x; 池数 1; 分项 L0/V15/B0/Buy8/Risk-40 | 只记录热度，不进入主榜 |

### D. 成熟池观察明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| LAB | BSC | [0x7ec4...25593a](https://bscscan.com/token/0x7ec43cf65f1663f820427c62a5780b8f2e25593a) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；成熟大市值 | Score 74; Tier Liquid; LP $1.47M; Vol24H $4.45M; 24H +7.01%; V/LP 3.03x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| ZAMA | BSC | [0x6907...87519f](https://bscscan.com/token/0x6907a5986c4950bdaf2f81828ec0737ce787519f) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；市值超过早期Alpha主榜上限 | Score 74; Tier Liquid; LP $1.34M; Vol24H $5.68M; 24H -2.57%; V/LP 4.25x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| [ANSEM](https://dexscreener.com/solana/fnzky6x7entq1er3d225dqyt7ybfka4pskbmqhb8l3cc) | SOL | [9cRCn9...TGpump](https://solscan.io/token/9cRCn9rGT8V2imeM2BaKs13yhMEais3ruM3rPvTGpump) | 24H波动可控；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 73; Tier Liquid; LP $2.00M; Vol24H $2.39M; 24H +9.80%; V/LP 1.20x; 池数 2; 分项 L20/V16/B17/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| [JUP](https://dexscreener.com/solana/3xngdc58axytrj64stqz5trdqwvtwhlr888irbbwznee) | SOL | [JUPyiw...NsDvCN](https://solscan.io/token/JUPyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；非主流报价池；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 71; Tier Mature; LP $389.33M; Vol24H $166.96M; 24H -1.48%; V/LP 0.43x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-15 | 成熟池观察，不占用早期Alpha主榜 |
| USDT | BSC | [0x55d3...197955](https://bscscan.com/token/0x55d398326f99059ff775485246999027b3197955) | 24H接近横盘；LP达主观察门槛；24H成交合格；Volume/LP未失真；卖出笔数占优；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 71; Tier Mature; LP $16.77M; Vol24H $31.29M; 24H -0.00%; V/LP 1.87x; 池数 1; 分项 L20/V17/B22/Buy0/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| [BOME](https://dexscreener.com/solana/dsuvc5qf5ljhhv5e2td184ixotsncnwj7i4jja4xsrmt) | SOL | [ukHH6c...Z74J82](https://solscan.io/token/ukHH6c7mMyiWCf1b9pnWe25TSpkDDt3H5pQZgZ74J82) | 24H波动可控；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限 | Score 69; Tier Mature; LP $9.79M; Vol24H $2.97M; 24H +17.66%; V/LP 0.30x; 池数 5; 分项 L20/V17/B17/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| AKE | BSC | [0x2c3a...12f7db](https://bscscan.com/token/0x2c3a8ee94ddd97244a93bc48298f97d2c412f7db) | 24H波动可控；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；成熟大市值 | Score 67; Tier Liquid; LP $959.5K; Vol24H $3.43M; 24H -12.19%; V/LP 3.58x; 池数 1; 分项 L18/V17/B17/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |

### E. 链上确认/紧急精查表
| Token | 链 | 合约地址 | 是否需要链上确认 | 紧急精查 | 预检状态 | 原因 |
|---|---|---|---|---|---|---|
| AA | BSC | [0x01bf...0f6936](https://bscscan.com/token/0x01bf3d77cd08b19bf3f2309972123a2cca0f6936) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| [Cupsey](https://dexscreener.com/solana/dpzkojvewah1wpchd3gwkeegm7g2mxkbw48urniagbvx) | SOL | [6NwarB...9vpump](https://solscan.io/token/6NwarBvDkXhByqVp2Qkq5i9XbtA2B3Bwe8SWGu9vpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| ESPORTS | BSC | [0xf39e...508e48](https://bscscan.com/token/0xf39e4b21c84e737df08e2c3b32541d856f508e48) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [Jimothy](https://dexscreener.com/solana/5pghkctym6odbhgo2tkmst2ajmjsb2uzbqrkkn4zuft5) | SOL | [Ge87Et...xTpump](https://solscan.io/token/Ge87EtsjwRQbHaqQmKRno69RFTwh9bfSsm99XNxTpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| sharkdog | SOL | [8gEtFe...2v5qFn](https://solscan.io/token/8gEtFeKeRt1QREkU51dRih9pQ39PyYpRRZTyLg2v5qFn) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| Cupsey2028 | SOL | [7LRpii...YWpump](https://solscan.io/token/7LRpiiDzNVRdxfatA5T1iGvQmPUP46pMkpfGnqYWpump) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| [Tiana](https://dexscreener.com/solana/4agoaezcnghm48te9jvw6kysjzsmxejyecyprfzom4gd) | SOL | [MeDy6n...m3pump](https://solscan.io/token/MeDy6nEaqwRs6g8bDuthTrMJfV8WEQDHA7bSHm3pump) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| [BullPad](https://dexscreener.com/solana/8xhumrdufgyaavn4rp27cpowpzcmnkc33ymtxt6wjmye) | SOL | [BcbuAE...xQpump](https://solscan.io/token/BcbuAEmVwQ4QWBNn1KQxcsJnpH39LGE76apE6XxQpump) | 是 | 否 | verified / address_preflight_v0.4 | 多池数据冲突，需链上/聚合源复核；PVP候选仅记录，非紧急精查 |
| Ferret | SOL | [HXuiny...tJpump](https://solscan.io/token/HXuinymFnfjaiM4LkaFDLvvQ4a1WL5qoupdyUGtJpump) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| [Cog](https://dexscreener.com/solana/b9ytardjvsmfujzzimy92bfj6lmm2wynzhzz4anlmczj) | SOL | [7rSpKg...d9pump](https://solscan.io/token/7rSpKgASuXN5hfw3jsKNZN6ysNCR1Eixb2PD2Nd9pump) | 是 | 否 | verified / address_preflight_v0.4 | 多池数据冲突，需链上/聚合源复核；PVP候选仅记录，非紧急精查 |

### F. 钱包行为 / AVE命中样本表
| Token | 链 | 合约地址 | 行为状态 | 行为层级 | AVE命中 | 判断 |
|---|---|---|---|---|---:|---|
| AA | BSC | [0x01bf...0f6936](https://bscscan.com/token/0x01bf3d77cd08b19bf3f2309972123a2cca0f6936) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |

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
| LP层级 | Micro 11 / Early 3 / Liquid 8 / Mature 3 | 下一步可以按层级分别设置进攻规则 |
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