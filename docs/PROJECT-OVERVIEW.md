# 拆AI工作坊 · 项目全景（SSOT）

> chai.aibay.asia 是「玄龙·拆AI」工作坊课程阵地。本仓（chai-workflow）继承 Loong/loong-workflow 的 core 工作流语料，作为拆AI工作坊项目的经验与口径唯一权威源。
> 更新时间：2026-11-01（六场全上线 + 需求/反馈表单邮件化）

## 一、项目定位

- **品牌**：玄龙·拆AI（讲师：杨辉 / 笔名玄龙，玄龙堂主理人 · 玄龙系统开发者）
- **主张**：不强调"拆书"，强调"拆"——拆 AI 软件、拆 AI、拆为己用。当场拆、当场接、当场跑通，带走自己做出来的东西。
- **受众**：初级学习者、想真正用起 AI 的人（原口径"初级拆书家"随品牌敏感性调整收缩，见 decisions/2026-10-31）
- **视觉**：Apple light 风格——#fbfbfd 底、#0071e3 蓝、SF Pro 字体栈、毛玻璃导航、980px 胶囊按钮
- **商业闭环（内部逻辑，不对外强调）**：默认 Agent 平台是 **workbuddy**；工作坊拆的软件都在 workbuddy 连接器清单内 → 跑通的工作流未来平移到 loong AI 定制手机，变成随身数字员工。

## 二、仓库拓扑（勿混淆）

| 仓库 | 位置 | 角色 | 最新（2026-11-01） |
|---|---|---|---|
| `kenyanghui/chaishu`（GitHub） | /root/gh-chaishu | **网站源码+部署仓**（React/Vite，GitHub Pages） | 0f6b06b（反馈表注入；需求邮件 5cbd66c） |
| `kenyang/chaishu`（Gitea GITEA_INTERNAL） | /root/chaishu | **课程材料仓**（按期分目录：01-ima知识库/02-github网站/03-知识星球/04-企查查/05-Harness工作台/06-AI手机/assets） | 18a5a5f |
| `kenyang/chai-workflow`（Gitea） | 本仓 | **项目工作流/经验 SSOT** | — |

- 两仓不是 rsync 镜像：网站改版只落 GitHub 仓；材料修改两边都要核（材料以 gh 仓 public/workshop/ 副本发布）。
- 线上：chai.aibay.asia → CNAME → kenyanghui.github.io（HTTPS/TLS1.3 正常）。

## 三、对外口径（当前有效）

- **微信**：ikoning365（业务微信，全站统一）；**邮箱**：554176937@qq.com
- **报名优先级（v4，dd76318）**：拆书帮公众号链接 `mp.weixin.qq.com/s/4lIyWBUPOFqsNlyJNd1K-Q` 为第一渠道，微信为辅助；口径不写「第 N 期」，统一日期化（首场「11 月 1 日（周日）14:00 · 报名中」）或「11 月排期中」；投票卡角标「我支持 N」（点击只涨不限次）
- **CTA**：统一「报名工作坊」（不写"报名第 N 期"）
- **讲师身份**：玄龙堂主理人 · 玄龙系统开发者；头衔仅留：混沌学园 AI 创新领教 / 国际人工智能产业联盟首席生态官 / 企业AI FDE教练
- **已清除**：悦洋海外集团首席人工智能官、"AI 摆渡人"、"与 aibay Loong 底座/LoongBuddy/AI 手机业务同源"对外叙事
- **拆书帮表述（2026-10-31 定稿）**：拆书帮（chaishubang.net）给了本工作坊方法论支持，**要尊重**——统一用致谢式「方法论支持：拆书帮（chaishubang.net）」；禁用的只是"同源/业务捆绑"类攀附表述，不是删名（详见 decisions/2026-10-31 D1）
- **栏目命名（v5，954e0e2，2026-10-31）**：成长路径（/learning-path）/ 经典拆页（/hot）/ 技能萃取（/skills）/ 拆书赏鉴（/hd-gallery）——旧名（学习路径/书库/技能卡/高清图）全站禁用；命名 rationale 见 decisions D8（拆书价值视角 + 拆书词族 + 管线闭环：拆页输入→技能萃取→赏鉴呈现→成长结果）
- **版权行（8009ac0）**：© 署名统一「杨辉（玄龙堂主理人）」；light 站内对比度纪律见 decisions D7

## 四、工作坊主题演变

