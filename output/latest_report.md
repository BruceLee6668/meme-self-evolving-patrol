# 自我进化轮巡

**本轮时间 UTC：** 2026-11-07T01:31:23Z
**版本：** 0.5.0-ave-cache-wallet-behavior-prep
**S0 时间锚点：** 2026-06-16T16:15:17+09:00

## 一句话结论
本轮从 152 个合并Token中筛出 3 个主观察候选。v0.5已在v0.4.1基础上增加AVE周缓存真实接口接入框架、Smart Wallet持久保存、wallet_behavior_latest.json，以及BSC Transfer级钱包行为样本。注意：BSC当前是Transfer样本，不等同完整Swap解码。
合约地址可用 25 个，缺失 0 个；缺失地址的候选不能进入后续链上精查。

## 本轮扫描摘要
| 指标 | 数量 |
|---|---:|
| 原始池子记录 | 248 |
| 合并后Token | 152 |
| 输出候选 | 25 |
| 主观察 | 3 |
| 次观察 | 7 |
| PVP风险池 | 8 |
| 成熟池观察 | 7 |
| 低优先观察 | 0 |
| 多池Token | 9 |
| 多池冲突 | 2 |
| Symbol桥接合并 | 3 |
| 合约地址可用 | 25 |
| 合约地址缺失 | 0 |
| Micro层 | 5 |
| Early层 | 9 |
| Liquid层 | 8 |
| Mature层 | 3 |
| 需要链上确认 | 18 |
| 紧急精查候选 | 2 |

## v0.5 数据确认状态
| 项目 | 状态 |
|---|---|
| AVE Smart Wallet周缓存 | active，钱包数 2405，刷新时间 2026-11-02T03:39:47Z，是否过期 否 |
| 链上预检 | 本轮检查 12 个，验证通过 12 个，失败 0 个 |
| Helius状态 | 未配置，SOL使用公共RPC或跳过增强解析 |
| 当前精查层级 | 0.5.0-chain-preflight-plus-wallet-behavior：地址/账户预检 + v0.5钱包行为样本，完整Swap留存仍待下一版 |
| 钱包行为样本 | 本轮检查 3 个，BSC Transfer样本 1 个，SOL签名级 2 个，AVE钱包命中 0 个 |

## 第一部分：生成结果表格

