# 自我进化轮巡

**本轮时间 UTC：** 2026-10-03T01:39:06Z
**版本：** 0.5.0-ave-cache-wallet-behavior-prep
**S0 时间锚点：** 2026-06-16T16:15:17+09:00

## 一句话结论
本轮从 130 个合并Token中筛出 1 个主观察候选。v0.5已在v0.4.1基础上增加AVE周缓存真实接口接入框架、Smart Wallet持久保存、wallet_behavior_latest.json，以及BSC Transfer级钱包行为样本。注意：BSC当前是Transfer样本，不等同完整Swap解码。
合约地址可用 25 个，缺失 0 个；缺失地址的候选不能进入后续链上精查。

## 本轮扫描摘要
| 指标 | 数量 |
|---|---:|
| 原始池子记录 | 222 |
| 合并后Token | 130 |
| 输出候选 | 25 |
| 主观察 | 1 |
| 次观察 | 5 |
| PVP风险池 | 8 |
| 成熟池观察 | 6 |
| 低优先观察 | 5 |
| 多池Token | 5 |
| 多池冲突 | 2 |
| Symbol桥接合并 | 2 |
| 合约地址可用 | 25 |
| 合约地址缺失 | 0 |
| Micro层 | 6 |
| Early层 | 11 |
| Liquid层 | 7 |
| Mature层 | 1 |
| 需要链上确认 | 15 |
| 紧急精查候选 | 1 |

## v0.5 数据确认状态
| 项目 | 状态 |
|---|---|
| AVE Smart Wallet周缓存 | active，钱包数 1651，刷新时间 2026-09-28T02:48:12Z，是否过期 否 |
| 链上预检 | 本轮检查 12 个，验证通过 12 个，失败 0 个 |
| Helius状态 | 未配置，SOL使用公共RPC或跳过增强解析 |
| 当前精查层级 | 0.5.0-chain-preflight-plus-wallet-behavior：地址/账户预检 + v0.5钱包行为样本，完整Swap留存仍待下一版 |
| 钱包行为样本 | 本轮检查 1 个，BSC Transfer样本 1 个，SOL签名级 0 个，AVE钱包命中 0 个 |

## 第一部分：生成结果表格