| 版本 | 口径 | 状态 |
|---|---|---|
| v1 | 五期：知识库→网站→获客→内容→通达信量化 | ❌ 通达信无连接器，废 |
| v2 | 五期连接器口径：ima / 微信读书·文档·邮箱 / 会议·飞书·滴答 / 企查查·企微 / 飞猪·携程·美团·地图，口号"从知识库到数字员工" | 已上线（b1e0bfd） |
| v3（已上线，fb860bc，2026-10-31） | **开放式主题工作坊**：01 ima 知识库（报名中）/ 02 GitHub 网站·workbuddy 工作流 / 03 企查查 / 04 知识星球；其余 **36 个主题心心投票卡片**（证券 14 + 办公 6 + 知识 6 + 生活 6 + 数据 3，localStorage 计数起步），票高先开 | ✅ 线上验证过（三页断言） |

**关键事实（workbuddy 连接器清单核查 2026-10-31）**：
- catalog（/root/workspace/Octop/src/octop/infra/connectors/catalog.py）25 个连接器，main/wanfeng/brand 分支一致。
- **无任何证券类连接器**（无通达信/同花顺/东方财富/雪球；yuandian"元点"仅有股票简称查企业字段，属企业数据类）。
- 知识星球（zsxq）不在清单；GitHub 不在清单（但 GitHub 类 workflow 走 git 生态不需要连接器）。
- 结论：证券主题投票卡是**需求探测**；若票高，需先在 workbuddy 侧新增证券连接器再开课（Gitea 已有 FinRL/FinRobot/OpenBB/qlib/backtrader/TradingAgents-CN/xuan-quant 等证券仓库可作技术底料）。

## 五、首期课既定口径（勿动）

- 2026-11-01（周日）14:00–17:00，广州越秀区雅苑·培正 5 号楼
- 非会员 39 元（含茶歇+资料）· 会员免费 · 仅限 10 人
- 材料：30 页课件 + 11 份 PDF（01 学习地图 … 09 自评量表 + 海报 + 课件 PDF），已全量核干净（旧微信 0 残留）

## 五b、第二场课既定口径（2026-11-01 定档更新）

- **2026-11-08（周日）9:30–12:30**（上午场，9:15 签到），广州越秀区雅苑·培正 5 号楼，**12 人小班**（workshops.js wk2 已填 dateISO/dateEndISO，到点自动翻转报名中→进行中→已交付）
- ⚠️ 旧口径「11 月 8 日（周六）14:00–17:00 · 10 人」作废——11/8 实为周日，原页错标周六已全站订正（站点 922ef6e / 材料仓 ff6d5c2，7 HTML+5 PDF）
- 对外名「GitHub 网站工作坊」/「AI 拆书课 · 11 月 8 日场」，不写「第二期」（D6 纪律）
- 三节结构 **安 → 跑 → 阵地**（复用第一期教学法骨架）：安 = GitHub 安家（五步 15′，交付① 个人网站）；跑 = workbuddy 自动产线（三步 19′，交付② 预览截图）；阵地 = 30 天计划（交付③）
- 验收红线：交付② 跑通到「新内容生成 + 站点更新预览」截图即算，真实对外宣传留课后；彩蛋 = 讲师个人网站模板仓
- 材料：29 页课件 + 海报 + 材料 01–09 + 入口页，全部落 `/root/chaishu/02-github网站/`，dist PDF 11 份已生成验证（定档后重打 5 份：01/07/08/海报/课件）
- 07 课前清单口径：GitHub 注册 + 邮箱验证课前完成（课上没时间现场注册）
- **PDF 重打坑**：root 跑 headless chrome 必须 `--no-sandbox`，否则静默失败（exit 0、旧文件原样）；PDF 文本流是字形索引非明文，验证更新用「新旧字节 cmp」而非字符串检索
- **dist 断链教训（14d8931 修复）**：gh 仓 `.gitignore` 裸 `dist` 规则把所有场次打印版 PDF 挡在仓外——线上「下载 PDF」一直是存量 404，且 `../dist/` 裸目录链接在 GitHub Pages 无目录列表也是 404。修复=gitignore 加 `!public/workshop/**/dist` 例外 + 补 02/04 场 dist + 三个 dist 目录生成 index.html；05/06 场 dist 链接指向 Gitea 仓不受影响

## 五c、第三场课既定口径（2026-10-31 定稿，材料仓待推）

