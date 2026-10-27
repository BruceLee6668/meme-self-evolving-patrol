# 自我进化轮巡

**本轮时间 UTC：** 2026-10-27T11:26:53Z
**版本：** 0.5.0-ave-cache-wallet-behavior-prep
**S0 时间锚点：** 2026-06-16T16:15:17+09:00

## 一句话结论
本轮没有出现可直接确认的“干净底部聪明钱扫货”。
合约地址可用 25 个，缺失 0 个；缺失地址的候选不能进入后续链上精查。

## 本轮扫描摘要
| 指标 | 数量 |
|---|---:|
| 原始池子记录 | 253 |
| 合并后Token | 141 |
| 输出候选 | 25 |
| 主观察 | 0 |
| 次观察 | 6 |
| PVP风险池 | 8 |
| 成熟池观察 | 4 |
| 低优先观察 | 7 |
| 多池Token | 9 |
| 多池冲突 | 4 |
| Symbol桥接合并 | 2 |
| 合约地址可用 | 25 |
| 合约地址缺失 | 0 |
| Micro层 | 7 |
| Early层 | 13 |
| Liquid层 | 4 |
| Mature层 | 1 |
| 需要链上确认 | 15 |
| 紧急精查候选 | 0 |

## v0.5 数据确认状态
| 项目 | 状态 |
|---|---|
| AVE Smart Wallet周缓存 | active，钱包数 2235，刷新时间 2026-10-26T02:30:11Z，是否过期 否 |
| 链上预检 | 本轮检查 12 个，验证通过 12 个，失败 0 个 |
| Helius状态 | 未配置，SOL使用公共RPC或跳过增强解析 |
| 当前精查层级 | 0.5.0-chain-preflight-plus-wallet-behavior：地址/账户预检 + v0.5钱包行为样本，完整Swap留存仍待下一版 |
| 钱包行为样本 | 本轮检查 0 个，BSC Transfer样本 0 个，SOL签名级 0 个，AVE钱包命中 0 个 |

## 第一部分：生成结果表格

