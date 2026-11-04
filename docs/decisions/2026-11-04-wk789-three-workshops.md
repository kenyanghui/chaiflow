# D26 · 三场新工作坊满编上线：worker 超时接管与课件打印态（2026-11-04）

## 背景

排期中扩到九场：07 DSA 每日股票分析 / 08 通达信 WorkBuddy 盯盘复盘 / 09 QuantDinger 量化全流程，按 04–06 全套规格（落地页+guide+handouts×11+课件 deck+海报+dist 打印包）满编生产。矩阵节点不可用，降级本机满编（D21–24 先例）：3 worker 后台并行产 HTML 主面，主会话做 reducer（workshops.js/specs/PDF 批产）与汇聚门（红线 grep+pypdf 验收）。

## 决策要点

1. **worker 生成大文件超时即接管，不无限加时**：首轮 3 worker 全撞 10 分钟默认超时（HTML 主面已落盘可用）；补派轮 timeout_minutes=25 仍全灭且零落盘。结论：~58KB 量级的课件 deck 超出 worker 单任务产能，主会话自产是正解——gen.py 生成器（模板 CSS/JS 切片复用+内容模块 content{7,9}.py）一次产三场，可控可验收。坑：task_status 报「超时全灭」后 wk8/ppt 仍在被写入（进程死透有延迟），接管前先 `md5sum`+45s 复查确认写者已死，防双写冲突。
2. **课件 deck 一套 HTML 两态输出**：屏幕态=模板翻页 deck（.slide 绝对定位+hash 定位+讲师备注）；打印态=`@media print` 块内 `@page{size:1123px 631px}` px 单位直定横版页——Chrome headless 打印精确复刻模板课件 PDF 尺寸（841.92×473.04pt=1123×631px@96dpi）。模板 deck 无任何 print CSS，其课件 PDF 必由打印态变体产出；自产 deck 内嵌 print 块后一套 HTML 即双态。px 单位 @page 有效性先以 3 页小样验证再投产。
3. **handout 打印 CSS 双坑（承接 D24）**：①内联样式未带模板 @media print 块（min-height:270mm 撑出空白第 2 页）②单 sheet 文件带 page-break-after:always 强制分页——单页卡二者皆须规避。修溢出顺序：先并块（弹性并入收尾行）再收样式（行高/margin 降一档），最后才删内容。
4. **红线 grep 须对照基准辨误报**：dist 打印索引（中性文件列表页）被合规句检查命中，但基准 wk03 dist 本就无合规句——合规句约束的是内容面（落地页/guide/handouts/deck/海报），不是文件索引。终检前先验基准同位置，避免为误报返工。
5. **deploy-pages 默认 10 分钟超时扛不住大工件**：三场新增 ~9.7MB PDF 后 deploy-pages@v4 两连败（`Timeout reached, aborting!`，内部默认 timeout: 600000ms）。修复=deploy-pages 步骤 `timeout: 1800000` + job 级 `timeout-minutes: 40` + workflow `concurrency: pages`（cancel-in-progress 取代卡死旧 run）。教训：Pages 工件逼近 55MB 时先改超时再重跑，盲 rerun 只会再烧 10 分钟。

## 落地与坑

- 三场产出：课件 deck 29/31/28 页（841.92×473.04pt 多页 PDF 精确同规格）+海报 PNG 900×1600（233K/169K/239K）+dist 13 件/场（11 任务卡 PDF+课件 PDF+海报 PNG）。wk8 deck 为接管时回收 worker 遗产（31 页标签平衡，注入 print CSS 后直接可用）。
- 双仓落位：chaiAI 654a8235（GitHub，94 文件）；chaiworkshop 04aae7a（Gitea，48 文件，含 ppt/——源仓同步面沿 wk04 先例=index+handouts+ppt，不带 gh 产线工件 dist）。
- 坑：`课件.pdf` 旧名残留（worker 中途产物）与新正名课件并存——回收 worker 遗产时清点异名重复件。
- 坑：curl 断连时 `| head` 管道吞退出码，`$?` 恒 0；线上验证用 `-m 15` 短超时+逐 URL 判 code。
- 坑：`builds/latest`（legacy Pages API）显示 5 月旧构建但站点活着——部署走 Actions 时以 `actions/runs` 为准，勿被 legacy 端点误导。
- worker 产物回收价值判断：`.head.html`/`_body.html` 脚手架中间态不回收；成品 HTML 标签平衡（div/section 开闭计数）+红线 grep 过即可直接用。

## 后续义务

- ~~线上验证九场入口~~ 已完成（2026-11-05）：run 171（4020856d，超时修复版）success；主面 14/14+dist 资产 7/7 全 200；SPA 九场条目在册（wk2「12 人」系旧数据非红线范围）。
- ~~Actions run 171 部署复验~~ 已完成：concurrency 取代卡死 run 170 后一次过；若未来再超时，备选=dist 工件瘦身（课件 PDF 压缩或海报 PNG 转 WebP）。
- 课件 deck 生成器（/tmp/octopus/wk789/ppt-lib/）为临时产物；后续扩场若复用，须先入仓归档。
- memory 更新 workshop 档案：worker 超时接管先例+deck 打印态配方+deploy-pages 超时修复。