- **时间待定**：对外一律「11 月 · 时间待定（报名后群内通知）」；站点 workshops.js wk4 statusLabel 同步待定，不写死日期
- 对外名「知识星球 · 私域知识变现工作流」，不写「第三期」（D6 纪律）；工具名只在徽章层露出
- 三节结构 **更 → 沉 → 续**：更 = 星球内容半自动产线（50′，交付① 帖子已发 + 截图 + 署名判断）；沉 = 精华沉淀与新人引导包（55′，交付② 置顶三篇 + 精华 2–3 类 + 引导帖）；续 = 续费提醒工作流（40′，交付③ 到期名单 + T–7/T–1/T+1 话术 + 流程截图）
- **CTA 纪律**：未发布场次不挂公众号链接，入口页一键复制微信 ikoning365（备注「知识星球」）
- 红线：不承诺「一夜涨粉 / 马上变现」；界面只写流程定位不写按钮名；彩蛋 = 星球运营素材包（选题 50 条 + 引导帖模板 + 话术模板）课后发群
- 材料：29 页课件 + 海报 + 材料 01–09 + 入口页，全部落 `/root/chaishu/03-知识星球/`，dist PDF 11 份

## 五d、站点场次详情页路由与双仓同步（2026-11-01 定稿）

- 路由：`/workshop/` 首期（ima 知识库）· `/workshop/02/` GitHub 网站场 · `/workshop/03/` 企查查场 · `/workshop/04/` 知识星球场；卡片链接统一走 `workshops.js` 的 `link` 字段，禁止组件硬编码单场地址。
- 无材料场次（企查查）只写站内场次数据已有字段（summary/outcomes/who），不虚构讲义/任务卡/交付物；页面不设空材料索引。
- 同步纪律：材料仓为源，gh 仓 `public/workshop/0N/` 为发布副本；口径改动两处同改并用 `diff -rq` 校验；改 HTML 必重生成对应 dist PDF（部署副本不含 dist）。
- 首次执行：02 期「11 月 8 日」→「11 月 · 时间待定」+ CTA 改微信 ikoning365，dist 11 份重生成（Gitea e965b10 / GitHub 911a8f8，详见 decisions D11）。

## 五e、第五场：DeepSeek Harness 企业自动化工作台（2026-11-01 上线，满编矩阵）

- 站点 /workshop/05/（课件 32 页 + 海报 + 材料 01–09）；材料仓 /root/chaishu/05-Harness工作台/（dist 11 份 PDF，5.5M）
- 工具只有 DeepSeek Harness + workbuddy；三节=搭(50′)→审(55′)→沉(40′)；三铁律=合成数据/AI 初稿人工确认/数据不出内网

## 五f、第六场：AI 手机生产力（2026-11-01 上线，满编矩阵）

- 站点 /workshop/06/（课件 31 页同构）；材料仓 /root/chaishu/06-AI手机/（dist 11 份 PDF，4.2M）
- **全场禁「福马/fuma/foma」及任何手机品牌词**（避免推销小公司嫌疑），统一「手机 AI/语音助手/拍照识别/录音转写」；三节=收(45′)→理(60′)→用(50′)
- 两场派发/验收/坑详见 decisions D16；workshops.js wk5/wk6 status 均 open

## 六、文档索引

