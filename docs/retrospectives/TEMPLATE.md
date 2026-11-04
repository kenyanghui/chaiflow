# 复盘模板（TEMPLATE）

> 用法：复制本文件为 `docs/retrospectives/YYYY-MM-DD-<主题>.md`，逐段填写，
> 写完对照文末自检表打勾。机制借鉴内部 loong-workflow 复盘清单
> （五段式 + 行动项四条硬约束），决策见
> [decisions/2026-11-04-borrow-loong-workflow-mechanisms.md](../decisions/2026-11-04-borrow-loong-workflow-mechanisms.md)。
> 与 rsi-ima-workbuddy-wechat-web 仓 `docs/retrospectives/TEMPLATE.md` 同源双落。
> 教人发指令类内容（指令卡/提示词区块）：指令终稿先写学习者最小动线
> （复制→粘贴→贴凭证→发送），规则见
> [retrospectives/2026-11-04-prompt-card-learner-first.md](./2026-11-04-prompt-card-learner-first.md)。
> owner 给出引号原话定稿时：只替换原话指向的对象本身，相邻标题/脚注/首行
> 等「一致性调整」先列清单征得同意再动，规则见
> [retrospectives/2026-11-04-owner-final-wording-literal.md](./2026-11-04-owner-final-wording-literal.md)。

# YYYY-MM-DD · <一句话主题>

## 1. 门（GATE — 事件与影响）

- 发生了什么（事实，含时间线）：
- 影响（谁/什么受影响，可量化则量化）：
- 怎么发现的（哪条读路径/哪个告警/哪次回读）：

## 2. 成（SUCCESS — 哪些机制起了作用）

- 哪条既有守则/手册/决策拦住了或缩短了事故：
- （没有也要写「本次无——暴露哪条守则缺失」，缺的守则进 ACTION）

## 3. 行（ACTION — 行动项）

> 硬约束：总量 ≤5 条；每条带具体文件路径；有 Owner；可度量；
> 禁「更努力/更仔细/下次小心」式空话。

| # | 行动项 | 文件路径 | Owner | 完成判据（可度量） |
|---|---|---|---|---|
| 1 |  |  |  |  |
| 2 |  |  |  |  |

## 4. 闭环（LOOP — 反馈回写）

- [ ] 行动项引用的素材文件已实际更新（决策/手册/README/PROJECT-OVERVIEW）：
- [ ] 更新内容已在本复盘记录（改了哪条守则/加了哪个断言）：
- [ ] PROJECT-OVERVIEW 文档索引已补本篇行（索引与文件一一对应）：
- [ ] 若本篇为内容打回类复盘：失真关键词已全仓克隆面清点（guide/落地页/handouts/workbook 等载体逐一 grep，不只改被打回的那个文件）：

## 5. 无指责（SAFE — 归因）

- 问题归因于流程/工具/信息不足（非个人能力）：
- 复盘不含个人指责：

---

## 自检表（提交前逐项打勾）

| # | 检查项 | 通过 |
|---|---|---|
| 1 | 行动项 ≤5 条 | ☐ |
| 2 | 每条行动项有具体文件路径 | ☐ |
| 3 | 每条行动项可度量 | ☐ |
| 4 | 无「下次小心」式空话 | ☐ |
| 5 | 无个人指责，归因于流程/工具/信息 | ☐ |
| 6 | LOOP 段 checkbox 已勾或注明未完成原因 | ☐ |
