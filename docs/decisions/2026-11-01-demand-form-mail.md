# D15：需求表单邮件直达站长邮箱（2026-11-01）

> 时序说明：本决策在站点提交序上（5cbd66c，21:36 前后）早于 D14 课后反馈表；D14 的 `/root/needs-backend/mail.json` 即源于本决策，D14 复用同一凭据。

## 背景
owner 要求：/workshops「说出你的需求」表单提交后直接发邮件到 554176937@qq.com（站长邮箱），发送成功后弹窗提示。

## 链路勘察（为什么是 smtp.qq.com:465）
- 现状：前端 `NEEDS_API = https://api.aibay.asia/needs/needs` → nginx `/needs/` → chai-needs.service（127.0.0.1:8193）**只落 sqlite 不发信**（D13）。
- 本机（阿里云 SERVER_IP）**出站 25 端口被封**（`/dev/tcp/mx1.qq.com/25` 实测 blocked）→ QQ MX 直投不可行（亦无 SPF）。
- 全机无现成 SMTP 凭据：QuantDinger `.env` 的 `SMTP_*` 全空不可复用；acme.sh 只有 ACCOUNT_EMAIL。
- 结论：**smtp.qq.com:465 SSL + QQ 邮箱授权码**（465 不受 25 封锁影响）。授权码由 owner 口头提供（16 位），落 `/root/needs-backend/mail.json`（600 权限），**授权码本身不写入任何文档/git**。

## 实现（/root/needs-backend/app.py）
- `send_mail(row)`：MIMEText 纯文本，主题「【AI拆书工坊】新需求 #N（联系方式）」，正文含编号/时间/IP/四字段；`SMTP_SSL(host, 465, timeout=20)` 登录后 sendmail。
- 配置热读：每次发信 `json.load(mail.json)`，**删掉该文件即自动降级**（SKIP 并返回 False），服务无需重启。
- `mail_async`：daemon 线程兜底；POST 主流程同步首发，失败则异步补发一次。
- `mail_log`：追加写 `/root/needs-backend/mail.log`（`#N OK 0.8s to=…` / `FAIL 异常` / `SKIP no-mail.json`）。
- POST 响应升级为 `{"ok":true,"mailed":bool}`——落库成功但发信失败时前端仍按提交成功处理。

## 前端（Workshops.jsx，5cbd66c）
- `d.mailed ? '提交成功！需求已发送到站长邮箱，我们会尽快回复你。' : '提交成功！我们按需求排期后，会通过你留的联系方式告诉你。'`，`window.alert` 弹窗；内联成功横幅保留。

## 验证链
- 无 mail.json 降级：POST 返回 `mailed:false` 且落库正常（本机+线上各测一次）。
- 配置后本机 E2E：`#7 OK 0.8s`、`mailed:true`；线上走 nginx 全链路 `#8 OK 0.6s`、`mailed:true`。
- GitHub Actions success；线上 bundle `index-CQz_CvLc.js` 含新弹窗文案，asset 200。

## 运维护知识
- 发信异常先看 `mail.log`；授权码失效（QQ 侧重置）表现为 FAIL 535，重新生成后改 mail.json 即可。
- 频控沿用 D13（单 IP 3 条/时），邮件风暴风险有限。
