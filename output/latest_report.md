# 自我进化轮巡

**本轮时间 UTC：** 2026-08-23T15:16:07Z
**版本：** 0.5.0-ave-cache-wallet-behavior-prep
**S0 时间锚点：** 2026-06-16T16:15:17+09:00

## 一句话结论
本轮从 145 个合并Token中筛出 4 个主观察候选。v0.5已在v0.4.1基础上增加AVE周缓存真实接口接入框架、Smart Wallet持久保存、wallet_behavior_latest.json，以及BSC Transfer级钱包行为样本。注意：BSC当前是Transfer样本，不等同完整Swap解码。
合约地址可用 25 个，缺失 0 个；缺失地址的候选不能进入后续链上精查。

## 本轮扫描摘要
| 指标 | 数量 |
|---|---:|
| 原始池子记录 | 281 |
| 合并后Token | 145 |
| 输出候选 | 25 |
| 主观察 | 4 |
| 次观察 | 5 |
| PVP风险池 | 8 |
| 成熟池观察 | 5 |
| 低优先观察 | 3 |
| 多池Token | 8 |
| 多池冲突 | 1 |
| Symbol桥接合并 | 2 |
| 合约地址可用 | 25 |
| 合约地址缺失 | 0 |
| Micro层 | 6 |
| Early层 | 9 |
| Liquid层 | 6 |
| Mature层 | 4 |
| 需要链上确认 | 18 |
| 紧急精查候选 | 3 |

## v0.5 数据确认状态
| 项目 | 状态 |
|---|---|
| AVE Smart Wallet周缓存 | active，钱包数 1035，刷新时间 2026-08-17T00:45:08Z，是否过期 否 |
| 链上预检 | 本轮检查 12 个，验证通过 12 个，失败 0 个 |
| Helius状态 | 未配置，SOL使用公共RPC或跳过增强解析 |
| 当前精查层级 | 0.5.0-chain-preflight-plus-wallet-behavior：地址/账户预检 + v0.5钱包行为样本，完整Swap留存仍待下一版 |
| 钱包行为样本 | 本轮检查 4 个，BSC Transfer样本 3 个，SOL签名级 1 个，AVE钱包命中 0 个 |

## 第一部分：生成结果表格

