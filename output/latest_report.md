# 自我进化轮巡

**本轮时间 UTC：** 2026-09-14T05:39:50Z
**版本：** 0.5.0-ave-cache-wallet-behavior-prep
**S0 时间锚点：** 2026-06-16T16:15:17+09:00

## 一句话结论
本轮从 128 个合并Token中筛出 3 个主观察候选。v0.5已在v0.4.1基础上增加AVE周缓存真实接口接入框架、Smart Wallet持久保存、wallet_behavior_latest.json，以及BSC Transfer级钱包行为样本。注意：BSC当前是Transfer样本，不等同完整Swap解码。
合约地址可用 25 个，缺失 0 个；缺失地址的候选不能进入后续链上精查。

## 本轮扫描摘要
| 指标 | 数量 |
|---|---:|
| 原始池子记录 | 221 |
| 合并后Token | 128 |
| 输出候选 | 25 |
| 主观察 | 3 |
| 次观察 | 10 |
| PVP风险池 | 8 |
| 成熟池观察 | 3 |
| 低优先观察 | 1 |
| 多池Token | 10 |
| 多池冲突 | 4 |
| Symbol桥接合并 | 0 |
| 合约地址可用 | 25 |
| 合约地址缺失 | 0 |
| Micro层 | 7 |
| Early层 | 11 |
| Liquid层 | 6 |
| Mature层 | 1 |
| 需要链上确认 | 21 |
| 紧急精查候选 | 2 |

## v0.5 数据确认状态
| 项目 | 状态 |
|---|---|
| AVE Smart Wallet周缓存 | active，钱包数 1323，刷新时间 2026-09-14T02:37:35Z，是否过期 否 |
| 链上预检 | 本轮检查 12 个，验证通过 12 个，失败 0 个 |
| Helius状态 | 未配置，SOL使用公共RPC或跳过增强解析 |
| 当前精查层级 | 0.5.0-chain-preflight-plus-wallet-behavior：地址/账户预检 + v0.5钱包行为样本，完整Swap留存仍待下一版 |
| 钱包行为样本 | 本轮检查 3 个，BSC Transfer样本 3 个，SOL签名级 0 个，AVE钱包命中 0 个 |

## 第一部分：生成结果表格

### A. 上次记录结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| EMBER | SOL | [5dvXTZ...k4QEC6](https://solscan.io/token/5dvXTZ5qwgafnHtwu3Ls3QrWx1U4LQsFeCuJgkk4QEC6) | 主观察 | Score 85; Tier Liquid; LP $1.24M; Vol24H $5.46M; 24H +14.42%; V/LP 4.41x; 池数 3; 分项 L19/V17/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [CHILLHOUSE](https://dexscreener.com/solana/35tqqmeirwebk6fr5qipwastuaavo32vjnuljpxvsxuk) | SOL | [GkyPYa...CZpump](https://solscan.io/token/GkyPYa7NnCFbduLknCfBfP7p8564X1VZhwZYJ6CZpump) | 主观察 | Score 82; Tier Early; LP $504.8K; Vol24H $3.57M; 24H -16.16%; V/LP 7.07x; 池数 1; 分项 L16/V17/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| ZCAT | SOL | [HcRLc9...qiDeJR](https://solscan.io/token/HcRLc9VDgjLeK154xDawfb1dmVJ98DoSqcwTHGqiDeJR) | 主观察 | Score 81; Tier Liquid; LP $1.34M; Vol24H $3.39M; 24H -29.88%; V/LP 2.54x; 池数 1; 分项 L20/V17/B8/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [OTC](https://dexscreener.com/solana/da4pm4xsdy4m9v4cgakkbvh1pw1ysctqqa5nekghukpt) | SOL | [MukLDt...udpump](https://solscan.io/token/MukLDtJ8Cx9DxLbeyLRSWPSposTMWuwHANbuaudpump) | 次观察 | Score 74; Tier Early; LP $350.9K; Vol24H $2.43M; 24H -42.52%; V/LP 6.92x; 池数 2; 分项 L14/V16/B8/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| BREW | BSC | [0xfa6d...3f2159](https://bscscan.com/token/0xfa6d9b504848606eb9aec04ccc161d169b3f2159) | 次观察 | Score 74; Tier Early; LP $719.5K; Vol24H $3.24M; 24H -31.47%; V/LP 4.51x; 池数 1; 分项 L17/V17/B8/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| CATE | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | 次观察 | Score 72; Tier Liquid; LP $2.51M; Vol24H $6.20M; 24H +29.12%; V/LP 2.47x; 池数 2; 分项 L20/V17/B8/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [SpaceX Meme](https://dexscreener.com/bsc/0xd0dd21d8dbcf95551647f15aea03e1d275a15632) | BSC | [0x28E6...03167E](https://bscscan.com/token/0x28E69efCF168813113E039341cBA335d1303167E) | 次观察 | Score 67; Tier Early; LP $148.6K; Vol24H $115.0K; 24H -7.10%; V/LP 0.77x; 池数 1; 分项 L11/V7/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| BNBCAT | BSC | [0x3efb...6a7777](https://bscscan.com/token/0x3efbfff95576e1d23cf6ead0acd2e73f4d6a7777) | 次观察 | Score 67; Tier Early; LP $131.9K; Vol24H $124.1K; 24H +1.72%; V/LP 0.94x; 池数 1; 分项 L10/V8/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| CNPY | BSC | [0xc69b...90ddd2](https://bscscan.com/token/0xc69b16cf18cea1e5d0bb6a1a9db802097790ddd2) | 次观察 | Score 65; Tier Liquid; LP $1.45M; Vol24H $25.44M; 24H -0.86%; V/LP 17.55x; 池数 1; 分项 L20/V17/B22/Buy0/Risk-18 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| AST | BSC | [0x265b...4affff](https://bscscan.com/token/0x265b3982ea730748100947f52561a4eab54affff) | 次观察 | Score 65; Tier Early; LP $182.5K; Vol24H $714.5K; 24H -28.16%; V/LP 3.92x; 池数 1; 分项 L12/V13/B8/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |

### B. 本轮扫描结果表
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
| EMBER | SOL | [5dvXTZ...k4QEC6](https://solscan.io/token/5dvXTZ5qwgafnHtwu3Ls3QrWx1U4LQsFeCuJgkk4QEC6) | 次观察 | Score 66; Tier Liquid; LP $991.4K; Vol24H $14.10M; 24H -22.84%; V/LP 14.23x; 池数 2; 分项 L18/V17/B17/Buy8/Risk-18 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [CHILLHOUSE](https://dexscreener.com/solana/35tqqmeirwebk6fr5qipwastuaavo32vjnuljpxvsxuk) | SOL | [GkyPYa...CZpump](https://solscan.io/token/GkyPYa7NnCFbduLknCfBfP7p8564X1VZhwZYJ6CZpump) | 次观察 | Score 65; Tier Early; LP $523.4K; Vol24H $1.21M; 24H -38.00%; V/LP 2.31x; 池数 1; 分项 L16/V14/B8/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| CNPY | BSC | [0xc69b...90ddd2](https://bscscan.com/token/0xc69b16cf18cea1e5d0bb6a1a9db802097790ddd2) | 次观察 | Score 65; Tier Liquid; LP $1.47M; Vol24H $25.90M; 24H +5.38%; V/LP 17.61x; 池数 1; 分项 L20/V17/B22/Buy0/Risk-18 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| DEBIT | BSC | [0x6666...83ce49](https://bscscan.com/token/0x66661c7229901f568f16bd1551b3ba826f83ce49) | PVP风险池 | Score 30; Tier Liquid; LP $2.91M; Vol24H $59.82M; 24H +47.24%; V/LP 20.52x; 池数 1; 分项 L20/V17/B8/Buy3/Risk-42 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| YOYO | SOL | [BHS8LH...Y5pump](https://solscan.io/token/BHS8LHW11NKxzxyCtqz9NJbTkh3h94WqeMVYgTY5pump) | PVP风险池 | Score 30; Tier Micro; LP $94.6K; Vol24H $2.15M; 24H -72.96%; V/LP 22.67x; 池数 1; 分项 L9/V16/B8/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### C. PVP风险池明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| DEBIT | BSC | [0x6666...83ce49](https://bscscan.com/token/0x66661c7229901f568f16bd1551b3ba826f83ce49) | 24H未过热但已明显波动；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP极端偏高；FDV超过早期Alpha主榜上限；成熟大市值 | Score 30; Tier Liquid; LP $2.91M; Vol24H $59.82M; 24H +47.24%; V/LP 20.52x; 池数 1; 分项 L20/V17/B8/Buy3/Risk-42 | 只记录热度，不进入主榜 |
| YOYO | SOL | [BHS8LH...Y5pump](https://solscan.io/token/BHS8LHW11NKxzxyCtqz9NJbTkh3h94WqeMVYgTY5pump) | 24H未过热但已明显波动；买卖基本均衡；LP未达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 30; Tier Micro; LP $94.6K; Vol24H $2.15M; 24H -72.96%; V/LP 22.67x; 池数 1; 分项 L9/V16/B8/Buy3/Risk-30 | 只记录热度，不进入主榜 |
| [TWINE](https://dexscreener.com/solana/5x74xfdesp5j2vfr7nw76mqgqkkmujuhgwxog4fajs9x) | SOL | [CNWxmo...oe78Gm](https://solscan.io/token/CNWxmoBSQZo2Sgp5KSAK5m9FwSqDbXQRP4CNMuoe78Gm) | 买卖基本均衡；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 26; Tier Early; LP $184.1K; Vol24H $5.91M; 24H +135.00%; V/LP 32.10x; 池数 1; 分项 L12/V17/B0/Buy3/Risk-30 | 只记录热度，不进入主榜 |
| NINA | SOL | [H22aqu...99pump](https://solscan.io/token/H22aquDouZNFyfykwnXmY5Y9z5sMQtLFy5tUKR99pump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 15; Tier Micro; LP $49.0K; Vol24H $5.79M; 24H +466.31%; V/LP 118.23x; 池数 2; 分项 L6/V17/B0/Buy8/Risk-40 | 只记录热度，不进入主榜 |
| MIZO | SOL | [5Zspim...ocpump](https://solscan.io/token/5Zspimi8VD6LctJLtaSjLqaSUvmh3Rs849iPtGocpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 15; Tier Micro; LP $39.7K; Vol24H $3.54M; 24H +326.70%; V/LP 89.30x; 池数 2; 分项 L6/V17/B0/Buy8/Risk-40 | 只记录热度，不进入主榜 |
| [BABYCATE](https://dexscreener.com/solana/erz48mrwpu8mddsyaqqqe4z9ri2nu6f1ahje9tngps4c) | SOL | [J8SJWC...b5pump](https://solscan.io/token/J8SJWCmak8yuiVAHvn1aArKnZW1DL2rEE8pGFYb5pump) | 买入笔数占优；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP偏高；年轻币短期暴拉 | Score 15; Tier Micro; LP $68.4K; Vol24H $1.13M; 24H +638.00%; V/LP 16.48x; 池数 2; 分项 L8/V14/B0/Buy12/Risk-43 | 只记录热度，不进入主榜 |
| [MEMEBACK](https://dexscreener.com/solana/afxfvrqahlchucbuati7wwtpg11abgb2pgksry9jffs5) | SOL | [GogsSn...Nspump](https://solscan.io/token/GogsSnkXwke5FEUxyV6FmR4eczFK1KJDVsaJNaNspump) | 买入笔数占优；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高；年轻币短期暴拉 | Score 6; Tier Micro; LP $88.4K; Vol24H $2.15M; 24H +1233.00%; V/LP 24.35x; 池数 8; 分项 L9/V16/B0/Buy12/Risk-55 | 只记录热度，不进入主榜 |
| [bikecate](https://dexscreener.com/solana/3wbmnexoxsgwpgxbawwpganvxgzsn5bqr1lnu76afzsz) | SOL | [3nkVw4...DBpump](https://solscan.io/token/3nkVw4JwdDLGM23Wzqpy2ptAPV5YgMnokEBgijDBpump) | 买入笔数占优；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高；年轻币短期暴拉 | Score 4; Tier Micro; LP $67.2K; Vol24H $1.38M; 24H +409.00%; V/LP 20.53x; 池数 5; 分项 L8/V15/B0/Buy12/Risk-55 | 只记录热度，不进入主榜 |

### D. 成熟池观察明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| BTCB | BSC | [0x7130...3ead9c](https://bscscan.com/token/0x7130d2a12b9bcbfae4f2634d864a1ee1ce3ead9c) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 74; Tier Mature; LP $26.06M; Vol24H $9.55M; 24H +0.32%; V/LP 0.37x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| [ANSEM](https://dexscreener.com/solana/fnzky6x7entq1er3d225dqyt7ybfka4pskbmqhb8l3cc) | SOL | [9cRCn9...TGpump](https://solscan.io/token/9cRCn9rGT8V2imeM2BaKs13yhMEais3ruM3rPvTGpump) | 24H波动可控；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 69; Tier Liquid; LP $2.23M; Vol24H $3.51M; 24H -8.64%; V/LP 1.57x; 池数 1; 分项 L20/V17/B17/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| MarsCoin | BSC | [0xfe18...5c7777](https://bscscan.com/token/0xfe189e97832da1573e4e4ff034f4ffc3a15c7777) | 24H波动可控；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限 | Score 67; Tier Early; LP $366.2K; Vol24H $2.42M; 24H -17.13%; V/LP 6.62x; 池数 1; 分项 L14/V16/B17/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |

### E. 链上确认/紧急精查表
| Token | 链 | 合约地址 | 是否需要链上确认 | 紧急精查 | 预检状态 | 原因 |
|---|---|---|---|---|---|---|
| BREW | BSC | [0xfa6d...3f2159](https://bscscan.com/token/0xfa6d9b504848606eb9aec04ccc161d169b3f2159) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| AST | BSC | [0x265b...4affff](https://bscscan.com/token/0x265b3982ea730748100947f52561a4eab54affff) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| $BANANA | BSC | [0x3d4f...a9a760](https://bscscan.com/token/0x3d4f0513e8a29669b960f9dbca61861548a9a760) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [OTC](https://dexscreener.com/solana/da4pm4xsdy4m9v4cgakkbvh1pw1ysctqqa5nekghukpt) | SOL | [MukLDt...udpump](https://solscan.io/token/MukLDtJ8Cx9DxLbeyLRSWPSposTMWuwHANbuaudpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| CATE | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [Nasduck](https://dexscreener.com/solana/937nyycpzqygdm71fx5xjzepdcnjlca9gsfe5esszk2h) | SOL | [7Y7V1a...qkraze](https://solscan.io/token/7Y7V1a4m2nWK7BMgbka5B4vR1pDvCK7yva3Hnrqkraze) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；多池数据冲突，需链上/聚合源复核 |
| [RAYCAT](https://dexscreener.com/solana/987vwvjz5frjwcy9zwc2trugl8fbmt1af4purt7xjpjd) | SOL | [CFNRDa...jNupFL](https://solscan.io/token/CFNRDaxFcvRwRSNnA5cHrCCr6AHhk9dNkHWpRUjNupFL) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [SpaceX Meme](https://dexscreener.com/bsc/0xd0dd21d8dbcf95551647f15aea03e1d275a15632) | BSC | [0x28E6...03167E](https://bscscan.com/token/0x28E69efCF168813113E039341cBA335d1303167E) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| BNBCAT | BSC | [0x3efb...6a7777](https://bscscan.com/token/0x3efbfff95576e1d23cf6ead0acd2e73f4d6a7777) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [MM](https://dexscreener.com/solana/abxlp7nmnipn7ijirjkrvoq8vs6snzkubrmfirvygvty) | SOL | [zzjkh1...2PN2tC](https://solscan.io/token/zzjkh1hLbvsFJXWLfE6h4JNbcnRj4eteuKRw42PN2tC) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |

### F. 钱包行为 / AVE命中样本表
| Token | 链 | 合约地址 | 行为状态 | 行为层级 | AVE命中 | 判断 |
|---|---|---|---|---|---:|---|
| BREW | BSC | [0xfa6d...3f2159](https://bscscan.com/token/0xfa6d9b504848606eb9aec04ccc161d169b3f2159) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| AST | BSC | [0x265b...4affff](https://bscscan.com/token/0x265b3982ea730748100947f52561a4eab54affff) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| $BANANA | BSC | [0x3d4f...a9a760](https://bscscan.com/token/0x3d4f0513e8a29669b960f9dbca61861548a9a760) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |

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
| 成熟池观察 | 3 个 | 成熟资产不占早期Alpha主榜 |
| 合约地址覆盖 | 可用 25，缺失 0 | 地址缺失会阻断BSC RPC/Helius精查，需要优先补齐 |
| LP层级 | Micro 7 / Early 11 / Liquid 6 / Mature 1 | 下一步可以按层级分别设置进攻规则 |
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