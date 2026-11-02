# 复盘：三期材料收官 + 各场详情页 + 双仓同步（2026-10-31 → 11-01）

接续 `2026-10-31-launch-redesign-lessons.md`，覆盖：知识星球场全套材料、首期页视频/源码增强、四场独立详情页（假链接纠正）、02 期材料口径双仓同步。

## 事件线

1. **第三场（知识星球）全套材料定稿**（Gitea 336dc12）：课件 29 页（622 行，禁令零命中）、海报 249 行、handouts 01–09、dist 11 份 PDF、README 三期导航。
   - 海报曾两次派 xuan 矩阵：`opencode/glm-5.3-flash-free` 与 `deepseek-v4.1-flash-free` 建会话后 3 分钟零 part（连工具调用都没有）＝模型卡死不是慢；收尾 `pkill -f "loong run"` 误杀自身 ssh（exit 255）。本机接管一次写完。
2. **首期页增强**（GitHub 3f5cca0）：加「课前先看」两个 B 站嵌入视频（ima `BV1gjLwz5ERY` 16:33 / workbuddy `BV1ABu96JEAR` 50:31）+ wechat-pub-workbuddy 源码下载区（双处链接）；Navbar「工作坊」→「拆AI工作坊」；wk1 标题价值化与 workshops.js 同步。
3. **假链接纠正：四场独立详情页**（GitHub 911a8f8）：`/workshops` 三个开放场的「看本场完整介绍 →」原本全部硬编码 `href="/workshop/"`——点第二、三场进去是首期内容。owner 定性「不要做假」。落地：`/workshop/02/`（02 期材料整包）、`/workshop/03/`（企查查，无材料只写站内数据）、`/workshop/04/`（03 期材料整包）；`workshops.js` 加 `link` 字段，`Workshops.jsx` 条件渲染，soon 卡补链接。
4. **02 期材料口径双仓同步**（Gitea e965b10）：13 个 HTML「11 月 8 日」→「11 月 · 时间待定」、CTA 公众号链接→微信 ikoning365 一键复制、dist 11 份 PDF 重生成（9 handout×1 页 + 海报 1 页 + 课件 29 页，pypdf 页数断言全过）。
5. **经验入册**（本仓 6eb6044）：decisions D11（详情页路由 + 双仓同步纪律）+ OVERVIEW 五d + 仓库版本表更新。

## 关键教训

### L1 链接与内容「不要做假」是硬红线
- 组件里硬编码单场地址 = 点进去是别场内容，属造假。**链接一律走数据（`link` 字段）+ 条件渲染**，无 link 不渲染按钮。
- 无材料的场次只许用站内场次数据已有的 summary/outcomes/who 建简页，**不虚构讲义、任务卡、交付物**；页面不设空材料索引。
- 「官方」身份未确认（B 站 UP 疑似官方号）就不挂「官方介绍视频」标签，页面措辞降级为「课前先看/介绍视频」。

### L2 口径变更三处一次到位
- 本次顺序错了：先修站点部署副本，源仓遗留旧日期，被 owner 要求「一起改，保持同步」。正确顺序：**源仓 HTML → 重生成 dist PDF → 覆盖 gh 仓发布副本 → `diff -rq` 校验**，一次完成。
- 材料仓是源，`public/workshop/0N/` 是发布副本（不含 dist）；只改副本不留源 = 下次同步口径回归（上次微信号替换就漏过 Gitea 3 处，同一类坑二犯即立规 → D11）。

### L3 矩阵派发补充实证（丰富 D10）
- 单文件任务（海报/单页）按切分红线本就该本机写；派矩阵只省 打字时间，赔上两次卡死的等待，**切片判定先行，不为派而派**。
- 节点模型实际 ID 是 `opencode/*-free` 系列（配置里的 `zhipuai/*` 不存在）；建会话 3 分钟零 part 直接判死换模型或收回本机，不重试观望。
- 节点上清理 loong 进程用 `pkill -f [l]oong`（`[.]`/`[x]` 方括号转义防自杀），或 `pkill -f "loong run"` 前先确认不在匹配串里。

### L4 工具与环境坑（本机）
- `perl -CSD -pe` 脚本里的中文字面量按字节匹配失败（-CSD 只管 IO 不管脚本编码），**多文件中文替换直接用 python3 `io.open(encoding='utf-8')`**，一次过。
- `/root/chaishu` 无 git 身份配置，提交必须带 `GIT_AUTHOR_*/GIT_COMMITTER_*` env（kenyanghui / yanghuihotmail@hotmail.com）。
- `rm -rf` 整条命令被代理安全规则拦截——同步副本用覆盖式 `cp -r src/. dst/` 替代删除重建。
- headless dump-dom 偶发 0 字节/404 页，重跑即可；**线上验证域名是 chai.aibay.asia，www.aibay.asia 是别的站**（本次真踩：404 页差点误判部署失败）。
- PDF 关键词断言只信页数（pypdf 可靠），CJK 文本提取（pypdf/pdftotext）对 chrome 子集字体不全，文本口径以 HTML 源为准。

### L5 内容选型与嵌入
- B 站嵌入 `//player.bilibili.com/player.html?bvid=<BV>&autoplay=0` 稳定可用；视频时长超课堂口径（≤5′）时页面标注「完整版 + 时长」，课堂按 RIA 截段讲。
- GitHub 仓作为客户下载物料时：链接放详情页「资源下载」区 + 材料索引双处，仓须 public + LICENSE（MIT）。

## 遗留

- 企查查场（wk3）材料未产出，详情页为数据简页——材料定稿后按 D11 流程补部署。
- 08 讲师资控手册片源清单仍是占位，可补上述两个 BV 号。
- 矩阵免费模型卡死问题未解（glm/deepseek free 均复现），上矩阵前先跑 1 分钟 part 探活。
