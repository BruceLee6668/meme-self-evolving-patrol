# 自我进化轮巡

**本轮时间 UTC：** 2026-09-14T11:31:39Z
**版本：** 0.5.0-ave-cache-wallet-behavior-prep
**S0 时间锚点：** 2026-06-16T16:15:17+09:00

## 一句话结论
本轮从 125 个合并Token中筛出 1 个主观察候选。v0.5已在v0.4.1基础上增加AVE周缓存真实接口接入框架、Smart Wallet持久保存、wallet_behavior_latest.json，以及BSC Transfer级钱包行为样本。注意：BSC当前是Transfer样本，不等同完整Swap解码。
合约地址可用 25 个，缺失 0 个；缺失地址的候选不能进入后续链上精查。

## 本轮扫描摘要
| 指标 | 数量 |
|---|---:|
| 原始池子记录 | 195 |
| 合并后Token | 125 |
| 输出候选 | 25 |
| 主观察 | 1 |
| 次观察 | 5 |
| PVP风险池 | 8 |
| 成熟池观察 | 6 |
| 低优先观察 | 5 |
| 多池Token | 8 |
| 多池冲突 | 3 |
| Symbol桥接合并 | 2 |
| 合约地址可用 | 25 |
| 合约地址缺失 | 0 |
| Micro层 | 5 |
| Early层 | 11 |
| Liquid层 | 7 |
| Mature层 | 2 |
| 需要链上确认 | 16 |
| 紧急精查候选 | 1 |

## v0.5 数据确认状态
| 项目 | 状态 |
|---|---|
| AVE Smart Wallet周缓存 | active，钱包数 1323，刷新时间 2026-09-14T02:37:35Z，是否过期 否 |
| 链上预检 | 本轮检查 12 个，验证通过 12 个，失败 0 个 |
| Helius状态 | 未配置，SOL使用公共RPC或跳过增强解析 |
| 当前精查层级 | 0.5.0-chain-preflight-plus-wallet-behavior：地址/账户预检 + v0.5钱包行为样本，完整Swap留存仍待下一版 |
| 钱包行为样本 | 本轮检查 1 个，BSC Transfer样本 1 个，SOL签名级 0 个，AVE钱包命中 0 个 |

## 第一部分：生成结果表格

