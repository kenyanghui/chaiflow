# 2026-11-04 拆搭子（chaibuddy）上线与 chailive 模块化改版复盘

## 目标与结果

三条线一天内完成并线上验证：

| 线 | 交付 | 结果 |
|---|---|---|
| chailive 模块化 | 31 章→6 兴趣模块（09f7226） | 卡片对账 19262 平，四视图 hash 路由上线 |
| chaibuddy 找搭子 | /hd-gallery 更名升级（6430f510…90f363e3） | 83 分舵 5473 拆书家名录+标签→六模式推荐+弹窗牵线 |
| 命名收敛 | 导航「共拆AI」→「拆搭子」（bc356ffb） | 徽章去拆书帮内部级别（Lv.N） |

## chaibuddy：把「名录」变成「能自我匹配的合作入口」

### 从 API 摸黑到全量采集 30 分钟
- 官网是 SPA，端点不在页面里——**下载 main bundle grep `"/pea/xxx.do"` 一次性挖出全部 113 个端点**，
  再从调用上下文读参数名（pageSize 驼峰、rudderId 必填，参数错返回中文「传入参数为空或非法」而不是 40x）。
- 采集面：`getAllEnableRudder.do`（83 分舵）→ 逐舵 `getPageUsersByWhile.do?rudderId&pn&pageSize=200`，
  0.5s 限速 3 分钟零失败。**去重必须在采集层做**：同一人在多舵出现（筹备舵+正式舵），按 user.id 全局去重 5473。
- 字段质量：email 100%（后端回显）、weixin 81%、description 仅 46%——**desc 是唯一兴趣源**，
  p50 长度为 0，标签提炼只能在 2529 人上做，接受这个覆盖率而不是硬造标签。

### 标签与推荐：确定性规则引擎，不上 LLM
- 27 类职业/兴趣标签纯关键词匹配（构建期一条 Python，可复跑可审计）：1325 人有标签，1224 人有推荐。
- **推荐必须指向真实资产**：六种合作模式各对应站内一个在跑项目（六场课件/拆专家工坊/WorkBuddy/chaiflow/chailive/信息图），
  每张卡带 href——推荐不落地成链接就是空话。
- 文案同源纪律：MODES 常量在 build_buddy.py（进 people.json 的 meta）与 Chaibuddy.jsx 各有一份，
  **改文案必须两边同步**，这是已知债；更好做法是构建期从单一源生成。

### 隐私与分寸（对外展示他人数据的红线）
- **发布版打码**：email/微信只留前2后2（`fe***@163.com`），防批量爬取骚扰；明文原始层只留本机 /tmp 不入仓。
- **不展示拆书帮内部级别**：Lv.1-4 是其会员体系，第三方站点展示等级既不准确也越界——统一为「认证拆书家」副行说明，
  主标签位让给本人职业/兴趣标签（全员都是拆书家，该信息零区分度）。
- 联系闭环不绕过站长：精确联系方式引导回官网查询或走牵线表单，由本人自愿留联系方式。

### 牵线弹窗：复用而非新建后端
- needs API（api.aibay.asia/needs）在第三方网关机不可改——但字段是自由文本，
  **映射复用**：software=【拆搭子牵线】姓名（分舵）、scene=模式+标签、expect=留言、contact=联系方式。
  提交前先用真实 payload 打一次探针确认字段兼容（ok:true mailed:true），别看文档上线。
- 表单体验：预填（名片进入自动带名字/分舵/推荐模式默认勾选）+ 校验（联系方式必填≥5字符）+
  **mailto 双通道**（网络失败/偏好邮件一键回落，mailto 链接同样预填全文）。
- 底部 CTA 同步换入口，搜索无结果的空态也引导到同一弹窗——所有「想聊」的出口收敛到一个表单。

## chailive 模块化：上加一层，不动底层

- **归组层方案**：31 章 ID 与 book_chapters 归类数据零改动，只加 modules.json（6 模块定义），
  build_cards.py 派生 CHAI_MODS 并 fail-closed 对账（每章恰归一模、sum=19262 不平即 sys.exit）——
  避免 19262 卡重跑 LLM 归类，改模块只动一个文件。
- 键值与文案分离：模块 hook 句、章名人话化都在 JSON 源里，管线全自动派生，页面零硬编码。
- 旧首页是 31 章平铺流，移动端一眼看不到分类——四视图 hash 路由（home 6 模块入口默认页/#m-mod 连读/
  #c-ch 单章带下一章/#all 全量带模块带）后，**入口页从「内容流」变「分类门」**，深链可分享。
- DOM stub 冒烟（18 断言）先于部署：四视图各断卡片数实算，别等线上发现路由错。

## 部署与验证坑（本次新增）

1. **SPA 路由与 public 真实目录撞名**：`public/chaibuddy/`（放 people.json）使 nginx 把 /chaibuddy
   301 到 /chaibuddy/ 再落 404.html 兜底——**微信分享卡片对 404 敏感**，build 加
   `cp dist/index.html dist/chaibuddy/index.html` 让路径直接 200。凡 SPA 路由下挂真实数据目录都要查这一条。
2. **大文件+抖动网络的验证法**：3.5MB+ chapters.js 全量抓取反复断——改 **HEAD content-length 比对本地字节数
   + Range: bytes=0-16383 抓头部 grep 标记**即可证新包；小文件仍 sha256 全量比对。别跟抖动网络硬刚全量下载。
3. **GitHub push 偶发 `Failed to connect`/`Failure receiving`**：一律 for 循环×sleep 20 重试，
   别手动单发；同会话 curl 也偶发 000/SSL 35，逐文件独立重试。
4. **React 19 lint 的新规矩**：`useEffect 里同步 setState`（set-state-in-effect）报错——
   筛选重置页码这类改事件驱动（onChange 里 setPage(1)），导航收起菜单同理点击时收。

## 产物位置

| 什么 | 哪里 |
|---|---|
| chaibuddy 页 | kenyanghui/chaishu src/pages/Chaibuddy.jsx（6430f510→90f363e3） |
| 名录数据 | 同仓 public/chaibuddy/people.json（1.07MB，5473 人，打码版） |
| 采集/构建脚本 | /tmp/octopus/csb/{crawl_all,build_buddy}.py（仓外工具，重跑即刷新数据） |
| chailive 模块化 | kenyanghui/chailive 09f7226（modules.json+build_cards.py+template-living.html） |
| 牵线邮件通道 | api.aibay.asia/needs/needs（复用 Workshops 需求表单后端） |