### A. 上次记录结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| APM | BSC | [0x72a2...a0921e](https://bscscan.com/token/0x72a22faa6a522c81a8f5d508381e18af3da0921e) | 主观察 | Score 91; Tier Liquid; LP $1.54M; Vol24H $8.25M; 24H +2.00%; V/LP 5.34x; 池数 1; 分项 L20/V17/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [CATE](https://dexscreener.com/solana/hmzvseemtzhhvznw9uwbag85hctmfnkbhzux16cy7ca3) | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | 主观察 | Score 86; Tier Liquid; LP $3.17M; Vol24H $4.69M; 24H +23.73%; V/LP 1.48x; 池数 1; 分项 L20/V17/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [e/acc](https://dexscreener.com/solana/4jankfddd5fftk5pxdj3pptwjutefswqejzjcgkq9kww) | SOL | [CbcyNo...kzpKoU](https://solscan.io/token/CbcyNo7m1amFWqEQm2m4PLv1UNvpcL3C1Ujm6AkzpKoU) | 主观察 | Score 78; Tier Early; LP $687.4K; Vol24H $5.19M; 24H -14.47%; V/LP 7.56x; 池数 2; 分项 L17/V17/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| PAID | SOL | [98kfF7...zypump](https://solscan.io/token/98kfF7rmsg1QDUEoCqNE7g7M1FdrTt92TEp2CLzypump) | 主观察 | Score 76; Tier Early; LP $644.6K; Vol24H $1.37M; 24H -21.35%; V/LP 2.13x; 池数 1; 分项 L17/V15/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| BREW | BSC | [0xfa6d...3f2159](https://bscscan.com/token/0xfa6d9b504848606eb9aec04ccc161d169b3f2159) | 次观察 | Score 75; Tier Early; LP $743.6K; Vol24H $1.08M; 24H +16.74%; V/LP 1.45x; 池数 1; 分项 L17/V14/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| TART | BSC | [0x7ab8...750314](https://bscscan.com/token/0x7ab8d02cbb51ff7223fde700eaaa2a91bf750314) | 次观察 | Score 72; Tier Early; LP $462.4K; Vol24H $170.4K; 24H +16.38%; V/LP 0.37x; 池数 1; 分项 L15/V8/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [EMBER](https://dexscreener.com/solana/2y6pcqa4fep3jlifdan9jvmw7lsk8f3gwstfy8p7trae) | SOL | [5dvXTZ...k4QEC6](https://solscan.io/token/5dvXTZ5qwgafnHtwu3Ls3QrWx1U4LQsFeCuJgkk4QEC6) | 次观察 | Score 71; Tier Early; LP $299.0K; Vol24H $341.7K; 24H -4.69%; V/LP 1.14x; 池数 1; 分项 L14/V11/B22/Buy3/Risk-3 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [Pinata](https://dexscreener.com/solana/braoezs1zhzdqwqwkwnh3z4ouylxvlcvglpfhhbvzcht) | SOL | [Edpcd9...vopump](https://solscan.io/token/Edpcd9aYh6BVRKV5hYrgnEuJ3MHAFcdnHtSL9yvopump) | 次观察 | Score 64; Tier Micro; LP $50.6K; Vol24H $240.1K; 24H +8.74%; V/LP 4.75x; 池数 1; 分项 L6/V9/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| ct | BSC | [0x0a09...867f46](https://bscscan.com/token/0x0a092e544da31150b439a1aaa1a3a2214a867f46) | PVP风险池 | Score 51; Tier Liquid; LP $1.65M; Vol24H $104.30M; 24H +9.16%; V/LP 63.04x; 池数 1; 分项 L20/V17/B17/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| Agency | SOL | [7Vertk...XVpump](https://solscan.io/token/7VertkgF9KLhxxJXHX6uaWuoYZTP9LdGj2bWmVXVpump) | PVP风险池 | Score 31; Tier Early; LP $191.6K; Vol24H $14.35M; 24H +3617.08%; V/LP 74.89x; 池数 2; 分项 L12/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### B. 本轮扫描结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| APM | BSC | [0x72a2...a0921e](https://bscscan.com/token/0x72a22faa6a522c81a8f5d508381e18af3da0921e) | 主观察 | Score 91; Tier Liquid; LP $1.55M; Vol24H $8.59M; 24H +2.48%; V/LP 5.53x; 池数 1; 分项 L20/V17/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [EMBER](https://dexscreener.com/solana/2y6pcqa4fep3jlifdan9jvmw7lsk8f3gwstfy8p7trae) | SOL | [5dvXTZ...k4QEC6](https://solscan.io/token/5dvXTZ5qwgafnHtwu3Ls3QrWx1U4LQsFeCuJgkk4QEC6) | 次观察 | Score 75; Tier Early; LP $303.9K; Vol24H $315.2K; 24H -7.45%; V/LP 1.04x; 池数 1; 分项 L14/V10/B22/Buy8/Risk-3 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| BREW | BSC | [0xfa6d...3f2159](https://bscscan.com/token/0xfa6d9b504848606eb9aec04ccc161d169b3f2159) | 次观察 | Score 75; Tier Liquid; LP $778.6K; Vol24H $1.07M; 24H +22.95%; V/LP 1.38x; 池数 1; 分项 L17/V14/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| TART | BSC | [0x7ab8...750314](https://bscscan.com/token/0x7ab8d02cbb51ff7223fde700eaaa2a91bf750314) | 次观察 | Score 73; Tier Early; LP $460.1K; Vol24H $173.4K; 24H +15.56%; V/LP 0.38x; 池数 1; 分项 L15/V9/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [GOIF](https://dexscreener.com/solana/4d56grhvrhh825hjbrkx4t6a5u9ujwcmgpsyv9bwhy3o) | SOL | [nZbPjC...6Dpump](https://solscan.io/token/nZbPjCn4GJcLxrdHWRnMhPt875EyHSNTzhFmD6Dpump) | 次观察 | Score 72; Tier Early; LP $265.6K; Vol24H $261.1K; 24H +23.62%; V/LP 0.98x; 池数 1; 分项 L13/V10/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| PAID | SOL | [98kfF7...zypump](https://solscan.io/token/98kfF7rmsg1QDUEoCqNE7g7M1FdrTt92TEp2CLzypump) | 次观察 | Score 71; Tier Early; LP $663.7K; Vol24H $1.17M; 24H -27.00%; V/LP 1.76x; 池数 1; 分项 L17/V14/B8/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| ct | BSC | [0x0a09...867f46](https://bscscan.com/token/0x0a092e544da31150b439a1aaa1a3a2214a867f46) | PVP风险池 | Score 51; Tier Liquid; LP $1.68M; Vol24H $95.45M; 24H +14.83%; V/LP 56.90x; 池数 1; 分项 L20/V17/B17/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| Agency | SOL | [7Vertk...XVpump](https://solscan.io/token/7VertkgF9KLhxxJXHX6uaWuoYZTP9LdGj2bWmVXVpump) | PVP风险池 | Score 31; Tier Early; LP $183.5K; Vol24H $13.05M; 24H +10219.70%; V/LP 71.13x; 池数 2; 分项 L12/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [www](https://dexscreener.com/solana/cr469kh7ocptqk5yademjvpbwx1dixxlioopfjn23jsg) | SOL | [GAwhcp...3Q9S9H](https://solscan.io/token/GAwhcphCqCv5bKHmCiN4VDdNWfbXJL4npmkc8L3Q9S9H) | PVP风险池 | Score 29; Tier Early; LP $133.6K; Vol24H $26.11M; 24H +2222.00%; V/LP 195.34x; 池数 3; 分项 L10/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| HOTBOT | SOL | [8nnaeW...MhXrGF](https://solscan.io/token/8nnaeWCw8mUypcGAgbmSuzAT85uWx4UN12adDrMhXrGF) | PVP风险池 | Score 29; Tier Early; LP $127.3K; Vol24H $5.75M; 24H +2646.96%; V/LP 45.14x; 池数 2; 分项 L10/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [ANON](https://dexscreener.com/solana/fyknankgfqr5ryskcx56ijvykadgekefnd9p5x97wfz) | SOL | [2AKrTT...Kjpump](https://solscan.io/token/2AKrTTVNsxhHV2FLNBWUBv6W6Vq35VJMuiAhjsKjpump) | PVP风险池 | Score 28; Tier Micro; LP $99.7K; Vol24H $6.45M; 24H +641.00%; V/LP 64.70x; 池数 1; 分项 L9/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [SOCKET](https://dexscreener.com/solana/ba2yyz4yuksmcmdgpqrv5fqiotgnykrc571pfhc66gje) | SOL | [XLBLxb...8Mpump](https://solscan.io/token/XLBLxbY1Mr7aadnqAbmqSBXLEyUdjvUXtXCnz8Mpump) | PVP风险池 | Score 28; Tier Micro; LP $84.8K; Vol24H $4.86M; 24H +1255.00%; V/LP 57.36x; 池数 2; 分项 L9/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [FILLED](https://dexscreener.com/solana/a8jmwc6ijm7duubftgrcpg9hqgsn9gipkj39q1hbhqzk) | SOL | [8dBnKH...4zpump](https://solscan.io/token/8dBnKHwNYH3hz2fFTJczVwzBTpJFAMtc53k3uA4zpump) | PVP风险池 | Score 26; Tier Early; LP $120.3K; Vol24H $3.93M; 24H +967.00%; V/LP 32.65x; 池数 1; 分项 L10/V17/B0/Buy8/Risk-33 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [CATGPT](https://dexscreener.com/solana/3hsl3g9q4zyzwlgyqvx2tcvm6hs2izkcduwehtpzzgfv) | SOL | [CNohWH...weEGg9](https://solscan.io/token/CNohWHNTurS7PpB55czspwUJfpk9yy92uf1wXdweEGg9) | PVP风险池 | Score 15; Tier Micro; LP $47.8K; Vol24H $9.16M; 24H +269.00%; V/LP 191.49x; 池数 1; 分项 L6/V17/B0/Buy8/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| AKE | BSC | [0x2c3a...12f7db](https://bscscan.com/token/0x2c3a8ee94ddd97244a93bc48298f97d2c412f7db) | 成熟池观察 | Score 73; Tier Liquid; LP $2.79M; Vol24H $2.21M; 24H +5.18%; V/LP 0.79x; 池数 1; 分项 L20/V16/B22/Buy3/Risk-12 | 钱包级数据不可用；当前仅代理指标；资产偏成熟，不按早期吸筹处理；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 成熟池观察，不占用早期Alpha主榜 |

