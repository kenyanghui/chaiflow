# 2026-11-01 经典拆页全量同步（chaishubang 源头 → chai.aibay.asia/hot）

## 目标与结果

把 /hot 经典拆页从 69 本精选升级为源头 chaishubang.com 全量：**2255 书 / 19262 拆页全文**，
两级懒加载架构上线，线上全链路验证通过。

## 架构定稿（教训驱动）

### 两级懒加载数据流
```
bundle（808KB）只带精选 69 本 meta 切片 src/data/hotBooks.js（兼容旧引用+仓颉默认输入）
   ↓ 超出部分按需
/hot/index.json（190KB 全量书目索引）→ /hot/books/<id>.json（书 meta+拆页列表，未压缩）
   ↓ 点开拆页才拉
/hot/memoirs/<memoirId>.json.gz（拆页全文，gzip；fetchJSON 里 DecompressionStream 透明解压）
```
- bundle 曾从 115MB→4.1MB→808KB 三轮瘦身：**不要把语料打进 bundle**，兼容切片只留 meta。
- books/*.json 保持未压缩（页面主路径，减少一次解压失败面）；memoirs 用 .gz，前端带
  `.gz` 失败回退 `.json` 的双兜底。
- 拆页正文 HTML→纯文本在**构建期**完成（build-hot-data.mjs 的 htmlToText 保留段落换行），
  渲染层不处理 HTML。

### 关键路由决策
- 拆页路由 id 化（`/hot/book/:id`、`/hot/memoir/:id`），旧 title 链接靠 index 反查兜底。
- 精选书 id 与源头一致；例外：认知觉醒旧站 id=0 源头已无，用 curated-legacy.json 全文兜底。

## 爬取纪律（chaishubang API）

- 端点：`/pea/getPageBooksByWhile.do`（分页参数是 **pn** 不是 page；pageSize≤50）、
  `/pea/getPageMemoirsByWhile.do`、`/pea/getMemoirById.do`；匿名即可，登录态不多给字段。
- 礼貌限速 0.4s×4 线程，50 分钟爬完 2255 书 19262 拆页，全程无封禁。
- **脱敏必须做在入库前**：源头 user 对象嵌 bcrypt password 哈希/remember_token/email，
  STRIP 集合：password/remember_token/email/weixin_code。凭据登记 koningyang/ops（不入对话摘要）。
- 爬虫带 checkpoint（文件存在即跳过），中断重跑安全。

## Pages 部署三个坑（本次新增）

1. **`public/<dir>/` 只有数据文件时，目录 URL 会被 Pages 回退成裸 JSON**：
   `/hot/` 直接返回 index.json 内容（638KB 裸 JSON 而不是页面），且不报错——
   **凡是 SPA 路由挂在目录路径下，必须在 public 放同名 index.html 跳板页**（本次修复 5c0d435a），
   同时把路由规范化 `/hot`→`/hot/books`，内部链接直指规范路由。
2. **深链 404 是正常的**：Pages 按文件找，找不到回 404.html（= index.html 副本），
   SPA 接管渲染。验证时看 content_type=html + body 有 `id="root"` + bundle hash 对不对，
   不要只看状态码。
3. **Pages push 大仓（19k 文件 165MB）会 408**：`git config http.postBuffer 524288000
   http.lowSpeedLimit 0 http.lowSpeedTime 999` 后重推即过；数据仓同理但建议 raw/generated
   分仓或拆 commit。

## 线上验证清单（/hot 全链路）

- `/hot/` → 200 text/html 跳板页（302 到 /hot/books）
- `/hot/books` → 200 html + id="root" + bundle hash 与本地 dist 一致
- 深链 `/hot/book/0`、`/hot/memoir/10000` → 404+html（SPA 兜底）
- `/hot/stats.json` → `{"totalBooks":2255,"booksWithMemoirs":1713,"totalMemoirs":19262}`
- 书 JSON 按字节比对本地（893213B）——本机到 Pages 网络抖动多，**大文件必须按 expected size
  重试到一致再 parse**，否则截断的 JSON 会误报字段缺失
- gz 懒加载：memoirs/20173.json.gz `gzip -t` + 解压出 texts/topic/quote 全有值

## 产物位置

| 什么 | 哪里 |
|---|---|
| 站点仓 | kenyanghui/chaishu（f3268681 数据 + 5c0d435a 修复） |
| 数据仓 | gitea kenyang/chaishu-hot（raw+generated+scripts，c02706c7） |
| 收官管线 | /root/chaishu-hot/scripts/finish-hot.sh（build→sync→仓颉→skills→构建→push 一键） |
| 仓颉语料 | pipeline-cangjie.js `--corpus`（全量 gz）/ 默认精选 123 skills；update-skills.js 同源语料加载（58 包/152 技能） |
| 站点 skills | .claude/skills 234 个 |

## 增量：封面全量自托管（2026-11-02，站点 78b5e100 / 数据仓 covers/）

- **源头封面三种态**：OSS 直链 770（可用）；weserv 代理 1369（**全部 404**，该代理服务对豆瓣源的转发已死——需从 query 解出豆瓣 s-id 直下）；豆瓣直链 90（可用但必须带 `Referer: book.douban.com`，否则 418）。
- 下载器：4 线程 + 0.22s 全局限速（curl 串行节流锁），统一 ≤480px JPEG q82（65MB/2229 张）。OpenLibrary ISBN 兜底 0 成功（中文书覆盖率差，别指望）。
- 26 本不可恢复（豆瓣源已删）：前端 onError 三级回退链 兜住——本地 `/hot/covers/<id>.jpg` → `imageFallback`（远程原 URL）→ placehold.co 标题占位。
- **顺手修的结构问题**：
  - index.json 瘦身到列表页真实消费面 8 字段（190KB→…+gz 174KB）；详情字段（publisher/pubdate/isbn/url/intro）只留 books/<id>.json——**bookFull 必须与 index 解耦**（原实现从 index 展开，瘦身会串味），独立 bookMeta()。
  - 列表页代码本就优先拉 `index.json.gz`，之前一直静默 404 回退——补上 gz。
  - build 脚本 CRAWL 默认路径 /tmp→数据仓 raw（/tmp 已清）。
- sync-data-repo.sh 增量纪律：CRAWL 不在则跳过 raw（仓内已有全量）；covers 用 rsync --delete 归档（重爬成本高）。
