# 自我进化轮巡

**本轮时间 UTC：** 2026-10-16T10:31:01Z
**版本：** 0.5.0-ave-cache-wallet-behavior-prep
**S0 时间锚点：** 2026-06-16T16:15:17+09:00

## 一句话结论
本轮从 143 个合并Token中筛出 5 个主观察候选。v0.5已在v0.4.1基础上增加AVE周缓存真实接口接入框架、Smart Wallet持久保存、wallet_behavior_latest.json，以及BSC Transfer级钱包行为样本。注意：BSC当前是Transfer样本，不等同完整Swap解码。
合约地址可用 25 个，缺失 0 个；缺失地址的候选不能进入后续链上精查。

## 本轮扫描摘要
| 指标 | 数量 |
|---|---:|
| 原始池子记录 | 239 |
| 合并后Token | 143 |
| 输出候选 | 25 |
| 主观察 | 5 |
| 次观察 | 7 |
| PVP风险池 | 8 |
| 成熟池观察 | 1 |
| 低优先观察 | 4 |
| 多池Token | 10 |
| 多池冲突 | 5 |
| Symbol桥接合并 | 4 |
| 合约地址可用 | 25 |
| 合约地址缺失 | 0 |
| Micro层 | 6 |
| Early层 | 12 |
| Liquid层 | 7 |
| Mature层 | 0 |
| 需要链上确认 | 20 |
| 紧急精查候选 | 1 |

## v0.5 数据确认状态
| 项目 | 状态 |
|---|---|
| AVE Smart Wallet周缓存 | active，钱包数 1888，刷新时间 2026-10-12T03:31:42Z，是否过期 否 |
| 链上预检 | 本轮检查 12 个，验证通过 12 个，失败 0 个 |
| Helius状态 | 未配置，SOL使用公共RPC或跳过增强解析 |
| 当前精查层级 | 0.5.0-chain-preflight-plus-wallet-behavior：地址/账户预检 + v0.5钱包行为样本，完整Swap留存仍待下一版 |
| 钱包行为样本 | 本轮检查 5 个，BSC Transfer样本 3 个，SOL签名级 2 个，AVE钱包命中 0 个 |

## 第一部分：生成结果表格