### A. 上次记录结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| BREW | BSC | [0xfa6d...3f2159](https://bscscan.com/token/0xfa6d9b504848606eb9aec04ccc161d169b3f2159) | 主观察 | Score 83; Tier Early; LP $748.8K; Vol24H $3.15M; 24H -8.60%; V/LP 4.20x; 池数 1; 分项 L17/V17/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| $BANANA | BSC | [0x3d4f...a9a760](https://bscscan.com/token/0x3d4f0513e8a29669b960f9dbca61861548a9a760) | 主观察 | Score 83; Tier Liquid; LP $4.11M; Vol24H $1.28M; 24H -0.77%; V/LP 0.31x; 池数 1; 分项 L20/V14/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| AST | BSC | [0x265b...4affff](https://bscscan.com/token/0x265b3982ea730748100947f52561a4eab54affff) | 主观察 | Score 79; Tier Early; LP $199.0K; Vol24H $688.6K; 24H +5.79%; V/LP 3.46x; 池数 1; 分项 L12/V13/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [OTC](https://dexscreener.com/solana/da4pm4xsdy4m9v4cgakkbvh1pw1ysctqqa5nekghukpt) | SOL | [MukLDt...udpump](https://solscan.io/token/MukLDtJ8Cx9DxLbeyLRSWPSposTMWuwHANbuaudpump) | 次观察 | Score 74; Tier Early; LP $343.8K; Vol24H $2.29M; 24H -36.09%; V/LP 6.65x; 池数 2; 分项 L14/V16/B8/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| CATE | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | 次观察 | Score 72; Tier Liquid; LP $2.77M; Vol24H $16.56M; 24H +28.95%; V/LP 5.98x; 池数 2; 分项 L20/V17/B8/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [Nasduck](https://dexscreener.com/solana/937nyycpzqygdm71fx5xjzepdcnjlca9gsfe5esszk2h) | SOL | [7Y7V1a...qkraze](https://solscan.io/token/7Y7V1a4m2nWK7BMgbka5B4vR1pDvCK7yva3Hnrqkraze) | 次观察 | Score 70; Tier Early; LP $119.5K; Vol24H $453.5K; 24H +22.37%; V/LP 3.79x; 池数 5; 分项 L10/V11/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [RAYCAT](https://dexscreener.com/solana/987vwvjz5frjwcy9zwc2trugl8fbmt1af4purt7xjpjd) | SOL | [CFNRDa...jNupFL](https://solscan.io/token/CFNRDaxFcvRwRSNnA5cHrCCr6AHhk9dNkHWpRUjNupFL) | 次观察 | Score 67; Tier Early; LP $531.5K; Vol24H $1.08M; 24H -42.44%; V/LP 2.03x; 池数 1; 分项 L16/V14/B8/Buy8/Risk-3 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [SpaceX Meme](https://dexscreener.com/bsc/0xd0dd21d8dbcf95551647f15aea03e1d275a15632) | BSC | [0x28E6...03167E](https://bscscan.com/token/0x28E69efCF168813113E039341cBA335d1303167E) | 次观察 | Score 67; Tier Early; LP $149.5K; Vol24H $103.4K; 24H -2.60%; V/LP 0.69x; 池数 1; 分项 L11/V7/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| BNBCAT | BSC | [0x3efb...6a7777](https://bscscan.com/token/0x3efbfff95576e1d23cf6ead0acd2e73f4d6a7777) | 次观察 | Score 67; Tier Early; LP $130.5K; Vol24H $124.8K; 24H +7.46%; V/LP 0.96x; 池数 1; 分项 L10/V8/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [MM](https://dexscreener.com/solana/abxlp7nmnipn7ijirjkrvoq8vs6snzkubrmfirvygvty) | SOL | [zzjkh1...2PN2tC](https://solscan.io/token/zzjkh1hLbvsFJXWLfE6h4JNbcnRj4eteuKRw42PN2tC) | 次观察 | Score 66; Tier Micro; LP $77.5K; Vol24H $489.6K; 24H +16.38%; V/LP 6.32x; 池数 3; 分项 L8/V12/B17/Buy8/Risk-3 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |

### B. 本轮扫描结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| BREW | BSC | [0xfa6d...3f2159](https://bscscan.com/token/0xfa6d9b504848606eb9aec04ccc161d169b3f2159) | 主观察 | Score 88; Tier Liquid; LP $767.5K; Vol24H $3.03M; 24H -7.06%; V/LP 3.94x; 池数 1; 分项 L17/V17/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| OTC | SOL | [MukLDt...udpump](https://solscan.io/token/MukLDtJ8Cx9DxLbeyLRSWPSposTMWuwHANbuaudpump) | 次观察 | Score 74; Tier Early; LP $352.1K; Vol24H $2.05M; 24H -45.76%; V/LP 5.82x; 池数 2; 分项 L14/V16/B8/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| AST | BSC | [0x265b...4affff](https://bscscan.com/token/0x265b3982ea730748100947f52561a4eab54affff) | 次观察 | Score 74; Tier Early; LP $193.1K; Vol24H $663.9K; 24H +15.99%; V/LP 3.44x; 池数 1; 分项 L12/V13/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [CHILLHOUSE](https://dexscreener.com/solana/35tqqmeirwebk6fr5qipwastuaavo32vjnuljpxvsxuk) | SOL | [GkyPYa...CZpump](https://solscan.io/token/GkyPYa7NnCFbduLknCfBfP7p8564X1VZhwZYJ6CZpump) | 次观察 | Score 73; Tier Early; LP $523.6K; Vol24H $722.3K; 24H -19.27%; V/LP 1.38x; 池数 1; 分项 L16/V13/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| CATE | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | 次观察 | Score 72; Tier Liquid; LP $2.92M; Vol24H $18.22M; 24H +46.17%; V/LP 6.25x; 池数 2; 分项 L20/V17/B8/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [SpaceX Meme](https://dexscreener.com/bsc/0xd0dd21d8dbcf95551647f15aea03e1d275a15632) | BSC | [0x28E6...03167E](https://bscscan.com/token/0x28E69efCF168813113E039341cBA335d1303167E) | 次观察 | Score 65; Tier Early; LP $147.1K; Vol24H $55.1K; 24H -3.69%; V/LP 0.37x; 池数 1; 分项 L11/V5/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [RAYCAT](https://dexscreener.com/solana/987vwvjz5frjwcy9zwc2trugl8fbmt1af4purt7xjpjd) | SOL | [CFNRDa...jNupFL](https://solscan.io/token/CFNRDaxFcvRwRSNnA5cHrCCr6AHhk9dNkHWpRUjNupFL) | PVP风险池 | Score 44; Tier Early; LP $532.1K; Vol24H $109.23M; 24H -25.95%; V/LP 205.27x; 池数 1; 分项 L16/V17/B8/Buy12/Risk-33 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [bikecate](https://dexscreener.com/solana/3wbmnexoxsgwpgxbawwpganvxgzsn5bqr1lnu76afzsz) | SOL | [3nkVw4...DBpump](https://solscan.io/token/3nkVw4JwdDLGM23Wzqpy2ptAPV5YgMnokEBgijDBpump) | PVP风险池 | Score 31; Tier Micro; LP $72.5K; Vol24H $3.30M; 24H +433.00%; V/LP 45.46x; 池数 1; 分项 L8/V17/B0/Buy12/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| DEBIT | BSC | [0x6666...83ce49](https://bscscan.com/token/0x66661c7229901f568f16bd1551b3ba826f83ce49) | PVP风险池 | Score 30; Tier Liquid; LP $2.98M; Vol24H $63.90M; 24H +49.87%; V/LP 21.48x; 池数 1; 分项 L20/V17/B8/Buy3/Risk-42 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [TWINE](https://dexscreener.com/solana/5x74xfdesp5j2vfr7nw76mqgqkkmujuhgwxog4fajs9x) | SOL | [CNWxmo...oe78Gm](https://solscan.io/token/CNWxmoBSQZo2Sgp5KSAK5m9FwSqDbXQRP4CNMuoe78Gm) | PVP风险池 | Score 26; Tier Early; LP $197.7K; Vol24H $6.32M; 24H +266.00%; V/LP 31.98x; 池数 1; 分项 L12/V17/B0/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| NINA | SOL | [H22aqu...99pump](https://solscan.io/token/H22aquDouZNFyfykwnXmY5Y9z5sMQtLFy5tUKR99pump) | PVP风险池 | Score 26; Tier Micro; LP $54.7K; Vol24H $6.00M; 24H +606.98%; V/LP 109.65x; 池数 2; 分项 L7/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [MIZO](https://dexscreener.com/solana/g2pnaefeuaq8arwbcye1wv8vrfd2zl8ljpn8mcjqgeop) | SOL | [5Zspim...ocpump](https://solscan.io/token/5Zspimi8VD6LctJLtaSjLqaSUvmh3Rs849iPtGocpump) | PVP风险池 | Score 22; Tier Micro; LP $39.8K; Vol24H $1.86M; 24H -51.65%; V/LP 46.77x; 池数 2; 分项 L6/V16/B8/Buy8/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [NAMI](https://dexscreener.com/solana/7lzqxfemhjbnxraw98dzdvzoek2kvtzngbcuznzyi924) | SOL | [9rbAB5...Mtpump](https://solscan.io/token/9rbAB5BTo12TkKt5ed5SzUXjgBckkFmtcKdPDbMtpump) | PVP风险池 | Score 12; Tier Micro; LP $2.8K; Vol24H $2.48M; 24H -96.74%; V/LP 897.04x; 池数 4; 分项 L0/V16/B0/Buy12/Risk-40 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [PVE](https://dexscreener.com/solana/gs2spb6kbpbb9s3mejkn8tadfjkik3bnx4z9cn67xr6c) | SOL | [6ssGtD...BYsp7N](https://solscan.io/token/6ssGtD5KUhzrENtn5BiEdTt4tcb6sfn7wPHRJyBYsp7N) | PVP风险池 | Score 8; Tier Micro; LP $28.9K; Vol24H $4.23M; 24H +126.00%; V/LP 146.54x; 池数 1; 分项 L4/V17/B0/Buy3/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [RAY](https://dexscreener.com/solana/2axxcn6on9bbt5owwmth53c7qhuxvhleu718kqt8rvy2) | SOL | [4k3Dyj...QrkX6R](https://solscan.io/token/4k3Dyjzvzp8eMZWUXbBCjEvwSkkk59S5iCNLY3QrkX6R) | 成熟池观察 | Score 79; Tier Liquid; LP $2.92M; Vol24H $7.62M; 24H -6.34%; V/LP 2.61x; 池数 1; 分项 L20/V17/B22/Buy8/Risk-12 | 钱包级数据不可用；当前仅代理指标；资产偏成熟，不按早期吸筹处理；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 成熟池观察，不占用早期Alpha主榜 |

