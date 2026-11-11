# 运维手册：chai.aibay.asia 构建部署与验证

> 适用：/root/gh-chaishu（GitHub kenyanghui/chaishu，main → GitHub Pages → chai.aibay.asia）

## 一、常规发布流程

```bash
# 1. 本机验证（SPA 必须 vite preview，python http.server 会 404 误报）
cd /root/gh-chaishu && npm run build
(npx vite preview --port 8898 --host 127.0.0.1 &)
# 2. 渲染断言（dump-dom 偶发 0 字节，重跑一次再判）
timeout 30 google-chrome --headless --no-sandbox --disable-gpu \
  --dump-dom --virtual-time-budget=5000 http://127.0.0.1:8898/workshops
#    每页至少 1 个特征关键词；某页 DOM 体积显著小于同站其他页（壳级）
#    即按「未渲染/渲染错主题」处理，不得按 200 判定通过
# 3. 提交推送（remote 内嵌 token 已失效，勿用；git 禁 -c/-C，用 workdir）
export HOME=/root
TOKEN=$(grep -oP 'https://[^:]+:\K[^@]+(?=@github\.com)' /root/.git-credentials | head -1)
git add -A
GIT_AUTHOR_NAME=GIT_AUTHOR \
GIT_COMMITTER_NAME=GIT_COMMITTER \
git commit -m "…"
git push "https://kenyanghui:${TOKEN}@github.com/kenyanghui/chaishu.git" main:main
# 4. 轮询部署（gh CLI 不可用；偶发 443 断连重试）
curl -s -H "Authorization: token $TOKEN" \
  "https://api.github.com/repos/kenyanghui/chaishu/actions/runs?per_page=1"
# 5. 线上验证：dump-dom → 正则抽可见文本 → 新关键词命中 + 旧关键词清零双断言
```

## 二、验证断言关键词集

- **必须命中**（当前口径）：ikoning365、目标期次主题词（随 workshops.js 更新）
- **必须清零**：kenyanghui（微信语境）、通达信、旧口号（"从知识到钱"等，随口径更新）
- **PDF 检查**：pdftotext 未装；用 python 解 zlib stream 逐流扫描（strings 是假阴性）

## 三、双仓口径同步纪律

| 改什么 | GitHub 网站仓 | Gitea 材料仓(/root/chaishu) |
|---|---|---|
| 网站页面/文案 | 改 src/ → build → push | 不涉及 |
| 课程材料 HTML | public/workshop/ 副本 | ppt/ handouts/ 源文件 |
| 微信/联系方式 | src/ + public/workshop/index.html | 同步 grep 三处以上（poster/07/index 曾漏） |

材料仓 push：分支是 **main**（不是 master）；remote 内嵌凭据可用：origin GITEA_INTERNAL/kenyang/chaishu.git

## 三之二、Navbar 数组编辑事故复盘（2026-11-02）

**事故**：「拆AI工坊」改名+移位时，navLinks 数组出现「成长路径」「经典拆页」双写，线上导航重复。已修（44f437dc）。

**根因**：edit 工具的 oldString 只含「首行+新增行」，未覆盖目标位置原有的后两行；newString 又把它们带上——结果新表插入后旧表残留，map 渲染出重复链接。

**守则**：
1. 改**有序数组/列表**（navLinks、菜单、路由表）优先**整表替换**：oldString 从数组声明行到 `]` 全量，一次成形；禁止「锚点局部插入」。
2. 编辑后**唯一性断言**：`grep -c "path: '/xxx'" src/components/Navbar.jsx` 每条 path 必须恰好 1；再 `grep -n "label:"` 肉眼过一遍顺序。
3. 多轮文案微调（本次连改 5 次）后，最后一次必须**整表读一遍**再 build，防止历次编辑叠加漂移。
4. 线上验证导航时 `sort|uniq -c` 只能查重复，**查顺序要去掉 sort** 按出现次序 uniq 输出（当时两命令结论差点打架）。

## 四、域名与证书

- chai.aibay.asia → CNAME → kenyanghui.github.io；DNSPod RecordId 2439810641（密钥 /root/.acme.sh/account.conf）
- 证书正常态：CN=chai.aibay.asia，TLSv1.3
- 线上 JS bundle ~823KB（gzip 279KB），本机到 Pages 裸连接慢（~6KB/s），curl 须 --compressed

## 五、集成前 HEAD 审计（多会话并行防漂移）

适用：往已上线分支做集成前；仓由多个会话/多人共用时**必做**。

1. 回读 `git log -5 --stat` + `git status --short`，核对提交主体（标题）、作者、文件清单是否与本会话预期基线一致。
2. 不一致即停：不 merge、不覆盖、不续推；先请示 owner 定夺范围（实测事故：另一并行会话的「整站换壳」提交顶掉 HEAD，品牌/导航/路由全换、原路由被删）。
3. 回滚收敛口径：只恢复基底文件（品牌配置/路由表/导航/首页/关于页）+ 删除换壳页，已产出的内容页与数据文件全部保留，修复只做「接线」不重写内容。
4. 交付汇报必须贴头 5 条提交回读结果，作为「集成分支干净」的证据。

## 六、部署瞬断处置（同步阶段超时/取消）

- 现象：build/lint 全绿，deploy 步骤卡在同步状态约 10 分钟后报 `Timeout reached, aborting` 并取消部署。
- 判据：先定位失败步骤——失败在「部署同步」而非 build/lint，即按平台瞬断处理。
- 处置：同一 SHA 重跑 workflow（Actions 页 Re-run，或 API `POST /repos/{owner}/{repo}/actions/runs/{id}/rerun`）；**连续两次失败**才回查代码与产物。
- 实测：重跑一次即 success，代码零改动；重跑期间不必改提交，避免制造无意义新 SHA。
