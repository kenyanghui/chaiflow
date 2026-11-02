# D14：六工作坊课后反馈表——提交直达讲师邮箱（2026-11-01）

## 背景
owner 原话要求：每个工作坊最后一定要有课后反馈表，提交后直接发邮件到 554176937@qq.com，提交成功要感谢学员。全程被 SMTP 凭据阻塞（全机无可用授权码），owner 口头提供 554176937@qq.com 的 16 位授权码后一次性落地。

## 架构（复用 D13 全部基建，零新增服务）
```
六张工作坊详情页（chai.aibay.asia/workshop/{,02,03,04,05,06}/）
  └─ 表单 fetch POST https://api.aibay.asia/needs/feedback
       └─ nginx 复用 location /needs/ → proxy_pass http://127.0.0.1:8193/（尾斜杠剥前缀）
            → 后端 /feedback 路由（chai-needs.service 同进程）
                 sqlite needs.db 新增 feedback 表 + SMTP_SSL 直发 554176937@qq.com
```
- **关键路由决策**：nginx 不加新 location——`/needs/feedback` 剥前缀后即后端 `/feedback`，与 `/needs/needs` 模式完全一致，零 nginx 改动、零生产风险（8190 不动）。
- 凭据：`/root/needs-backend/mail.json`（600），host smtp.qq.com:465 SSL；SMTP 冒烟 250 通过（0.7s）。

## 表单字段与防灌水
- 字段：workshop（页内 data-workshop 预填场次名）+ rating 星级 1-5（必填）+ useful（最有用，600）/ next_topic（下次想听，300）/ suggestion（建议，600）+ contact 选填 60 + 蜜罐 website
- 服务端校验：workshop 与 rating 缺一即 400；rating clamp 到 1-5
- 频控独立分桶：feedback 单 IP 5 条/小时（`fb_rate_ok`，与 /needs 的 3 条/时互不占额）
- 发信失败兜底：同步首发失败 → `mailed=0` 入库 + 后台线程重试（`fb_async`）；成功置 `mailed=1`
- 感谢态：`{"ok":true}` 后卡片切 `.done`，显示「提交成功，谢谢你的反馈！已送达讲师邮箱，每一条都会认真读。期待下一期见。」

## 前端注入（0f6b06b，450 行）
- python 脚本幂等注入 `.foot` 前（`/tmp/octopus/inject_feedback.py`，fb-card 检测跳过已注入）
- 配色自适应：检测 `--bg:#0a0d16`（深色页）用 `#a78bfa` 紫，浅色页用 `#0071e3` 蓝——02/04 深色紫，root/03/05/06 浅色蓝
- 纯原生 JS 无依赖（静态页无 React），风格与各页 CSS 变量一致

## 管理页
- 本机：`curl "http://127.0.0.1:8193/admin/feedback?token=$(cat /root/needs-backend/token)"`（HTML 表格含 mailed 列）
- CSV：`/admin/feedback.csv?token=...`（BOM，Excel 直开）；管理页互链客户需求页

## 验证链
- 编译 OK → 重启 active → 本机 E2E FB#1 mailed=true（0.6s）→ 外网 E2E FB#2 走 nginx 全链路 mailed=true → Actions success（0f6b06b）→ dump-dom 03 页 fb-card 命中、data-workshop 正确 → 测试数据 DELETE（remaining 0）
- mail.log 记录：`FB#N OK 0.6s to=554176937@qq.com`；历史 #7/#8 为 needs 表邮件（mail.json 配置时即通）

## 运维
- 换授权码：改 mail.json（保持 600）→ `systemctl restart chai-needs`
- 邮件失败排查：`tail /root/needs-backend/mail.log`（FB#N FAIL 行）+ 管理页 mailed=0 即待重发（重启服务不会自动补发历史失败件，需重跑或手动）
