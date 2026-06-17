# 自我进化轮巡

**版本：** 0.5.0-ave-cache-wallet-behavior-prep

v0.5 代码已准备。上传并运行 GitHub Actions 后，本文件会被每小时轮巡自动覆盖生成完整报告。

v0.5 新增：

- AVE Smart Wallet 周缓存可配置接口框架；
- `output/smart_wallet_cache.json` 持久保存 smart wallet；
- `output/wallet_behavior_latest.json` 每小时钱包行为样本；
- BSC ERC20 Transfer 样本与 AVE 缓存命中匹配；
- 不把 Transfer 样本等同于完整 Swap 留存。
