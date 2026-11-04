# chaiflow · 拆AI工作坊开源档案

> 决策与经验的公开档案——一个「拆AI工作坊」从想法到六场交付的全部决策过程、踩坑复盘与可复用手册。**不是代码库，是决策库。**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
关联站点：[chai.aibay.asia](https://chai.aibay.asia) · 方法论支持：拆书帮（chaishubang.net）

---

## 这是什么

「拆AI工作坊」是一系列线下 AI 实操课：每期拆一个真实 AI 软件/技能/专家，学员当场带着电脑做出可用的东西离场。六场主题——ima 知识库、GitHub 网站、知识星球、企查查、DeepSeek Harness、AI 手机。

本仓是这门课的**决策与经验档案**（内部 chai-workflow 仓的脱敏开源版）：

- **为什么公开**：拆书帮的 RIA 方法论核心是「拆为己用」——我们把自己拆 AI 的过程也拆出来，别人可以直接取用决策与教训，不必重踩。
- **为什么不是代码**：课程代码在别处（网站开源于 chaiAI 相关仓、技能包开源于 rsi-ima-workbuddy-wechat-web）；这里存的是**「为什么这么做」**——决策记录（ADR）、复盘（lessons learned）、手册（playbook）。

## 仓内结构

```
chaiflow/
├── README.md                  ← 本文件
├── docs/
│   ├── PROJECT-OVERVIEW.md    ← 项目全景：定位、六场结构、仓矩阵、文档索引（先读这个）
│   ├── decisions/             ← 决策记录（ADR）：带编号 D1–D24，按日期命名
│   ├── retrospectives/        ← 复盘：上线翻车、全量同步、模块改版等大动作的教训沉淀
│   └── playbooks/             ← 手册：可复用的标准作业流程（SOP）
│       ├── site-deploy-playbook.md      # 网站构建/推送/验证运维手册（含 Navbar 数组编辑事故复盘）
│       ├── print-materials-playbook.md  # A4 单页打印材料生产（两个 CSS 坑 + 双仓同步收尾清单）
│       └── humanize-titles-playbook.md  # 内容站章名人性化命名四范式
└── external/                  ← 参照系：8 个「拆书成 Skill」同行仓的只读快照
    ├── ATTRIBUTION.md         # 归属声明（全部版权归原作者，快照仅供学习对照）
    ├── kangarooking_*         # 毛选/巴菲特致股东信/段永平/穷查宝典/黄帝内经/第一性原理 6 仓
    ├── ace3000chao_book2startup
    └── shenqistart__book2skill
```

## 决策记录怎么读

decisions/ 按日期命名、正文带编号（D12–D24 已入库），每篇含四段：**背景 → 决策要点 → 落地与坑 → 后续义务**。挑几篇有代表性的：

| 编号 | 主题 | 一句话 |
|---|---|---|
| D12 | 投票主题聚合 | 35 个主题按交付价值合并成 16 个；矩阵派发时 `env -i` 会剥掉 API key 静默死亡 |
| D13 | 需求收集接口 | 自建轻接口：蜜罐+频控+token 鉴权管理页 |
| D16 | 满编矩阵上线 | 六节点同发的调度打法；scp 后必须验字节 |
| D17 | 工作手册引擎 | 六场线上可填写手册，一个静态引擎 + specs.js 规格 |
| D18 | 二期飞轮升级 | 一库一站一号：素材只写一次，进库→上站→分发到号 |
| D19 | 拆本站主线 | 二期拆的就是 chai.aibay.asia 本身：GitHub 安家→六模块 RIA 拆页→便签上站闭环 |
| D20 | fork 讲师站主线 | 学员直接 fork 源码仓五步安家：fork→clone→换装→推回→Enable workflows；最大坑=Actions 默认关闭 |
| D21 | 借工作流机制 | 从内部 loong-workflow 借五件纪律机制（规则文件化/写后回读/复测定性/证据真实/漂移防护）；索引 guard 首跑即抓出 D17/D19 撞号与幻影索引行 |
| D24 | 全量校对轮 | 四执行位并行校对 18 错落刀；教训=派发前基准必须对齐最新决策（附 D 编号），多源冲突用 git -S 考古定谳 |

## 复盘与手册的价值点

- **复盘不写「下次小心」**，写具体守则：如 Navbar 事故沉淀为「改有序数组必须整表替换 + path 唯一性断言」。
- **手册是可执行的 SOP**：打印材料手册里连「root 跑 headless chrome 必须 `--no-sandbox`」「PDF 验证用字节 cmp 而非字符串检索」都写成硬规则。
- **决策带后续义务**：每篇 ADR 的结尾是「后续谁改到相关文件时必须遵守什么」，档案因此保持活着。

## 脱敏与同步机制

- 本仓由内部 chai-workflow 仓**人工精选+脱敏**后同步（非镜像）：剔除 pending 未定稿与内部语料；IP/端口/凭据/个人邮箱替换为 `SERVER_IP` / `GITEA_INTERNAL` / `GIT_AUTHOR` 等占位符。
- 同步义务：内部仓新增 decision/retro/playbook 且定稿后，应在下次同步时精选入本仓，并同步更新 `docs/PROJECT-OVERVIEW.md` 的文档索引。
- `external/` 为一次性 vendor 快照，不追上游版本；版权归原作者（见 ATTRIBUTION.md）。

## 取用方式

- **办自己的工作坊**：PROJECT-OVERVIEW 看六场结构 → D18/D19 看单场怎么设计 → print-materials 手册看材料怎么产。
- **做 AI 技能包**：external/ 里 8 个同行仓是「把书/思想拆成可下载 Skill」的完整参照系。
- **研究 RIA × AI**：D19 的「六模块拆页 + 便签上站」是把拆书法移植到拆软件/拆网站的完整实例。

## License

MIT（`external/` 内容版权归原作者，仅快照对照学习）。
