# 自我进化轮巡

**本轮时间 UTC：** 2026-08-24T08:40:31Z
**版本：** 0.5.0-ave-cache-wallet-behavior-prep
**S0 时间锚点：** 2026-06-16T16:15:17+09:00

## 一句话结论
本轮从 126 个合并Token中筛出 1 个主观察候选。v0.5已在v0.4.1基础上增加AVE周缓存真实接口接入框架、Smart Wallet持久保存、wallet_behavior_latest.json，以及BSC Transfer级钱包行为样本。注意：BSC当前是Transfer样本，不等同完整Swap解码。
合约地址可用 25 个，缺失 0 个；缺失地址的候选不能进入后续链上精查。

## 本轮扫描摘要
| 指标 | 数量 |
|---|---:|
| 原始池子记录 | 244 |
| 合并后Token | 126 |
| 输出候选 | 25 |
| 主观察 | 1 |
| 次观察 | 4 |
| PVP风险池 | 8 |
| 成熟池观察 | 3 |
| 低优先观察 | 9 |
| 多池Token | 11 |
| 多池冲突 | 4 |
| Symbol桥接合并 | 4 |
| 合约地址可用 | 25 |
| 合约地址缺失 | 0 |
| Micro层 | 6 |
| Early层 | 12 |
| Liquid层 | 5 |
| Mature层 | 2 |
| 需要链上确认 | 15 |
| 紧急精查候选 | 1 |

## v0.5 数据确认状态
| 项目 | 状态 |
|---|---|
| AVE Smart Wallet周缓存 | active，钱包数 1089，刷新时间 2026-08-24T00:46:57Z，是否过期 否 |
| 链上预检 | 本轮检查 12 个，验证通过 12 个，失败 0 个 |
| Helius状态 | 未配置，SOL使用公共RPC或跳过增强解析 |
| 当前精查层级 | 0.5.0-chain-preflight-plus-wallet-behavior：地址/账户预检 + v0.5钱包行为样本，完整Swap留存仍待下一版 |
| 钱包行为样本 | 本轮检查 1 个，BSC Transfer样本 1 个，SOL签名级 0 个，AVE钱包命中 0 个 |

## 第一部分：生成结果表格

