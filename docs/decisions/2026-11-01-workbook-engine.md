# D17：六工作坊线上可填写工作手册（workbook）——填完导出 + 一键发讲师邮箱（2026-11-01）

## 背景
打印版材料只能纸面填，学员回家不带走、数据收不上来。补一个线上同构版：内容与打印版一致，可填、可导出、可提交给讲师，作为「台账式」抓手。

## 架构（零新增服务，复用 D13/D14 的 8193 通道）
```
chai.aibay.asia/workbook/           静态页（vanilla JS + 无构建）
  ├─ specs.js  window.WORKBOOK_SPECS（六场字段规格，机械解析打印版生成）
  └─ 表单 → POST https://api.aibay.asia/needs/workbook
        └─ nginx /needs/ 剥前缀 → 127.0.0.1:8193 /workbook（chai-needs.service）
             sqlite needs.db 新增 workbook 表 + SMTP 直发 554176937@qq.com
```
- **关键点**：用原生 HTML+JS 而非 React——静态页无构建链，改规格只改 `specs.js` 数据；改文案不动引擎。
- specs 由 `/tmp/octopus/gen_workbook_specs.py` 机械解析打印版素材生成（新场次/新步骤重跑即可），手改仅用于结构性补充（如 wk2 的 s0）。
- 路由沿用 `/needs/workbook` → 后端 `/workbook`：nginx 零改动、8190 生产 API 不动。
- 录入：`workbook(id, created_at, ip, ua, workshop, name, team, leader, contact, data_json, mailed)`；频控 `wb_rate_ok` = 5 条/小时/IP（独立分桶，与 needs/feedback 互不占额）；蜜罐 `website` 字段。
- 发信失败兜底同 D14：`mailed=0` 入库 + `wb_async` 后台重试；管理页 `/admin/workbook`（token 鉴权）与 `/admin/workbook.csv`。
- 前端：场次 tab（`location.hash` 选场，如 `/workbook/#02`）、基本信息、各节任务卡勾选+记录、30 天三栏、复盘卡、验收、自评 10 题；`localStorage` 键 `chai-wb:{no}` 自动续填；导出 `.md`。

## 第 0 节（底盘）字段
引擎支持可选 `s0`（h1 / hint / items[{a,r}]），渲染为「第 0 节 · 底盘」卡片并在导出中成段。**只有 wk2 配了 s0**（ima 五步 / 公众号四步 / 老学员回灌三项），其余五场无底盘节，引擎自动跳过。

## 验收
- 本机与线上 headless 渲染：`/workbook/#02` 显示「第 0 节 · 底盘：把库和号接通（20′）」+ s0_0..2 三个勾选；
- 线上真实提交：`{"ok":true,"mailed":true}`，`mail.log` `WB#2 OK 0.7s`。
