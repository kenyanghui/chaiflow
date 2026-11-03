# chaiflow · 拆AI工坊的决策与经验档案

> 「拆」的工程化：把一个真实运营的 AI 工作坊站点（[chai.aibay.asia](https://chai.aibay.asia/)）从建站、招生、材料生产到反馈闭环的**全部决策记录、踩坑复盘与操作手册**开源。

chaiflow 不是代码库，而是一套**可复用的运营方法论语料**：每个决策为什么这么做、每次事故怎么发生又怎么防、每份材料怎么稳定产出。适合正在用 AI 工作流运营课程、社群或内容站点的人直接抄作业。

## 在线站点

| 链接 | 说明 |
|---|---|
| [https://chai.aibay.asia/](https://chai.aibay.asia/) | 拆AI工坊课程阵地（本档案对应的真实站点） |
| [https://chai.aibay.asia/workshops](https://chai.aibay.asia/workshops) | 主题投票与需求收集（16 主题按交付价值合并） |
| [https://chai.aibay.asia/workbook/](https://chai.aibay.asia/workbook/) | 六场线上可填写工作手册（D17 workbook 引擎） |
| [https://chai.aibay.asia/about](https://chai.aibay.asia/about) | 讲师与联系方式 |

## 档案结构

```
docs/
├── PROJECT-OVERVIEW.md        # 全景：站点架构、双仓纪律、决策索引（从这里开始读）
├── decisions/                 # D7–D19 决策记录：品牌口径、投票聚合、需求/反馈表、
│                              #   workbook 引擎、海报 PNG 化、二期飞轮、过级自评表…
├── retrospectives/            # 事故复盘：经典拆页全量同步、材料三期收官、上线改版、
│                              #   拆搭子名录找搭子与 chailive 模块化
└── playbooks/                 # 操作手册：
    ├── site-deploy-playbook.md      # 构建→部署→线上验证全流程（含导航数组编辑事故复盘）
    ├── print-materials-playbook.md  # A4 单页打印材料的生产纪律与矩阵派发
    └── humanize-titles-playbook.md  # 内容章名人性化命名（四范式+模型二审+人工终判）
```

## 至今为止的核心经验（速览）

细节都在各档案里，这里是最值钱的几条：

**站点与部署**
- SPA 本地验证必须 `vite preview`（python http.server 会 404 误报）；headless chrome root 下必须 `--no-sandbox`，否则 exit 0 但旧文件原样 = 静默失败
- dump-dom 偶发 0 字节，重跑再判；验证 = 新关键词命中 + 旧关键词**清零**双断言
- 线上验证导航顺序时别用 `sort | uniq -c`（排序会掩盖次序），按出现次序 `uniq` 输出
- 有序数组（导航/路由表）编辑用**整表替换**，改完对每条 path 断言唯一——曾因局部插入把「成长路径/经典拆页」双写到线上

**内容与材料**
- 表格类需求是**填写物**不是陈列物：过级自评表第一版按页面归档导致漏做，改为按能力归档走 workbook 引擎
- 印刷材料 A4 单页两坑：min-height 穿透 @media print、表格字号需固定 px
- 海报 PDF→PNG 化：A4 分页切断的根治方案；PDF 文本流是字形索引，strings 查内容是假阴性，用新旧字节 cmp 验证
- 图文/引用口径：外链在微信正文不可点，地址要写成纯文本；star 数发布当日回查 API，不抄旧文
- 脱敏必须做在入库前：源数据 user 对象嵌 bcrypt 哈希/token，入库前 STRIP

**运营与产品**
- CTA 纪律：未发布场次不挂链接，入口页一键复制微信；文案写「时间待定」不写猜测日期
- 投票主题按**交付价值**合并（35→16），不做关键词的搬运工
- 反馈/需求收集零新增服务：一个轻接口 + nginx 反代 + 蜜罐/频控，管理页不出公网
- 邮件通道设计成**可降级**：配置文件热读，删掉即自动跳过发信，落库不受影响

**AI 工作流派发**
- 矩阵派发契约先行：CONTRACT.md 随包落节点，验收命令写进契约
- `env -i` 剥环境变量会连 API key 一起剥掉 → nohup 进程静默死亡；只 unset 需要屏蔽的前缀
- 站点序 ≠ 时间序：双仓编号错位（站点 03=材料仓 04），同步按主题对位，勿按号直拷

## 为什么开源

拆书的方法论是「把一本书拆成可以带走的技能」；chaiflow 用同样的方法对待**运营本身**——每个决策可追溯、每条经验可执行。欢迎 fork 改成你自己的项目档案模板。

## 联系

微信 ikoning365（备注「chaiflow」）· [chai.aibay.asia/about](https://chai.aibay.asia/about)

## License

MIT
