# D12：投票主题聚合改版——按交付价值合并，LoongBuddy 优先（2026-11-01）

## 背景
owner 指令：多个同类软件合并成一个主题，竞品可放一起，关键是「交付价值相同、学员导向目标一致」；连接器优先级 LoongBuddy（腾讯 Octop 项目，25 连接器）> workbuddy；热点需求上网调研后纳入；「上矩阵，跑！」并行执行。

## 决策
1. **聚合原则**：主题按交付价值分簇，不再按软件名开卡。旧 35 主题 → 新 16 主题，六类：赚钱·盯盘投研（3）/ 上班·办公一条线（4）/ 认知·知识产线（3）/ 生活·出行账本（4）/ 科研·文献综述（1）/ 做生意·尽调风控（1）。
2. **竞品合并进同簇**：如 飞猪+携程问道+美团+百度地图+滴滴 →「AI 行程规划与出行代办」；通达信/同花顺/东财/雪球/Level-2/科创北交/缠论/龙虎榜/打新 →「AI 盯盘与自动复盘」。desc 里写「——XX/YY 任选」。
3. **平台徽章**：`platform: 'loongbuddy'`（10 个，全部工具在 Octop catalog 内）→「⚡ LoongBuddy」黑徽章；`'need'`（6 个，证券类等）→「连接器待补」灰标，票高立项补连接器。数据字段进 voteThemes，SupportCard 双徽章渲染。
4. **文案双平台口径**：「默认 AI 平台 workbuddy」→「优先平台 LoongBuddy（25+ 官方连接器），workbuddy 同步支持」；补「同类软件已合并为一个主题，开课时用你手头那款」。
5. **热点纳入（矩阵调研产出）**：周报日报、汇报 PPT、多维表格中枢、AI 笔记 Wiki、AI 记账、AI 求职 6 个新主题；金融 MCP 可溯源并入投研主题。
6. **弃用**：策略回测/因子挖掘（门槛高不符受众）、RAG 独立主题（并入团队知识库）、AI 比价（热度弱）。

## 矩阵执行记录（上矩阵第三实证）
- 派发：xuan/hermes/kma 三路。**xuan、hermes 的 opencode 免费池额度耗尽**（part 落「⚠️ Free limit reached」+ watchdog-stale 收尾，此前 3 分钟零 part 判据升级为：看最后 text part 内容）。
- **kma 独活**：免费池同样耗尽，但 kma 引擎是 DeepSeek（DEEPSEEK_API_KEY），`-m deepseek/deepseek-flash` 可用。
- **⚠️ 派发大坑**：`env -i` 剥环境会把 `DEEPSEEK_API_KEY` 一起剥掉 → nohup 进程静默死亡（run2.log 0 字节、无 part）。正确姿势：**保留完整登录环境，只 `unset` OCTOPUS_* 变量**。冒烟验证必须与真任务同环境（前台测试带 env 所以能跑通，nohup env -i 却死，勿被前台成功误导）。
- 产出：`/root/matrix-tasks/hot-needs-research.md`（15.4KB，5 域 × top5 热点 + 证据链接全 200 回查 + 15 候选），本机存档 /tmp/octopus/aggregation/hot-needs-research.md。

## 实现
- workshops.js：voteThemes 整块重写（ef72fe6）；Workshops.jsx：SupportCard 徽章区 + 投票说明文案。
- 构建 241ms 过；推送 61aafac..ef72fe6；Actions success；dump-dom 验证：7 新关键词命中、LoongBuddy×12、连接器待补×6、旧文案清零。
- 工作树混入并行 03 期材料改动（public/workshop/03/），**只 add 本次两个文件**，不混提。

## 遗留
- workbuddy 连接器清单无本地源（/tmp/octopus/workbuddy.git 仅公众号技能仓），本轮回落用旧 voteThemes 工具名兜底；待 owner 提供源仓后再校徽章。
- 证券 6 簇连接器待补：票数高则立项（对应 Octop/LoongBuddy 补连接器）。
- 旧卡 id 弃用换簇 id（c-*），localStorage 旧票数不迁移（站点 10-31 才上线，损失可忽略）。