### A. 上次记录结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| ZEREBRO | SOL | [8x5Vqb...eSo2Wn](https://solscan.io/token/8x5VqbHA8D7NkD52uNuS5nnt3PwA8pLD34ymskeSo2Wn) | 主观察 | Score 86; Tier Liquid; LP $3.52M; Vol24H $13.52M; 24H -3.38%; V/LP 3.84x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| 龙虾 | BSC | [0xeccb...7e4444](https://bscscan.com/token/0xeccbb861c0dda7efd964010085488b69317e4444) | 主观察 | Score 84; Tier Liquid; LP $1.67M; Vol24H $1.55M; 24H -1.90%; V/LP 0.93x; 池数 12; 分项 L20/V15/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| AEON | BSC | [0x277a...ec9b80](https://bscscan.com/token/0x277add739c6e0477616948357af9e79fe1ec9b80) | 主观察 | Score 80; Tier Liquid; LP $1.05M; Vol24H $3.23M; 24H -8.05%; V/LP 3.07x; 池数 1; 分项 L19/V17/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| VEIL | SOL | [HgTGdc...6vpump](https://solscan.io/token/HgTGdc29D5bDMrDvsCLnorxz899VyDj7ZN7FPa6vpump) | 主观察 | Score 79; Tier Early; LP $207.6K; Vol24H $983.9K; 24H -13.53%; V/LP 4.74x; 池数 2; 分项 L12/V14/B17/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| JEANPHIL | SOL | [GTBxUi...yDpump](https://solscan.io/token/GTBxUiw6wJdmmkCGZgRHLyYxqu1vG4KtRpeox6yDpump) | 主观察 | Score 78; Tier Early; LP $406.9K; Vol24H $1.02M; 24H +7.88%; V/LP 2.52x; 池数 1; 分项 L15/V14/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| PUFFER | BSC | [0x87d0...5392b6](https://bscscan.com/token/0x87d00066cf131ff54b72b134a217d5401e5392b6) | 次观察 | Score 77; Tier Early; LP $621.6K; Vol24H $3.67M; 24H -13.40%; V/LP 5.91x; 池数 1; 分项 L16/V17/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，不直接进攻 |
| SIREN | BSC | [0x997a...fc18e1](https://bscscan.com/token/0x997a58129890bbda032231a52ed1ddc845fc18e1) | 次观察 | Score 76; Tier Liquid; LP $2.45M; Vol24H $2.13M; 24H +49.72%; V/LP 0.87x; 池数 1; 分项 L20/V16/B8/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，不直接进攻 |
| [SI276](https://dexscreener.com/solana/12jc1dzjpzbcdakum4brakh9jcfry2tlg1ffgsl4ftcg) | SOL | [HMYd9t...6upump](https://solscan.io/token/HMYd9tosnUXuNHmq7pXmoePRVBLBBjA3JBfydq6upump) | 次观察 | Score 75; Tier Early; LP $119.3K; Vol24H $615.9K; 24H +9.76%; V/LP 5.16x; 池数 3; 分项 L10/V12/B17/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [OTC](https://dexscreener.com/solana/da4pm4xsdy4m9v4cgakkbvh1pw1ysctqqa5nekghukpt) | SOL | [MukLDt...udpump](https://solscan.io/token/MukLDtJ8Cx9DxLbeyLRSWPSposTMWuwHANbuaudpump) | 次观察 | Score 75; Tier Early; LP $619.2K; Vol24H $1.74M; 24H +71.11%; V/LP 2.81x; 池数 1; 分项 L16/V15/B8/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| TART | BSC | [0x7ab8...750314](https://bscscan.com/token/0x7ab8d02cbb51ff7223fde700eaaa2a91bf750314) | 次观察 | Score 73; Tier Liquid; LP $769.7K; Vol24H $292.6K; 24H +1.22%; V/LP 0.38x; 池数 1; 分项 L17/V10/B22/Buy0/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |

### B. 本轮扫描结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| ZEREBRO | SOL | [8x5Vqb...eSo2Wn](https://solscan.io/token/8x5VqbHA8D7NkD52uNuS5nnt3PwA8pLD34ymskeSo2Wn) | 主观察 | Score 86; Tier Liquid; LP $4.00M; Vol24H $12.91M; 24H +0.39%; V/LP 3.23x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| AEON | BSC | [0x277a...ec9b80](https://bscscan.com/token/0x277add739c6e0477616948357af9e79fe1ec9b80) | 主观察 | Score 85; Tier Liquid; LP $1.05M; Vol24H $2.78M; 24H -4.81%; V/LP 2.65x; 池数 1; 分项 L19/V17/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| 龙虾 | BSC | [0xeccb...7e4444](https://bscscan.com/token/0xeccbb861c0dda7efd964010085488b69317e4444) | 主观察 | Score 83; Tier Liquid; LP $1.66M; Vol24H $1.16M; 24H +2.42%; V/LP 0.70x; 池数 13; 分项 L20/V14/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [VEIL](https://dexscreener.com/solana/4mwjp1abqqe9y6ic5cd3nrvvwwchsn2lgpjwymdk7u7e) | SOL | [HgTGdc...6vpump](https://solscan.io/token/HgTGdc29D5bDMrDvsCLnorxz899VyDj7ZN7FPa6vpump) | 主观察 | Score 79; Tier Early; LP $215.4K; Vol24H $972.1K; 24H +10.70%; V/LP 4.51x; 池数 2; 分项 L12/V14/B17/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| SIREN | BSC | [0x997a...fc18e1](https://bscscan.com/token/0x997a58129890bbda032231a52ed1ddc845fc18e1) | 主观察 | Score 77; Tier Liquid; LP $2.37M; Vol24H $2.71M; 24H +42.49%; V/LP 1.14x; 池数 1; 分项 L20/V17/B8/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [OTC](https://dexscreener.com/solana/da4pm4xsdy4m9v4cgakkbvh1pw1ysctqqa5nekghukpt) | SOL | [MukLDt...udpump](https://solscan.io/token/MukLDtJ8Cx9DxLbeyLRSWPSposTMWuwHANbuaudpump) | 次观察 | Score 76; Tier Early; LP $610.6K; Vol24H $1.89M; 24H +47.87%; V/LP 3.09x; 池数 1; 分项 L16/V16/B8/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，不直接进攻 |
| SI276 | SOL | [HMYd9t...6upump](https://solscan.io/token/HMYd9tosnUXuNHmq7pXmoePRVBLBBjA3JBfydq6upump) | 次观察 | Score 74; Tier Early; LP $106.2K; Vol24H $575.3K; 24H -11.44%; V/LP 5.42x; 池数 3; 分项 L9/V12/B17/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| TART | BSC | [0x7ab8...750314](https://bscscan.com/token/0x7ab8d02cbb51ff7223fde700eaaa2a91bf750314) | 次观察 | Score 74; Tier Liquid; LP $780.4K; Vol24H $424.8K; 24H -1.60%; V/LP 0.54x; 池数 1; 分项 L17/V11/B22/Buy0/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| JEANPHIL | SOL | [GTBxUi...yDpump](https://solscan.io/token/GTBxUiw6wJdmmkCGZgRHLyYxqu1vG4KtRpeox6yDpump) | 次观察 | Score 73; Tier Early; LP $409.6K; Vol24H $1.05M; 24H +11.92%; V/LP 2.56x; 池数 1; 分项 L15/V14/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [ARF](https://dexscreener.com/solana/4lrgvuhfffbgz9hcwd66sqfggbehmpyt1q4ooztzcu1n) | SOL | [GDXDqy...B4pump](https://solscan.io/token/GDXDqyrDDSQnfJ3WtiVTB7vngJxFc97ezQGKmMB4pump) | 次观察 | Score 67; Tier Early; LP $355.4K; Vol24H $226.0K; 24H +27.89%; V/LP 0.64x; 池数 1; 分项 L14/V9/B8/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [GTA](https://dexscreener.com/solana/5isvs31h7hmdggmyuvzmhdsywv7cydd6czjtbqzctlii) | SOL | [BsbsB3...uLpump](https://solscan.io/token/BsbsB3WLq7vbY5En3MBCAsTrcwaCxNKY2Mp5pGuLpump) | 次观察 | Score 66; Tier Early; LP $132.0K; Vol24H $500.7K; 24H +24.81%; V/LP 3.79x; 池数 5; 分项 L10/V12/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| DOPE | SOL | [33jENU...CNpump](https://solscan.io/token/33jENUQnjoitkMFpvNJcSHyLAHFWJuHwT6E3E8CNpump) | 次观察 | Score 66; Tier Early; LP $266.9K; Vol24H $3.27M; 24H -3.94%; V/LP 12.26x; 池数 2; 分项 L13/V17/B22/Buy8/Risk-18 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [Nihilism](https://dexscreener.com/solana/2f1amisbhbrqxlp6kxfw2smaxrzgzmnt6o7qfsnbanas) | SOL | [2ay4jN...zmpump](https://solscan.io/token/2ay4jNY3JxfuXJzhZ8DrAKkGzpirgD7Dv2ccL9zmpump) | PVP风险池 | Score 42; Tier Micro; LP $52.4K; Vol24H $2.12M; 24H -13.56%; V/LP 40.49x; 池数 1; 分项 L7/V16/B17/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [FTR](https://dexscreener.com/solana/fk5mugv2h3qpt6axdhs2khgdl2os424bvfeoqfntdv9y) | SOL | [DFMt2F...TLpump](https://solscan.io/token/DFMt2FyLpB6ekPNAzVErLXgpSnJ9CRf1VnxBAkTLpump) | PVP风险池 | Score 33; Tier Early; LP $301.0K; Vol24H $22.21M; 24H +1731.00%; V/LP 73.79x; 池数 2; 分项 L14/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [OWLDACITY](https://dexscreener.com/solana/ggm3wpy8mtxx7afvs1rsxbztbnz9kk1heg9mbfmyada1) | SOL | [D61pTa...sYpump](https://solscan.io/token/D61pTaTqR93axxVvu7AX5TW6c3a4vhffPPMfCnsYpump) | PVP风险池 | Score 32; Tier Micro; LP $87.8K; Vol24H $2.78M; 24H +1340.00%; V/LP 31.72x; 池数 1; 分项 L9/V17/B0/Buy12/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### C. PVP风险池明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| [Nihilism](https://dexscreener.com/solana/2f1amisbhbrqxlp6kxfw2smaxrzgzmnt6o7qfsnbanas) | SOL | [2ay4jN...zmpump](https://solscan.io/token/2ay4jNY3JxfuXJzhZ8DrAKkGzpirgD7Dv2ccL9zmpump) | 24H波动可控；买卖略偏买入；LP未达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 42; Tier Micro; LP $52.4K; Vol24H $2.12M; 24H -13.56%; V/LP 40.49x; 池数 1; 分项 L7/V16/B17/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [FTR](https://dexscreener.com/solana/fk5mugv2h3qpt6axdhs2khgdl2os424bvfeoqfntdv9y) | SOL | [DFMt2F...TLpump](https://solscan.io/token/DFMt2FyLpB6ekPNAzVErLXgpSnJ9CRf1VnxBAkTLpump) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 33; Tier Early; LP $301.0K; Vol24H $22.21M; 24H +1731.00%; V/LP 73.79x; 池数 2; 分项 L14/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [OWLDACITY](https://dexscreener.com/solana/ggm3wpy8mtxx7afvs1rsxbztbnz9kk1heg9mbfmyada1) | SOL | [D61pTa...sYpump](https://solscan.io/token/D61pTaTqR93axxVvu7AX5TW6c3a4vhffPPMfCnsYpump) | 买入笔数占优；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 32; Tier Micro; LP $87.8K; Vol24H $2.78M; 24H +1340.00%; V/LP 31.72x; 池数 1; 分项 L9/V17/B0/Buy12/Risk-30 | 只记录热度，不进入主榜 |
| [1](https://dexscreener.com/solana/aqn7ukkysnazns61dvw2q6hqmm7wifsayjbon6fvwhgf) | SOL | [2bCCHQ...qVpump](https://solscan.io/token/2bCCHQadi4QeHWPKG3w13siCyWWQPgkFtniouTqVpump) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高；非主流报价池 | Score 26; Tier Early; LP $135.6K; Vol24H $10.19M; 24H +3220.00%; V/LP 75.14x; 池数 4; 分项 L10/V17/B0/Buy8/Risk-33 | 只记录热度，不进入主榜 |
| [Dacity](https://dexscreener.com/solana/g2uurbmvdzdfp4qyobjrskbxsi7d6v4bpp9thps36y4b) | SOL | [nxPqZ4...Rjpump](https://solscan.io/token/nxPqZ4F7ux8Vph5NFu25rEP6Kx9Gr1U6Fmj36Rjpump) | 买卖基本均衡；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高；非主流报价池 | Score 22; Tier Early; LP $149.9K; Vol24H $8.51M; 24H +1271.00%; V/LP 56.80x; 池数 2; 分项 L11/V17/B0/Buy3/Risk-33 | 只记录热度，不进入主榜 |
| [Groklet](https://dexscreener.com/solana/7odjba4hzozvnwboksrwfetstnm4ia5witkwfr1lsy8t) | SOL | [4qH8A5...B7pump](https://solscan.io/token/4qH8A5GxvRMZgpRFjXASc6U9HAoEzKeUqxY2dPB7pump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 14; Tier Micro; LP $43.8K; Vol24H $2.27M; 24H +515.00%; V/LP 51.91x; 池数 1; 分项 L6/V16/B0/Buy8/Risk-40 | 只记录热度，不进入主榜 |
| [Macca](https://dexscreener.com/solana/4fonnnmmkma66ppcia9557cg63s2bnn9uofcakxxbmvg) | SOL | [AKotzk...kFpump](https://solscan.io/token/AKotzk1dhcNangAJBtvNKtT9bhbSVZc2mMhRFgkFpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高；非主流报价池 | Score 11; Tier Micro; LP $45.3K; Vol24H $1.87M; 24H +426.00%; V/LP 41.30x; 池数 3; 分项 L6/V16/B0/Buy8/Risk-43 | 只记录热度，不进入主榜 |
| [GOAT11](https://dexscreener.com/solana/cagcwzhhemnkrc1ygp4yywegdssdcaebpqhefxemusg9) | SOL | [GjkMsv...qbpump](https://solscan.io/token/GjkMsvYmuFR37SyKnJoD8DwccLb3HKMQBnNe5Nqbpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 9; Tier Micro; LP $3.3K; Vol24H $2.80M; 24H -93.89%; V/LP 851.27x; 池数 3; 分项 L0/V17/B0/Buy8/Risk-40 | 只记录热度，不进入主榜 |

### D. 成熟池观察明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| AKE | BSC | [0x2c3a...12f7db](https://bscscan.com/token/0x2c3a8ee94ddd97244a93bc48298f97d2c412f7db) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 74; Tier Liquid; LP $2.60M; Vol24H $12.84M; 24H +0.42%; V/LP 4.94x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |

### E. 链上确认/紧急精查表
| Token | 链 | 合约地址 | 是否需要链上确认 | 紧急精查 | 预检状态 | 原因 |
|---|---|---|---|---|---|---|
| [VEIL](https://dexscreener.com/solana/4mwjp1abqqe9y6ic5cd3nrvvwwchsn2lgpjwymdk7u7e) | SOL | [HgTGdc...6vpump](https://solscan.io/token/HgTGdc29D5bDMrDvsCLnorxz899VyDj7ZN7FPa6vpump) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| ZEREBRO | SOL | [8x5Vqb...eSo2Wn](https://solscan.io/token/8x5VqbHA8D7NkD52uNuS5nnt3PwA8pLD34ymskeSo2Wn) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| AEON | BSC | [0x277a...ec9b80](https://bscscan.com/token/0x277add739c6e0477616948357af9e79fe1ec9b80) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| 龙虾 | BSC | [0xeccb...7e4444](https://bscscan.com/token/0xeccbb861c0dda7efd964010085488b69317e4444) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；多池数据冲突，需链上/聚合源复核 |
| SIREN | BSC | [0x997a...fc18e1](https://bscscan.com/token/0x997a58129890bbda032231a52ed1ddc845fc18e1) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [OTC](https://dexscreener.com/solana/da4pm4xsdy4m9v4cgakkbvh1pw1ysctqqa5nekghukpt) | SOL | [MukLDt...udpump](https://solscan.io/token/MukLDtJ8Cx9DxLbeyLRSWPSposTMWuwHANbuaudpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| SI276 | SOL | [HMYd9t...6upump](https://solscan.io/token/HMYd9tosnUXuNHmq7pXmoePRVBLBBjA3JBfydq6upump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| TART | BSC | [0x7ab8...750314](https://bscscan.com/token/0x7ab8d02cbb51ff7223fde700eaaa2a91bf750314) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| JEANPHIL | SOL | [GTBxUi...yDpump](https://solscan.io/token/GTBxUiw6wJdmmkCGZgRHLyYxqu1vG4KtRpeox6yDpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [ARF](https://dexscreener.com/solana/4lrgvuhfffbgz9hcwd66sqfggbehmpyt1q4ooztzcu1n) | SOL | [GDXDqy...B4pump](https://solscan.io/token/GDXDqyrDDSQnfJ3WtiVTB7vngJxFc97ezQGKmMB4pump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |

### F. 钱包行为 / AVE命中样本表
| Token | 链 | 合约地址 | 行为状态 | 行为层级 | AVE命中 | 判断 |
|---|---|---|---|---|---:|---|
| [VEIL](https://dexscreener.com/solana/4mwjp1abqqe9y6ic5cd3nrvvwwchsn2lgpjwymdk7u7e) | SOL | [HgTGdc...6vpump](https://solscan.io/token/HgTGdc29D5bDMrDvsCLnorxz899VyDj7ZN7FPa6vpump) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| ZEREBRO | SOL | [8x5Vqb...eSo2Wn](https://solscan.io/token/8x5VqbHA8D7NkD52uNuS5nnt3PwA8pLD34ymskeSo2Wn) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| AEON | BSC | [0x277a...ec9b80](https://bscscan.com/token/0x277add739c6e0477616948357af9e79fe1ec9b80) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| 龙虾 | BSC | [0xeccb...7e4444](https://bscscan.com/token/0xeccbb861c0dda7efd964010085488b69317e4444) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| SIREN | BSC | [0x997a...fc18e1](https://bscscan.com/token/0x997a58129890bbda032231a52ed1ddc845fc18e1) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |

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
| 主观察候选 | 5 个 | 主榜继续稀缺，但必须结合合约地址进入链上确认 |
| PVP风险池 | 8 个 | v0.3已单独展示明细，便于判断噪声来源 |
| 成熟池观察 | 1 个 | 成熟资产不占早期Alpha主榜 |
| 合约地址覆盖 | 可用 25，缺失 0 | 地址缺失会阻断BSC RPC/Helius精查，需要优先补齐 |
| LP层级 | Micro 6 / Early 12 / Liquid 7 / Mature 0 | 下一步可以按层级分别设置进攻规则 |
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