### C. PVP风险池明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| ct | BSC | [0x0a09...867f46](https://bscscan.com/token/0x0a092e544da31150b439a1aaa1a3a2214a867f46) | 24H波动可控；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 51; Tier Liquid; LP $1.68M; Vol24H $95.45M; 24H +14.83%; V/LP 56.90x; 池数 1; 分项 L20/V17/B17/Buy3/Risk-30 | 只记录热度，不进入主榜 |
| Agency | SOL | [7Vertk...XVpump](https://solscan.io/token/7VertkgF9KLhxxJXHX6uaWuoYZTP9LdGj2bWmVXVpump) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 31; Tier Early; LP $183.5K; Vol24H $13.05M; 24H +10219.70%; V/LP 71.13x; 池数 2; 分项 L12/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [www](https://dexscreener.com/solana/cr469kh7ocptqk5yademjvpbwx1dixxlioopfjn23jsg) | SOL | [GAwhcp...3Q9S9H](https://solscan.io/token/GAwhcphCqCv5bKHmCiN4VDdNWfbXJL4npmkc8L3Q9S9H) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 29; Tier Early; LP $133.6K; Vol24H $26.11M; 24H +2222.00%; V/LP 195.34x; 池数 3; 分项 L10/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| HOTBOT | SOL | [8nnaeW...MhXrGF](https://solscan.io/token/8nnaeWCw8mUypcGAgbmSuzAT85uWx4UN12adDrMhXrGF) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 29; Tier Early; LP $127.3K; Vol24H $5.75M; 24H +2646.96%; V/LP 45.14x; 池数 2; 分项 L10/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [ANON](https://dexscreener.com/solana/fyknankgfqr5ryskcx56ijvykadgekefnd9p5x97wfz) | SOL | [2AKrTT...Kjpump](https://solscan.io/token/2AKrTTVNsxhHV2FLNBWUBv6W6Vq35VJMuiAhjsKjpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 28; Tier Micro; LP $99.7K; Vol24H $6.45M; 24H +641.00%; V/LP 64.70x; 池数 1; 分项 L9/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [SOCKET](https://dexscreener.com/solana/ba2yyz4yuksmcmdgpqrv5fqiotgnykrc571pfhc66gje) | SOL | [XLBLxb...8Mpump](https://solscan.io/token/XLBLxbY1Mr7aadnqAbmqSBXLEyUdjvUXtXCnz8Mpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 28; Tier Micro; LP $84.8K; Vol24H $4.86M; 24H +1255.00%; V/LP 57.36x; 池数 2; 分项 L9/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [FILLED](https://dexscreener.com/solana/a8jmwc6ijm7duubftgrcpg9hqgsn9gipkj39q1hbhqzk) | SOL | [8dBnKH...4zpump](https://solscan.io/token/8dBnKHwNYH3hz2fFTJczVwzBTpJFAMtc53k3uA4zpump) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高；非主流报价池 | Score 26; Tier Early; LP $120.3K; Vol24H $3.93M; 24H +967.00%; V/LP 32.65x; 池数 1; 分项 L10/V17/B0/Buy8/Risk-33 | 只记录热度，不进入主榜 |
| [CATGPT](https://dexscreener.com/solana/3hsl3g9q4zyzwlgyqvx2tcvm6hs2izkcduwehtpzzgfv) | SOL | [CNohWH...weEGg9](https://solscan.io/token/CNohWHNTurS7PpB55czspwUJfpk9yy92uf1wXdweEGg9) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 15; Tier Micro; LP $47.8K; Vol24H $9.16M; 24H +269.00%; V/LP 191.49x; 池数 1; 分项 L6/V17/B0/Buy8/Risk-40 | 只记录热度，不进入主榜 |

### D. 成熟池观察明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| AKE | BSC | [0x2c3a...12f7db](https://bscscan.com/token/0x2c3a8ee94ddd97244a93bc48298f97d2c412f7db) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 73; Tier Liquid; LP $2.79M; Vol24H $2.21M; 24H +5.18%; V/LP 0.79x; 池数 1; 分项 L20/V16/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| Bonk | SOL | [DezXAZ...pPB263](https://solscan.io/token/DezXAZ8z7PnrnRJjz3wXBoRgixCa6xjnB7YaB1pPB263) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 69; Tier Early; LP $415.6K; Vol24H $3.29M; 24H -2.48%; V/LP 7.92x; 池数 1; 分项 L15/V17/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| MarsCoin | BSC | [0xfe18...5c7777](https://bscscan.com/token/0xfe189e97832da1573e4e4ff034f4ffc3a15c7777) | 24H波动可控；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限 | Score 68; Tier Early; LP $413.6K; Vol24H $2.39M; 24H -13.65%; V/LP 5.79x; 池数 1; 分项 L15/V16/B17/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| UAI | BSC | [0x3e5d...ba9ea0](https://bscscan.com/token/0x3e5d4f8aee0d9b3082d5f6da5d6e225d17ba9ea0) | 24H波动可控；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；成熟大市值 | Score 68; Tier Liquid; LP $1.13M; Vol24H $5.39M; 24H -18.37%; V/LP 4.77x; 池数 1; 分项 L19/V17/B17/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| CARDS | SOL | [CARDSc...dKxYjp](https://solscan.io/token/CARDSccUMFKoPRZxt5vt3ksUbxEFEcnZ3H2pd3dKxYjp) | 24H未过热但已明显波动；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 60; Tier Liquid; LP $4.02M; Vol24H $13.04M; 24H +40.45%; V/LP 3.24x; 池数 1; 分项 L20/V17/B8/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| [PUMP FUN](https://dexscreener.com/solana/hvth7essypg7ewzwd8ztect4wzlznxtgxbjn2xdztgez) | SOL | [3At4zC...js5R4x](https://solscan.io/token/3At4zCkWM5C9JV66WyVLBT4z9PcpGCUTPvBuhEjs5R4x) | 24H接近横盘；买入笔数占优；LP达主观察门槛；Volume/LP未失真；24H成交不足；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 58; Tier Mature; LP $56.85M; Vol24H $41.13; 24H +0.00%; V/LP 0.00x; 池数 1; 分项 L20/V0/B22/Buy12/Risk-20 | 成熟池观察，不占用早期Alpha主榜 |

### E. 链上确认/紧急精查表
| Token | 链 | 合约地址 | 是否需要链上确认 | 紧急精查 | 预检状态 | 原因 |
|---|---|---|---|---|---|---|
| APM | BSC | [0x72a2...a0921e](https://bscscan.com/token/0x72a22faa6a522c81a8f5d508381e18af3da0921e) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| [EMBER](https://dexscreener.com/solana/2y6pcqa4fep3jlifdan9jvmw7lsk8f3gwstfy8p7trae) | SOL | [5dvXTZ...k4QEC6](https://solscan.io/token/5dvXTZ5qwgafnHtwu3Ls3QrWx1U4LQsFeCuJgkk4QEC6) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| BREW | BSC | [0xfa6d...3f2159](https://bscscan.com/token/0xfa6d9b504848606eb9aec04ccc161d169b3f2159) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| TART | BSC | [0x7ab8...750314](https://bscscan.com/token/0x7ab8d02cbb51ff7223fde700eaaa2a91bf750314) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [GOIF](https://dexscreener.com/solana/4d56grhvrhh825hjbrkx4t6a5u9ujwcmgpsyv9bwhy3o) | SOL | [nZbPjC...6Dpump](https://solscan.io/token/nZbPjCn4GJcLxrdHWRnMhPt875EyHSNTzhFmD6Dpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| PAID | SOL | [98kfF7...zypump](https://solscan.io/token/98kfF7rmsg1QDUEoCqNE7g7M1FdrTt92TEp2CLzypump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| 龙虾 | BSC | [0xeccb...7e4444](https://bscscan.com/token/0xeccbb861c0dda7efd964010085488b69317e4444) | 是 | 否 | verified / address_preflight_v0.4 | 多池数据冲突，需链上/聚合源复核 |
| ct | BSC | [0x0a09...867f46](https://bscscan.com/token/0x0a092e544da31150b439a1aaa1a3a2214a867f46) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| Agency | SOL | [7Vertk...XVpump](https://solscan.io/token/7VertkgF9KLhxxJXHX6uaWuoYZTP9LdGj2bWmVXVpump) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| [www](https://dexscreener.com/solana/cr469kh7ocptqk5yademjvpbwx1dixxlioopfjn23jsg) | SOL | [GAwhcp...3Q9S9H](https://solscan.io/token/GAwhcphCqCv5bKHmCiN4VDdNWfbXJL4npmkc8L3Q9S9H) | 是 | 否 | verified / address_preflight_v0.4 | 多池数据冲突，需链上/聚合源复核；PVP候选仅记录，非紧急精查 |

### F. 钱包行为 / AVE命中样本表
| Token | 链 | 合约地址 | 行为状态 | 行为层级 | AVE命中 | 判断 |
|---|---|---|---|---|---:|---|
| APM | BSC | [0x72a2...a0921e](https://bscscan.com/token/0x72a22faa6a522c81a8f5d508381e18af3da0921e) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |

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
| 成熟池观察 | 6 个 | 成熟资产不占早期Alpha主榜 |
| 合约地址覆盖 | 可用 25，缺失 0 | 地址缺失会阻断BSC RPC/Helius精查，需要优先补齐 |
| LP层级 | Micro 6 / Early 11 / Liquid 7 / Mature 1 | 下一步可以按层级分别设置进攻规则 |
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
| dexscreener_boosts | {'ok': True, 'count': 29, 'expanded': 25} |
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