### A. 上次记录结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| NVDAB | BSC | [0x02fc...8a7436](https://bscscan.com/token/0x02fca66c1d1afb4e2a7884261eb00f63598a7436) | 主观察 | Score 86; Tier Liquid; LP $2.07M; Vol24H $2.76M; 24H +1.43%; V/LP 1.34x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| WKC | BSC | [0x6ec9...128edb](https://bscscan.com/token/0x6ec90334d89dbdc89e08a133271be3d104128edb) | 主观察 | Score 84; Tier Liquid; LP $1.41M; Vol24H $264.3K; 24H +1.23%; V/LP 0.19x; 池数 1; 分项 L20/V10/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| PURPE | SOL | [HBoNJ5...fhGkvL](https://solscan.io/token/HBoNJ5v8g71s2boRivrHnfSB5MVPLDHHyVjruPfhGkvL) | 主观察 | Score 82; Tier Early; LP $505.6K; Vol24H $625.4K; 24H +7.33%; V/LP 1.24x; 池数 1; 分项 L16/V12/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| TUT | BSC | [0xcaae...b799f3](https://bscscan.com/token/0xcaae2a2f939f51d97cdfa9a86e79e3f085b799f3) | 主观察 | Score 77; Tier Liquid; LP $4.17M; Vol24H $3.55M; 24H +47.02%; V/LP 0.85x; 池数 1; 分项 L20/V17/B8/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [BARRON](https://dexscreener.com/solana/bjfpiz79shxybx59ghz7p9r9dfqpksm4xzu46mnmshcz) | SOL | [ECY31g...nSpump](https://solscan.io/token/ECY31gWwxy4s2VnMkYhmqDkrV75KrwR2yTtsnrnSpump) | 次观察 | Score 75; Tier Early; LP $271.2K; Vol24H $685.1K; 24H -10.81%; V/LP 2.53x; 池数 3; 分项 L13/V13/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [UOTF](https://dexscreener.com/solana/gertjb3hmeppgdaspb1ryrxvdmmqv2ukxszhzeytgptu) | SOL | [HXRgj1...Uhpump](https://solscan.io/token/HXRgj1EdGa2Y31RGAmnSXS5VMob5iqz5NA9q3pUhpump) | 次观察 | Score 73; Tier Early; LP $438.3K; Vol24H $51.7K; 24H +22.26%; V/LP 0.12x; 池数 1; 分项 L15/V5/B17/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [USTF](https://dexscreener.com/solana/4y5uejvt5nmkwmtgs39e1k9qgwzfwmvqa5jwsxi7cf7w) | SOL | [EhVASr...Dcpump](https://solscan.io/token/EhVASrKR2U74uzzvDhNWPDZRSZeq7GkxE61KXDcpump) | 次观察 | Score 69; Tier Early; LP $200.1K; Vol24H $171.5K; 24H +23.45%; V/LP 0.86x; 池数 1; 分项 L12/V8/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [App](https://dexscreener.com/solana/95xzpaggkdazgfdenx1dxfkuyzfvk53geu7mfa58qffw) | SOL | [49nkLr...Ta8pTL](https://solscan.io/token/49nkLrXi8nCZBVKsShDNasEtPe4Vn1mx9Xbr3kTa8pTL) | 次观察 | Score 66; Tier Early; LP $133.3K; Vol24H $528.0K; 24H -15.87%; V/LP 3.96x; 池数 3; 分项 L10/V12/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [CATE](https://dexscreener.com/solana/hmzvseemtzhhvznw9uwbag85hctmfnkbhzux16cy7ca3) | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | PVP风险池 | Score 56; Tier Liquid; LP $1.89M; Vol24H $52.33M; 24H -19.68%; V/LP 27.63x; 池数 2; 分项 L20/V17/B17/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| 牛来 | BSC | [0xbeea...377777](https://bscscan.com/token/0xbeea1d618e533a387d941f58a7d4c9b7bd377777) | PVP风险池 | Score 45; Tier Early; LP $350.1K; Vol24H $9.98M; 24H -14.30%; V/LP 28.52x; 池数 32; 分项 L14/V17/B17/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### B. 本轮扫描结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| NVDAB | BSC | [0x02fc...8a7436](https://bscscan.com/token/0x02fca66c1d1afb4e2a7884261eb00f63598a7436) | 主观察 | Score 86; Tier Liquid; LP $2.06M; Vol24H $2.89M; 24H +1.57%; V/LP 1.40x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| WKC | BSC | [0x6ec9...128edb](https://bscscan.com/token/0x6ec90334d89dbdc89e08a133271be3d104128edb) | 主观察 | Score 84; Tier Liquid; LP $1.40M; Vol24H $252.7K; 24H +1.64%; V/LP 0.18x; 池数 1; 分项 L20/V10/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| TUT | BSC | [0xcaae...b799f3](https://bscscan.com/token/0xcaae2a2f939f51d97cdfa9a86e79e3f085b799f3) | 主观察 | Score 77; Tier Liquid; LP $4.13M; Vol24H $3.61M; 24H +40.09%; V/LP 0.87x; 池数 1; 分项 L20/V17/B8/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| PURPE | SOL | [HBoNJ5...fhGkvL](https://solscan.io/token/HBoNJ5v8g71s2boRivrHnfSB5MVPLDHHyVjruPfhGkvL) | 主观察 | Score 77; Tier Early; LP $510.4K; Vol24H $591.0K; 24H -8.37%; V/LP 1.16x; 池数 1; 分项 L16/V12/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [BARRON](https://dexscreener.com/solana/bjfpiz79shxybx59ghz7p9r9dfqpksm4xzu46mnmshcz) | SOL | [ECY31g...nSpump](https://solscan.io/token/ECY31gWwxy4s2VnMkYhmqDkrV75KrwR2yTtsnrnSpump) | 次观察 | Score 75; Tier Early; LP $259.4K; Vol24H $674.7K; 24H -16.05%; V/LP 2.60x; 池数 3; 分项 L13/V13/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [UOTF](https://dexscreener.com/solana/gertjb3hmeppgdaspb1ryrxvdmmqv2ukxszhzeytgptu) | SOL | [HXRgj1...Uhpump](https://solscan.io/token/HXRgj1EdGa2Y31RGAmnSXS5VMob5iqz5NA9q3pUhpump) | 次观察 | Score 73; Tier Early; LP $438.3K; Vol24H $52.3K; 24H +22.98%; V/LP 0.12x; 池数 1; 分项 L15/V5/B17/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [App](https://dexscreener.com/solana/95xzpaggkdazgfdenx1dxfkuyzfvk53geu7mfa58qffw) | SOL | [49nkLr...Ta8pTL](https://solscan.io/token/49nkLrXi8nCZBVKsShDNasEtPe4Vn1mx9Xbr3kTa8pTL) | 次观察 | Score 71; Tier Early; LP $138.8K; Vol24H $532.8K; 24H +1.87%; V/LP 3.84x; 池数 3; 分项 L10/V12/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [USTF](https://dexscreener.com/solana/4y5uejvt5nmkwmtgs39e1k9qgwzfwmvqa5jwsxi7cf7w) | SOL | [EhVASr...Dcpump](https://solscan.io/token/EhVASrKR2U74uzzvDhNWPDZRSZeq7GkxE61KXDcpump) | 次观察 | Score 69; Tier Early; LP $200.2K; Vol24H $170.8K; 24H +22.26%; V/LP 0.85x; 池数 1; 分项 L12/V8/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| KII | BSC | [0xeec6...197886](https://bscscan.com/token/0xeec6574eabba52bac3f0277f2cd5ac7e67197886) | 次观察 | Score 68; Tier Liquid; LP $1.92M; Vol24H $25.88M; 24H -7.97%; V/LP 13.51x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-18 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| CATE | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | PVP风险池 | Score 61; Tier Liquid; LP $1.98M; Vol24H $53.06M; 24H -5.59%; V/LP 26.81x; 池数 2; 分项 L20/V17/B22/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| WINNING | SOL | [FW6R4Q...g8pump](https://solscan.io/token/FW6R4QQeP4fzqRwDHbBkpjHx3ecvYwhd5g7chKg8pump) | PVP风险池 | Score 47; Tier Micro; LP $59.6K; Vol24H $5.99M; 24H +9.70%; V/LP 100.42x; 池数 2; 分项 L7/V17/B17/Buy12/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [RAYCAT](https://dexscreener.com/solana/987vwvjz5frjwcy9zwc2trugl8fbmt1af4purt7xjpjd) | SOL | [CFNRDa...jNupFL](https://solscan.io/token/CFNRDaxFcvRwRSNnA5cHrCCr6AHhk9dNkHWpRUjNupFL) | PVP风险池 | Score 41; Tier Micro; LP $75.0K; Vol24H $7.91M; 24H -11.25%; V/LP 105.43x; 池数 1; 分项 L8/V17/B17/Buy8/Risk-33 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| Bicat | BSC | [0xdbc6...207777](https://bscscan.com/token/0xdbc6333a7d8bcd95f96641eda4d095e69f207777) | PVP风险池 | Score 39; Tier Early; LP $186.9K; Vol24H $7.66M; 24H -59.34%; V/LP 40.98x; 池数 1; 分项 L12/V17/B8/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [CATLIST](https://dexscreener.com/solana/gyz6rxjfnb3yjp2j2e7hmonojgqekzuxeeujurncqj1w) | SOL | [BKaXDg...g7pump](https://solscan.io/token/BKaXDgZxUSC9njpX89xpQ5USh2pnK1yzZvgk8Mg7pump) | PVP风险池 | Score 31; Tier Micro; LP $78.3K; Vol24H $5.08M; 24H +1142.00%; V/LP 64.93x; 池数 1; 分项 L8/V17/B0/Buy12/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| BORT | BSC | [0x2a84...374444](https://bscscan.com/token/0x2a846aaaf896ef393ccb76398c1d96ea97374444) | PVP风险池 | Score 27; Tier Early; LP $236.9K; Vol24H $5.57M; 24H +141.22%; V/LP 23.53x; 池数 1; 分项 L13/V17/B0/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### C. PVP风险池明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| CATE | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | 24H接近横盘；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 61; Tier Liquid; LP $1.98M; Vol24H $53.06M; 24H -5.59%; V/LP 26.81x; 池数 2; 分项 L20/V17/B22/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| WINNING | SOL | [FW6R4Q...g8pump](https://solscan.io/token/FW6R4QQeP4fzqRwDHbBkpjHx3ecvYwhd5g7chKg8pump) | 24H波动可控；买入笔数占优；LP未达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 47; Tier Micro; LP $59.6K; Vol24H $5.99M; 24H +9.70%; V/LP 100.42x; 池数 2; 分项 L7/V17/B17/Buy12/Risk-30 | 只记录热度，不进入主榜 |
| [RAYCAT](https://dexscreener.com/solana/987vwvjz5frjwcy9zwc2trugl8fbmt1af4purt7xjpjd) | SOL | [CFNRDa...jNupFL](https://solscan.io/token/CFNRDaxFcvRwRSNnA5cHrCCr6AHhk9dNkHWpRUjNupFL) | 24H波动可控；买卖略偏买入；LP未达主观察门槛；24H成交合格；Volume/LP极端偏高；非主流报价池 | Score 41; Tier Micro; LP $75.0K; Vol24H $7.91M; 24H -11.25%; V/LP 105.43x; 池数 1; 分项 L8/V17/B17/Buy8/Risk-33 | 只记录热度，不进入主榜 |
| Bicat | BSC | [0xdbc6...207777](https://bscscan.com/token/0xdbc6333a7d8bcd95f96641eda4d095e69f207777) | 24H未过热但已明显波动；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 39; Tier Early; LP $186.9K; Vol24H $7.66M; 24H -59.34%; V/LP 40.98x; 池数 1; 分项 L12/V17/B8/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [CATLIST](https://dexscreener.com/solana/gyz6rxjfnb3yjp2j2e7hmonojgqekzuxeeujurncqj1w) | SOL | [BKaXDg...g7pump](https://solscan.io/token/BKaXDgZxUSC9njpX89xpQ5USh2pnK1yzZvgk8Mg7pump) | 买入笔数占优；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 31; Tier Micro; LP $78.3K; Vol24H $5.08M; 24H +1142.00%; V/LP 64.93x; 池数 1; 分项 L8/V17/B0/Buy12/Risk-30 | 只记录热度，不进入主榜 |
| BORT | BSC | [0x2a84...374444](https://bscscan.com/token/0x2a846aaaf896ef393ccb76398c1d96ea97374444) | 买卖基本均衡；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 27; Tier Early; LP $236.9K; Vol24H $5.57M; 24H +141.22%; V/LP 23.53x; 池数 1; 分项 L13/V17/B0/Buy3/Risk-30 | 只记录热度，不进入主榜 |
| Dinger | SOL | [3kvZYB...EYpump](https://solscan.io/token/3kvZYBrBPEySFwQfXZGEvJSeMWRa6BkTS34suBEYpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 25; Tier Micro; LP $50.2K; Vol24H $10.39M; 24H +589.63%; V/LP 207.01x; 池数 4; 分项 L6/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| YOMOGI | SOL | [4978aT...gzpump](https://solscan.io/token/4978aTN9W3CDuUREGxAQaBYqhPXt8142N4o4Sfgzpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 14; Tier Micro; LP $34.5K; Vol24H $8.36M; 24H +201.88%; V/LP 242.22x; 池数 2; 分项 L5/V17/B0/Buy8/Risk-40 | 只记录热度，不进入主榜 |

### D. 成熟池观察明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| [BOME](https://dexscreener.com/solana/dsuvc5qf5ljhhv5e2td184ixotsncnwj7i4jja4xsrmt) | SOL | [ukHH6c...Z74J82](https://solscan.io/token/ukHH6c7mMyiWCf1b9pnWe25TSpkDDt3H5pQZgZ74J82) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大池 | Score 74; Tier Mature; LP $17.38M; Vol24H $5.92M; 24H +4.12%; V/LP 0.34x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| BTCB | BSC | [0x7130...3ead9c](https://bscscan.com/token/0x7130d2a12b9bcbfae4f2634d864a1ee1ce3ead9c) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 74; Tier Mature; LP $18.32M; Vol24H $22.80M; 24H +0.30%; V/LP 1.24x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| [ANSEM](https://dexscreener.com/solana/fnzky6x7entq1er3d225dqyt7ybfka4pskbmqhb8l3cc) | SOL | [9cRCn9...TGpump](https://solscan.io/token/9cRCn9rGT8V2imeM2BaKs13yhMEais3ruM3rPvTGpump) | 24H波动可控；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 73; Tier Liquid; LP $2.77M; Vol24H $2.07M; 24H -10.25%; V/LP 0.75x; 池数 1; 分项 L20/V16/B17/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| [JUP](https://dexscreener.com/solana/eoftfbgdbxzkeqzc5dtygvnkicwevfezgtzqm9eftj6b) | SOL | [JUPyiw...NsDvCN](https://solscan.io/token/JUPyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；非主流报价池；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 71; Tier Mature; LP $71.21M; Vol24H $80.25M; 24H -4.40%; V/LP 1.13x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-15 | 成熟池观察，不占用早期Alpha主榜 |
| [PUMP](https://dexscreener.com/solana/4c8kctyztmtzwv83y5actpvt2axyyu2t9zhhdotfgnno) | SOL | [pumpCm...7H9Dfn](https://solscan.io/token/pumpCmXqMfrsAkQ5r49WcJnRayYRqmXz6ae8H7H9Dfn) | 24H波动可控；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；非主流报价池；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 66; Tier Mature; LP $110.01M; Vol24H $45.67M; 24H +9.35%; V/LP 0.42x; 池数 4; 分项 L20/V17/B17/Buy3/Risk-15 | 成熟池观察，不占用早期Alpha主榜 |

### E. 链上确认/紧急精查表
| Token | 链 | 合约地址 | 是否需要链上确认 | 紧急精查 | 预检状态 | 原因 |
|---|---|---|---|---|---|---|
| NVDAB | BSC | [0x02fc...8a7436](https://bscscan.com/token/0x02fca66c1d1afb4e2a7884261eb00f63598a7436) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| WKC | BSC | [0x6ec9...128edb](https://bscscan.com/token/0x6ec90334d89dbdc89e08a133271be3d104128edb) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| PURPE | SOL | [HBoNJ5...fhGkvL](https://solscan.io/token/HBoNJ5v8g71s2boRivrHnfSB5MVPLDHHyVjruPfhGkvL) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| TUT | BSC | [0xcaae...b799f3](https://bscscan.com/token/0xcaae2a2f939f51d97cdfa9a86e79e3f085b799f3) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [BARRON](https://dexscreener.com/solana/bjfpiz79shxybx59ghz7p9r9dfqpksm4xzu46mnmshcz) | SOL | [ECY31g...nSpump](https://solscan.io/token/ECY31gWwxy4s2VnMkYhmqDkrV75KrwR2yTtsnrnSpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [UOTF](https://dexscreener.com/solana/gertjb3hmeppgdaspb1ryrxvdmmqv2ukxszhzeytgptu) | SOL | [HXRgj1...Uhpump](https://solscan.io/token/HXRgj1EdGa2Y31RGAmnSXS5VMob5iqz5NA9q3pUhpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [App](https://dexscreener.com/solana/95xzpaggkdazgfdenx1dxfkuyzfvk53geu7mfa58qffw) | SOL | [49nkLr...Ta8pTL](https://solscan.io/token/49nkLrXi8nCZBVKsShDNasEtPe4Vn1mx9Xbr3kTa8pTL) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [USTF](https://dexscreener.com/solana/4y5uejvt5nmkwmtgs39e1k9qgwzfwmvqa5jwsxi7cf7w) | SOL | [EhVASr...Dcpump](https://solscan.io/token/EhVASrKR2U74uzzvDhNWPDZRSZeq7GkxE61KXDcpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| KII | BSC | [0xeec6...197886](https://bscscan.com/token/0xeec6574eabba52bac3f0277f2cd5ac7e67197886) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [PUMP](https://dexscreener.com/solana/4c8kctyztmtzwv83y5actpvt2axyyu2t9zhhdotfgnno) | SOL | [pumpCm...7H9Dfn](https://solscan.io/token/pumpCmXqMfrsAkQ5r49WcJnRayYRqmXz6ae8H7H9Dfn) | 是 | 否 | verified / address_preflight_v0.4 | 多池数据冲突，需链上/聚合源复核 |

### F. 钱包行为 / AVE命中样本表
| Token | 链 | 合约地址 | 行为状态 | 行为层级 | AVE命中 | 判断 |
|---|---|---|---|---|---:|---|
| NVDAB | BSC | [0x02fc...8a7436](https://bscscan.com/token/0x02fca66c1d1afb4e2a7884261eb00f63598a7436) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| WKC | BSC | [0x6ec9...128edb](https://bscscan.com/token/0x6ec90334d89dbdc89e08a133271be3d104128edb) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| PURPE | SOL | [HBoNJ5...fhGkvL](https://solscan.io/token/HBoNJ5v8g71s2boRivrHnfSB5MVPLDHHyVjruPfhGkvL) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
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
| 主观察候选 | 4 个 | 主榜继续稀缺，但必须结合合约地址进入链上确认 |
| PVP风险池 | 8 个 | v0.3已单独展示明细，便于判断噪声来源 |
| 成熟池观察 | 5 个 | 成熟资产不占早期Alpha主榜 |
| 合约地址覆盖 | 可用 25，缺失 0 | 地址缺失会阻断BSC RPC/Helius精查，需要优先补齐 |
| LP层级 | Micro 6 / Early 9 / Liquid 6 / Mature 4 | 下一步可以按层级分别设置进攻规则 |
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
| dexscreener_search | {'ok': True, 'count': 360} |
| geckoterminal_bsc_trending | {'ok': True, 'count': 20} |
| geckoterminal_solana_trending | {'ok': True, 'count': 20} |

## 数据限制
- This v0.4 scan uses free public sources plus lightweight chain address/account preflight when enabled.
- AVE Smart Money weekly cache structure is connected; real AVE API refresh is handled by the weekly workflow/cache file.
- S0 exact historical replay is not implemented yet; candidates are marked with current metrics only.
- Wallet-level buy/sell retention is not implemented yet; v0.4 only preflights token contract/account existence.
- v0.4 adds chain preflight status and Smart Wallet cache status on top of contract-address output, liquidity tiers, visible PVP/mature detail tables, and chain-verify flags.
- Contract addresses are extracted from DEXScreener baseToken or GeckoTerminal relationships when available; missing addresses are explicitly marked unavailable.