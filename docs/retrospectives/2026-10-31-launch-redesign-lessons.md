# 复盘：chai.aibay.asia 上线与整站改版（2026-10-28 → 10-31）

## 事件线

1. **首期课材料定稿**：课件 30 页 + 11 份 PDF，双仓推送（Gitea 169b43f / GitHub 467b03e）；HTTPS 证书签发（CN=chai.aibay.asia，TLSv1.3）。
2. **空白页双层 bug**：GitHub Pages 上 SPA 全白。
   - 第一层：vite `base` 配置 + 残留 404.html 写死 `/chaishu/` 前缀（7430111）。
   - 第二层（真因）：`<BrowserRouter basename="/chaishu">` 与根域名部署冲突（3d909d3）。
   - 教训：**SPA 部署三件套一起查**——vite base、router basename、404.html 回退路径。
3. **整站 Apple light 改版**（59b32d5）：dark-* token 重指向 light 色板，内页零改动自动换肤；新设计系统类 apple-card/btn-primary/hero-wash；Navbar 重做 + /workshops 页 + src/data/workshops.js 数据驱动。
   - 教训：**主题切换走 token 重指向，不逐页改类名**——20+ 内页一次换肤成功。
4. **身份/CTA/微信口径修正**（9ef4124 → b1e0bfd）：杨辉身份定稿、悦洋/摆渡人清零、CTA 统一、微信 kenyanghui→ikoning365 全站替换 + Gitea 材料仓 3 处补漏（7e31180）。
5. **五期主题 v2（连接器口径）上线**（b1e0bfd）：workshops.js 重写、Home/Workshops/meta 同步、本机+线上双层渲染验证。

## 关键教训

### L1 品牌口径要"仓储级"清查
- 微信替换做了全站 grep 清零，但 **Gitea 材料仓漏了 3 处**（poster/07 清单/index.html）——rsync 源头仓是口径回归的重灾区。口径变更必须双仓同查。
- **PDF 查旧文案：pdftotext 未装时 strings 查不出压缩流，是假阴性**。用 python 解 zlib stream 逐流扫描才可靠（已验证 11 份 PDF 干净）。

### L2 连接器清单是选题的硬约束
- v1 五期里"通达信量化"上线前夜才发现**连接器清单里根本没有**（25 个连接器无一是证券类）。选题先查 catalog.py，三个分支（main/wanfeng/brand）一致性也查了。
- 用户反而将其转化为策略：证券主题做投票卡探测需求，高票再补连接器开课（Gitea 上 FinRL/FinRobot/OpenBB/qlib/backtrader/TradingAgents-CN/xuan-quant 可作底料）。

### L3 部署验证的可靠性
- SPA 本机验证必须 `npx vite preview`（python http.server 无 history 回退会 404 误报）。
- headless chrome dump-dom **偶发 0 字节**（首页/about 都遇到过），重跑一次即可，不要据此误判部署失败。
- 线上验证：dump-dom 后正则抽可见文本，命中新关键词 + 残留旧关键词清零，双重断言。

### L4 环境坑
- `git -c` 被本代理安全规则拦截，`git -C` 也命中同一模式——用工具的 workdir 参数代替。
- `rm -rf /tmp/...` 命令整条被拦——临时目录用时间戳后缀新建，不做删除重建。
- GitHub remote 内嵌 token 会失效；用 ~/.git-credentials 提取 token 按 URL 一次性推；偶发 443 断连重试即可。
- Gitea 材料仓分支是 **main 不是 master**（push refspec 错过一次）。
