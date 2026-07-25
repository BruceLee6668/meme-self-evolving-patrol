# 自我进化轮巡

**本轮时间 UTC：** 2026-07-25T13:12:32Z
**版本：** 0.5.0-ave-cache-wallet-behavior-prep
**S0 时间锚点：** 2026-06-16T16:15:17+09:00

## 一句话结论
本轮没有出现可直接确认的“干净底部聪明钱扫货”。
合约地址可用 25 个，缺失 0 个；缺失地址的候选不能进入后续链上精查。

## 本轮扫描摘要
| 指标 | 数量 |
|---|---:|
| 原始池子记录 | 260 |
| 合并后Token | 110 |
| 输出候选 | 25 |
| 主观察 | 0 |
| 次观察 | 2 |
| PVP风险池 | 8 |
| 成熟池观察 | 3 |
| 低优先观察 | 10 |
| 多池Token | 12 |
| 多池冲突 | 4 |
| Symbol桥接合并 | 3 |
| 合约地址可用 | 25 |
| 合约地址缺失 | 0 |
| Micro层 | 8 |
| Early层 | 5 |
| Liquid层 | 9 |
| Mature层 | 2 |
| 需要链上确认 | 12 |
| 紧急精查候选 | 0 |

## v0.5 数据确认状态
| 项目 | 状态 |
|---|---|
| AVE Smart Wallet周缓存 | active，钱包数 732，刷新时间 2026-07-20T02:12:03Z，是否过期 否 |
| 链上预检 | 本轮检查 12 个，验证通过 12 个，失败 0 个 |
| Helius状态 | 未配置，SOL使用公共RPC或跳过增强解析 |
| 当前精查层级 | 0.5.0-chain-preflight-plus-wallet-behavior：地址/账户预检 + v0.5钱包行为样本，完整Swap留存仍待下一版 |
| 钱包行为样本 | 本轮检查 0 个，BSC Transfer样本 0 个，SOL签名级 0 个，AVE钱包命中 0 个 |

## 第一部分：生成结果表格

