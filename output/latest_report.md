# 自我进化轮巡

**本轮时间 UTC：** 2026-10-17T05:22:48Z
**版本：** 0.5.0-ave-cache-wallet-behavior-prep
**S0 时间锚点：** 2026-06-16T16:15:17+09:00

## 一句话结论
本轮从 142 个合并Token中筛出 4 个主观察候选。v0.5已在v0.4.1基础上增加AVE周缓存真实接口接入框架、Smart Wallet持久保存、wallet_behavior_latest.json，以及BSC Transfer级钱包行为样本。注意：BSC当前是Transfer样本，不等同完整Swap解码。
合约地址可用 25 个，缺失 0 个；缺失地址的候选不能进入后续链上精查。

## 本轮扫描摘要
| 指标 | 数量 |
|---|---:|
| 原始池子记录 | 241 |
| 合并后Token | 142 |
| 输出候选 | 25 |
| 主观察 | 4 |
| 次观察 | 2 |
| PVP风险池 | 8 |
| 成熟池观察 | 5 |
| 低优先观察 | 6 |
| 多池Token | 7 |
| 多池冲突 | 2 |
| Symbol桥接合并 | 2 |
| 合约地址可用 | 25 |
| 合约地址缺失 | 0 |
| Micro层 | 5 |
| Early层 | 9 |
| Liquid层 | 8 |
| Mature层 | 3 |
| 需要链上确认 | 14 |
| 紧急精查候选 | 1 |

## v0.5 数据确认状态
| 项目 | 状态 |
|---|---|
| AVE Smart Wallet周缓存 | active，钱包数 1888，刷新时间 2026-10-12T03:31:42Z，是否过期 否 |
| 链上预检 | 本轮检查 12 个，验证通过 12 个，失败 0 个 |
| Helius状态 | 未配置，SOL使用公共RPC或跳过增强解析 |
| 当前精查层级 | 0.5.0-chain-preflight-plus-wallet-behavior：地址/账户预检 + v0.5钱包行为样本，完整Swap留存仍待下一版 |
| 钱包行为样本 | 本轮检查 4 个，BSC Transfer样本 3 个，SOL签名级 1 个，AVE钱包命中 0 个 |

## 第一部分：生成结果表格

### A. 上次记录结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| SIREN | BSC | [0x997a...fc18e1](https://bscscan.com/token/0x997a58129890bbda032231a52ed1ddc845fc18e1) | 主观察 | Score 90; Tier Liquid; LP $2.46M; Vol24H $1.97M; 24H -2.89%; V/LP 0.80x; 池数 1; 分项 L20/V16/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| CATE | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | 主观察 | Score 88; Tier Liquid; LP $2.86M; Vol24H $1.18M; 24H +1.19%; V/LP 0.41x; 池数 1; 分项 L20/V14/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [OTC](https://dexscreener.com/solana/da4pm4xsdy4m9v4cgakkbvh1pw1ysctqqa5nekghukpt) | SOL | [MukLDt...udpump](https://solscan.io/token/MukLDtJ8Cx9DxLbeyLRSWPSposTMWuwHANbuaudpump) | 主观察 | Score 80; Tier Early; LP $547.6K; Vol24H $1.56M; 24H -8.60%; V/LP 2.84x; 池数 1; 分项 L16/V15/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| TART | BSC | [0x7ab8...750314](https://bscscan.com/token/0x7ab8d02cbb51ff7223fde700eaaa2a91bf750314) | 主观察 | Score 77; Tier Liquid; LP $767.8K; Vol24H $361.0K; 24H +1.17%; V/LP 0.47x; 池数 1; 分项 L17/V11/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [ARF](https://dexscreener.com/solana/4lrgvuhfffbgz9hcwd66sqfggbehmpyt1q4ooztzcu1n) | SOL | [GDXDqy...B4pump](https://solscan.io/token/GDXDqyrDDSQnfJ3WtiVTB7vngJxFc97ezQGKmMB4pump) | 主观察 | Score 76; Tier Early; LP $368.6K; Vol24H $223.3K; 24H +16.66%; V/LP 0.61x; 池数 1; 分项 L14/V9/B17/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| AEON | BSC | [0x277a...ec9b80](https://bscscan.com/token/0x277add739c6e0477616948357af9e79fe1ec9b80) | 次观察 | Score 75; Tier Liquid; LP $1.03M; Vol24H $2.53M; 24H -9.29%; V/LP 2.46x; 池数 1; 分项 L18/V16/B17/Buy0/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| STBL | BSC | [0x8ded...7979e3](https://bscscan.com/token/0x8dedf84656fa932157e27c060d8613824e7979e3) | 次观察 | Score 72; Tier Liquid; LP $1.72M; Vol24H $12.12M; 24H -28.04%; V/LP 7.05x; 池数 1; 分项 L20/V17/B8/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| SI276 | SOL | [HMYd9t...6upump](https://solscan.io/token/HMYd9tosnUXuNHmq7pXmoePRVBLBBjA3JBfydq6upump) | 次观察 | Score 69; Tier Micro; LP $93.8K; Vol24H $397.6K; 24H -10.63%; V/LP 4.24x; 池数 2; 分项 L9/V11/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| DOPE | SOL | [33jENU...CNpump](https://solscan.io/token/33jENUQnjoitkMFpvNJcSHyLAHFWJuHwT6E3E8CNpump) | 次观察 | Score 68; Tier Early; LP $237.4K; Vol24H $1.67M; 24H -35.16%; V/LP 7.04x; 池数 2; 分项 L13/V15/B8/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [VEIL](https://dexscreener.com/solana/4mwjp1abqqe9y6ic5cd3nrvvwwchsn2lgpjwymdk7u7e) | SOL | [HgTGdc...6vpump](https://solscan.io/token/HgTGdc29D5bDMrDvsCLnorxz899VyDj7ZN7FPa6vpump) | 次观察 | Score 67; Tier Early; LP $228.8K; Vol24H $1.73M; 24H +49.11%; V/LP 7.56x; 池数 2; 分项 L12/V15/B8/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |

### B. 本轮扫描结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| SIREN | BSC | [0x997a...fc18e1](https://bscscan.com/token/0x997a58129890bbda032231a52ed1ddc845fc18e1) | 主观察 | Score 84; Tier Liquid; LP $2.56M; Vol24H $1.73M; 24H +8.94%; V/LP 0.68x; 池数 1; 分项 L20/V15/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| AEON | BSC | [0x277a...ec9b80](https://bscscan.com/token/0x277add739c6e0477616948357af9e79fe1ec9b80) | 主观察 | Score 81; Tier Liquid; LP $1.03M; Vol24H $2.51M; 24H -3.22%; V/LP 2.43x; 池数 1; 分项 L19/V16/B22/Buy0/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [ARF](https://dexscreener.com/solana/3q56fvb1graevwtcpyqailozfsuxywzh5mihprafp7vt) | SOL | [WHvP6N...Wopump](https://solscan.io/token/WHvP6NTRYdovnG9ZDVVrF8bR2bTChSDjLaGbeWopump) | 主观察 | Score 77; Tier Early; LP $475.3K; Vol24H $182.0K; 24H +9.86%; V/LP 0.38x; 池数 2; 分项 L15/V9/B17/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| TART | BSC | [0x7ab8...750314](https://bscscan.com/token/0x7ab8d02cbb51ff7223fde700eaaa2a91bf750314) | 主观察 | Score 77; Tier Liquid; LP $782.9K; Vol24H $354.2K; 24H +0.93%; V/LP 0.45x; 池数 1; 分项 L17/V11/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| DOPE | SOL | [33jENU...CNpump](https://solscan.io/token/33jENUQnjoitkMFpvNJcSHyLAHFWJuHwT6E3E8CNpump) | 次观察 | Score 67; Tier Early; LP $223.8K; Vol24H $1.73M; 24H -34.02%; V/LP 7.73x; 池数 2; 分项 L12/V15/B8/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [PsyopAnime](https://dexscreener.com/solana/fpyosqzp5ijfrxqqbvnm67rfam7vsbvnam7puf8yvt1c) | SOL | [2nP9yK...2gpump](https://solscan.io/token/2nP9yKQNSGQy851iyawDvBkzkK2R2aqKArQCKc2gpump) | 次观察 | Score 64; Tier Early; LP $159.4K; Vol24H $865.6K; 24H -35.50%; V/LP 5.43x; 池数 2; 分项 L11/V13/B8/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| CNPY | BSC | [0xc69b...90ddd2](https://bscscan.com/token/0xc69b16cf18cea1e5d0bb6a1a9db802097790ddd2) | PVP风险池 | Score 55; Tier Liquid; LP $1.32M; Vol24H $60.49M; 24H +1.65%; V/LP 45.84x; 池数 1; 分项 L19/V17/B22/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [FTR](https://dexscreener.com/solana/fk5mugv2h3qpt6axdhs2khgdl2os424bvfeoqfntdv9y) | SOL | [DFMt2F...TLpump](https://solscan.io/token/DFMt2FyLpB6ekPNAzVErLXgpSnJ9CRf1VnxBAkTLpump) | PVP风险池 | Score 40; Tier Early; LP $249.7K; Vol24H $8.58M; 24H -35.24%; V/LP 34.37x; 池数 3; 分项 L13/V17/B8/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [1](https://dexscreener.com/solana/aqn7ukkysnazns61dvw2q6hqmm7wifsayjbon6fvwhgf) | SOL | [2bCCHQ...qVpump](https://solscan.io/token/2bCCHQadi4QeHWPKG3w13siCyWWQPgkFtniouTqVpump) | PVP风险池 | Score 34; Tier Early; LP $135.6K; Vol24H $4.91M; 24H +35.44%; V/LP 36.24x; 池数 2; 分项 L10/V17/B8/Buy8/Risk-33 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [NUBI](https://dexscreener.com/solana/265gq6qkcegwncwsl8csjzd3iddruzwj7k9pa7vst73m) | SOL | [2e3zQi...xVpump](https://solscan.io/token/2e3zQiA8JWeDjjVeuqzv9X1Q3aqRRaPqL8UYEbxVpump) | PVP风险池 | Score 33; Tier Early; LP $138.7K; Vol24H $5.07M; 24H +3786.00%; V/LP 36.52x; 池数 2; 分项 L10/V17/B0/Buy12/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [simulator](https://dexscreener.com/solana/ezjv2ygpbs3vm5qwmgqyq4gpvi77ldhwgfhay6u4ts1u) | SOL | [8hnMfF...jvHje4](https://solscan.io/token/8hnMfF4XL717GVwzDmvqjJvULozKW6w7BhHFABjvHje4) | PVP风险池 | Score 31; Tier Early; LP $187.8K; Vol24H $4.39M; 24H +1629.00%; V/LP 23.36x; 池数 1; 分项 L12/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| AGT | BSC | [0x5dbd...cae274](https://bscscan.com/token/0x5dbde81fce337ff4bcaaee4ca3466c00aecae274) | PVP风险池 | Score 22; Tier Liquid; LP $2.76M; Vol24H $86.16M; 24H +111.43%; V/LP 31.22x; 池数 1; 分项 L20/V17/B0/Buy3/Risk-42 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| DNA | BSC | [0xa991...c5cf7b](https://bscscan.com/token/0xa991f61940095aea0724ef54077223b048c5cf7b) | PVP风险池 | Score 22; Tier Liquid; LP $1.76M; Vol24H $51.16M; 24H +299.83%; V/LP 29.14x; 池数 1; 分项 L20/V17/B0/Buy3/Risk-42 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [onboard](https://dexscreener.com/solana/dbzf8tq3mtlsdgmlcdj1ya7e8hqatq22jafqma92fi4) | SOL | [5ubruM...4bpump](https://solscan.io/token/5ubruMYpgKqw9ip5J1qrXbVGmMdn2VCsMg421B4bpump) | PVP风险池 | Score 12; Tier Micro; LP $41.7K; Vol24H $4.39M; 24H +289.00%; V/LP 105.21x; 池数 1; 分项 L6/V17/B0/Buy8/Risk-43 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| PUMP | SOL | [pumpCm...7H9Dfn](https://solscan.io/token/pumpCmXqMfrsAkQ5r49WcJnRayYRqmXz6ae8H7H9Dfn) | 成熟池观察 | Score 79; Tier Mature; LP $23.94M; Vol24H $5.73M; 24H +1.43%; V/LP 0.24x; 池数 1; 分项 L20/V17/B22/Buy8/Risk-12 | 钱包级数据不可用；当前仅代理指标；资产偏成熟，不按早期吸筹处理；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 成熟池观察，不占用早期Alpha主榜 |

