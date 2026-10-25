# 自我进化轮巡

**本轮时间 UTC：** 2026-10-25T14:43:31Z
**版本：** 0.5.0-ave-cache-wallet-behavior-prep
**S0 时间锚点：** 2026-06-16T16:15:17+09:00

## 一句话结论
本轮从 134 个合并Token中筛出 4 个主观察候选。v0.5已在v0.4.1基础上增加AVE周缓存真实接口接入框架、Smart Wallet持久保存、wallet_behavior_latest.json，以及BSC Transfer级钱包行为样本。注意：BSC当前是Transfer样本，不等同完整Swap解码。
合约地址可用 25 个，缺失 0 个；缺失地址的候选不能进入后续链上精查。

## 本轮扫描摘要
| 指标 | 数量 |
|---|---:|
| 原始池子记录 | 241 |
| 合并后Token | 134 |
| 输出候选 | 25 |
| 主观察 | 4 |
| 次观察 | 5 |
| PVP风险池 | 8 |
| 成熟池观察 | 6 |
| 低优先观察 | 2 |
| 多池Token | 6 |
| 多池冲突 | 1 |
| Symbol桥接合并 | 1 |
| 合约地址可用 | 25 |
| 合约地址缺失 | 0 |
| Micro层 | 4 |
| Early层 | 11 |
| Liquid层 | 9 |
| Mature层 | 1 |
| 需要链上确认 | 17 |
| 紧急精查候选 | 3 |

## v0.5 数据确认状态
| 项目 | 状态 |
|---|---|
| AVE Smart Wallet周缓存 | active，钱包数 2069，刷新时间 2026-10-19T02:35:21Z，是否过期 否 |
| 链上预检 | 本轮检查 12 个，验证通过 12 个，失败 0 个 |
| Helius状态 | 未配置，SOL使用公共RPC或跳过增强解析 |
| 当前精查层级 | 0.5.0-chain-preflight-plus-wallet-behavior：地址/账户预检 + v0.5钱包行为样本，完整Swap留存仍待下一版 |
| 钱包行为样本 | 本轮检查 4 个，BSC Transfer样本 2 个，SOL签名级 2 个，AVE钱包命中 0 个 |

## 第一部分：生成结果表格