- `decisions/2026-10-31-branding-and-themes.md` — 品牌敏感性与主题口径决策记录
- `decisions/2026-11-01-vote-themes-aggregation.md` — D12 投票主题聚合改版（35→16 按交付价值合并、LoongBuddy 优先徽章、kma DeepSeek 派发坑：env -i 剥掉 DEEPSEEK_API_KEY 静默死亡，正确姿势只 unset OCTOPUS_*）
- `decisions/2026-11-01-needs-collector.md` — D13 客户自助需求收集板块（api.aibay.asia/needs/ 自建轻接口、8193 端口、蜜罐+频控、管理页 token 鉴权）
- `decisions/2026-11-01-feedback-form.md` — D14 六工作坊课后反馈表（/needs/feedback 复用路由零 nginx 改动、SMTP 直发讲师邮箱、星级+三问+感谢态、mailed 标志+失败重试）
- `decisions/2026-11-01-demand-form-mail.md` — D15 需求表单邮件直达站长邮箱（smtp.qq.com:465+授权码、mail.json 热读可降级、出站 25 被封勘察、mailed 标志前端弹窗）
- `decisions/2026-11-01-matrix-full-court-05-06.md` — D16 五/六场满编矩阵上线（先切分六节点同发、xuan 死单改派 kma、E 块缺件 ssh 直打、scp 验字节、禁品牌词契约）
- `decisions/2026-11-01-workbook-engine.md` — D17 六场线上可填写工作手册（/workbook 静态引擎 + specs.js 六场规格 + /needs/workbook 复用 8193、导出 md、第 0 节 s0 可选）
- `decisions/2026-11-01-wk2-flywheel-upgrade.md` — D18 第二期升级一库一站一号飞轮（180′ 时间表、四交付物、分组组长五职责、共享材料 10/11 六场通用、A4 单页两个 CSS 坑）
- `decisions/2026-11-02-poster-png.md` — D22 六场海报 PDF→PNG 化（.poster 高 2720–3024px 超 A4 打印断裂，PDF 改 PNG 上线；编号史见文头：初版误编 D17，guard 抓出撞号重编）
- `decisions/2026-11-02-tf-assess.md` — D23 过级自评表 /tf-assess/（评分表正确形态是可填写不是陈列、复用 workbook 引擎四 Level×三档；编号史见文头：初版误编 D19，同批重编）
- `decisions/2026-11-04-wk2-fork-mainline.md` — D20 二期操作主线定稿 fork 讲师站（fork→clone→换装→推回→Enable workflows 五步、Actions 默认关闭坑）
- `decisions/2026-11-04-wk2-chai-site-teardown.md` — D19 第二期主线定稿「拆本站」（GitHub 安家→六模块 RIA 拆页→便签上站闭环、材料 12 新增、A4 单页并入式加内容教训、SETUP.md 与材料 02 逐字一致义务）
- `decisions/2026-11-04-borrow-loong-workflow-mechanisms.md` — D21 借鉴内部 loong-workflow 工作流机制（规则文件化/写后回读/复测定性/展示真实性/漂移防护五件借、DAG 流水线不借；机制层落 rsi 仓 RULES+guards，档案层落本仓 retro 模板+索引 guard）
- `decisions/2026-11-04-wk2-proofread-matrix.md` — D24 工作坊材料全量校对（基准对齐先于派发：git -S 考古定谳时长冲突、交付物编号纪律、A4 单页加内容三步法、改标题全链路 grep 清零双验证；编号史：内部仓同决策编 D21）
- `retrospectives/2026-10-31-launch-redesign-lessons.md` — 上线与整站改版复盘（空白页、token 换肤、PDF 深扫）
- `retrospectives/2026-11-01-materials-trilogy-and-session-pages-lessons.md` — 三期材料收官 + 各场详情页 + 双仓同步复盘（假链接红线、口径三处一次到位、矩阵二实证）
- `retrospectives/2026-11-04-workshop01-card-authenticity.md` — 工作坊 01 指令卡失真复盘（聊天式三卡 vs 真实配置三步；立规：教人照做的指令卡 = 源资产蒸馏，上线前逐凭证名对账源仓）
- `retrospectives/2026-11-04-wk-guides-clone-surface.md` — 做站四轮调整复盘（六 guide 上线/wk2 钥匙版/指令卡化/资料区标题）：01 打回修正漏了 guide 克隆面；TEMPLATE LOOP 补「失真关键词全仓克隆面清点」项
- `retrospectives/2026-11-04-prompt-card-learner-first.md` — 指令卡三稿演进复盘（想象聊天卡→真实配置卡但步骤腔→owner 三句定稿）；立规：内容真实+形式最短，指令句先写学习者动线四步，「第一步/请验证」类句式禁入指令正文
- `retrospectives/2026-11-04-owner-final-wording-literal.md` — owner 定稿逐字落实复盘（越权顺带改卡②标题/脚注/首行被整笔回退）；立规：逐字定稿=最小落实面，周边一致性调整须先获批
- `retrospectives/TEMPLATE.md` — 复盘模板（五段式 GATE/SUCCESS/ACTION/LOOP/SAFE + 行动项四条硬约束：≤5 条/带文件路径/可度量/无指责）
- `playbooks/site-deploy-playbook.md` — 网站构建/推送/验证运维手册
- `playbooks/print-materials-playbook.md` — 打印材料 A4 单页（min-height 穿透 print、table 固定字号两个坑）+ 矩阵四块合入三处必改 + 双仓/dist 收尾清单
- `playbooks/humanize-titles-playbook.md` — 内容站章名人性化命名四范式（损失厌恶/划算框架/悬念反差/场景直白）+ 人写→模型二审→人工终判生产流（chailive 31 章实证）