### C. PVP风险池明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| CNPY | BSC | [0xc69b...90ddd2](https://bscscan.com/token/0xc69b16cf18cea1e5d0bb6a1a9db802097790ddd2) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 55; Tier Liquid; LP $1.32M; Vol24H $60.49M; 24H +1.65%; V/LP 45.84x; 池数 1; 分项 L19/V17/B22/Buy3/Risk-30 | 只记录热度，不进入主榜 |
| [FTR](https://dexscreener.com/solana/fk5mugv2h3qpt6axdhs2khgdl2os424bvfeoqfntdv9y) | SOL | [DFMt2F...TLpump](https://solscan.io/token/DFMt2FyLpB6ekPNAzVErLXgpSnJ9CRf1VnxBAkTLpump) | 24H未过热但已明显波动；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 40; Tier Early; LP $249.7K; Vol24H $8.58M; 24H -35.24%; V/LP 34.37x; 池数 3; 分项 L13/V17/B8/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [1](https://dexscreener.com/solana/aqn7ukkysnazns61dvw2q6hqmm7wifsayjbon6fvwhgf) | SOL | [2bCCHQ...qVpump](https://solscan.io/token/2bCCHQadi4QeHWPKG3w13siCyWWQPgkFtniouTqVpump) | 24H未过热但已明显波动；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP极端偏高；非主流报价池 | Score 34; Tier Early; LP $135.6K; Vol24H $4.91M; 24H +35.44%; V/LP 36.24x; 池数 2; 分项 L10/V17/B8/Buy8/Risk-33 | 只记录热度，不进入主榜 |
| [NUBI](https://dexscreener.com/solana/265gq6qkcegwncwsl8csjzd3iddruzwj7k9pa7vst73m) | SOL | [2e3zQi...xVpump](https://solscan.io/token/2e3zQiA8JWeDjjVeuqzv9X1Q3aqRRaPqL8UYEbxVpump) | 买入笔数占优；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 33; Tier Early; LP $138.7K; Vol24H $5.07M; 24H +3786.00%; V/LP 36.52x; 池数 2; 分项 L10/V17/B0/Buy12/Risk-30 | 只记录热度，不进入主榜 |
| [simulator](https://dexscreener.com/solana/ezjv2ygpbs3vm5qwmgqyq4gpvi77ldhwgfhay6u4ts1u) | SOL | [8hnMfF...jvHje4](https://solscan.io/token/8hnMfF4XL717GVwzDmvqjJvULozKW6w7BhHFABjvHje4) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 31; Tier Early; LP $187.8K; Vol24H $4.39M; 24H +1629.00%; V/LP 23.36x; 池数 1; 分项 L12/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| AGT | BSC | [0x5dbd...cae274](https://bscscan.com/token/0x5dbde81fce337ff4bcaaee4ca3466c00aecae274) | 买卖基本均衡；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高；FDV超过早期Alpha主榜上限；成熟大市值 | Score 22; Tier Liquid; LP $2.76M; Vol24H $86.16M; 24H +111.43%; V/LP 31.22x; 池数 1; 分项 L20/V17/B0/Buy3/Risk-42 | 只记录热度，不进入主榜 |
| DNA | BSC | [0xa991...c5cf7b](https://bscscan.com/token/0xa991f61940095aea0724ef54077223b048c5cf7b) | 买卖基本均衡；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高；FDV超过早期Alpha主榜上限；成熟大市值 | Score 22; Tier Liquid; LP $1.76M; Vol24H $51.16M; 24H +299.83%; V/LP 29.14x; 池数 1; 分项 L20/V17/B0/Buy3/Risk-42 | 只记录热度，不进入主榜 |
| [onboard](https://dexscreener.com/solana/dbzf8tq3mtlsdgmlcdj1ya7e8hqatq22jafqma92fi4) | SOL | [5ubruM...4bpump](https://solscan.io/token/5ubruMYpgKqw9ip5J1qrXbVGmMdn2VCsMg421B4bpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高；非主流报价池 | Score 12; Tier Micro; LP $41.7K; Vol24H $4.39M; 24H +289.00%; V/LP 105.21x; 池数 1; 分项 L6/V17/B0/Buy8/Risk-43 | 只记录热度，不进入主榜 |

### D. 成熟池观察明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| PUMP | SOL | [pumpCm...7H9Dfn](https://solscan.io/token/pumpCmXqMfrsAkQ5r49WcJnRayYRqmXz6ae8H7H9Dfn) | 24H接近横盘；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 79; Tier Mature; LP $23.94M; Vol24H $5.73M; 24H +1.43%; V/LP 0.24x; 池数 1; 分项 L20/V17/B22/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| [RAY](https://dexscreener.com/solana/2axxcn6on9bbt5owwmth53c7qhuxvhleu718kqt8rvy2) | SOL | [4k3Dyj...QrkX6R](https://solscan.io/token/4k3Dyjzvzp8eMZWUXbBCjEvwSkkk59S5iCNLY3QrkX6R) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 74; Tier Liquid; LP $2.23M; Vol24H $5.76M; 24H +0.03%; V/LP 2.58x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| AKE | BSC | [0x2c3a...12f7db](https://bscscan.com/token/0x2c3a8ee94ddd97244a93bc48298f97d2c412f7db) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 74; Tier Liquid; LP $2.58M; Vol24H $5.33M; 24H -6.82%; V/LP 2.07x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| ARK | BSC | [0xcae1...618b9d](https://bscscan.com/token/0xcae117ca6bc8a341d2e7207f30e180f0e5618b9d) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 73; Tier Mature; LP $57.71M; Vol24H $1.95M; 24H -0.14%; V/LP 0.03x; 池数 1; 分项 L20/V16/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| [JUP](https://dexscreener.com/solana/3xngdc58axytrj64stqz5trdqwvtwhlr888irbbwznee) | SOL | [JUPyiw...NsDvCN](https://solscan.io/token/JUPyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN) | 买入笔数占优；LP达主观察门槛；24H成交合格；Volume/LP未失真；24H涨跌幅过热；非主流报价池；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 58; Tier Mature; LP $1085.28M; Vol24H $258.22M; 24H +471510.00%; V/LP 0.24x; 池数 1; 分项 L20/V17/B0/Buy12/Risk-15 | 成熟池观察，不占用早期Alpha主榜 |

### E. 链上确认/紧急精查表
| Token | 链 | 合约地址 | 是否需要链上确认 | 紧急精查 | 预检状态 | 原因 |
|---|---|---|---|---|---|---|
| SIREN | BSC | [0x997a...fc18e1](https://bscscan.com/token/0x997a58129890bbda032231a52ed1ddc845fc18e1) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| AEON | BSC | [0x277a...ec9b80](https://bscscan.com/token/0x277add739c6e0477616948357af9e79fe1ec9b80) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [ARF](https://dexscreener.com/solana/3q56fvb1graevwtcpyqailozfsuxywzh5mihprafp7vt) | SOL | [WHvP6N...Wopump](https://solscan.io/token/WHvP6NTRYdovnG9ZDVVrF8bR2bTChSDjLaGbeWopump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；多池数据冲突，需链上/聚合源复核 |
| TART | BSC | [0x7ab8...750314](https://bscscan.com/token/0x7ab8d02cbb51ff7223fde700eaaa2a91bf750314) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| DOPE | SOL | [33jENU...CNpump](https://solscan.io/token/33jENUQnjoitkMFpvNJcSHyLAHFWJuHwT6E3E8CNpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [PsyopAnime](https://dexscreener.com/solana/fpyosqzp5ijfrxqqbvnm67rfam7vsbvnam7puf8yvt1c) | SOL | [2nP9yK...2gpump](https://solscan.io/token/2nP9yKQNSGQy851iyawDvBkzkK2R2aqKArQCKc2gpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| CNPY | BSC | [0xc69b...90ddd2](https://bscscan.com/token/0xc69b16cf18cea1e5d0bb6a1a9db802097790ddd2) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| [FTR](https://dexscreener.com/solana/fk5mugv2h3qpt6axdhs2khgdl2os424bvfeoqfntdv9y) | SOL | [DFMt2F...TLpump](https://solscan.io/token/DFMt2FyLpB6ekPNAzVErLXgpSnJ9CRf1VnxBAkTLpump) | 是 | 否 | verified / address_preflight_v0.4 | 多池数据冲突，需链上/聚合源复核；PVP候选仅记录，非紧急精查 |
| [1](https://dexscreener.com/solana/aqn7ukkysnazns61dvw2q6hqmm7wifsayjbon6fvwhgf) | SOL | [2bCCHQ...qVpump](https://solscan.io/token/2bCCHQadi4QeHWPKG3w13siCyWWQPgkFtniouTqVpump) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| [NUBI](https://dexscreener.com/solana/265gq6qkcegwncwsl8csjzd3iddruzwj7k9pa7vst73m) | SOL | [2e3zQi...xVpump](https://solscan.io/token/2e3zQiA8JWeDjjVeuqzv9X1Q3aqRRaPqL8UYEbxVpump) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |

### F. 钱包行为 / AVE命中样本表
| Token | 链 | 合约地址 | 行为状态 | 行为层级 | AVE命中 | 判断 |
|---|---|---|---|---|---:|---|
| SIREN | BSC | [0x997a...fc18e1](https://bscscan.com/token/0x997a58129890bbda032231a52ed1ddc845fc18e1) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| AEON | BSC | [0x277a...ec9b80](https://bscscan.com/token/0x277add739c6e0477616948357af9e79fe1ec9b80) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| [ARF](https://dexscreener.com/solana/3q56fvb1graevwtcpyqailozfsuxywzh5mihprafp7vt) | SOL | [WHvP6N...Wopump](https://solscan.io/token/WHvP6NTRYdovnG9ZDVVrF8bR2bTChSDjLaGbeWopump) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| TART | BSC | [0x7ab8...750314](https://bscscan.com/token/0x7ab8d02cbb51ff7223fde700eaaa2a91bf750314) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |

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
| 成熟池观察 | 5 个 | 成熟资产不占早期Alpha主榜 |
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