### A. 上次记录结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| TART | BSC | [0x7ab8...750314](https://bscscan.com/token/0x7ab8d02cbb51ff7223fde700eaaa2a91bf750314) | 主观察 | Score 81; Tier Liquid; LP $915.5K; Vol24H $231.5K; 24H +3.63%; V/LP 0.25x; 池数 1; 分项 L18/V9/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [Dacity](https://dexscreener.com/solana/g2uurbmvdzdfp4qyobjrskbxsi7d6v4bpp9thps36y4b) | SOL | [nxPqZ4...Rjpump](https://solscan.io/token/nxPqZ4F7ux8Vph5NFu25rEP6Kx9Gr1U6Fmj36Rjpump) | 主观察 | Score 80; Tier Early; LP $427.4K; Vol24H $1.19M; 24H +5.15%; V/LP 2.78x; 池数 1; 分项 L15/V14/B22/Buy8/Risk-3 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [XTO](https://dexscreener.com/solana/4pbedygxzvuvr94sgtjc6c5cx7nmgbdnv1x8ac9opj7o) | SOL | [XtogpW...JeJfHt](https://solscan.io/token/XtogpWjiAgvkemc5gr1auxkh77w3vKgSQN1nxJeJfHt) | 主观察 | Score 78; Tier Early; LP $274.8K; Vol24H $116.9K; 24H +7.37%; V/LP 0.43x; 池数 4; 分项 L13/V7/B22/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [Kimchi](https://dexscreener.com/solana/6dnxwecbtdnnstpb5tdnxzsfge3hmsngeuzhdue4b1ph) | SOL | [CSocnz...m7pump](https://solscan.io/token/CSocnzcRpgSCr1naKcNTieWZUxb6rABe45j844m7pump) | 主观察 | Score 77; Tier Early; LP $328.5K; Vol24H $1.24M; 24H -7.75%; V/LP 3.76x; 池数 1; 分项 L14/V14/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [SI276](https://dexscreener.com/solana/12jc1dzjpzbcdakum4brakh9jcfry2tlg1ffgsl4ftcg) | SOL | [HMYd9t...6upump](https://solscan.io/token/HMYd9tosnUXuNHmq7pXmoePRVBLBBjA3JBfydq6upump) | 次观察 | Score 75; Tier Micro; LP $87.6K; Vol24H $146.4K; 24H -2.52%; V/LP 1.67x; 池数 1; 分项 L9/V8/B22/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [EXFIL](https://dexscreener.com/solana/2zpfdgd48k7b2u9yqz4hjspaptovu9uiebfqyxeoexkv) | SOL | [6FhVPc...y6pump](https://solscan.io/token/6FhVPctYg363pQbs4iSvqyHe2cJzfsvFD96gePy6pump) | 次观察 | Score 71; Tier Early; LP $186.3K; Vol24H $245.8K; 24H +7.30%; V/LP 1.32x; 池数 1; 分项 L12/V10/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [UDTF](https://dexscreener.com/solana/h7nwfrmv5afadanarsfxlj1fwojfpwbogdgc5elbcw5e) | SOL | [oF2XvG...7ypump](https://solscan.io/token/oF2XvGAX3v8VCNje6yMxJqQZraXz2hPth2kPg7ypump) | 次观察 | Score 69; Tier Early; LP $500.2K; Vol24H $189.5K; 24H +43.04%; V/LP 0.38x; 池数 1; 分项 L16/V9/B8/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| LMAO! | SOL | [H74CYm...uApump](https://solscan.io/token/H74CYmXgMkYHYuSRsZt6RJb4NYp2u72Vw8BS5huApump) | 次观察 | Score 66; Tier Early; LP $306.7K; Vol24H $3.57M; 24H +19.10%; V/LP 11.64x; 池数 2; 分项 L14/V17/B17/Buy12/Risk-18 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [GATO](https://dexscreener.com/solana/5e3dxlxgwmtdcoka51wyyakttjfzbwqcoyuhbui5gt2m) | SOL | [HsprHx...k6pump](https://solscan.io/token/HsprHxBRgiVaQdRf3TnKNuZZtaX9JUSPgMFdAkk6pump) | 次观察 | Score 65; Tier Early; LP $201.7K; Vol24H $853.4K; 24H +27.18%; V/LP 4.23x; 池数 6; 分项 L12/V13/B8/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| BTW | BSC | [0x4440...35acaa](https://bscscan.com/token/0x444045b0ee1ee319a660a5e3d604ca0ffa35acaa) | PVP风险池 | Score 31; Tier Early; LP $219.2K; Vol24H $5.65M; 24H -17.37%; V/LP 25.78x; 池数 1; 分项 L12/V17/B17/Buy3/Risk-42 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### B. 本轮扫描结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| [Kimchi](https://dexscreener.com/solana/6dnxwecbtdnnstpb5tdnxzsfge3hmsngeuzhdue4b1ph) | SOL | [CSocnz...m7pump](https://solscan.io/token/CSocnzcRpgSCr1naKcNTieWZUxb6rABe45j844m7pump) | 次观察 | Score 72; Tier Early; LP $322.6K; Vol24H $957.7K; 24H -18.88%; V/LP 2.97x; 池数 1; 分项 L14/V14/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [DOAS](https://dexscreener.com/solana/9mgjpszild1tj43xms98bg3pvyoux9aclkobdsn8v8gp) | SOL | [2qPoPQ...Z4pump](https://solscan.io/token/2qPoPQQCHGtDbgdSxXfrzW1iRS3cGbKmMWSMapZ4pump) | 次观察 | Score 70; Tier Early; LP $439.8K; Vol24H $358.3K; 24H +78.21%; V/LP 0.81x; 池数 2; 分项 L15/V11/B8/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [UDTF](https://dexscreener.com/solana/h7nwfrmv5afadanarsfxlj1fwojfpwbogdgc5elbcw5e) | SOL | [oF2XvG...7ypump](https://solscan.io/token/oF2XvGAX3v8VCNje6yMxJqQZraXz2hPth2kPg7ypump) | 次观察 | Score 69; Tier Early; LP $530.1K; Vol24H $186.6K; 24H +50.43%; V/LP 0.35x; 池数 1; 分项 L16/V9/B8/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [BTC](https://dexscreener.com/solana/3m9svgl4u6atkaiexf3xhqqnfmb6ijvzk3memcqaen1w) | SOL | [C5xph2...L6pump](https://solscan.io/token/C5xph2yL6gMdxmuLGxJBkGpmuDFfyi5fqkBNhvL6pump) | 次观察 | Score 66; Tier Early; LP $306.8K; Vol24H $409.6K; 24H -17.94%; V/LP 1.34x; 池数 1; 分项 L14/V11/B17/Buy3/Risk-3 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [EXFIL](https://dexscreener.com/solana/2zpfdgd48k7b2u9yqz4hjspaptovu9uiebfqyxeoexkv) | SOL | [6FhVPc...y6pump](https://solscan.io/token/6FhVPctYg363pQbs4iSvqyHe2cJzfsvFD96gePy6pump) | 次观察 | Score 65; Tier Early; LP $179.4K; Vol24H $177.7K; 24H -16.77%; V/LP 0.99x; 池数 1; 分项 L12/V9/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [GATO](https://dexscreener.com/solana/5e3dxlxgwmtdcoka51wyyakttjfzbwqcoyuhbui5gt2m) | SOL | [HsprHx...k6pump](https://solscan.io/token/HsprHxBRgiVaQdRf3TnKNuZZtaX9JUSPgMFdAkk6pump) | 次观察 | Score 65; Tier Early; LP $207.3K; Vol24H $902.3K; 24H +35.08%; V/LP 4.35x; 池数 1; 分项 L12/V13/B8/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| BTW | BSC | [0x4440...35acaa](https://bscscan.com/token/0x444045b0ee1ee319a660a5e3d604ca0ffa35acaa) | PVP风险池 | Score 37; Tier Early; LP $273.1K; Vol24H $5.96M; 24H -5.73%; V/LP 21.83x; 池数 1; 分项 L13/V17/B22/Buy3/Risk-42 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| Q | BSC | [0xc07e...690589](https://bscscan.com/token/0xc07e1300dc138601fa6b0b59f8d0fa477e690589) | PVP风险池 | Score 30; Tier Liquid; LP $1.37M; Vol24H $33.15M; 24H +26.96%; V/LP 24.22x; 池数 2; 分项 L20/V17/B8/Buy3/Risk-42 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [Nothing](https://dexscreener.com/solana/gfgxhqzmkf1v2mfs94ldmk8ckgf7rhzpjdzzttjjzkhq) | SOL | [51SfaA...Kupump](https://solscan.io/token/51SfaAyrYaR8FpibXT4TXtxEpnZSNoDwYVRojtKupump) | PVP风险池 | Score 28; Tier Micro; LP $98.4K; Vol24H $4.66M; 24H +1917.00%; V/LP 47.40x; 池数 2; 分项 L9/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [ELON2028](https://dexscreener.com/solana/6jede2e3c6j7snnq9vtblluz2wsyi7rx5ovvwy8hypdg) | SOL | [27Qg7E...iJpump](https://solscan.io/token/27Qg7EcnGfmbthfQeQXTs4qjfnvU6gXf8W1ahJiJpump) | PVP风险池 | Score 25; Tier Micro; LP $27.8K; Vol24H $4.32M; 24H +79.39%; V/LP 155.12x; 池数 1; 分项 L4/V17/B8/Buy12/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [TRUMP2028](https://dexscreener.com/solana/7yvfsjjzheggz3c4qqutxn8zbch3dazfkc6ntxcpuyvd) | SOL | [6zMfMX...gapump](https://solscan.io/token/6zMfMXjovo7ivtrypSP7YspHm5TcbV4Sh5TwSDgapump) | PVP风险池 | Score 17; Tier Micro; LP $29.8K; Vol24H $4.03M; 24H +122.00%; V/LP 135.26x; 池数 3; 分项 L4/V17/B0/Buy12/Risk-40 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [Shitcoin](https://dexscreener.com/solana/9kahpmrriblcujm9jhwnmwcz6qvwjuyylcxeuspwxd9w) | SOL | [JVtVUd...Nopump](https://solscan.io/token/JVtVUduUFx3HL3fA87YA77YDGn5iQoYDeDaLFNopump) | PVP风险池 | Score 9; Tier Micro; LP $31.5K; Vol24H $1.80M; 24H +149.00%; V/LP 57.29x; 池数 1; 分项 L5/V15/B0/Buy8/Risk-43 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [TOMAMI](https://dexscreener.com/solana/4adc2vgykxhfskqzmyvqabh9rcaipithsmk5xn7btt3o) | SOL | [5bDtxo...ozpump](https://solscan.io/token/5bDtxo7ytnRQUTi72XNfzYA2YWCSdmRbQ3mgKJozpump) | PVP风险池 | Score 7; Tier Micro; LP $2.6K; Vol24H $1.54M; 24H -94.47%; V/LP 585.64x; 池数 3; 分项 L0/V15/B0/Buy8/Risk-40 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [urmom](https://dexscreener.com/solana/8tyacyuttfqbglwez8nt6wkbkpqsej8oqq3k6fnp8vwu) | SOL | [5XapX9...XZpump](https://solscan.io/token/5XapX9FpytfrwqY8Y7mNStwrur8u5fNnJjEcJNXZpump) | PVP风险池 | Score 7; Tier Micro; LP $2.4K; Vol24H $1.39M; 24H -94.90%; V/LP 572.97x; 池数 4; 分项 L0/V15/B0/Buy8/Risk-40 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| STONK | SOL | [6GmAFS...MpUNgx](https://solscan.io/token/6GmAFSYs4gk3FDao5FzzySQpPZaWsa4rUJHacpMpUNgx) | 成熟池观察 | Score 79; Tier Liquid; LP $2.54M; Vol24H $4.81M; 24H +0.72%; V/LP 1.89x; 池数 1; 分项 L20/V17/B22/Buy8/Risk-12 | 钱包级数据不可用；当前仅代理指标；资产偏成熟，不按早期吸筹处理；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 成熟池观察，不占用早期Alpha主榜 |