### A. 上次记录结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| [TOESCOIN](https://dexscreener.com/solana/ee3zk9fxp9guair2xerefxf4tsexezffuwetrna2pkcv) | SOL | [6ehEcT...HDpump](https://solscan.io/token/6ehEcTMCc85aNF4x9CWx8HuvWGhxQtvKdhKVf2HDpump) | 主观察 | Score 86; Tier Early; LP $274.5K; Vol24H $1.48M; 24H -7.18%; V/LP 5.40x; 池数 10; 分项 L13/V15/B22/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| ESPORTS | BSC | [0xf39e...508e48](https://bscscan.com/token/0xf39e4b21c84e737df08e2c3b32541d856f508e48) | 主观察 | Score 84; Tier Liquid; LP $1.06M; Vol24H $2.14M; 24H -7.91%; V/LP 2.01x; 池数 1; 分项 L19/V16/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [Staccana](https://dexscreener.com/solana/2higkrf25q9wmcyfgyk96aaufvv5zucfdafhhduvetcq) | SOL | [73edX6...i1pump](https://solscan.io/token/73edX6xoGY4v5y2hzuKdrUbJXLntqgmo74au1Ki1pump) | 次观察 | Score 73; Tier Micro; LP $74.4K; Vol24H $99.6K; 24H +0.34%; V/LP 1.34x; 池数 1; 分项 L8/V7/B22/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [PLASTIC](https://dexscreener.com/solana/83dtgbjqp1xgknjqdxvqzf9shqduhjgaid5yrvgkz4oh) | SOL | [58smR4...3vrise](https://solscan.io/token/58smR4GCZBxXfUUiX6KZ4JXkK6jmX42vjatWgA3vrise) | 次观察 | Score 66; Tier Liquid; LP $1.45M; Vol24H $851.53; 24H -1.82%; V/LP 0.00x; 池数 1; 分项 L20/V0/B22/Buy8/Risk-8 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| KET | SOL | [9Pfync...Lxpump](https://solscan.io/token/9Pfync3ejPC9eHqVzq3nYQJAhyhjqpnB9UsaSfLxpump) | 次观察 | Score 65; Tier Early; LP $357.3K; Vol24H $2.28M; 24H +61.17%; V/LP 6.39x; 池数 2; 分项 L14/V16/B8/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| AKE | BSC | [0x2c3a...12f7db](https://bscscan.com/token/0x2c3a8ee94ddd97244a93bc48298f97d2c412f7db) | PVP风险池 | Score 37; Tier Liquid; LP $960.4K; Vol24H $27.61M; 24H +16.84%; V/LP 28.74x; 池数 2; 分项 L18/V17/B17/Buy3/Risk-42 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [looong](https://dexscreener.com/solana/9u25cchjce4cmi7cemfcphtkasz6gyrtrvalye4ujfts) | SOL | [AkchGA...6wpump](https://solscan.io/token/AkchGAUdXXRGHt3HXaHbTvw3JLGUwtJRmYnkG66wpump) | PVP风险池 | Score 36; Tier Micro; LP $92.8K; Vol24H $4.45M; 24H -30.59%; V/LP 47.93x; 池数 2; 分项 L9/V17/B8/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| Z | BSC | [0x0402...ab4444](https://bscscan.com/token/0x04020e4d81a20701afe303ee3267f2c3caab4444) | PVP风险池 | Score 30; Tier Early; LP $139.6K; Vol24H $4.37M; 24H +2150.57%; V/LP 31.29x; 池数 7; 分项 L11/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| TRUMP2028 | SOL | [2d2GZd...TQpump](https://solscan.io/token/2d2GZdehy2YGrj1MJ3y3yhXjficMa2J3GtncxkTQpump) | PVP风险池 | Score 27; Tier Micro; LP $79.0K; Vol24H $11.04M; 24H +2223.57%; V/LP 139.75x; 池数 7; 分项 L8/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [MEMENOTE](https://dexscreener.com/solana/5za2q4gfzwtozntrb8etyw3atc1zwgzy8ucgafuedrlw) | SOL | [2vBS6D...Lopump](https://solscan.io/token/2vBS6D5mTPbQHChbZevmJ3Ck4uyrmdhbt1LkbyLopump) | PVP风险池 | Score 26; Tier Micro; LP $63.8K; Vol24H $5.40M; 24H +439.00%; V/LP 84.64x; 池数 10; 分项 L7/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### B. 本轮扫描结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| ESPORTS | BSC | [0xf39e...508e48](https://bscscan.com/token/0xf39e4b21c84e737df08e2c3b32541d856f508e48) | 次观察 | Score 70; Tier Liquid; LP $1.19M; Vol24H $2.35M; 24H +27.74%; V/LP 1.97x; 池数 1; 分项 L19/V16/B8/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| KET | SOL | [9Pfync...Lxpump](https://solscan.io/token/9Pfync3ejPC9eHqVzq3nYQJAhyhjqpnB9UsaSfLxpump) | 次观察 | Score 65; Tier Early; LP $333.1K; Vol24H $2.25M; 24H +34.62%; V/LP 6.75x; 池数 2; 分项 L14/V16/B8/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| AKE | BSC | [0x2c3a...12f7db](https://bscscan.com/token/0x2c3a8ee94ddd97244a93bc48298f97d2c412f7db) | PVP风险池 | Score 37; Tier Liquid; LP $968.1K; Vol24H $26.83M; 24H +21.95%; V/LP 27.72x; 池数 2; 分项 L18/V17/B17/Buy3/Risk-42 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| looong | SOL | [AkchGA...6wpump](https://solscan.io/token/AkchGAUdXXRGHt3HXaHbTvw3JLGUwtJRmYnkG66wpump) | PVP风险池 | Score 36; Tier Micro; LP $87.7K; Vol24H $4.24M; 24H -29.48%; V/LP 48.37x; 池数 2; 分项 L9/V17/B8/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| Z | BSC | [0x0402...ab4444](https://bscscan.com/token/0x04020e4d81a20701afe303ee3267f2c3caab4444) | PVP风险池 | Score 30; Tier Early; LP $141.3K; Vol24H $3.91M; 24H +215.87%; V/LP 27.65x; 池数 7; 分项 L11/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| TRUMP2028 | SOL | [2d2GZd...TQpump](https://solscan.io/token/2d2GZdehy2YGrj1MJ3y3yhXjficMa2J3GtncxkTQpump) | PVP风险池 | Score 27; Tier Micro; LP $65.6K; Vol24H $11.28M; 24H +1477.75%; V/LP 171.99x; 池数 9; 分项 L8/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [MEMENOTE](https://dexscreener.com/solana/5za2q4gfzwtozntrb8etyw3atc1zwgzy8ucgafuedrlw) | SOL | [2vBS6D...Lopump](https://solscan.io/token/2vBS6D5mTPbQHChbZevmJ3Ck4uyrmdhbt1LkbyLopump) | PVP风险池 | Score 27; Tier Micro; LP $74.7K; Vol24H $5.44M; 24H +1006.00%; V/LP 72.72x; 池数 8; 分项 L8/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [RAKO](https://dexscreener.com/solana/hmvaoct9ag9jpmxvke8nbg2ieomreezs3yb3bgna49fa) | SOL | [5sd8bK...Xipump](https://solscan.io/token/5sd8bKraewJNHFg72scxxYXNeLCASVct1gxqi3Xipump) | PVP风险池 | Score 26; Tier Micro; LP $53.0K; Vol24H $2.72M; 24H +1310.00%; V/LP 51.38x; 池数 2; 分项 L7/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [CHANGE](https://dexscreener.com/solana/cgbnfl4nsqnvc5bpe92tmr2zsyutafkpecgfvukqfsrq) | SOL | [D9cCca...Bfpump](https://solscan.io/token/D9cCcaA7ByHST1zj4KMLCXM4iZJgKfvYhsbYCvBfpump) | PVP风险池 | Score 13; Tier Micro; LP $35.3K; Vol24H $1.92M; 24H +181.00%; V/LP 54.37x; 池数 1; 分项 L5/V16/B0/Buy8/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [Waddles](https://dexscreener.com/solana/fbw5p9fzdswtmnmhasjfkofexlcosfund8taufwjguzr) | SOL | [EbzAM6...Hypump](https://solscan.io/token/EbzAM6hw7MQP8VNiwixoc5mgW18NkR348HFxVMHypump) | PVP风险池 | Score 11; Tier Micro; LP $20.6K; Vol24H $2.37M; 24H +128.00%; V/LP 115.28x; 池数 1; 分项 L3/V16/B0/Buy8/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [ANSEM](https://dexscreener.com/solana/fnzky6x7entq1er3d225dqyt7ybfka4pskbmqhb8l3cc) | SOL | [9cRCn9...TGpump](https://solscan.io/token/9cRCn9rGT8V2imeM2BaKs13yhMEais3ruM3rPvTGpump) | 成熟池观察 | Score 76; Tier Liquid; LP $1.87M; Vol24H $1.23M; 24H -1.08%; V/LP 0.66x; 池数 1; 分项 L20/V14/B22/Buy8/Risk-12 | 钱包级数据不可用；当前仅代理指标；资产偏成熟，不按早期吸筹处理；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 成熟池观察，不占用早期Alpha主榜 |
| ZAMA | BSC | [0x6907...87519f](https://bscscan.com/token/0x6907a5986c4950bdaf2f81828ec0737ce787519f) | 成熟池观察 | Score 74; Tier Liquid; LP $1.34M; Vol24H $8.11M; 24H +0.15%; V/LP 6.06x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-12 | 钱包级数据不可用；当前仅代理指标；资产偏成熟，不按早期吸筹处理；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 成熟池观察，不占用早期Alpha主榜 |
| [NEVERZERO](https://dexscreener.com/solana/dmryq83qiugurjd36qky5y2cefzajqrhuxw8kyvg1z2e) | SOL | [7MsJCv...g2rise](https://solscan.io/token/7MsJCvDi5t5U3Ya2UAs5bR75VJyVMr2FKdzGmeg2rise) | 成熟池观察 | Score 71; Tier Mature; LP $19.73M; Vol24H $59.6K; 24H -0.10%; V/LP 0.00x; 池数 1; 分项 L20/V5/B22/Buy12/Risk-12 | 钱包级数据不可用；当前仅代理指标；资产偏成熟，不按早期吸筹处理；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 成熟池观察，不占用早期Alpha主榜 |
| [FISTFLOOR](https://dexscreener.com/solana/3fgmjpi5wgr9jhqf37lz8uh3dzsydjzslkrff4gagw5s) | SOL | [3XJb1B...Mirise](https://solscan.io/token/3XJb1BtqeXNNAeAAfCzqF5ReWjok11cnStJdM1Mirise) | 低优先观察 | Score 63; Tier Liquid; LP $1.83M; Vol24H $22.5K; 24H +0.66%; V/LP 0.01x; 池数 1; 分项 L20/V2/B22/Buy3/Risk-8 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 低优先观察，不追高 |
| AA | BSC | [0x01bf...0f6936](https://bscscan.com/token/0x01bf3d77cd08b19bf3f2309972123a2cca0f6936) | 低优先观察 | Score 63; Tier Liquid; LP $1.09M; Vol24H $5.57M; 24H +294.35%; V/LP 5.09x; 池数 1; 分项 L19/V17/B0/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 低优先观察，不追高 |

### C. PVP风险池明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| AKE | BSC | [0x2c3a...12f7db](https://bscscan.com/token/0x2c3a8ee94ddd97244a93bc48298f97d2c412f7db) | 24H波动可控；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP极端偏高；FDV超过早期Alpha主榜上限；成熟大市值 | Score 37; Tier Liquid; LP $968.1K; Vol24H $26.83M; 24H +21.95%; V/LP 27.72x; 池数 2; 分项 L18/V17/B17/Buy3/Risk-42 | 只记录热度，不进入主榜 |
| looong | SOL | [AkchGA...6wpump](https://solscan.io/token/AkchGAUdXXRGHt3HXaHbTvw3JLGUwtJRmYnkG66wpump) | 24H未过热但已明显波动；买卖略偏买入；LP未达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 36; Tier Micro; LP $87.7K; Vol24H $4.24M; 24H -29.48%; V/LP 48.37x; 池数 2; 分项 L9/V17/B8/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| Z | BSC | [0x0402...ab4444](https://bscscan.com/token/0x04020e4d81a20701afe303ee3267f2c3caab4444) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 30; Tier Early; LP $141.3K; Vol24H $3.91M; 24H +215.87%; V/LP 27.65x; 池数 7; 分项 L11/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| TRUMP2028 | SOL | [2d2GZd...TQpump](https://solscan.io/token/2d2GZdehy2YGrj1MJ3y3yhXjficMa2J3GtncxkTQpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 27; Tier Micro; LP $65.6K; Vol24H $11.28M; 24H +1477.75%; V/LP 171.99x; 池数 9; 分项 L8/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [MEMENOTE](https://dexscreener.com/solana/5za2q4gfzwtozntrb8etyw3atc1zwgzy8ucgafuedrlw) | SOL | [2vBS6D...Lopump](https://solscan.io/token/2vBS6D5mTPbQHChbZevmJ3Ck4uyrmdhbt1LkbyLopump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 27; Tier Micro; LP $74.7K; Vol24H $5.44M; 24H +1006.00%; V/LP 72.72x; 池数 8; 分项 L8/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [RAKO](https://dexscreener.com/solana/hmvaoct9ag9jpmxvke8nbg2ieomreezs3yb3bgna49fa) | SOL | [5sd8bK...Xipump](https://solscan.io/token/5sd8bKraewJNHFg72scxxYXNeLCASVct1gxqi3Xipump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 26; Tier Micro; LP $53.0K; Vol24H $2.72M; 24H +1310.00%; V/LP 51.38x; 池数 2; 分项 L7/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [CHANGE](https://dexscreener.com/solana/cgbnfl4nsqnvc5bpe92tmr2zsyutafkpecgfvukqfsrq) | SOL | [D9cCca...Bfpump](https://solscan.io/token/D9cCcaA7ByHST1zj4KMLCXM4iZJgKfvYhsbYCvBfpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 13; Tier Micro; LP $35.3K; Vol24H $1.92M; 24H +181.00%; V/LP 54.37x; 池数 1; 分项 L5/V16/B0/Buy8/Risk-40 | 只记录热度，不进入主榜 |
| [Waddles](https://dexscreener.com/solana/fbw5p9fzdswtmnmhasjfkofexlcosfund8taufwjguzr) | SOL | [EbzAM6...Hypump](https://solscan.io/token/EbzAM6hw7MQP8VNiwixoc5mgW18NkR348HFxVMHypump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 11; Tier Micro; LP $20.6K; Vol24H $2.37M; 24H +128.00%; V/LP 115.28x; 池数 1; 分项 L3/V16/B0/Buy8/Risk-40 | 只记录热度，不进入主榜 |

### D. 成熟池观察明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| [ANSEM](https://dexscreener.com/solana/fnzky6x7entq1er3d225dqyt7ybfka4pskbmqhb8l3cc) | SOL | [9cRCn9...TGpump](https://solscan.io/token/9cRCn9rGT8V2imeM2BaKs13yhMEais3ruM3rPvTGpump) | 24H接近横盘；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 76; Tier Liquid; LP $1.87M; Vol24H $1.23M; 24H -1.08%; V/LP 0.66x; 池数 1; 分项 L20/V14/B22/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| ZAMA | BSC | [0x6907...87519f](https://bscscan.com/token/0x6907a5986c4950bdaf2f81828ec0737ce787519f) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；市值超过早期Alpha主榜上限 | Score 74; Tier Liquid; LP $1.34M; Vol24H $8.11M; 24H +0.15%; V/LP 6.06x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| [NEVERZERO](https://dexscreener.com/solana/dmryq83qiugurjd36qky5y2cefzajqrhuxw8kyvg1z2e) | SOL | [7MsJCv...g2rise](https://solscan.io/token/7MsJCvDi5t5U3Ya2UAs5bR75VJyVMr2FKdzGmeg2rise) | 24H接近横盘；买入笔数占优；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限；成熟大池 | Score 71; Tier Mature; LP $19.73M; Vol24H $59.6K; 24H -0.10%; V/LP 0.00x; 池数 1; 分项 L20/V5/B22/Buy12/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |

### E. 链上确认/紧急精查表
| Token | 链 | 合约地址 | 是否需要链上确认 | 紧急精查 | 预检状态 | 原因 |
|---|---|---|---|---|---|---|
| ESPORTS | BSC | [0xf39e...508e48](https://bscscan.com/token/0xf39e4b21c84e737df08e2c3b32541d856f508e48) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| KET | SOL | [9Pfync...Lxpump](https://solscan.io/token/9Pfync3ejPC9eHqVzq3nYQJAhyhjqpnB9UsaSfLxpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [PUMP](https://dexscreener.com/solana/9ww15cehwhuapsr3a2ysu3ilk3vswwbqfp9rzbpvaiph) | SOL | [8FtafP...sC5yBx](https://solscan.io/token/8FtafPHhmYVtKQYrbNs4ZSS2Hwykw5dJ3t1JtGsC5yBx) | 是 | 否 | verified / address_preflight_v0.4 | 多池数据冲突，需链上/聚合源复核 |
| [Agamemnon](https://dexscreener.com/solana/636bkx7ugs6vdb9fhajdwfdi4afuphdarrtw2ntvueag) | SOL | [2cAtqs...rCpump](https://solscan.io/token/2cAtqsRafKS7baN3mvJARhyZiMRdW4fZYNUUWUrCpump) | 是 | 否 | verified / address_preflight_v0.4 | 多池数据冲突，需链上/聚合源复核 |
| AKE | BSC | [0x2c3a...12f7db](https://bscscan.com/token/0x2c3a8ee94ddd97244a93bc48298f97d2c412f7db) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| looong | SOL | [AkchGA...6wpump](https://solscan.io/token/AkchGAUdXXRGHt3HXaHbTvw3JLGUwtJRmYnkG66wpump) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| Z | BSC | [0x0402...ab4444](https://bscscan.com/token/0x04020e4d81a20701afe303ee3267f2c3caab4444) | 是 | 否 | verified / address_preflight_v0.4 | 多池数据冲突，需链上/聚合源复核；PVP候选仅记录，非紧急精查 |
| TRUMP2028 | SOL | [2d2GZd...TQpump](https://solscan.io/token/2d2GZdehy2YGrj1MJ3y3yhXjficMa2J3GtncxkTQpump) | 是 | 否 | verified / address_preflight_v0.4 | 多池数据冲突，需链上/聚合源复核；PVP候选仅记录，非紧急精查 |
| [MEMENOTE](https://dexscreener.com/solana/5za2q4gfzwtozntrb8etyw3atc1zwgzy8ucgafuedrlw) | SOL | [2vBS6D...Lopump](https://solscan.io/token/2vBS6D5mTPbQHChbZevmJ3Ck4uyrmdhbt1LkbyLopump) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| [RAKO](https://dexscreener.com/solana/hmvaoct9ag9jpmxvke8nbg2ieomreezs3yb3bgna49fa) | SOL | [5sd8bK...Xipump](https://solscan.io/token/5sd8bKraewJNHFg72scxxYXNeLCASVct1gxqi3Xipump) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |

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
| 成熟池观察 | 3 个 | 成熟资产不占早期Alpha主榜 |
| 合约地址覆盖 | 可用 25，缺失 0 | 地址缺失会阻断BSC RPC/Helius精查，需要优先补齐 |
| LP层级 | Micro 8 / Early 5 / Liquid 9 / Mature 2 | 下一步可以按层级分别设置进攻规则 |
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