### C. PVP风险池明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| [RAYCAT](https://dexscreener.com/solana/987vwvjz5frjwcy9zwc2trugl8fbmt1af4purt7xjpjd) | SOL | [CFNRDa...jNupFL](https://solscan.io/token/CFNRDaxFcvRwRSNnA5cHrCCr6AHhk9dNkHWpRUjNupFL) | 24H未过热但已明显波动；买入笔数占优；LP达主观察门槛；24H成交合格；Volume/LP极端偏高；非主流报价池 | Score 44; Tier Early; LP $532.1K; Vol24H $109.23M; 24H -25.95%; V/LP 205.27x; 池数 1; 分项 L16/V17/B8/Buy12/Risk-33 | 只记录热度，不进入主榜 |
| [bikecate](https://dexscreener.com/solana/3wbmnexoxsgwpgxbawwpganvxgzsn5bqr1lnu76afzsz) | SOL | [3nkVw4...DBpump](https://solscan.io/token/3nkVw4JwdDLGM23Wzqpy2ptAPV5YgMnokEBgijDBpump) | 买入笔数占优；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 31; Tier Micro; LP $72.5K; Vol24H $3.30M; 24H +433.00%; V/LP 45.46x; 池数 1; 分项 L8/V17/B0/Buy12/Risk-30 | 只记录热度，不进入主榜 |
| DEBIT | BSC | [0x6666...83ce49](https://bscscan.com/token/0x66661c7229901f568f16bd1551b3ba826f83ce49) | 24H未过热但已明显波动；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP极端偏高；FDV超过早期Alpha主榜上限；成熟大市值 | Score 30; Tier Liquid; LP $2.98M; Vol24H $63.90M; 24H +49.87%; V/LP 21.48x; 池数 1; 分项 L20/V17/B8/Buy3/Risk-42 | 只记录热度，不进入主榜 |
| [TWINE](https://dexscreener.com/solana/5x74xfdesp5j2vfr7nw76mqgqkkmujuhgwxog4fajs9x) | SOL | [CNWxmo...oe78Gm](https://solscan.io/token/CNWxmoBSQZo2Sgp5KSAK5m9FwSqDbXQRP4CNMuoe78Gm) | 买卖基本均衡；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 26; Tier Early; LP $197.7K; Vol24H $6.32M; 24H +266.00%; V/LP 31.98x; 池数 1; 分项 L12/V17/B0/Buy3/Risk-30 | 只记录热度，不进入主榜 |
| NINA | SOL | [H22aqu...99pump](https://solscan.io/token/H22aquDouZNFyfykwnXmY5Y9z5sMQtLFy5tUKR99pump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 26; Tier Micro; LP $54.7K; Vol24H $6.00M; 24H +606.98%; V/LP 109.65x; 池数 2; 分项 L7/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [MIZO](https://dexscreener.com/solana/g2pnaefeuaq8arwbcye1wv8vrfd2zl8ljpn8mcjqgeop) | SOL | [5Zspim...ocpump](https://solscan.io/token/5Zspimi8VD6LctJLtaSjLqaSUvmh3Rs849iPtGocpump) | 24H未过热但已明显波动；买卖略偏买入；LP未达主观察门槛；24H成交合格；LP偏薄；Volume/LP极端偏高 | Score 22; Tier Micro; LP $39.8K; Vol24H $1.86M; 24H -51.65%; V/LP 46.77x; 池数 2; 分项 L6/V16/B8/Buy8/Risk-40 | 只记录热度，不进入主榜 |
| [NAMI](https://dexscreener.com/solana/7lzqxfemhjbnxraw98dzdvzoek2kvtzngbcuznzyi924) | SOL | [9rbAB5...Mtpump](https://solscan.io/token/9rbAB5BTo12TkKt5ed5SzUXjgBckkFmtcKdPDbMtpump) | 买入笔数占优；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 12; Tier Micro; LP $2.8K; Vol24H $2.48M; 24H -96.74%; V/LP 897.04x; 池数 4; 分项 L0/V16/B0/Buy12/Risk-40 | 只记录热度，不进入主榜 |
| [PVE](https://dexscreener.com/solana/gs2spb6kbpbb9s3mejkn8tadfjkik3bnx4z9cn67xr6c) | SOL | [6ssGtD...BYsp7N](https://solscan.io/token/6ssGtD5KUhzrENtn5BiEdTt4tcb6sfn7wPHRJyBYsp7N) | 买卖基本均衡；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 8; Tier Micro; LP $28.9K; Vol24H $4.23M; 24H +126.00%; V/LP 146.54x; 池数 1; 分项 L4/V17/B0/Buy3/Risk-40 | 只记录热度，不进入主榜 |

### D. 成熟池观察明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| [RAY](https://dexscreener.com/solana/2axxcn6on9bbt5owwmth53c7qhuxvhleu718kqt8rvy2) | SOL | [4k3Dyj...QrkX6R](https://solscan.io/token/4k3Dyjzvzp8eMZWUXbBCjEvwSkkk59S5iCNLY3QrkX6R) | 24H接近横盘；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 79; Tier Liquid; LP $2.92M; Vol24H $7.62M; 24H -6.34%; V/LP 2.61x; 池数 1; 分项 L20/V17/B22/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| [PUMP](https://dexscreener.com/solana/2uf4xh61rdwxng9woyxsvqp7zua6klfpb3nvnrqeoisd) | SOL | [pumpCm...7H9Dfn](https://solscan.io/token/pumpCmXqMfrsAkQ5r49WcJnRayYRqmXz6ae8H7H9Dfn) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 74; Tier Mature; LP $20.67M; Vol24H $7.32M; 24H -1.93%; V/LP 0.35x; 池数 2; 分项 L20/V17/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| ANSEM | SOL | [9cRCn9...TGpump](https://solscan.io/token/9cRCn9rGT8V2imeM2BaKs13yhMEais3ruM3rPvTGpump) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 74; Tier Liquid; LP $2.24M; Vol24H $3.68M; 24H -4.93%; V/LP 1.64x; 池数 2; 分项 L20/V17/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| BTCB | BSC | [0x7130...3ead9c](https://bscscan.com/token/0x7130d2a12b9bcbfae4f2634d864a1ee1ce3ead9c) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 74; Tier Mature; LP $26.13M; Vol24H $10.19M; 24H +1.57%; V/LP 0.39x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| 牛来 | BSC | [0xbeea...377777](https://bscscan.com/token/0xbeea1d618e533a387d941f58a7d4c9b7bd377777) | 24H波动可控；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限 | Score 69; Tier Liquid; LP $1.46M; Vol24H $8.12M; 24H -14.22%; V/LP 5.55x; 池数 8; 分项 L20/V17/B17/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| MarsCoin | BSC | [0xfe18...5c7777](https://bscscan.com/token/0xfe189e97832da1573e4e4ff034f4ffc3a15c7777) | 24H波动可控；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限 | Score 67; Tier Early; LP $300.9K; Vol24H $2.28M; 24H -11.32%; V/LP 7.59x; 池数 1; 分项 L14/V16/B17/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |

### E. 链上确认/紧急精查表
| Token | 链 | 合约地址 | 是否需要链上确认 | 紧急精查 | 预检状态 | 原因 |
|---|---|---|---|---|---|---|
| BREW | BSC | [0xfa6d...3f2159](https://bscscan.com/token/0xfa6d9b504848606eb9aec04ccc161d169b3f2159) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| OTC | SOL | [MukLDt...udpump](https://solscan.io/token/MukLDtJ8Cx9DxLbeyLRSWPSposTMWuwHANbuaudpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| AST | BSC | [0x265b...4affff](https://bscscan.com/token/0x265b3982ea730748100947f52561a4eab54affff) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [PUMP](https://dexscreener.com/solana/2uf4xh61rdwxng9woyxsvqp7zua6klfpb3nvnrqeoisd) | SOL | [pumpCm...7H9Dfn](https://solscan.io/token/pumpCmXqMfrsAkQ5r49WcJnRayYRqmXz6ae8H7H9Dfn) | 是 | 否 | verified / address_preflight_v0.4 | 多池数据冲突，需链上/聚合源复核 |
| [CHILLHOUSE](https://dexscreener.com/solana/35tqqmeirwebk6fr5qipwastuaavo32vjnuljpxvsxuk) | SOL | [GkyPYa...CZpump](https://solscan.io/token/GkyPYa7NnCFbduLknCfBfP7p8564X1VZhwZYJ6CZpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| CATE | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| 牛来 | BSC | [0xbeea...377777](https://bscscan.com/token/0xbeea1d618e533a387d941f58a7d4c9b7bd377777) | 是 | 否 | verified / address_preflight_v0.4 | 多池数据冲突，需链上/聚合源复核 |
| [SpaceX Meme](https://dexscreener.com/bsc/0xd0dd21d8dbcf95551647f15aea03e1d275a15632) | BSC | [0x28E6...03167E](https://bscscan.com/token/0x28E69efCF168813113E039341cBA335d1303167E) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [RAYCAT](https://dexscreener.com/solana/987vwvjz5frjwcy9zwc2trugl8fbmt1af4purt7xjpjd) | SOL | [CFNRDa...jNupFL](https://solscan.io/token/CFNRDaxFcvRwRSNnA5cHrCCr6AHhk9dNkHWpRUjNupFL) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| [bikecate](https://dexscreener.com/solana/3wbmnexoxsgwpgxbawwpganvxgzsn5bqr1lnu76afzsz) | SOL | [3nkVw4...DBpump](https://solscan.io/token/3nkVw4JwdDLGM23Wzqpy2ptAPV5YgMnokEBgijDBpump) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |

### F. 钱包行为 / AVE命中样本表
| Token | 链 | 合约地址 | 行为状态 | 行为层级 | AVE命中 | 判断 |
|---|---|---|---|---|---:|---|
| BREW | BSC | [0xfa6d...3f2159](https://bscscan.com/token/0xfa6d9b504848606eb9aec04ccc161d169b3f2159) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |

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
| LP层级 | Micro 5 / Early 11 / Liquid 7 / Mature 2 | 下一步可以按层级分别设置进攻规则 |
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