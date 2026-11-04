# D25 · 三锚对齐与六场远程支持：远端真身先于重试（2026-11-04）

## 背景

第二期定档后、开课前，材料面三件收尾：①两期全套资料对齐「三锚」——开工前几件事、WorkBuddy 提示词、源码仓口径（站仓 chaiAI 6eca0bed / 源仓 7835169 同步落刀）；②六场工作坊全部补「远程也能参加」块（企微群二维码+会议链接群公告）与「远程伙伴四个注意」（站仓 e781e2d5 / 源仓 f27f71e）；③源仓推送收口时连续多轮被拒，引出远端真身问题。

## 决策要点

1. **三锚以站仓为首发面**：开工前几件事（ima Client ID/API Key、WorkBuddy 装注册、公众号 AppID/AppSecret+IP 白名单、wk2 另领 classic PAT）统一落在落地页「开工前三件事」区块+guide 备查区+07 课前清单三处，三处同口径；指令卡一律 owner 三句定稿原文（98776384），guide 可步骤腔、指令卡不可。
2. **远程支持块为六场标配**：结构=「远程也能参加」卡片（112px 企微群二维码+会议链接只发群公告）+四条注意（提前进群/带电脑耳机稳网络/课前备账号钥匙/报错截图发群）；主题按各页深/浅色适配，深色 cyan、浅色 blue。
3. **推送被拒先查远端真身，不做盲重试**：连续「fetch first」拒绝+API 响应异常时，第一动作是 `ls-remote`+API 解析仓库重定向，而不是加时重试——本轮源仓 origin 实为本机 Gitea 且仓已改名 `chaishu→chaiworkshop`，GitHub 上的 `kenyanghui/chaishu` 是改名残影（301→站仓 chaiAI），对它的一切 fetch/push 都打错靶。
4. **管道吞退出码禁令重申**：`git pull | tail` 假阳性已入前案，本轮复现——原子 if/then 才算数。

## 落地与坑

- 修破版用 `.pain b:first-child` 而非删样式规则：标题 `<b>` 恒为卡片首子元素，保留卡片标题样式的同时行内术语不再被拆独占行。
- 远程注意事项措辞分两档：有「开工前」区块的页（wk1/02）指「开工前三件事」，无该区块的页（03–06 及源仓全部）指「课前准备清单」。
- GitHub API 报 `Moved Permanently`/响应非 list 即重定向信号：跟 `Location` 头到 `/repositories/{id}` 才见真身；owner 仓清单 grep 无 `chaishu` 可佐证改名。
- 本机 Gitea 仓改名后 git fetch 会自动跟随重定向（warning: redirecting to …/chaiworkshop/），本地 remote URL 无需改。
- 坑：默认 `git -C` 被安全层拦（匹配 `-c` 模式），用 workdir 参数替代。

## 后续义务

- 涉源仓操作前先 `git remote -v` 确认真身（本机 Gitea chaiworkshop，非 GitHub）；两仓同步口径的提交信息保留「与站仓同步/与站仓 xxx 对齐」惯例。
- 开课前新增页面（海报卡/清单卡）须同 commit 带「远程也能参加」块；线上验证六页 远程块/注意/二维码 三 grep。
- 三锚口径再改，以本仓决策为准，双仓（chaiAI+chaiworkshop）同波次落刀。
