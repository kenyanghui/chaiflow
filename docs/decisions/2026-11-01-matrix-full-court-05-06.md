# D16：05/06 两场（DeepSeek Harness + AI手机）满编矩阵上线（2026-11-01）

> 与既往材料场（D11 三部曲）同构，但首次采用「先切分、六节点同时发起」的满编调度，且出现 xuan 双块死单、E 块缺件 ssh 直打两个新坑。06 场课件 31 页，05 场课件 32 页。

## 两场契约要点（历场通用口径 + 本场新增）
- 历场通用：禁「第 N 期」；「11 月 · 时间待定（报名后群内通知）」；广州越秀区雅苑·培正 5 号楼；仅 10 人；会员免费/非会员 39 元含茶歇；报名=拆书帮公众号优先+微信 ikoning365；拆书帮致谢式表述；light 白底（handout.css）。
- **05 场（DeepSeek Harness 企业自动化工作台）**：工具只有 DeepSeek Harness + workbuddy；三节=搭(50′)→审(55′)→沉(40′)；三铁律=合成数据/AI 初稿人工确认/数据不出内网。
- **06 场（AI 手机生产力）**：全场禁「福马/fuma/foma」及任何手机品牌词（owner：避免推销小公司嫌疑），统一用「手机 AI/语音助手/拍照识别/录音转写」；三节=收(45′)→理(60′)→用(50′)。

## 满编矩阵派发（对比既往 kma 双跑）
- 切分：两场 × A课件/B-C材料/D海报/E-PDF = 8 块；派发 xuan=05A+06A、kma=05B+06B、openclaw=05C、wechat=06C、hermes=05D、xinma=06D；契约先行（CONTRACT-05/06.md + prompt 模板 + runner2.sh scp 到各节点 /root/w2/）。
- runner2.sh 要点：剥 OCTOPUS_* 环境变量、只 export 单 key 行；`--dangerously-skip-permissions`；kma 模型 `deepseek/deepseek-flash`。
- 探针验收：标记字（SMOKE5）grep 日志 + 节点库 part.data 双保险（stdout 只有 ANSI 启动头不可信；loong 库 schema 已变，part 无 text 列，用 `json.loads(data).get('text')`；xinma 库在 `/home/ubuntu/.local/share/octopus/octopus.db`）。

## 新坑与对策（关键经验）
1. **xuan 双课件块死在起步**：mkdir 后进程消失、日志仅 308 字节，重启不活 → 改派 kma 双跑（05A+06A）成功。**xuan 暂不作 loong run 派发首选。**
2. **06B 因 runner2.sh 缺失首启失败**：直接重启即成，不必改包。
3. **E 块缺件不重派 agent**：agent 只出 14/22 份 PDF，直接 ssh 循环 `google-chrome --headless --no-pdf-header-footer` 补打 8 份，更快更稳。
4. **scp 大文件静默失败**：传输后必须 `wc -c` 验字节（w2-pkg.tar.gz=68286 才算到齐）。
5. 详情页 05/06 由本机手写拼装（复用 03 页版式），不派 agent；workshops.js 补 wk5/wk6（status 均 open）。

## 产物与终态
- 站点仓 8297368：/workshop/05/（32 页课件+海报+材料01-09）/workshop/06/（31 页同构）；材料仓 0da9a5f：05-Harness工作台/、06-AI手机/ 各 dist 11 份 PDF（5.5M/4.2M）；README 六期化（66 份 PDF、六列编号对照）。
- 线上 /workshop/05/、/workshop/06/ 及 ppt/handouts/poster 全链接 200。
- 收尾遗留：六节点 /root/w2/、本机 /tmp/octopus/w2* 未清；模板包在 /tmp/octopus/w2-pkg/（CONTRACT-05/06.md、prompt-A~E、runner2.sh）可复用。