### A. 上次记录结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| TUT | BSC | [0xcaae...b799f3](https://bscscan.com/token/0xcaae2a2f939f51d97cdfa9a86e79e3f085b799f3) | 主观察 | Score 85; Tier Liquid; LP $4.68M; Vol24H $2.05M; 24H +21.50%; V/LP 0.44x; 池数 1; 分项 L20/V16/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| CATE | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | 次观察 | Score 68; Tier Liquid; LP $1.63M; Vol24H $19.43M; 24H -20.14%; V/LP 11.95x; 池数 2; 分项 L20/V17/B17/Buy8/Risk-18 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| QQQB | BSC | [0x2058...11efc7](https://bscscan.com/token/0x205812cdbed920aff76c6580abd681a46d11efc7) | 次观察 | Score 68; Tier Liquid; LP $1.88M; Vol24H $26.00M; 24H -0.41%; V/LP 13.84x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-18 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [UOTF](https://dexscreener.com/solana/2vjymaw6z3gnxvgb6yrsk7br9tnabcbgs8arzerorjtd) | SOL | [nWtPgk...82pump](https://solscan.io/token/nWtPgkXqZhfufMD3ojkNPwMbgP1bzKRfJ2UtM82pump) | 次观察 | Score 67; Tier Early; LP $112.0K; Vol24H $167.6K; 24H +20.79%; V/LP 1.50x; 池数 1; 分项 L10/V8/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| 牛来 | BSC | [0xbeea...377777](https://bscscan.com/token/0xbeea1d618e533a387d941f58a7d4c9b7bd377777) | 次观察 | Score 64; Tier Early; LP $521.8K; Vol24H $9.01M; 24H -18.03%; V/LP 17.26x; 池数 18; 分项 L16/V17/B17/Buy8/Risk-18 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| Bicat | BSC | [0xdbc6...207777](https://bscscan.com/token/0xdbc6333a7d8bcd95f96641eda4d095e69f207777) | PVP风险池 | Score 37; Tier Early; LP $117.5K; Vol24H $3.91M; 24H -42.36%; V/LP 33.25x; 池数 1; 分项 L10/V17/B8/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [CATALORIAN](https://dexscreener.com/solana/fvyok1cenymtxgpxblhymvubq2ievgq18uj4k7vkoj5q) | SOL | [4cvZwC...nFpump](https://solscan.io/token/4cvZwC17oMiUA7peKX5GhbaUWv4U5Lwrd8118xnFpump) | PVP风险池 | Score 33; Tier Early; LP $343.5K; Vol24H $10.89M; 24H +9413.00%; V/LP 31.70x; 池数 2; 分项 L14/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| BNBCAT | BSC | [0x3efb...6a7777](https://bscscan.com/token/0x3efbfff95576e1d23cf6ead0acd2e73f4d6a7777) | PVP风险池 | Score 32; Tier Early; LP $247.4K; Vol24H $11.95M; 24H +375.46%; V/LP 48.33x; 池数 6; 分项 L13/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| Morty | SOL | [GUmbtf...jzpump](https://solscan.io/token/GUmbtfjSZkybSFgPibBcvwExEBdXwewJHR5PkTjzpump) | PVP风险池 | Score 30; Tier Early; LP $144.6K; Vol24H $6.17M; 24H +674.52%; V/LP 42.64x; 池数 2; 分项 L11/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| CYBERCAT | SOL | [9HHTQ7...SVpump](https://solscan.io/token/9HHTQ7YMx82E987cNqF9KczyZrfKgqvKNyA2yHSVpump) | PVP风险池 | Score 30; Tier Micro; LP $60.2K; Vol24H $5.16M; 24H +834.76%; V/LP 85.68x; 池数 2; 分项 L7/V17/B0/Buy12/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### B. 本轮扫描结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| TUT | BSC | [0xcaae...b799f3](https://bscscan.com/token/0xcaae2a2f939f51d97cdfa9a86e79e3f085b799f3) | 主观察 | Score 85; Tier Liquid; LP $4.69M; Vol24H $2.09M; 24H +22.38%; V/LP 0.45x; 池数 1; 分项 L20/V16/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [App](https://dexscreener.com/solana/95xzpaggkdazgfdenx1dxfkuyzfvk53geu7mfa58qffw) | SOL | [49nkLr...Ta8pTL](https://solscan.io/token/49nkLrXi8nCZBVKsShDNasEtPe4Vn1mx9Xbr3kTa8pTL) | 次观察 | Score 68; Tier Early; LP $119.3K; Vol24H $525.1K; 24H +7.76%; V/LP 4.40x; 池数 3; 分项 L10/V12/B22/Buy0/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [CATE](https://dexscreener.com/solana/hmzvseemtzhhvznw9uwbag85hctmfnkbhzux16cy7ca3) | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | 次观察 | Score 68; Tier Liquid; LP $1.59M; Vol24H $19.26M; 24H -21.30%; V/LP 12.12x; 池数 2; 分项 L20/V17/B17/Buy8/Risk-18 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| QQQB | BSC | [0x2058...11efc7](https://bscscan.com/token/0x205812cdbed920aff76c6580abd681a46d11efc7) | 次观察 | Score 68; Tier Liquid; LP $1.88M; Vol24H $26.28M; 24H -0.66%; V/LP 13.96x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-18 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [UOTF](https://dexscreener.com/solana/2vjymaw6z3gnxvgb6yrsk7br9tnabcbgs8arzerorjtd) | SOL | [nWtPgk...82pump](https://solscan.io/token/nWtPgkXqZhfufMD3ojkNPwMbgP1bzKRfJ2UtM82pump) | 次观察 | Score 67; Tier Early; LP $111.1K; Vol24H $167.3K; 24H +19.20%; V/LP 1.51x; 池数 1; 分项 L10/V8/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| Bicat | BSC | [0xdbc6...207777](https://bscscan.com/token/0xdbc6333a7d8bcd95f96641eda4d095e69f207777) | PVP风险池 | Score 37; Tier Early; LP $109.3K; Vol24H $3.77M; 24H -66.08%; V/LP 34.48x; 池数 1; 分项 L10/V17/B8/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| BNBCAT | BSC | [0x3efb...6a7777](https://bscscan.com/token/0x3efbfff95576e1d23cf6ead0acd2e73f4d6a7777) | PVP风险池 | Score 32; Tier Early; LP $249.3K; Vol24H $11.96M; 24H +516.39%; V/LP 47.97x; 池数 5; 分项 L13/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [CATALORIAN](https://dexscreener.com/solana/fvyok1cenymtxgpxblhymvubq2ievgq18uj4k7vkoj5q) | SOL | [4cvZwC...nFpump](https://solscan.io/token/4cvZwC17oMiUA7peKX5GhbaUWv4U5Lwrd8118xnFpump) | PVP风险池 | Score 31; Tier Early; LP $217.1K; Vol24H $11.16M; 24H +3728.00%; V/LP 51.39x; 池数 2; 分项 L12/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [Morty](https://dexscreener.com/solana/8wa7x9ewdfvkikqrecmr3omwljmaqks2csjxw1pws7dh) | SOL | [GUmbtf...jzpump](https://solscan.io/token/GUmbtfjSZkybSFgPibBcvwExEBdXwewJHR5PkTjzpump) | PVP风险池 | Score 30; Tier Early; LP $151.6K; Vol24H $6.14M; 24H +591.00%; V/LP 40.50x; 池数 2; 分项 L11/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| CYBERCAT | SOL | [9HHTQ7...SVpump](https://solscan.io/token/9HHTQ7YMx82E987cNqF9KczyZrfKgqvKNyA2yHSVpump) | PVP风险池 | Score 30; Tier Micro; LP $60.9K; Vol24H $5.18M; 24H +866.84%; V/LP 85.15x; 池数 2; 分项 L7/V17/B0/Buy12/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [CVXV666](https://dexscreener.com/solana/hcqesmkzs1d1kgh1ymkwsekd7yp22g1wmgkxgtmkzq2q) | SOL | [C3bajJ...iBpump](https://solscan.io/token/C3bajJW843KN9Uu441JkXN7zVMs4VM2HvdAGyGiBpump) | PVP风险池 | Score 29; Tier Early; LP $123.2K; Vol24H $8.24M; 24H +3999.00%; V/LP 66.90x; 池数 1; 分项 L10/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [memes](https://dexscreener.com/bsc/0xd3c8668bff07b02d78019afe7f9a6e581499def2) | BSC | [0xF745...EE4444](https://bscscan.com/token/0xF74548802f4c700315F019FdE17178b392EE4444) | PVP风险池 | Score 28; Tier Micro; LP $87.3K; Vol24H $5.59M; 24H +50.73%; V/LP 64.03x; 池数 5; 分项 L9/V17/B8/Buy3/Risk-33 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| Polycat | SOL | [B4iCqV...QTpump](https://solscan.io/token/B4iCqVsAZv9dBiBVv58GJiBxWGmwkwbtPTn4sUQTpump) | PVP风险池 | Score 26; Tier Micro; LP $61.7K; Vol24H $3.87M; 24H +1069.41%; V/LP 62.78x; 池数 2; 分项 L7/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [ANSEM](https://dexscreener.com/solana/fnzky6x7entq1er3d225dqyt7ybfka4pskbmqhb8l3cc) | SOL | [9cRCn9...TGpump](https://solscan.io/token/9cRCn9rGT8V2imeM2BaKs13yhMEais3ruM3rPvTGpump) | 成熟池观察 | Score 77; Tier Liquid; LP $2.68M; Vol24H $1.54M; 24H -3.95%; V/LP 0.57x; 池数 1; 分项 L20/V15/B22/Buy8/Risk-12 | 钱包级数据不可用；当前仅代理指标；资产偏成熟，不按早期吸筹处理；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 成熟池观察，不占用早期Alpha主榜 |
| BTCB | BSC | [0x7130...3ead9c](https://bscscan.com/token/0x7130d2a12b9bcbfae4f2634d864a1ee1ce3ead9c) | 成熟池观察 | Score 74; Tier Mature; LP $18.33M; Vol24H $14.32M; 24H +0.74%; V/LP 0.78x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-12 | 钱包级数据不可用；当前仅代理指标；资产偏成熟，不按早期吸筹处理；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 成熟池观察，不占用早期Alpha主榜 |

### C. PVP风险池明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| Bicat | BSC | [0xdbc6...207777](https://bscscan.com/token/0xdbc6333a7d8bcd95f96641eda4d095e69f207777) | 24H未过热但已明显波动；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 37; Tier Early; LP $109.3K; Vol24H $3.77M; 24H -66.08%; V/LP 34.48x; 池数 1; 分项 L10/V17/B8/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| BNBCAT | BSC | [0x3efb...6a7777](https://bscscan.com/token/0x3efbfff95576e1d23cf6ead0acd2e73f4d6a7777) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 32; Tier Early; LP $249.3K; Vol24H $11.96M; 24H +516.39%; V/LP 47.97x; 池数 5; 分项 L13/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [CATALORIAN](https://dexscreener.com/solana/fvyok1cenymtxgpxblhymvubq2ievgq18uj4k7vkoj5q) | SOL | [4cvZwC...nFpump](https://solscan.io/token/4cvZwC17oMiUA7peKX5GhbaUWv4U5Lwrd8118xnFpump) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 31; Tier Early; LP $217.1K; Vol24H $11.16M; 24H +3728.00%; V/LP 51.39x; 池数 2; 分项 L12/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [Morty](https://dexscreener.com/solana/8wa7x9ewdfvkikqrecmr3omwljmaqks2csjxw1pws7dh) | SOL | [GUmbtf...jzpump](https://solscan.io/token/GUmbtfjSZkybSFgPibBcvwExEBdXwewJHR5PkTjzpump) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 30; Tier Early; LP $151.6K; Vol24H $6.14M; 24H +591.00%; V/LP 40.50x; 池数 2; 分项 L11/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| CYBERCAT | SOL | [9HHTQ7...SVpump](https://solscan.io/token/9HHTQ7YMx82E987cNqF9KczyZrfKgqvKNyA2yHSVpump) | 买入笔数占优；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 30; Tier Micro; LP $60.9K; Vol24H $5.18M; 24H +866.84%; V/LP 85.15x; 池数 2; 分项 L7/V17/B0/Buy12/Risk-30 | 只记录热度，不进入主榜 |
| [CVXV666](https://dexscreener.com/solana/hcqesmkzs1d1kgh1ymkwsekd7yp22g1wmgkxgtmkzq2q) | SOL | [C3bajJ...iBpump](https://solscan.io/token/C3bajJW843KN9Uu441JkXN7zVMs4VM2HvdAGyGiBpump) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 29; Tier Early; LP $123.2K; Vol24H $8.24M; 24H +3999.00%; V/LP 66.90x; 池数 1; 分项 L10/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [memes](https://dexscreener.com/bsc/0xd3c8668bff07b02d78019afe7f9a6e581499def2) | BSC | [0xF745...EE4444](https://bscscan.com/token/0xF74548802f4c700315F019FdE17178b392EE4444) | 24H未过热但已明显波动；买卖基本均衡；LP未达主观察门槛；24H成交合格；Volume/LP极端偏高；非主流报价池 | Score 28; Tier Micro; LP $87.3K; Vol24H $5.59M; 24H +50.73%; V/LP 64.03x; 池数 5; 分项 L9/V17/B8/Buy3/Risk-33 | 只记录热度，不进入主榜 |
| Polycat | SOL | [B4iCqV...QTpump](https://solscan.io/token/B4iCqVsAZv9dBiBVv58GJiBxWGmwkwbtPTn4sUQTpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 26; Tier Micro; LP $61.7K; Vol24H $3.87M; 24H +1069.41%; V/LP 62.78x; 池数 2; 分项 L7/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |

### D. 成熟池观察明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| [ANSEM](https://dexscreener.com/solana/fnzky6x7entq1er3d225dqyt7ybfka4pskbmqhb8l3cc) | SOL | [9cRCn9...TGpump](https://solscan.io/token/9cRCn9rGT8V2imeM2BaKs13yhMEais3ruM3rPvTGpump) | 24H接近横盘；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 77; Tier Liquid; LP $2.68M; Vol24H $1.54M; 24H -3.95%; V/LP 0.57x; 池数 1; 分项 L20/V15/B22/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| BTCB | BSC | [0x7130...3ead9c](https://bscscan.com/token/0x7130d2a12b9bcbfae4f2634d864a1ee1ce3ead9c) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 74; Tier Mature; LP $18.33M; Vol24H $14.32M; 24H +0.74%; V/LP 0.78x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| [PUMP](https://dexscreener.com/solana/4c8kctyztmtzwv83y5actpvt2axyyu2t9zhhdotfgnno) | SOL | [pumpCm...7H9Dfn](https://solscan.io/token/pumpCmXqMfrsAkQ5r49WcJnRayYRqmXz6ae8H7H9Dfn) | 24H波动可控；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；非主流报价池；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 66; Tier Mature; LP $108.57M; Vol24H $64.24M; 24H -11.29%; V/LP 0.59x; 池数 3; 分项 L20/V17/B17/Buy3/Risk-15 | 成熟池观察，不占用早期Alpha主榜 |

### E. 链上确认/紧急精查表
| Token | 链 | 合约地址 | 是否需要链上确认 | 紧急精查 | 预检状态 | 原因 |
|---|---|---|---|---|---|---|
| TUT | BSC | [0xcaae...b799f3](https://bscscan.com/token/0xcaae2a2f939f51d97cdfa9a86e79e3f085b799f3) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| [App](https://dexscreener.com/solana/95xzpaggkdazgfdenx1dxfkuyzfvk53geu7mfa58qffw) | SOL | [49nkLr...Ta8pTL](https://solscan.io/token/49nkLrXi8nCZBVKsShDNasEtPe4Vn1mx9Xbr3kTa8pTL) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [CATE](https://dexscreener.com/solana/hmzvseemtzhhvznw9uwbag85hctmfnkbhzux16cy7ca3) | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| QQQB | BSC | [0x2058...11efc7](https://bscscan.com/token/0x205812cdbed920aff76c6580abd681a46d11efc7) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [UOTF](https://dexscreener.com/solana/2vjymaw6z3gnxvgb6yrsk7br9tnabcbgs8arzerorjtd) | SOL | [nWtPgk...82pump](https://solscan.io/token/nWtPgkXqZhfufMD3ojkNPwMbgP1bzKRfJ2UtM82pump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [PUMP](https://dexscreener.com/solana/4c8kctyztmtzwv83y5actpvt2axyyu2t9zhhdotfgnno) | SOL | [pumpCm...7H9Dfn](https://solscan.io/token/pumpCmXqMfrsAkQ5r49WcJnRayYRqmXz6ae8H7H9Dfn) | 是 | 否 | verified / address_preflight_v0.4 | 多池数据冲突，需链上/聚合源复核 |
| 牛来 | BSC | [0xbeea...377777](https://bscscan.com/token/0xbeea1d618e533a387d941f58a7d4c9b7bd377777) | 是 | 否 | verified / address_preflight_v0.4 | 多池数据冲突，需链上/聚合源复核 |
| Bicat | BSC | [0xdbc6...207777](https://bscscan.com/token/0xdbc6333a7d8bcd95f96641eda4d095e69f207777) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| BNBCAT | BSC | [0x3efb...6a7777](https://bscscan.com/token/0x3efbfff95576e1d23cf6ead0acd2e73f4d6a7777) | 是 | 否 | verified / address_preflight_v0.4 | 多池数据冲突，需链上/聚合源复核；PVP候选仅记录，非紧急精查 |
| [CATALORIAN](https://dexscreener.com/solana/fvyok1cenymtxgpxblhymvubq2ievgq18uj4k7vkoj5q) | SOL | [4cvZwC...nFpump](https://solscan.io/token/4cvZwC17oMiUA7peKX5GhbaUWv4U5Lwrd8118xnFpump) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |

### F. 钱包行为 / AVE命中样本表
| Token | 链 | 合约地址 | 行为状态 | 行为层级 | AVE命中 | 判断 |
|---|---|---|---|---|---:|---|
| TUT | BSC | [0xcaae...b799f3](https://bscscan.com/token/0xcaae2a2f939f51d97cdfa9a86e79e3f085b799f3) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |

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
| 成熟池观察 | 3 个 | 成熟资产不占早期Alpha主榜 |
| 合约地址覆盖 | 可用 25，缺失 0 | 地址缺失会阻断BSC RPC/Helius精查，需要优先补齐 |
| LP层级 | Micro 6 / Early 12 / Liquid 5 / Mature 2 | 下一步可以按层级分别设置进攻规则 |
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
| dexscreener_search | {'ok': True, 'count': 342} |
| geckoterminal_bsc_trending | {'ok': True, 'count': 20} |
| geckoterminal_solana_trending | {'ok': True, 'count': 20} |

## 数据限制
- This v0.4 scan uses free public sources plus lightweight chain address/account preflight when enabled.
- AVE Smart Money weekly cache structure is connected; real AVE API refresh is handled by the weekly workflow/cache file.
- S0 exact historical replay is not implemented yet; candidates are marked with current metrics only.
- Wallet-level buy/sell retention is not implemented yet; v0.4 only preflights token contract/account existence.
- v0.4 adds chain preflight status and Smart Wallet cache status on top of contract-address output, liquidity tiers, visible PVP/mature detail tables, and chain-verify flags.
- Contract addresses are extracted from DEXScreener baseToken or GeckoTerminal relationships when available; missing addresses are explicitly marked unavailable.