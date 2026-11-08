# D28 · website-workflow 仓并入 chaiflow：决策库收拢，原仓删除

- 日期：2026-11-08
- 状态：已定稿（owner 指令「仓库 website-workflow 就合并进入 chaiflow，原来的仓库删掉」）
- 范围：Gitea `Loong/website-workflow` 仓（7 文件：README+3 rules+2 retrospectives+1 checklist）全部精选迁入，原仓删除

## 背景

website-workflow（2026-10-31 立）是 loong-workflow 在网站场景的领域特化仓，沉淀官网迭代的合规/验证/漏斗三铁律。但一年不到已现维护成本：同为「经验教训沉淀」却与 chai-workflow（chaiflow 的内部源仓）分立两处，索引/复盘纪律各维护一套；且其复盘格式早于 chaiflow 五段式 TEMPLATE 定稿，未对齐。

## 决策

1. **并入而非保留**：website-workflow 全部 7 文件精选迁入 chaiflow——3 rules+1 checklist 融合为一册 `playbooks/site-iteration-playbook.md`（六节：合规白标/真实验证/漏斗一致性/发布清单/宣传改写方法论/push 失败两类）；2 retrospectives 脱敏迁入 `docs/retrospectives/`（补迁入说明头）。
2. **格式对齐**：playbook 采用 chaiflow 手册体例（如 print-materials-playbook 的分节+硬规则写法）；复盘不改写为五段式（历史文件保留原结构，只做脱敏与迁入说明）。
3. **原仓删除**：迁入 guard 通过+推送后，删除 Gitea 原仓与本地克隆；原仓 README 中「本目录是网站类项目的唯一权威源」表述由 chaiflow 承接（chaiflow 成为对外站点经验 SSOT）。
4. **脱敏口径**（公开仓红线）：内网 IP/端口、token 值与文件路径、Gitea 凭据细节、客户/厂商黑名单具体词条不随迁；黑名单 grep 模式改为「清单在各站内部规则文件维护」的指针式表述。原仓在内网 Gitea（登录墙后），未删前内部可见性不变。

## 落地与坑

- 原仓 retrospectives 含内网地址与凭据路径（ops 仓/token 文件位置），公开版一律指针化——「找凭据第一步查内部 ops 仓」的教训保留，具体路径不迁。
- checklist 与 rules 有大量重叠（清单是规则的勾选版）——融合为一册时以清单为骨架、规则为释义，避免同一铁律两处维护。

## 后续义务

- 对外站点迭代经验新沉淀一律落 chaiflow（决策/复盘/手册），不再新建独立仓。
- site-iteration-playbook 与 print-materials/site-deploy 两册的边界：前者管「内容与合规与漏斗」，后两册管「构建发布与打印材料」——新经验先对号入座再落盘。
