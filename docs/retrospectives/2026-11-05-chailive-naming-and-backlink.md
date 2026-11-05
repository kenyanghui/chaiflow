# 2026-11-05 · chailive 命名不统一未自察 + 无回主站通路

## 1. 门（GATE — 事件与影响）

- 发生了什么（事实，含时间线）：
  - chailive 站（www.aibay.asia/chailive/）此前以「拆生活指南」为模块名上线，与主站及各落地页统一口径「拆学习」不一致（index.html 6 处、books.html 1 处、scripts/{template-living.html,template.html,build_cards.py} 各若干处）。
  - 同站 books.html 与其产线源 scripts/template.html 存在 152–163 行双 body 残留（第二个 `</head><body><header>` 块被 merge_build.py L206 整读带入产物），线上书库页实拍双 header。
  - 全站四页（index/books 两产物 + 两模板）无任何指向 chai.aibay.asia 的链接，子站成信息孤岛。
  - 2026-11-05 一次性修复：五文件统一「拆学习」、四页 header 加「回主站」按钮、清除双 body 残留，commit fbb7921 推双远端，线上回读全过。
- 影响（谁/什么受影响，可量化则量化）：
  - 用户侧：子站访客无路径回主站（转化漏斗断裂）；同一产品两个名字（「拆学习」vs「拆生活指南」）造成认知摩擦。
  - 站点侧：书库页双 header（视觉 bug，长期在线未被发现）。
- 怎么发现的（哪条读路径/哪个告警/哪次回读）：
  - 命名不一致：跨站走查时 grep「生活指南」命中 chailive 六处才发现——非任何自动检查报警。
  - 双 body 残留：修命名时顺带读 template.html 152–163 行发现，再以线上 books 页 curl 实证双 header。
  - 无回主站：页面走查发现 header 仅「书库/拆学习」两站内互跳。

## 2. 成（SUCCESS — 哪些机制起了作用）

- 本次无——命名一致性、站间互链、HTML 结构有效性均无守则与检查器，三问题全靠人工走查偶然发现。缺失的检查进 ACTION（转 loong-workflow 内容一致性工作流承接）。

## 3. 行（ACTION — 行动项）

| # | 行动项 | 文件路径 | Owner | 完成判据（可度量） |
|---|---|---|---|---|
| 1 | 内容一致性检查工作流立项（站名/模块名跨站口径检查） | /data/loong-workflow/core/rules/ | builder | 规则文档+检查脚本落仓，guard 通过 |
| 2 | 一致性检查脚本覆盖 chailive（旧词清零断言+回主站链接断言） | 同上脚本内 | builder | 对 www.aibay.asia/chailive/ 跑通：旧词=0、回主站链接≥1 |
| 3 | 双 body 类结构残留在检查脚本中加断言（header 数=1） | 同上脚本内 | builder | books.html `<header class="bar">` 计数=1 断言生效 |
| 4 | chailive 记忆档案补命名终态与构建源同步关系 | /root/.octopus/memory/global/chailive.md | builder | 档案含「拆学习」终态+模板↔产物拷贝关系 |

## 4. 闭环（LOOP — 反馈回写）

- [x] 行动项引用的素材文件已实际更新（决策/手册/README/PROJECT-OVERVIEW）：本复盘+索引
- [x] 更新内容已在本复盘记录（命名统一口径、模板↔产物同步义务、双 body 教训）
- [x] PROJECT-OVERVIEW 文档索引已补本篇行（索引与文件一一对应）
- [x] 若本篇为内容打回类复盘：失真关键词已全仓克隆面清点——「生活指南」已对 chailive 全仓（html/py/js/md，排除 .git）grep 清零，线上两页回读=0；chaiAI/chaishu 此前排查已零命中

## 5. 无指责（SAFE — 归因）

- 问题归因于流程/工具/信息不足：改名决策未同步到 chailive 子站（无跨站命名清单）；模板与产物双份维护无「改必同改」检查；HTML 无结构校验。三者为机制缺失，非个人疏漏。
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
