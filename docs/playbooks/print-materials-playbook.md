# 运维手册：打印材料 A4 单页与矩阵块合入

> 适用：`public/workshop/{,02..06}/handouts/`、`/root/chaishu/0N-*/handouts/`。目标：每份材料**打印出来正好 A4 一页**，材料仓与发布仓同源一致。

## 一、A4 单页的判定与压制

1. **判定用真实打印，不用目测**：`google-chrome --headless=new --no-sandbox --print-to-pdf=/tmp/x.pdf file://$PWD/f.html`，再数页对象 `python3 -c "re.findall(rb'/Type\s*/Page[^s]',d)"`。root 跑 headless 必须 `--no-sandbox`，否则 exit 0 但写出旧文件（静默失败）。
2. **只动 inline `<style>`，不动 `handout.css`**：共享样式一改六场全变，风险大。
3. **两个必踩的坑**（本次 08 卡了三轮）：
   - `.sheet{min-height:...}` 写在页面 `<style>` 里会**穿透 `@media print`**，把最后一页强行撑出来。要么只在 `@media screen` 里设 min-height，要么在 `@media print` 里 `min-height:0`。
   - `handout.css` 给 table 显式 `font-size:11.8px`，只缩 `body` 字号对表格无效。压页必须同时缩 `table`（如 `table{font-size:9.7px}`）。
4. **字号阶梯实测**：11.2px/1.4 可容 6 段表格（06）；10.9px/1.36 可容 7 段（07）；9.4px/1.32 + 文案精简才收得住最密的一页（08）。**先精简文案，再降字号**——降到 9px 以下手机上已不可读。
5. 每次改完**当场打 PDF 数页**，不要攒到最后；一页的判定包含「最后一页无孤行表格」。

## 二、矩阵块合入纪律（四块并行产出 → 单一主干）

1. **先审后并**：read 每份回传文件全文，对照 SPEC.md 校验口径（时间表、交付物、红线），再落仓。
2. **三处必改**（块产出天然带错）：
   - 路径 `../wk2handouts/xxx.html` → 同目录 `xxx.html`（落地目录已扁平化）；
   - 硬编码场次日期 → 站点真实日期（本次 11-08 周日；块里曾写错周六）；
   - 共享材料页眉 brand → 「六场通用 · 现场发」，不写单场名。
3. **拷贝到六场前先定「差异/共享」**：只有内容有场次差异的才复制六份；共享材料（10/11）复制六份但内容必须零差异，靠页眉声明通用。
4. **目录挂接双形态**：卡片式场次改 `.card` 列表并改「九件材料→十一件」；表格式场次（站点 03）加两行并改标题计数。改完 `grep -c` 复核条数。
5. **同步顺序固定**：材料仓源 → gh 仓副本 → 重生成两侧 dist PDF → 站点 build → 推送 → 线上逐 URL 200 + 关键文本命中。跳过 dist 重生成 = 线上 PDF 是旧版。

## 三、线上同构校验（打印版 ↔ 线上可填写版）

- 打印版改完必须回查 `public/workbook/specs.js` 对应场次：标题、节数、每节条目数、三栏列名、验收组数。两处不一致 = 学员纸面与线上填的不是同一套。
- specs 是手写数据，没有生成器兜底（`gen_workbook_specs.py` 只是初版机械解析）；结构改动（新增第 0 节）必须手改并 headless 渲染 `#0N` 断言关键 h1 出现。
- 真实提交一次（非 dry-run）验证 `mailed:true` + `mail.log` 有记录，才算端到端通。只测前端渲染会漏掉 SMTP/频控/表结构问题。

## 四、收尾清单

- [ ] 六场每份材料 PDF 页数 = 1
- [ ] 六场 index 材料条数 = 11，10/11 可点
- [ ] 六场 01 含「分组与组长」表
- [ ] 双仓 HEAD 一致内容、dist 已重生成
- [ ] 线上 11 链接全 200，workbook `#0N` 见第 0 节
- [ ] Actions 最新 run `conclusion=success`
