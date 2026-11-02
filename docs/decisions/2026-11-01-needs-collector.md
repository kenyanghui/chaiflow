# D13：客户自助需求收集板块——自建轻接口（2026-11-01）

## 背景
owner 需求：投票区之外新增板块，让客户自己填需求（列表里没有的软件/场景）。方案对比后 owner 拍板 B：自建轻接口（站内原生表单不跳走）。

## 架构（零新域名、零新证书、零第三方依赖）
```
chai.aibay.asia/workshops（GitHub Pages 静态）
  └─ NeedsForm POST https://api.aibay.asia/needs/needs
       └─ nginx（api.aibay.asia 公网 DNS 已有 → SERVER_IP；泛域名证书 *.aibay.asia 免 certbot）
            location /needs/ → proxy_pass http://127.0.0.1:8193/
              └─ chai-needs.service（python3 标准库 ThreadingHTTPServer，零 pip 依赖）
                   sqlite /root/needs-backend/needs.db（needs 表）
```
- **8190 是 App 生产 API 不能动**——本服务用 8193；nginx 只反代 `/needs/`，`/admin` 不出公网。

## 防灌水与安全
- 蜜罐：隐藏字段 `website`，填了直接返回 `{"ok":true}` 不入库
- 频控：单 IP 3 条/小时（内存滑动窗口）
- 字段上限 software 120 / scene 600 / expect 600 / contact 60；contact≥5 且三内容字段合计≥4
- CORS 仅放行 `https://chai.aibay.asia`
- 真实 IP：读 `X-Real-IP`（反代后 `client_address` 恒为 127.0.0.1 的坑）

## 管理页（owner 查需求）
- 本机直开：`curl "http://127.0.0.1:8193/admin/needs?token=$(cat /root/needs-backend/token)"`（HTML 表格，最新 500 条）
- CSV 导出：同 URL 换 `/admin/needs.csv?token=...`（带 BOM，Excel 直开）
- token：`/root/needs-backend/token`（600 权限），勿入仓库/日志；外网查看走 ssh 隧道

## 前端（c732ce5）
- Workshops.jsx 新增 `NeedsForm` 组件 + 「说出你的需求」板块（投票区下方，四字段：想拆的软件/联系方式*/现在怎么做的/想要 AI 做到什么）
- 失败回退：网络异常/报错时展示「复制微信 ikoning365」按钮
- 投票区文案尾句改「列表里没有你想拆的？到下方『说出你的需求』填一下」

## 验证链
- 后端冒烟（本地+外网 nginx 链路）→ IP 修复复验 → build 258ms → 推送 2d1d934..c732ce5（GitHub 偶发超时重试即过）→ Actions success → dump-dom 5 关键词命中 → E2E 外网 POST 入库（真实 IP 记录）→ 冒烟数据清理（remaining 0）

## 运维
- `systemctl restart chai-needs`（Restart=always 自拉起）
- 换库/备份：直接拷 `/root/needs-backend/needs.db`