### A. 上次记录结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| B13B | BSC | [0x4902...eeec3f](https://bscscan.com/token/0x4902c5ebc598265ed2212b559b042de8a5eeec3f) | 主观察 | Score 91; Tier Liquid; LP $3.51M; Vol24H $6.76M; 24H +6.76%; V/LP 1.92x; 池数 1; 分项 L20/V17/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [Dacity](https://dexscreener.com/solana/g2uurbmvdzdfp4qyobjrskbxsi7d6v4bpp9thps36y4b) | SOL | [nxPqZ4...Rjpump](https://solscan.io/token/nxPqZ4F7ux8Vph5NFu25rEP6Kx9Gr1U6Fmj36Rjpump) | 主观察 | Score 85; Tier Early; LP $415.7K; Vol24H $1.74M; 24H +0.39%; V/LP 4.17x; 池数 1; 分项 L15/V15/B22/Buy12/Risk-3 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| LAB | BSC | [0x7ec4...25593a](https://bscscan.com/token/0x7ec43cf65f1663f820427c62a5780b8f2e25593a) | 主观察 | Score 76; Tier Liquid; LP $797.0K; Vol24H $1.58M; 24H +9.78%; V/LP 1.98x; 池数 1; 分项 L17/V15/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| ANSEM | SOL | [9cRCn9...TGpump](https://solscan.io/token/9cRCn9rGT8V2imeM2BaKs13yhMEais3ruM3rPvTGpump) | 次观察 | Score 74; Tier Liquid; LP $1.40M; Vol24H $1.19M; 24H +31.43%; V/LP 0.85x; 池数 2; 分项 L20/V14/B8/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [UODF](https://dexscreener.com/solana/dfcrxve7mejyf8r6dr91klhveaoyve6lacgfp8airkxv) | SOL | [QreCV2...CVpump](https://solscan.io/token/QreCV24giHAXE9eofxhNXKX1uATsp82ReumMFCVpump) | 次观察 | Score 72; Tier Early; LP $416.1K; Vol24H $156.7K; 24H +15.08%; V/LP 0.38x; 池数 1; 分项 L15/V8/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [XCAT](https://dexscreener.com/solana/8kxzr2bikmkcgzhp4srlgyhbpsqqwzk2echqhxqrd589) | SOL | [1226TM...e5xfun](https://solscan.io/token/1226TMaWZiZYWdP7CBZBqfJGXoWXaKXJJiKf45e5xfun) | 次观察 | Score 70; Tier Early; LP $386.1K; Vol24H $195.2K; 24H +16.38%; V/LP 0.51x; 池数 1; 分项 L15/V9/B17/Buy8/Risk-3 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [GATO](https://dexscreener.com/solana/5e3dxlxgwmtdcoka51wyyakttjfzbwqcoyuhbui5gt2m) | SOL | [HsprHx...k6pump](https://solscan.io/token/HsprHxBRgiVaQdRf3TnKNuZZtaX9JUSPgMFdAkk6pump) | 次观察 | Score 70; Tier Early; LP $360.7K; Vol24H $1.48M; 24H +10.96%; V/LP 4.10x; 池数 1; 分项 L14/V15/B17/Buy0/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [EXFIL](https://dexscreener.com/solana/2zpfdgd48k7b2u9yqz4hjspaptovu9uiebfqyxeoexkv) | SOL | [6FhVPc...y6pump](https://solscan.io/token/6FhVPctYg363pQbs4iSvqyHe2cJzfsvFD96gePy6pump) | 次观察 | Score 67; Tier Early; LP $162.2K; Vol24H $117.7K; 24H +6.28%; V/LP 0.73x; 池数 1; 分项 L11/V7/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [DESSA](https://dexscreener.com/solana/dextcer4k9dwbxtmu8znvvwgevvmvhmb183pf2xxzwvh) | SOL | [npz2Fh...Svpump](https://solscan.io/token/npz2FhoufQ7pKqhGpaipYWacrAkidyW2yDpVWSvpump) | 次观察 | Score 66; Tier Early; LP $442.0K; Vol24H $1.88M; 24H -37.18%; V/LP 4.24x; 池数 1; 分项 L15/V16/B8/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [SI276](https://dexscreener.com/solana/12jc1dzjpzbcdakum4brakh9jcfry2tlg1ffgsl4ftcg) | SOL | [HMYd9t...6upump](https://solscan.io/token/HMYd9tosnUXuNHmq7pXmoePRVBLBBjA3JBfydq6upump) | 次观察 | Score 65; Tier Micro; LP $56.9K; Vol24H $56.3K; 24H -8.44%; V/LP 0.99x; 池数 10; 分项 L7/V5/B17/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |

### B. 本轮扫描结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| [Dacity](https://dexscreener.com/solana/g2uurbmvdzdfp4qyobjrskbxsi7d6v4bpp9thps36y4b) | SOL | [nxPqZ4...Rjpump](https://solscan.io/token/nxPqZ4F7ux8Vph5NFu25rEP6Kx9Gr1U6Fmj36Rjpump) | 主观察 | Score 85; Tier Early; LP $415.2K; Vol24H $1.66M; 24H -3.91%; V/LP 4.01x; 池数 1; 分项 L15/V15/B22/Buy12/Risk-3 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| ANSEM | SOL | [9cRCn9...TGpump](https://solscan.io/token/9cRCn9rGT8V2imeM2BaKs13yhMEais3ruM3rPvTGpump) | 主观察 | Score 84; Tier Liquid; LP $1.35M; Vol24H $1.51M; 24H +21.66%; V/LP 1.12x; 池数 2; 分项 L20/V15/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| LAB | BSC | [0x7ec4...25593a](https://bscscan.com/token/0x7ec43cf65f1663f820427c62a5780b8f2e25593a) | 主观察 | Score 76; Tier Liquid; LP $794.5K; Vol24H $1.45M; 24H +10.06%; V/LP 1.82x; 池数 1; 分项 L17/V15/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [GATO](https://dexscreener.com/solana/5e3dxlxgwmtdcoka51wyyakttjfzbwqcoyuhbui5gt2m) | SOL | [HsprHx...k6pump](https://solscan.io/token/HsprHxBRgiVaQdRf3TnKNuZZtaX9JUSPgMFdAkk6pump) | 次观察 | Score 75; Tier Early; LP $356.1K; Vol24H $1.60M; 24H -2.13%; V/LP 4.50x; 池数 6; 分项 L14/V15/B22/Buy0/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [jeff](https://dexscreener.com/solana/jcxwfczgjgjc8nza5qb6jp3cgvqw4vgug4tqj87g5zny) | SOL | [HAsTKX...gqwP6k](https://solscan.io/token/HAsTKXYvv65zM7J6Cu5o5PcZsiKMQYo5oz4WPjgqwP6k) | 次观察 | Score 74; Tier Micro; LP $83.2K; Vol24H $140.3K; 24H +3.11%; V/LP 1.69x; 池数 2; 分项 L8/V8/B22/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [UODF](https://dexscreener.com/solana/dfcrxve7mejyf8r6dr91klhveaoyve6lacgfp8airkxv) | SOL | [QreCV2...CVpump](https://solscan.io/token/QreCV24giHAXE9eofxhNXKX1uATsp82ReumMFCVpump) | 次观察 | Score 72; Tier Early; LP $421.2K; Vol24H $159.1K; 24H +15.67%; V/LP 0.38x; 池数 1; 分项 L15/V8/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [XCAT](https://dexscreener.com/solana/8kxzr2bikmkcgzhp4srlgyhbpsqqwzk2echqhxqrd589) | SOL | [1226TM...e5xfun](https://solscan.io/token/1226TMaWZiZYWdP7CBZBqfJGXoWXaKXJJiKf45e5xfun) | 次观察 | Score 70; Tier Early; LP $391.6K; Vol24H $207.9K; 24H +17.23%; V/LP 0.53x; 池数 1; 分项 L15/V9/B17/Buy8/Risk-3 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [DESSA](https://dexscreener.com/solana/dextcer4k9dwbxtmu8znvvwgevvmvhmb183pf2xxzwvh) | SOL | [npz2Fh...Svpump](https://solscan.io/token/npz2FhoufQ7pKqhGpaipYWacrAkidyW2yDpVWSvpump) | 次观察 | Score 70; Tier Early; LP $450.6K; Vol24H $1.74M; 24H -34.58%; V/LP 3.86x; 池数 1; 分项 L15/V15/B8/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| SI276 | SOL | [HMYd9t...6upump](https://solscan.io/token/HMYd9tosnUXuNHmq7pXmoePRVBLBBjA3JBfydq6upump) | 次观察 | Score 68; Tier Micro; LP $59.9K; Vol24H $88.9K; 24H -1.38%; V/LP 1.48x; 池数 10; 分项 L7/V7/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [COGE](https://dexscreener.com/solana/8gjmy6ipysxfmwwrpu9c7atssorjg6al88d9xttzslqe) | SOL | [8UQdy5...Xcpump](https://solscan.io/token/8UQdy5sHMVWUWSHeA5B3ZuuAVNumjSLPXdf19MXcpump) | 次观察 | Score 65; Tier Early; LP $278.7K; Vol24H $2.01M; 24H +233.00%; V/LP 7.20x; 池数 2; 分项 L13/V16/B0/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| GM | BSC | [0x1392...0f7777](https://bscscan.com/token/0x13920fe6467e9e3c852b8d365a036c995f0f7777) | PVP风险池 | Score 33; Tier Early; LP $335.4K; Vol24H $8.44M; 24H +883.77%; V/LP 25.17x; 池数 4; 分项 L14/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [AMD](https://dexscreener.com/solana/6zv8dyrdxh56au2ebhpzzbmkprp5ixbkprj7hb2pj3rr) | SOL | [oCZHH8...RPpump](https://solscan.io/token/oCZHH8HnEBCPipEGdEcP3f45pQAaM7nh7P6EkRPpump) | PVP风险池 | Score 29; Tier Early; LP $126.1K; Vol24H $4.08M; 24H +5314.00%; V/LP 32.36x; 池数 10; 分项 L10/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| UAI | BSC | [0x3e5d...ba9ea0](https://bscscan.com/token/0x3e5d4f8aee0d9b3082d5f6da5d6e225d17ba9ea0) | PVP风险池 | Score 27; Tier Liquid; LP $772.9K; Vol24H $59.06M; 24H +48.69%; V/LP 76.41x; 池数 1; 分项 L17/V17/B8/Buy3/Risk-42 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [coin](https://dexscreener.com/solana/gacmbdqtw7hbuev6bwe583yxw5gs9gjgr59gymvygtri) | SOL | [GdY4Z6...vxpump](https://solscan.io/token/GdY4Z6pYUcr3HFrABV5FEZay3J4GnjN1Uzsw6Dvxpump) | PVP风险池 | Score 26; Tier Micro; LP $64.0K; Vol24H $3.12M; 24H +222.00%; V/LP 48.85x; 池数 2; 分项 L7/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [Diamond](https://dexscreener.com/solana/ghfsapdvu75kcpsuvk7cz8a1tdjyeo6yvzx1qibgwfsj) | SOL | [5VCEFq...qopump](https://solscan.io/token/5VCEFq1aATjga39QtDunYjJqYBx67w8V8TXwHrqopump) | PVP风险池 | Score 24; Tier Micro; LP $69.2K; Vol24H $3.37M; 24H +572.00%; V/LP 48.71x; 池数 2; 分项 L8/V17/B0/Buy8/Risk-33 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### C. PVP风险池明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| GM | BSC | [0x1392...0f7777](https://bscscan.com/token/0x13920fe6467e9e3c852b8d365a036c995f0f7777) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 33; Tier Early; LP $335.4K; Vol24H $8.44M; 24H +883.77%; V/LP 25.17x; 池数 4; 分项 L14/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [AMD](https://dexscreener.com/solana/6zv8dyrdxh56au2ebhpzzbmkprp5ixbkprj7hb2pj3rr) | SOL | [oCZHH8...RPpump](https://solscan.io/token/oCZHH8HnEBCPipEGdEcP3f45pQAaM7nh7P6EkRPpump) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 29; Tier Early; LP $126.1K; Vol24H $4.08M; 24H +5314.00%; V/LP 32.36x; 池数 10; 分项 L10/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| UAI | BSC | [0x3e5d...ba9ea0](https://bscscan.com/token/0x3e5d4f8aee0d9b3082d5f6da5d6e225d17ba9ea0) | 24H未过热但已明显波动；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP极端偏高；FDV超过早期Alpha主榜上限；成熟大市值 | Score 27; Tier Liquid; LP $772.9K; Vol24H $59.06M; 24H +48.69%; V/LP 76.41x; 池数 1; 分项 L17/V17/B8/Buy3/Risk-42 | 只记录热度，不进入主榜 |
| [coin](https://dexscreener.com/solana/gacmbdqtw7hbuev6bwe583yxw5gs9gjgr59gymvygtri) | SOL | [GdY4Z6...vxpump](https://solscan.io/token/GdY4Z6pYUcr3HFrABV5FEZay3J4GnjN1Uzsw6Dvxpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 26; Tier Micro; LP $64.0K; Vol24H $3.12M; 24H +222.00%; V/LP 48.85x; 池数 2; 分项 L7/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [Diamond](https://dexscreener.com/solana/ghfsapdvu75kcpsuvk7cz8a1tdjyeo6yvzx1qibgwfsj) | SOL | [5VCEFq...qopump](https://solscan.io/token/5VCEFq1aATjga39QtDunYjJqYBx67w8V8TXwHrqopump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高；非主流报价池 | Score 24; Tier Micro; LP $69.2K; Vol24H $3.37M; 24H +572.00%; V/LP 48.71x; 池数 2; 分项 L8/V17/B0/Buy8/Risk-33 | 只记录热度，不进入主榜 |
| AKE | BSC | [0x2c3a...12f7db](https://bscscan.com/token/0x2c3a8ee94ddd97244a93bc48298f97d2c412f7db) | 买卖基本均衡；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 21; Tier Liquid; LP $1.26M; Vol24H $79.81M; 24H +139.26%; V/LP 63.44x; 池数 1; 分项 L19/V17/B0/Buy3/Risk-42 | 只记录热度，不进入主榜 |
| RM | SOL | [EW1b9r...jTpump](https://solscan.io/token/EW1b9rcLAJe634mgxb5r4bVYxDoGU37o7YazBzjTpump) | 24H未过热但已明显波动；买卖略偏买入；LP未达主观察门槛；24H成交合格；LP偏薄；Volume/LP极端偏高 | Score 16; Tier Micro; LP $10.4K; Vol24H $2.01M; 24H -48.71%; V/LP 193.61x; 池数 1; 分项 L0/V16/B8/Buy8/Risk-40 | 只记录热度，不进入主榜 |
| [MET](https://dexscreener.com/solana/3xngdc58axytrj64stqz5trdqwvtwhlr888irbbwznee) | SOL | [METvsv...n6mWQL](https://solscan.io/token/METvsvVRapdj9cFLzq4Tr43xK4tAjQfwX76z3n6mWQL) | LP达主观察门槛；24H成交合格；24H涨跌幅过热；卖出笔数占优；Volume/LP极端偏高；非主流报价池；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 7; Tier Early; LP $146.0K; Vol24H $67.17M; 24H -99.98%; V/LP 460.01x; 池数 1; 分项 L11/V17/B0/Buy0/Risk-45 | 只记录热度，不进入主榜 |

### D. 成熟池观察明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| [RAY](https://dexscreener.com/solana/2axxcn6on9bbt5owwmth53c7qhuxvhleu718kqt8rvy2) | SOL | [4k3Dyj...QrkX6R](https://solscan.io/token/4k3Dyjzvzp8eMZWUXbBCjEvwSkkk59S5iCNLY3QrkX6R) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 74; Tier Liquid; LP $2.06M; Vol24H $3.22M; 24H +5.16%; V/LP 1.56x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| ARK | BSC | [0xcae1...618b9d](https://bscscan.com/token/0xcae117ca6bc8a341d2e7207f30e180f0e5618b9d) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 74; Tier Mature; LP $58.34M; Vol24H $4.17M; 24H +0.50%; V/LP 0.07x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| ARIA | BSC | [0x5d3a...555238](https://bscscan.com/token/0x5d3a12c42e5372b2cc3264ab3cdcf660a1555238) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；成熟大市值 | Score 74; Tier Liquid; LP $1.80M; Vol24H $11.72M; 24H +6.05%; V/LP 6.50x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| PUMP | SOL | [pumpCm...7H9Dfn](https://solscan.io/token/pumpCmXqMfrsAkQ5r49WcJnRayYRqmXz6ae8H7H9Dfn) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 74; Tier Mature; LP $22.25M; Vol24H $3.62M; 24H +0.12%; V/LP 0.16x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| TRUMP | SOL | [6p6xgH...jfGiPN](https://solscan.io/token/6p6xgHyF7AeE6TZkSmFsko444wqoP15icUSqi2jfGiPN) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 74; Tier Mature; LP $6.32M; Vol24H $3.26M; 24H -1.12%; V/LP 0.52x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| PIEVERSE | BSC | [0x0e63...0225a9](https://bscscan.com/token/0x0e63b9c287e32a05e6b9ab8ee8df88a2760225a9) | 24H波动可控；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 69; Tier Liquid; LP $2.25M; Vol24H $5.23M; 24H +11.13%; V/LP 2.32x; 池数 1; 分项 L20/V17/B17/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| BIRB | SOL | [G7vQWu...FpKNwG](https://solscan.io/token/G7vQWurMkMMm2dU3iZpXYFTHT9Biio4F4gZCrwFpKNwG) | 24H波动可控；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限 | Score 69; Tier Liquid; LP $1.71M; Vol24H $10.47M; 24H +11.65%; V/LP 6.11x; 池数 1; 分项 L20/V17/B17/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |

### E. 链上确认/紧急精查表
| Token | 链 | 合约地址 | 是否需要链上确认 | 紧急精查 | 预检状态 | 原因 |
|---|---|---|---|---|---|---|
| [Dacity](https://dexscreener.com/solana/g2uurbmvdzdfp4qyobjrskbxsi7d6v4bpp9thps36y4b) | SOL | [nxPqZ4...Rjpump](https://solscan.io/token/nxPqZ4F7ux8Vph5NFu25rEP6Kx9Gr1U6Fmj36Rjpump) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| ANSEM | SOL | [9cRCn9...TGpump](https://solscan.io/token/9cRCn9rGT8V2imeM2BaKs13yhMEais3ruM3rPvTGpump) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| LAB | BSC | [0x7ec4...25593a](https://bscscan.com/token/0x7ec43cf65f1663f820427c62a5780b8f2e25593a) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [GATO](https://dexscreener.com/solana/5e3dxlxgwmtdcoka51wyyakttjfzbwqcoyuhbui5gt2m) | SOL | [HsprHx...k6pump](https://solscan.io/token/HsprHxBRgiVaQdRf3TnKNuZZtaX9JUSPgMFdAkk6pump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [jeff](https://dexscreener.com/solana/jcxwfczgjgjc8nza5qb6jp3cgvqw4vgug4tqj87g5zny) | SOL | [HAsTKX...gqwP6k](https://solscan.io/token/HAsTKXYvv65zM7J6Cu5o5PcZsiKMQYo5oz4WPjgqwP6k) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [UODF](https://dexscreener.com/solana/dfcrxve7mejyf8r6dr91klhveaoyve6lacgfp8airkxv) | SOL | [QreCV2...CVpump](https://solscan.io/token/QreCV24giHAXE9eofxhNXKX1uATsp82ReumMFCVpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [XCAT](https://dexscreener.com/solana/8kxzr2bikmkcgzhp4srlgyhbpsqqwzk2echqhxqrd589) | SOL | [1226TM...e5xfun](https://solscan.io/token/1226TMaWZiZYWdP7CBZBqfJGXoWXaKXJJiKf45e5xfun) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [DESSA](https://dexscreener.com/solana/dextcer4k9dwbxtmu8znvvwgevvmvhmb183pf2xxzwvh) | SOL | [npz2Fh...Svpump](https://solscan.io/token/npz2FhoufQ7pKqhGpaipYWacrAkidyW2yDpVWSvpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| SI276 | SOL | [HMYd9t...6upump](https://solscan.io/token/HMYd9tosnUXuNHmq7pXmoePRVBLBBjA3JBfydq6upump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [COGE](https://dexscreener.com/solana/8gjmy6ipysxfmwwrpu9c7atssorjg6al88d9xttzslqe) | SOL | [8UQdy5...Xcpump](https://solscan.io/token/8UQdy5sHMVWUWSHeA5B3ZuuAVNumjSLPXdf19MXcpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |

### F. 钱包行为 / AVE命中样本表
| Token | 链 | 合约地址 | 行为状态 | 行为层级 | AVE命中 | 判断 |
|---|---|---|---|---|---:|---|
| [Dacity](https://dexscreener.com/solana/g2uurbmvdzdfp4qyobjrskbxsi7d6v4bpp9thps36y4b) | SOL | [nxPqZ4...Rjpump](https://solscan.io/token/nxPqZ4F7ux8Vph5NFu25rEP6Kx9Gr1U6Fmj36Rjpump) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| ANSEM | SOL | [9cRCn9...TGpump](https://solscan.io/token/9cRCn9rGT8V2imeM2BaKs13yhMEais3ruM3rPvTGpump) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| LAB | BSC | [0x7ec4...25593a](https://bscscan.com/token/0x7ec43cf65f1663f820427c62a5780b8f2e25593a) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |

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
| 成熟池观察 | 7 个 | 成熟资产不占早期Alpha主榜 |
| 合约地址覆盖 | 可用 25，缺失 0 | 地址缺失会阻断BSC RPC/Helius精查，需要优先补齐 |
| LP层级 | Micro 5 / Early 9 / Liquid 8 / Mature 3 | 下一步可以按层级分别设置进攻规则 |
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