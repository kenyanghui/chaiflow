# D27 · 跟做手册图文并茂：实景截图产线与登录墙探针

- 日期：2026-11-08
- 状态：已定稿（6 张实景截图上线 chaiAI@5f6e74f7，Actions success+线上 6 图全 200；二期矩阵任务当晚跑）
- 范围：chaiAI 仓 `public/workshop/{,02/}guide.html` 手册配图；范式可复用于一切静态站手册

## 背景

两册跟做手册（01 存理用 / 02 建站）460+ 行纯文字，学员对照界面找按钮费劲；owner 定「图文并茂 + 上矩阵跑」。站内 `/public/screenshots/` 只有 9 张模块图（About 用），手册 0 配图。

## 决策要点

1. **配图分两类**：实景截图（匿名可访问的公开页：工具官网/仓库页/已上线站点）+ 示意图（登录墙内页，HTML/CSS 仿界面画）——登录墙页匿名硬拍全是 Sign in 墙（实测 fork 页 DOM 含 16 处 Sign in），必须改画。
2. **实景产线**：`google-chrome --headless --disable-gpu --no-sandbox --hide-scrollbars --window-size=1440,900 --screenshot=…`。
3. **插图前先验内容**：`--dump-dom | grep -c "Sign in"` 探登录墙；PIL 采样平均亮度（≈255 即空白页）；`file` 验 PNG 头。
4. **figure.shot 插图范式**：CSS 三行内联进册 `<style>`（圆角边框+figcaption 灰底），img `loading=lazy`，figcaption 一句话图注——口径与步骤文案严格一致，不发明新口径。
5. **示意图诚信红线**：必带「示意图·非实际截图」水印、不用真截图冒充、不仿品牌 logo（文字站名代替）、界面文案只演绎手册已有步骤。

## 落地与坑

| 坑 | 现象 | 对策 |
|---|---|---|
| 远端截图拍空 | 远端 URL 产出 0 字节且进程不报错（静默失败） | 必加 `--disable-dev-shm-usage`，实测一发命中 |
| vtb 害远端 | `--virtual-time-budget` 虚拟时钟快进，远端页拍到空壳 | 该参数只对本地 file:// 用 |
| github DOM 抖动 | dump-dom 多次 0 字节后突然成功 | 重试+换渲染参数，别判页面坏 |
| 改了没生效 | guide 是纯静态 HTML 不进 vite 构建 | 直接改 `public/workshop/**` 即生效；guide 无 PDF 版，handouts 有（改后必须 headless --print-to-pdf 重产） |
| 长页截图 | 页脚整页 2600px 太高 | 先拍全页再 PIL crop 到目标区 |
| 截图上线静默坏 | 0 字节文件若推上线即破图 | 上线前逐张 curl 200 + 字节数对账 |

## 后续义务

- 后续手册/课件配图沿用本产线与 figure.shot 范式；示意图水印红线不可让步。
- 二期（F1 全项复核+S1-S3 三张登录墙示意图+R1 汇聚插图）任务卡在内部 loong-workflow `runs/guide-illustrated/`，REPORT 落地后回填本篇状态。
