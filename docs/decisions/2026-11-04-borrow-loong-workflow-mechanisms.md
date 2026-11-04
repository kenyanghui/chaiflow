# D21 · 借鉴 loong-workflow 工作流机制到拆AI资产仓（2026-11-04）

## 背景

站长要求「重新学习 loong-workflow，看能借鉴什么，学到的就实现，直接更新仓库内容」。loong-workflow 是内部的 provider 中立 AI 编程工作流语料仓（18 技能 + 23 规则 + 13 清单 + guards 漂移防护脚本，SSOT 在 Gitea Loong/loong-workflow），其价值不在技能本身，而在**纪律机制**：规则文件化、复盘清单化、外部写入回读验证、展示真实性、漂移防护。拆AI资产仓（chaiflow 决策档案 + rsi-ima-workbuddy-wechat-web 工作坊主仓）此前只有「事实性记录」（决策/复盘/手册），没有**防再犯的机制层**。

## 决策要点

1. **借机制不借流程**：loong-workflow 的 DAG 拆解/多角色流水线/Schema 全家桶面向多人开发环路，教学资产仓不需要；借的是五件轻机制——规则文件化（每条规则注明层级+立规出处）、写后回读验证（push 后 contents API 确认才记账成功）、复测定性（瞬时抖动≠持久故障）、展示真实性（证据逐块标注实际结论）、漂移防护（文档声称 vs 仓库实际互相断言）。
2. **机制层落在 rsi 仓**（有脚本有 CI，机制可执行）：`docs/RULES.md` 六条仓规 + `guards/check_docs_drift.py` + site_check `--retry` + site-ops 二轮复测 + 复盘模板，rsi 仓 020c24a 落地。学习笔记落 `rsi` 仓 `docs/BORROWED-FROM-LOONG-WORKFLOW.md`，含「明确不借」清单（借的时候说清不借什么，防止未来盲目照搬）。
3. **档案层落在 chaiflow 仓**（纯文档仓，机制变薄）：本决策 + `docs/retrospectives/TEMPLATE.md`（复盘五段式+行动项四条硬约束）+ `guards/check_docs_index.py`（索引漂移防护，见下）。chaiflow 不引 RULES 全文——它的规则本来就是决策记录本身。
4. **漂移防护当场抓到真漂移**：落地前盘点发现 PROJECT-OVERVIEW 文档索引引用了不存在的 `pending/voting-cards-redesign.md` 与 `core/`（计划未落地即写了索引）——正是漂移防护要防的事故，两行已清理，guard 防复发。
5. **表述红线**：loong-workflow 无公开 GitHub 镜像，对外档案（本仓）只写「内部工作流语料仓」，不引外部链接。

## 落地与坑

- rsi 仓 020c24a：9 文件 +401/-70，push 后 contents API 回读确认（遵守刚立的 R1）。
- 坑：**并行会话撞车**——同一时段另一会话已在 chaiflow 落了 D20（fork 讲师站主线），本决策编号顺延 D21；rsi 仓也出现并行提交 dc9cc8b（fork_chaiai.py 主线），push 前以 `git log origin/main..main` 确认无冲突后干净落位。教训：多会话同仓作业，push 前必 fetch 对账，编号类资源（决策编号）先查再占。
- 坑：rsi 仓 evidence.txt 旧版末尾 `EVIDENCE-PASS` 单标记与中间 JSON 块 `overall:fail` 脱节——展示真实性纪律的活反例，已重构为逐块标注+VERDICT 行，反例本身存档在文件头（反例不删，删了就失去教育价值）。
- CI 隐患自查：原 site-ops.yml 的告警步挂 `if: steps.sitecheck.outcome == 'failure'`，但 GitHub Actions 隐式前置 `success()` 导致该步在体检失败时反而被跳过（原告警步是死代码）——重构为 `continue-on-error` + 二轮复测 + `always()` 漂移防护 + 两轮全挂才告警。

## 后续义务

- chaiflow 后续每篇复盘一律从 `docs/retrospectives/TEMPLATE.md` 起笔（行动项 ≤5、带文件路径、可度量、无指责）；旧行动项措辞「下次小心」类视为此前技术债，不回溯改写。
- PROJECT-OVERVIEW 文档索引与 README 结构树改动后必须过 `python3 guards/check_docs_index.py`（本地或 CI）。
- rsi 仓 RULES 六条与 chaiflow 本决策为**同源双落**：一方修改机制口径（如复测间隔、断言清单），须同步检查另一方表述是否需要跟改。
- 内部 loong-workflow 上游若有机制演进（规则/guards 新增），下次同步时按「借机制不借流程」重新筛选。
