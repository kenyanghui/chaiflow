# 2026-11-12 · 3.1 工作坊 openclaw→hermes 口径纠偏与定档发布

## 1. 门（GATE — 事件与影响）

- 发生了什么（事实，含时间线）：
  - owner 下发 3.1 工作坊时口径两次修正：先「云服务器数字助理」→ 中转「hermes/openclaw 配置使用」→ 终版「配置 hermes，与 openclaw 是两个软件，不得文本置换」。第一版资产按 openclaw 事实产成并上线（ea94bd29）。
  - 主会话彻查 hermes 真实身份：memory 档案中 hermes 仅为矩阵节点名（非软件）；网络核实=**NousResearch/hermes-agent**（开源个人 AI 智能体，OpenClaw 替代品），官方 Quickstart 事实全套锚定（install.sh 单命令、~/.hermes 目录、.env+config.yaml 双文件、hermes setup/model/config/gateway/doctor/skills 命令族、≥64K 上下文门槛、官方故障对照表）。
  - worker 内容级重写 45min 超时，接管清单验收：openclaw 全清零、hermes 78 处、命令族齐、红线净、ast-ok → dist 15 件重产 → push 74de7788 → 线上验证绿（guide 200 / openclaw=0 / hermes=78）。
  - owner 定档 11 月 15 日（周日）14:00–17:00，要求道虾产公众号文章推「AI创新增长杨教练」（yangjiaolian）草稿箱。
  - 文章产发：复用道虾 baoyu-post-to-wechat 产线（EXTEND.md 账号 yangjiaolian=wx93f751bb1892503c）+自写 make_cover.py（PIL 云服务器/手机消息往返主题封面 1410×600）→ npx -y bun 推送成功（media_id 3xAF8cx…），manifest 落盘审计，未群发（人工闸门）。
- 影响：线上 m3-1 已是 hermes 正确版本；公众号草稿箱已有一篇可群发的招募文章。
- 怎么发现的：owner 主动纠偏；主会话对 hermes 身份三源核实（memory/本机进程/官方文档）后才动手，避免了第二次凭空写。

## 2. 成（SUCCESS — 哪些机制起了作用）

- 「指令不得凭空编」纪律升级生效：hermes 与 openclaw 名字相近且 memory 有同名节点干扰，主会话坚持官方文档核实后才注入 worker prompt，命令族全部可溯源。
- 接管清单（上轮固化）再次零重派收尾：worker 超时后 find 清点→grep 计数→红线→ast，磁盘已近完成态即接管，省一轮 45 分钟。
- 道虾产线复用：EXTEND.md 多账号配置+push_draft.sh 范式+make_cover.py 模板三件直接拼装，文章从写作到草稿箱约一轮工序；硬红线「仅 draft/add 绝不 --submit」全程守住。

## 3. 行（ACTION — 行动项）

| # | 行动项 | 文件路径 | Owner | 完成判据（可度量） |
|---|---|---|---|---|
| 1 | 工具名口径以 owner 终版为准且动手前必须官方文档核实身份；名字相近的软件（hermes/hermes-agent/openclaw/hermes 节点名）须消歧后再产内容 | /root/.octopus/memory/global/workshop-guides-production.md | builder | memory 增补消歧条目 |
| 2 | wechat-api.ts 无执行位且 bun 不在 PATH：统一用 `npx -y bun <skill.ts>` 调用（勿 bun run/直接 exec） | /root/.octopus/memory/global/ops-data-feedback-loop.md | builder | memory 增补调用式 |
| 3 | 公众号文章推送后 manifest.json 必落盘（media_id/账号/事件/「未群发」备注）供审计 | docs/retrospectives/2026-11-12-m31-hermes-swap-and-publish.md（本篇） | builder | 本篇记录+daoxia 已落盘 |

## 4. 闭环（LOOP — 反馈回写）

- [x] 行动项引用的素材文件已实际更新：两个 memory 文件增补
- [x] 更新内容已在本复盘记录（见 ACTION 表）
- [x] PROJECT-OVERVIEW 文档索引已补本篇行
- [x] 内容纠偏克隆面已全量清点：m3-1 全目录 grep openclaw=0（本地+线上双验证）

## 5. 无指责（SAFE — 归因）

- 问题归因于信息与流程：口径两次修正是需求演进（非错误）；openclaw 首版源于中转口径的字面理解；工具链摩擦（执行位/bun 缺失）属环境事实。
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
