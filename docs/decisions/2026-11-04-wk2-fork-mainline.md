# D20 · 二期操作主线定稿：fork 讲师站（2026-11-04）

## 背景

D19 定了「二期拆的就是 chai.aibay.asia」，但操作层仍留悬空：学员从零建 generic 站看不到全貌，讲师站成品无法直接带走。用户定稿：**操作主线改为 fork 讲师站 chaiAI**——学员经 WorkBuddy 把源码仓 chaiAI fork 到自己 GitHub，用 rsi 技能控制信息流/改功能，ima+公众号联动不受影响。看的站=fork 的站=拆完拥有的站。

## 决策要点

1. **fork 而非从零**：fork 一步得到整条产线（六大模块、工作坊详情、材料回看、每日巡检 Actions）；从零最小站保留为 rsi SETUP 路径 B，不再上课堂主线。
2. **五步安家口径**（替代原六步）：fork → clone → 换装（「把站换成我的」）→ 推回 → Enable workflows+验收；上线网址=用户名.github.io/chaiAI。
3. **换装红线**：第一周只改数据文件（workshops 数据、people 数据、页面 title、关于页文案），组件骨架不动；联动凭据在本机 ~/.config/，fork 不破坏。
4. **rsi 仓 v3**：fork_chaiai.py 五步向导 + fork-chaiai.md（红线/上游同步/坑表）；SKILL 路由表首行挂 fork，触发语「fork 讲师站/把站换成我的/clone 我的 fork/推回我的 fork」。
5. **课件+网页同步范围**：材料 02 六步表整表换五步、成品 box 改「你 fork 的就是讲师站本尊」；07 GitHub 行、index 第 1 节、PPT 第 12 页（notes 含 Actions 默认关闭最大坑）与第 27 页；网页 workshops 标题/摘要/交付物/适合人群 + 共创页联动措辞。

## 落地与坑

- 三仓全部推送且线上验证：材料仓与站仓 Actions success；材料 02/PPT fork 关键词命中；首页与 workshops 页 dump-dom 新口径命中、「一库一站一号/素材只写一次/my-site/六步」全量清零。
- **fork 最大坑：Actions 默认关闭**，推回后必须手动 Enable workflows，否则 Pages 不更新——五步表和 PPT notes 都显式写了。
- 项目 vite base '/chaiAI/' 已配好：仓不改名就不用动；若改名需同步 base 与 Router basename，写进 fork-chaiai.md 坑表。
- SPA 文案验证必须 chrome headless --dump-dom（curl 拿到的是空壳）；静态材料页与 SPA 详情页是两个对象，别验错。

## 后续义务

- 02 场材料/网页若再改，五步口径以本决策为准；rsi 仓 SETUP 与材料 02 保持逐字一致。
- 讲师仓上游更新时，学员 fork 用 upstream remote 同步（fork-chaiai.md 已写方法）。