### A. 上次记录结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| [Dacity](https://dexscreener.com/solana/g2uurbmvdzdfp4qyobjrskbxsi7d6v4bpp9thps36y4b) | SOL | [nxPqZ4...Rjpump](https://solscan.io/token/nxPqZ4F7ux8Vph5NFu25rEP6Kx9Gr1U6Fmj36Rjpump) | 主观察 | Score 83; Tier Early; LP $395.5K; Vol24H $3.08M; 24H -0.61%; V/LP 7.78x; 池数 1; 分项 L15/V17/B22/Buy8/Risk-3 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| DOPE | SOL | [33jENU...CNpump](https://solscan.io/token/33jENUQnjoitkMFpvNJcSHyLAHFWJuHwT6E3E8CNpump) | 主观察 | Score 79; Tier Early; LP $236.9K; Vol24H $882.8K; 24H +11.87%; V/LP 3.73x; 池数 2; 分项 L13/V13/B17/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| TART | BSC | [0x7ab8...750314](https://bscscan.com/token/0x7ab8d02cbb51ff7223fde700eaaa2a91bf750314) | 主观察 | Score 78; Tier Liquid; LP $891.6K; Vol24H $373.2K; 24H -10.87%; V/LP 0.42x; 池数 1; 分项 L18/V11/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| BTC | SOL | [C5xph2...L6pump](https://solscan.io/token/C5xph2yL6gMdxmuLGxJBkGpmuDFfyi5fqkBNhvL6pump) | 次观察 | Score 69; Tier Early; LP $494.7K; Vol24H $3.39M; 24H +529.98%; V/LP 6.85x; 池数 2; 分项 L16/V17/B0/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [UDTF](https://dexscreener.com/solana/h7nwfrmv5afadanarsfxlj1fwojfpwbogdgc5elbcw5e) | SOL | [oF2XvG...7ypump](https://solscan.io/token/oF2XvGAX3v8VCNje6yMxJqQZraXz2hPth2kPg7ypump) | 次观察 | Score 68; Tier Early; LP $383.6K; Vol24H $183.2K; 24H +64.45%; V/LP 0.48x; 池数 1; 分项 L15/V9/B8/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [GATO](https://dexscreener.com/solana/5e3dxlxgwmtdcoka51wyyakttjfzbwqcoyuhbui5gt2m) | SOL | [HsprHx...k6pump](https://solscan.io/token/HsprHxBRgiVaQdRf3TnKNuZZtaX9JUSPgMFdAkk6pump) | 次观察 | Score 68; Tier Early; LP $166.7K; Vol24H $709.5K; 24H -12.92%; V/LP 4.26x; 池数 1; 分项 L11/V13/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [SI276](https://dexscreener.com/solana/12jc1dzjpzbcdakum4brakh9jcfry2tlg1ffgsl4ftcg) | SOL | [HMYd9t...6upump](https://solscan.io/token/HMYd9tosnUXuNHmq7pXmoePRVBLBBjA3JBfydq6upump) | 次观察 | Score 67; Tier Micro; LP $87.7K; Vol24H $51.8K; 24H -12.63%; V/LP 0.59x; 池数 1; 分项 L9/V5/B17/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [HELL](https://dexscreener.com/solana/ewsyhiuznynqh5f65ypfsoqblq2kyetuvhm5un7wsfdg) | SOL | [A75Xx6...9jpump](https://solscan.io/token/A75Xx6SeftAmWduv9KGwb2GCjXUAhxozcCUCys9jpump) | 次观察 | Score 66; Tier Early; LP $152.4K; Vol24H $181.0K; 24H +1.63%; V/LP 1.19x; 池数 3; 分项 L11/V9/B22/Buy3/Risk-3 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [EXFIL](https://dexscreener.com/solana/2zpfdgd48k7b2u9yqz4hjspaptovu9uiebfqyxeoexkv) | SOL | [6FhVPc...y6pump](https://solscan.io/token/6FhVPctYg363pQbs4iSvqyHe2cJzfsvFD96gePy6pump) | 次观察 | Score 66; Tier Early; LP $171.3K; Vol24H $214.5K; 24H +7.76%; V/LP 1.25x; 池数 1; 分项 L11/V9/B22/Buy0/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| JEANPHIL | SOL | [GTBxUi...yDpump](https://solscan.io/token/GTBxUiw6wJdmmkCGZgRHLyYxqu1vG4KtRpeox6yDpump) | 次观察 | Score 64; Tier Early; LP $287.1K; Vol24H $457.3K; 24H +28.09%; V/LP 1.59x; 池数 1; 分项 L13/V11/B8/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |

### B. 本轮扫描结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| ARIA | BSC | [0x5d3a...555238](https://bscscan.com/token/0x5d3a12c42e5372b2cc3264ab3cdcf660a1555238) | 主观察 | Score 86; Tier Liquid; LP $1.49M; Vol24H $3.79M; 24H -1.14%; V/LP 2.54x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| TART | BSC | [0x7ab8...750314](https://bscscan.com/token/0x7ab8d02cbb51ff7223fde700eaaa2a91bf750314) | 主观察 | Score 83; Tier Liquid; LP $896.3K; Vol24H $343.1K; 24H -5.01%; V/LP 0.38x; 池数 1; 分项 L18/V11/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [Dacity](https://dexscreener.com/solana/g2uurbmvdzdfp4qyobjrskbxsi7d6v4bpp9thps36y4b) | SOL | [nxPqZ4...Rjpump](https://solscan.io/token/nxPqZ4F7ux8Vph5NFu25rEP6Kx9Gr1U6Fmj36Rjpump) | 主观察 | Score 81; Tier Early; LP $374.8K; Vol24H $2.00M; 24H -4.70%; V/LP 5.32x; 池数 1; 分项 L14/V16/B22/Buy8/Risk-3 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [DOPE](https://dexscreener.com/solana/6iep3egqksbzwgzmbcyajtivtvykcgl9bnpbewlr8agq) | SOL | [33jENU...CNpump](https://solscan.io/token/33jENUQnjoitkMFpvNJcSHyLAHFWJuHwT6E3E8CNpump) | 主观察 | Score 79; Tier Early; LP $229.6K; Vol24H $692.2K; 24H -13.38%; V/LP 3.01x; 池数 2; 分项 L13/V13/B17/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [Kimchi](https://dexscreener.com/solana/6dnxwecbtdnnstpb5tdnxzsfge3hmsngeuzhdue4b1ph) | SOL | [CSocnz...m7pump](https://solscan.io/token/CSocnzcRpgSCr1naKcNTieWZUxb6rABe45j844m7pump) | 次观察 | Score 70; Tier Early; LP $289.9K; Vol24H $663.3K; 24H +12.35%; V/LP 2.29x; 池数 1; 分项 L13/V13/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [UDTF](https://dexscreener.com/solana/h7nwfrmv5afadanarsfxlj1fwojfpwbogdgc5elbcw5e) | SOL | [oF2XvG...7ypump](https://solscan.io/token/oF2XvGAX3v8VCNje6yMxJqQZraXz2hPth2kPg7ypump) | 次观察 | Score 68; Tier Early; LP $392.3K; Vol24H $184.1K; 24H +62.08%; V/LP 0.47x; 池数 1; 分项 L15/V9/B8/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [swordcat](https://dexscreener.com/solana/8ewuf2o8acro7fqwepz3tkhkbbjndzu4ldk9scrpw83d) | SOL | [5tCju6...SFpump](https://solscan.io/token/5tCju6YNxHq5zrA6tGndr6F7TK42mpUFmeE31cSFpump) | 次观察 | Score 68; Tier Early; LP $239.6K; Vol24H $1.69M; 24H +57.02%; V/LP 7.06x; 池数 2; 分项 L13/V15/B8/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [GATO](https://dexscreener.com/solana/5e3dxlxgwmtdcoka51wyyakttjfzbwqcoyuhbui5gt2m) | SOL | [HsprHx...k6pump](https://solscan.io/token/HsprHxBRgiVaQdRf3TnKNuZZtaX9JUSPgMFdAkk6pump) | 次观察 | Score 67; Tier Early; LP $165.0K; Vol24H $650.5K; 24H -13.79%; V/LP 3.94x; 池数 1; 分项 L11/V12/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| JEANPHIL | SOL | [GTBxUi...yDpump](https://solscan.io/token/GTBxUiw6wJdmmkCGZgRHLyYxqu1vG4KtRpeox6yDpump) | 次观察 | Score 64; Tier Early; LP $290.7K; Vol24H $448.1K; 24H +31.55%; V/LP 1.54x; 池数 1; 分项 L13/V11/B8/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| JCT | BSC | [0xea37...b17707](https://bscscan.com/token/0xea37a8de1de2d9d10772eeb569e28bfa5cb17707) | PVP风险池 | Score 49; Tier Liquid; LP $980.2K; Vol24H $37.30M; 24H +8.04%; V/LP 38.05x; 池数 1; 分项 L18/V17/B17/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| DNA | BSC | [0xa991...c5cf7b](https://bscscan.com/token/0xa991f61940095aea0724ef54077223b048c5cf7b) | PVP风险池 | Score 39; Tier Liquid; LP $1.77M; Vol24H $39.42M; 24H +8.20%; V/LP 22.28x; 池数 1; 分项 L20/V17/B17/Buy3/Risk-42 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| IRYS | BSC | [0x9115...7c035d](https://bscscan.com/token/0x91152b4ef635403efbae860edd0f8c321d7c035d) | PVP风险池 | Score 38; Tier Early; LP $604.2K; Vol24H $20.07M; 24H -36.34%; V/LP 33.21x; 池数 1; 分项 L16/V17/B8/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| SWORDOPE | SOL | [3SVjZ7...EFpump](https://solscan.io/token/3SVjZ7BfT9FxiR49nZc7UdBmLgzRLJY7XBZDKhEFpump) | PVP风险池 | Score 33; Tier Early; LP $115.1K; Vol24H $6.12M; 24H +373.29%; V/LP 53.21x; 池数 2; 分项 L10/V17/B0/Buy12/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| CATTLEAXE | SOL | [H7VZNC...kWpump](https://solscan.io/token/H7VZNCBynDK5ikBS9krDJ2Tx8CUr1wxedV19ZgkWpump) | PVP风险池 | Score 33; Tier Early; LP $117.3K; Vol24H $5.18M; 24H +292.18%; V/LP 44.12x; 池数 2; 分项 L10/V17/B0/Buy12/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [███](https://dexscreener.com/solana/9sy4amm2rfpsbq1qgcqtxcjfvhmfj9k4d2j5xfm1k75m) | SOL | [EwX2T1...4Qpump](https://solscan.io/token/EwX2T1p2PmgTsSq2Bi6XtQYxPC5krR4P2fxPfN4Qpump) | PVP风险池 | Score 26; Tier Micro; LP $78.0K; Vol24H $2.14M; 24H +929.00%; V/LP 27.42x; 池数 1; 分项 L8/V16/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### C. PVP风险池明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| JCT | BSC | [0xea37...b17707](https://bscscan.com/token/0xea37a8de1de2d9d10772eeb569e28bfa5cb17707) | 24H波动可控；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 49; Tier Liquid; LP $980.2K; Vol24H $37.30M; 24H +8.04%; V/LP 38.05x; 池数 1; 分项 L18/V17/B17/Buy3/Risk-30 | 只记录热度，不进入主榜 |
| DNA | BSC | [0xa991...c5cf7b](https://bscscan.com/token/0xa991f61940095aea0724ef54077223b048c5cf7b) | 24H波动可控；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP极端偏高；FDV超过早期Alpha主榜上限；成熟大市值 | Score 39; Tier Liquid; LP $1.77M; Vol24H $39.42M; 24H +8.20%; V/LP 22.28x; 池数 1; 分项 L20/V17/B17/Buy3/Risk-42 | 只记录热度，不进入主榜 |
| IRYS | BSC | [0x9115...7c035d](https://bscscan.com/token/0x91152b4ef635403efbae860edd0f8c321d7c035d) | 24H未过热但已明显波动；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 38; Tier Early; LP $604.2K; Vol24H $20.07M; 24H -36.34%; V/LP 33.21x; 池数 1; 分项 L16/V17/B8/Buy3/Risk-30 | 只记录热度，不进入主榜 |
| SWORDOPE | SOL | [3SVjZ7...EFpump](https://solscan.io/token/3SVjZ7BfT9FxiR49nZc7UdBmLgzRLJY7XBZDKhEFpump) | 买入笔数占优；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 33; Tier Early; LP $115.1K; Vol24H $6.12M; 24H +373.29%; V/LP 53.21x; 池数 2; 分项 L10/V17/B0/Buy12/Risk-30 | 只记录热度，不进入主榜 |
| CATTLEAXE | SOL | [H7VZNC...kWpump](https://solscan.io/token/H7VZNCBynDK5ikBS9krDJ2Tx8CUr1wxedV19ZgkWpump) | 买入笔数占优；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 33; Tier Early; LP $117.3K; Vol24H $5.18M; 24H +292.18%; V/LP 44.12x; 池数 2; 分项 L10/V17/B0/Buy12/Risk-30 | 只记录热度，不进入主榜 |
| [███](https://dexscreener.com/solana/9sy4amm2rfpsbq1qgcqtxcjfvhmfj9k4d2j5xfm1k75m) | SOL | [EwX2T1...4Qpump](https://solscan.io/token/EwX2T1p2PmgTsSq2Bi6XtQYxPC5krR4P2fxPfN4Qpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 26; Tier Micro; LP $78.0K; Vol24H $2.14M; 24H +929.00%; V/LP 27.42x; 池数 1; 分项 L8/V16/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [KURUMI](https://dexscreener.com/solana/dxvcfzrle4dycthuzm5xchmb9zueaek56zkpbyuivfdf) | SOL | [AUHK6b...xipump](https://solscan.io/token/AUHK6bsTMU6nemt7epnvELJtGezx9JS76Lm48pxipump) | 24H未过热但已明显波动；买入笔数占优；LP未达主观察门槛；24H成交合格；LP偏薄；Volume/LP极端偏高 | Score 23; Tier Micro; LP $24.0K; Vol24H $1.96M; 24H +59.69%; V/LP 81.64x; 池数 1; 分项 L3/V16/B8/Buy12/Risk-40 | 只记录热度，不进入主榜 |
| Marvin | SOL | [Fmuciq...yrpump](https://solscan.io/token/FmuciqKXRRnKqhi7BNin5mYH6fm3oTrfVB5A5Fyrpump) | 24H未过热但已明显波动；买卖略偏买入；LP未达主观察门槛；24H成交合格；LP偏薄；Volume/LP极端偏高 | Score 20; Tier Micro; LP $23.6K; Vol24H $3.69M; 24H +65.38%; V/LP 156.17x; 池数 3; 分项 L3/V17/B8/Buy8/Risk-40 | 只记录热度，不进入主榜 |

### D. 成熟池观察明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| KTI | BSC | [0xe254...ddb9d6](https://bscscan.com/token/0xe254ee6b463807b6f8040797ccd909f5ecddb9d6) | 24H接近横盘；买入笔数占优；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；成熟大市值 | Score 80; Tier Liquid; LP $1.60M; Vol24H $1.07M; 24H +4.19%; V/LP 0.67x; 池数 1; 分项 L20/V14/B22/Buy12/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| [RAY](https://dexscreener.com/solana/2axxcn6on9bbt5owwmth53c7qhuxvhleu718kqt8rvy2) | SOL | [4k3Dyj...QrkX6R](https://solscan.io/token/4k3Dyjzvzp8eMZWUXbBCjEvwSkkk59S5iCNLY3QrkX6R) | 24H接近横盘；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 79; Tier Liquid; LP $2.21M; Vol24H $2.69M; 24H +2.32%; V/LP 1.22x; 池数 1; 分项 L20/V17/B22/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| SKYAI | BSC | [0x92aa...3ffb10](https://bscscan.com/token/0x92aa03137385f18539301349dcfc9ebc923ffb10) | 24H波动可控；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限 | Score 74; Tier Mature; LP $5.41M; Vol24H $4.03M; 24H +15.93%; V/LP 0.75x; 池数 1; 分项 L20/V17/B17/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| STONK | SOL | [6GmAFS...MpUNgx](https://solscan.io/token/6GmAFSYs4gk3FDao5FzzySQpPZaWsa4rUJHacpMpUNgx) | 24H波动可控；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限 | Score 74; Tier Liquid; LP $2.15M; Vol24H $4.30M; 24H +12.75%; V/LP 2.00x; 池数 1; 分项 L20/V17/B17/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| Q | BSC | [0xc07e...690589](https://bscscan.com/token/0xc07e1300dc138601fa6b0b59f8d0fa477e690589) | 24H接近横盘；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP偏高；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 61; Tier Liquid; LP $1.40M; Vol24H $14.14M; 24H -7.11%; V/LP 10.12x; 池数 1; 分项 L20/V17/B22/Buy8/Risk-30 | 成熟池观察，不占用早期Alpha主榜 |
| [AODF](https://dexscreener.com/solana/j8hydnqhuejpu7ztczt84vniawvpfsxzjadfmnevmxcr) | SOL | [E7yGML...EVpump](https://solscan.io/token/E7yGMLy8drjm2YnVQXyGKizSR5nx594CyrhBCEVpump) | 24H未过热但已明显波动；买入笔数占优；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 60; Tier Liquid; LP $1.40M; Vol24H $168.9K; 24H +27.00%; V/LP 0.12x; 池数 1; 分项 L20/V8/B8/Buy12/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |

### E. 链上确认/紧急精查表
| Token | 链 | 合约地址 | 是否需要链上确认 | 紧急精查 | 预检状态 | 原因 |
|---|---|---|---|---|---|---|
| TART | BSC | [0x7ab8...750314](https://bscscan.com/token/0x7ab8d02cbb51ff7223fde700eaaa2a91bf750314) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| [Dacity](https://dexscreener.com/solana/g2uurbmvdzdfp4qyobjrskbxsi7d6v4bpp9thps36y4b) | SOL | [nxPqZ4...Rjpump](https://solscan.io/token/nxPqZ4F7ux8Vph5NFu25rEP6Kx9Gr1U6Fmj36Rjpump) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| [DOPE](https://dexscreener.com/solana/6iep3egqksbzwgzmbcyajtivtvykcgl9bnpbewlr8agq) | SOL | [33jENU...CNpump](https://solscan.io/token/33jENUQnjoitkMFpvNJcSHyLAHFWJuHwT6E3E8CNpump) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| ARIA | BSC | [0x5d3a...555238](https://bscscan.com/token/0x5d3a12c42e5372b2cc3264ab3cdcf660a1555238) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [Kimchi](https://dexscreener.com/solana/6dnxwecbtdnnstpb5tdnxzsfge3hmsngeuzhdue4b1ph) | SOL | [CSocnz...m7pump](https://solscan.io/token/CSocnzcRpgSCr1naKcNTieWZUxb6rABe45j844m7pump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [UDTF](https://dexscreener.com/solana/h7nwfrmv5afadanarsfxlj1fwojfpwbogdgc5elbcw5e) | SOL | [oF2XvG...7ypump](https://solscan.io/token/oF2XvGAX3v8VCNje6yMxJqQZraXz2hPth2kPg7ypump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [swordcat](https://dexscreener.com/solana/8ewuf2o8acro7fqwepz3tkhkbbjndzu4ldk9scrpw83d) | SOL | [5tCju6...SFpump](https://solscan.io/token/5tCju6YNxHq5zrA6tGndr6F7TK42mpUFmeE31cSFpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [GATO](https://dexscreener.com/solana/5e3dxlxgwmtdcoka51wyyakttjfzbwqcoyuhbui5gt2m) | SOL | [HsprHx...k6pump](https://solscan.io/token/HsprHxBRgiVaQdRf3TnKNuZZtaX9JUSPgMFdAkk6pump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| JEANPHIL | SOL | [GTBxUi...yDpump](https://solscan.io/token/GTBxUiw6wJdmmkCGZgRHLyYxqu1vG4KtRpeox6yDpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| JCT | BSC | [0xea37...b17707](https://bscscan.com/token/0xea37a8de1de2d9d10772eeb569e28bfa5cb17707) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |

### F. 钱包行为 / AVE命中样本表
| Token | 链 | 合约地址 | 行为状态 | 行为层级 | AVE命中 | 判断 |
|---|---|---|---|---|---:|---|
| TART | BSC | [0x7ab8...750314](https://bscscan.com/token/0x7ab8d02cbb51ff7223fde700eaaa2a91bf750314) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| [Dacity](https://dexscreener.com/solana/g2uurbmvdzdfp4qyobjrskbxsi7d6v4bpp9thps36y4b) | SOL | [nxPqZ4...Rjpump](https://solscan.io/token/nxPqZ4F7ux8Vph5NFu25rEP6Kx9Gr1U6Fmj36Rjpump) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| [DOPE](https://dexscreener.com/solana/6iep3egqksbzwgzmbcyajtivtvykcgl9bnpbewlr8agq) | SOL | [33jENU...CNpump](https://solscan.io/token/33jENUQnjoitkMFpvNJcSHyLAHFWJuHwT6E3E8CNpump) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| ARIA | BSC | [0x5d3a...555238](https://bscscan.com/token/0x5d3a12c42e5372b2cc3264ab3cdcf660a1555238) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |

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
| 主观察候选 | 4 个 | 主榜继续稀缺，但必须结合合约地址进入链上确认 |
| PVP风险池 | 8 个 | v0.3已单独展示明细，便于判断噪声来源 |
| 成熟池观察 | 6 个 | 成熟资产不占早期Alpha主榜 |
| 合约地址覆盖 | 可用 25，缺失 0 | 地址缺失会阻断BSC RPC/Helius精查，需要优先补齐 |
| LP层级 | Micro 4 / Early 11 / Liquid 9 / Mature 1 | 下一步可以按层级分别设置进攻规则 |
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
| dexscreener_search | {'ok': True, 'count': 335} |
| geckoterminal_bsc_trending | {'ok': True, 'count': 20} |
| geckoterminal_solana_trending | {'ok': True, 'count': 20} |

## 数据限制
- This v0.4 scan uses free public sources plus lightweight chain address/account preflight when enabled.
- AVE Smart Money weekly cache structure is connected; real AVE API refresh is handled by the weekly workflow/cache file.
- S0 exact historical replay is not implemented yet; candidates are marked with current metrics only.
- Wallet-level buy/sell retention is not implemented yet; v0.4 only preflights token contract/account existence.
- v0.4 adds chain preflight status and Smart Wallet cache status on top of contract-address output, liquidity tiers, visible PVP/mature detail tables, and chain-verify flags.
- Contract addresses are extracted from DEXScreener baseToken or GeckoTerminal relationships when available; missing addresses are explicitly marked unavailable.