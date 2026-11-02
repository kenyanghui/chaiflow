# D17 · 海报 PDF→PNG 化（六场换装）

- 日期：2026-11-02
- 状态：已上线（双仓 b62ad92 / dfa7fc70，六场线上 PNG 全 200）

## 背景
活动海报页 `.poster` 宽 760px，自然高度 2720–3024px（root 场 2720、05 场最高 3024），远超 A4 单页（≈794×1123 @96dpi）。Chrome 打印按 A4 分页，海报被硬切成 3 页，底部内容断裂。

## 决策
海报场景放弃 PDF，改发**整页长图 PNG**（用户拍板）。其余打印材料（任务卡、手册等）仍走 PDF——它们本来就是 A4 排版。

## 做法
1. `google-chrome --headless --no-sandbox --hide-scrollbars --window-size=800,5400 --screenshot` 整页截图（窗口高 5400 > 内容最高 3024，无截断）。
2. PIL `ImageChops.difference` 对背景色取 `getbbox` 裁剪 + 40px padding，输出 `活动海报.png`（800×1202 ~ 800×3024）。
3. 双仓 dist 换装：删六场 `活动海报-A4.pdf`（gh 03 另删遗留 `poster.pdf`），放 `活动海报.png`。
4. 六份 dist `index.html` 重生成：PNG 条目置顶（橙底高亮），下接 12 份 PDF，标题改「打印版材料」。

## 关键事实
- **站点序≠材料序**：root↔01-ima知识库、gh 02↔02-github网站、**gh 03↔04-企查查**、**gh 04↔03-知识星球**、gh 05↔05-Harness、gh 06↔06-AI手机。
- root 场 dist 真实路径是 `public/workshop/dist/`（无 `root/` 子目录）——脚本里 root 需特判。
- 二维码是 `.frame` 文字占位框（无 canvas/img 外链），截图安全。
- gh 副本 index.html 与材料仓源差 fb-card 反馈表注入块（D14），同步时勿整拷 index.html。
- root 场 Chrome 截 PDF 必须 `--no-sandbox`，截图同理。

## 产物
- 生成脚本：/tmp/octopus/poster/{crop.py,gen_index.py}（会话暂存，未入仓）
- 六场 PNG 源：/tmp/octopus/poster/活动海报-{root,02..06}.png
