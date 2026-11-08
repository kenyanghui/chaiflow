# 2026-11-08 · 工作坊插期改号（新 03/04 上线+全仓重编号）

## 1. 门（GATE — 事件与影响）

- 发生了什么（事实，含时间线）：
  - owner 决定在序列中插入两期新场：新 03「企业微信·分舵自动运营」、新 04「短视频·自动创作与发布」；原 03 企查查起依次延后，原 06 AI 手机提前为 05。
  - 本次实施：workshops.js 重排为 11 期新序；public/workshop/ 目录防碰撞倒序搬家（09→11、08→10、07→09、05→08、06→05、04→07、03→06）；全仓期数与 /workshop/0X 交叉引用 sed 改号；两 worker 并行产新 03/04 全资产（guide/handouts/ppt）；05-11 dist 全量重产（PDF+海报+dist/index）；build+push（47844001）+线上验证全绿。
- 影响：站上工作坊从 9 期变 11 期；新 03/04 页面上线（200）；05-11 编号与内容对应关系全部变化，任何漏改即「第 N 场」与目录号错位。
- 怎么发现的：push 前终检 grep（红线词/旧路径/旧期数）+线上 curl 200+bundle md5 对比（4331a5e… 本地线上一致）。

## 2. 成（SUCCESS — 哪些机制起了作用）

- 防碰撞倒序搬家（大号先挪）一次成功，68R+3RM 全部 git 识别为 rename，历史保留。
- 红线 grep 终检清单（（　）占位/第一步腔/请验证腔/旧路径/旧期数/工程禁词）在主会话对 worker 产物复核，两期均空。
- 已知坑档案直接复用：443 瞬断重试推过；中文变量名 bash 赋值失败（`课件=…` 被当命令）改 ASCII 变量后重渲；curl 大文件 -C - 续传比对 md5。

## 3. 行（ACTION — 行动项）

| # | 行动项 | 文件路径 | Owner | 完成判据（可度量） |
|---|---|---|---|---|
| 1 | 派发矩阵 worker 须显式设 timeout_minutes（默认 10 分钟对全资产产出必超时，本次两 worker 首轮均超时废跑） | /root/.octopus/memory/global/workshop-guides-production.md | builder | memory 增补该条且下次派发带超时参数 |
| 2 | bash 循环里含中文的文件名禁用中文变量名接收，统一 ASCII 变量+basename 展开 | /root/.octopus/memory/global/workshop-guides-production.md | builder | memory 增补 `$课件` 残留案例 |
| 3 | git status 带引号路径禁止 awk 空白切列（中文文件名被切坏产出 `.html".pdf` 垃圾），改 find -print0 循环 | /root/.octopus/memory/global/workshop-guides-production.md | builder | memory 增补该条 |
| 4 | dist 渲染后必须 ls 清点件数+grep 垃圾文件名（`$`/引号/`.html"`）再 git add | docs/retrospectives/2026-11-08-wk-insert-renumber.md（本篇） | builder | 本篇记录+本次已清 3 个 `$课件` |

## 4. 闭环（LOOP — 反馈回写）

- [x] 行动项引用的素材文件已实际更新：workshop-guides-production.md 增补三条坑位
- [x] 更新内容已在本复盘记录（见 ACTION 表）
- [x] PROJECT-OVERVIEW 文档索引已补本篇行
- [x] 本篇为流程类复盘，无内容失真克隆面；插期改号的克隆面（期数+路径双改）已在主仓 grep 清零

## 5. 无指责（SAFE — 归因）

- 问题归因于流程/工具：worker 默认超时过短（工具默认值）、bash 中文变量与带引号路径解析（工具行为）、无 dist 产出清点步骤（流程缺失）。
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