### C. PVP风险池明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| BTW | BSC | [0x4440...35acaa](https://bscscan.com/token/0x444045b0ee1ee319a660a5e3d604ca0ffa35acaa) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP极端偏高；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 37; Tier Early; LP $273.1K; Vol24H $5.96M; 24H -5.73%; V/LP 21.83x; 池数 1; 分项 L13/V17/B22/Buy3/Risk-42 | 只记录热度，不进入主榜 |
| Q | BSC | [0xc07e...690589](https://bscscan.com/token/0xc07e1300dc138601fa6b0b59f8d0fa477e690589) | 24H未过热但已明显波动；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP极端偏高；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 30; Tier Liquid; LP $1.37M; Vol24H $33.15M; 24H +26.96%; V/LP 24.22x; 池数 2; 分项 L20/V17/B8/Buy3/Risk-42 | 只记录热度，不进入主榜 |
| [Nothing](https://dexscreener.com/solana/gfgxhqzmkf1v2mfs94ldmk8ckgf7rhzpjdzzttjjzkhq) | SOL | [51SfaA...Kupump](https://solscan.io/token/51SfaAyrYaR8FpibXT4TXtxEpnZSNoDwYVRojtKupump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 28; Tier Micro; LP $98.4K; Vol24H $4.66M; 24H +1917.00%; V/LP 47.40x; 池数 2; 分项 L9/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [ELON2028](https://dexscreener.com/solana/6jede2e3c6j7snnq9vtblluz2wsyi7rx5ovvwy8hypdg) | SOL | [27Qg7E...iJpump](https://solscan.io/token/27Qg7EcnGfmbthfQeQXTs4qjfnvU6gXf8W1ahJiJpump) | 24H未过热但已明显波动；买入笔数占优；LP未达主观察门槛；24H成交合格；LP偏薄；Volume/LP极端偏高 | Score 25; Tier Micro; LP $27.8K; Vol24H $4.32M; 24H +79.39%; V/LP 155.12x; 池数 1; 分项 L4/V17/B8/Buy12/Risk-40 | 只记录热度，不进入主榜 |
| [TRUMP2028](https://dexscreener.com/solana/7yvfsjjzheggz3c4qqutxn8zbch3dazfkc6ntxcpuyvd) | SOL | [6zMfMX...gapump](https://solscan.io/token/6zMfMXjovo7ivtrypSP7YspHm5TcbV4Sh5TwSDgapump) | 买入笔数占优；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 17; Tier Micro; LP $29.8K; Vol24H $4.03M; 24H +122.00%; V/LP 135.26x; 池数 3; 分项 L4/V17/B0/Buy12/Risk-40 | 只记录热度，不进入主榜 |
| [Shitcoin](https://dexscreener.com/solana/9kahpmrriblcujm9jhwnmwcz6qvwjuyylcxeuspwxd9w) | SOL | [JVtVUd...Nopump](https://solscan.io/token/JVtVUduUFx3HL3fA87YA77YDGn5iQoYDeDaLFNopump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高；非主流报价池 | Score 9; Tier Micro; LP $31.5K; Vol24H $1.80M; 24H +149.00%; V/LP 57.29x; 池数 1; 分项 L5/V15/B0/Buy8/Risk-43 | 只记录热度，不进入主榜 |
| [TOMAMI](https://dexscreener.com/solana/4adc2vgykxhfskqzmyvqabh9rcaipithsmk5xn7btt3o) | SOL | [5bDtxo...ozpump](https://solscan.io/token/5bDtxo7ytnRQUTi72XNfzYA2YWCSdmRbQ3mgKJozpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 7; Tier Micro; LP $2.6K; Vol24H $1.54M; 24H -94.47%; V/LP 585.64x; 池数 3; 分项 L0/V15/B0/Buy8/Risk-40 | 只记录热度，不进入主榜 |
| [urmom](https://dexscreener.com/solana/8tyacyuttfqbglwez8nt6wkbkpqsej8oqq3k6fnp8vwu) | SOL | [5XapX9...XZpump](https://solscan.io/token/5XapX9FpytfrwqY8Y7mNStwrur8u5fNnJjEcJNXZpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 7; Tier Micro; LP $2.4K; Vol24H $1.39M; 24H -94.90%; V/LP 572.97x; 池数 4; 分项 L0/V15/B0/Buy8/Risk-40 | 只记录热度，不进入主榜 |

### D. 成熟池观察明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| STONK | SOL | [6GmAFS...MpUNgx](https://solscan.io/token/6GmAFSYs4gk3FDao5FzzySQpPZaWsa4rUJHacpMpUNgx) | 24H接近横盘；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限 | Score 79; Tier Liquid; LP $2.54M; Vol24H $4.81M; 24H +0.72%; V/LP 1.89x; 池数 1; 分项 L20/V17/B22/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| PUMP | SOL | [pumpCm...7H9Dfn](https://solscan.io/token/pumpCmXqMfrsAkQ5r49WcJnRayYRqmXz6ae8H7H9Dfn) | 24H接近横盘；LP达主观察门槛；24H成交合格；Volume/LP未失真；卖出笔数占优；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 71; Tier Mature; LP $22.84M; Vol24H $5.25M; 24H -2.01%; V/LP 0.23x; 池数 1; 分项 L20/V17/B22/Buy0/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| ARIA | BSC | [0x5d3a...555238](https://bscscan.com/token/0x5d3a12c42e5372b2cc3264ab3cdcf660a1555238) | 24H波动可控；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限 | Score 69; Tier Liquid; LP $1.55M; Vol24H $7.58M; 24H -11.59%; V/LP 4.90x; 池数 1; 分项 L20/V17/B17/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| TAG | BSC | [0x208b...682025](https://bscscan.com/token/0x208bf3e7da9639f1eaefa2de78c23396b0682025) | 24H未过热但已明显波动；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 60; Tier Liquid; LP $2.39M; Vol24H $11.73M; 24H +62.58%; V/LP 4.91x; 池数 1; 分项 L20/V17/B8/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |

### E. 链上确认/紧急精查表
| Token | 链 | 合约地址 | 是否需要链上确认 | 紧急精查 | 预检状态 | 原因 |
|---|---|---|---|---|---|---|
| [Kimchi](https://dexscreener.com/solana/6dnxwecbtdnnstpb5tdnxzsfge3hmsngeuzhdue4b1ph) | SOL | [CSocnz...m7pump](https://solscan.io/token/CSocnzcRpgSCr1naKcNTieWZUxb6rABe45j844m7pump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [DOAS](https://dexscreener.com/solana/9mgjpszild1tj43xms98bg3pvyoux9aclkobdsn8v8gp) | SOL | [2qPoPQ...Z4pump](https://solscan.io/token/2qPoPQQCHGtDbgdSxXfrzW1iRS3cGbKmMWSMapZ4pump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [UDTF](https://dexscreener.com/solana/h7nwfrmv5afadanarsfxlj1fwojfpwbogdgc5elbcw5e) | SOL | [oF2XvG...7ypump](https://solscan.io/token/oF2XvGAX3v8VCNje6yMxJqQZraXz2hPth2kPg7ypump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [BTC](https://dexscreener.com/solana/3m9svgl4u6atkaiexf3xhqqnfmb6ijvzk3memcqaen1w) | SOL | [C5xph2...L6pump](https://solscan.io/token/C5xph2yL6gMdxmuLGxJBkGpmuDFfyi5fqkBNhvL6pump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [EXFIL](https://dexscreener.com/solana/2zpfdgd48k7b2u9yqz4hjspaptovu9uiebfqyxeoexkv) | SOL | [6FhVPc...y6pump](https://solscan.io/token/6FhVPctYg363pQbs4iSvqyHe2cJzfsvFD96gePy6pump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [GATO](https://dexscreener.com/solana/5e3dxlxgwmtdcoka51wyyakttjfzbwqcoyuhbui5gt2m) | SOL | [HsprHx...k6pump](https://solscan.io/token/HsprHxBRgiVaQdRf3TnKNuZZtaX9JUSPgMFdAkk6pump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [USDF](https://dexscreener.com/solana/7c8vwwpwhpky4uchjxdvfzrhpjlepw9rpb92leodjdbw) | SOL | [9k6gfT...jYpump](https://solscan.io/token/9k6gfTLbDaUpx635kQaGTeDvzYs7hWdDW1MerpjYpump) | 是 | 否 | verified / address_preflight_v0.4 | 多池数据冲突，需链上/聚合源复核 |
| BTW | BSC | [0x4440...35acaa](https://bscscan.com/token/0x444045b0ee1ee319a660a5e3d604ca0ffa35acaa) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| Q | BSC | [0xc07e...690589](https://bscscan.com/token/0xc07e1300dc138601fa6b0b59f8d0fa477e690589) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| [Nothing](https://dexscreener.com/solana/gfgxhqzmkf1v2mfs94ldmk8ckgf7rhzpjdzzttjjzkhq) | SOL | [51SfaA...Kupump](https://solscan.io/token/51SfaAyrYaR8FpibXT4TXtxEpnZSNoDwYVRojtKupump) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |

### F. 钱包行为 / AVE命中样本表
| Token | 链 | 合约地址 | 行为状态 | 行为层级 | AVE命中 | 判断 |
|---|---|---|---|---|---:|---|
| - | - | - | 本轮无钱包行为样本 | - | 0 | - |

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
| 主观察候选 | 0 个 | 主榜继续稀缺，但必须结合合约地址进入链上确认 |
| PVP风险池 | 8 个 | v0.3已单独展示明细，便于判断噪声来源 |
| 成熟池观察 | 4 个 | 成熟资产不占早期Alpha主榜 |
| 合约地址覆盖 | 可用 25，缺失 0 | 地址缺失会阻断BSC RPC/Helius精查，需要优先补齐 |
| LP层级 | Micro 7 / Early 13 / Liquid 4 / Mature 1 | 下一步可以按层级分别设置进攻规则 |
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