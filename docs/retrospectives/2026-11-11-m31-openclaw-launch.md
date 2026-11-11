# 2026-11-11 · 3.1 云服务器数字助理上线（openclaw 配置使用版）

## 1. 门（GATE — 事件与影响）

- 发生了什么（事实，含时间线）：
  - owner 下发「3.1 云服务器构建数字助理」工作坊，按 wk1/wk2 纪律上矩阵生产；首派后被 owner 修正口径：重点=hermes/openclaw 的配置和使用（非泛云服务器技能）。
  - 首派 worker 被取消（无残留）；口径修正后重派，worker 45 分钟超时，但磁盘 20 文件已全部落盘且内容正确（任务卡 03=openclaw 配置与冒烟，guide openclaw 52 处、agent/cron/dashboard/gateway 命令族齐全）。
  - 主会话接管验收（红线净/四关键词/ast-ok）→ dist 15 件渲染 → build+push（ea94bd29）→ 线上验证：m3-1 与 guide 200、占位态「敬请期待/即将上线」清零、bundle 前缀 md5 一致（0885df8e…，内容哈希命名佐证同版）。
- 影响：模块三首讲（3.1）从占位页变满资产上线；目录页与 Home live 标记翻转。
- 怎么发现的：主会话独立红线 grep+openclaw 关键词计数复核 worker 产物；线上 curl 200+md5 前缀比对。

## 2. 成（SUCCESS — 哪些机制起了作用）

- 上轮复盘沉淀的「worker 超时≠产物废」直接复用：超时后先 find 清点磁盘再决定重派，本次 20 文件齐、零重派，省一轮 45 分钟。
- 「指令不得凭空编」纪律落地成方法：派发前主会话先从 memory 档案锚定本地实证事实（~/.openclaw/openclaw.json、openclaw agent 冒烟话术、cron job 显式 --model 坑）写进 worker prompt，产物命令族全部可溯源。
- 线上大文件比对新招：aibay 镜像拖尾卡顿时，用「前缀等长 md5 比对+内容哈希文件名」替代全量下载，秒级判定同版本。

## 3. 行（ACTION — 行动项）

| # | 行动项 | 文件路径 | Owner | 完成判据（可度量） |
|---|---|---|---|---|
| 1 | 教 openclaw/云工具类工作坊派发前，必须先在主会话锚定本地实证事实清单（配置路径/冒烟命令/已知坑）注入 prompt，禁 worker 自行想象产品路径 | /root/.octopus/memory/global/workshop-guides-production.md | builder | memory 增补该条 |
| 2 | 大文件线上一致性判定用「前缀等长 md5+内容哈希命名」双佐证，不硬扛全量下载（aibay 镜像 >600KB 拖尾易超时） | /root/.octopus/memory/global/workshop-guides-production.md | builder | memory 增补该条 |
| 3 | worker 超时后接管清单固化：find 清点→关键内容 grep 计数→红线→ast→缺啥补啥，不自动重派 | docs/retrospectives/2026-11-11-m31-openclaw-launch.md（本篇） | builder | 本篇记录 |

## 4. 闭环（LOOP — 反馈回写）

- [x] 行动项引用的素材文件已实际更新：workshop-guides-production.md 增补两条
- [x] 更新内容已在本复盘记录（见 ACTION 表）
- [x] PROJECT-OVERVIEW 文档索引已补本篇行
- [x] 本篇为流程类复盘，无内容失真克隆面；占位态关键词线上已清零验证

## 5. 无指责（SAFE — 归因）

- 问题归因于工具与流程：worker 默认超时上限（工具约束）、镜像网络拖尾（环境）、口径二次修正（信息增量，非错误）。
- 复盘不含个人指责。

---

## 自检表（提交前逐项打勾）

| # | 检查项 | 通过 |
|---|---|---|
| 1 | 行动项 ≤5 条 | ☑ |
| 2 | 每条行动项有具体文件路径 | ☑ |
| 3 | 每条行动项可度量 | ☑ |
| 4 | 无「下次小心」式空话 | ☑ |
| 5 | 无个人指责，归因于流程/工具/信息 | ☑ |
| 6 | LOOP 段 checkbox 已勾或注明未完成原因 | ☑ |
