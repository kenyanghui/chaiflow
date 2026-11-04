# 原则候选 — 《黄帝内经·灵枢》

> 由 principle-extractor 提取，阶段 1.5 三重验证前。不做筛选，宁多勿漏。

```yaml
- id: p01
  title: 虚则补之，实则泻之
  source_chapter: 九针十二原第一
  source_quote: "凡用针者，虚则实之，满则泄之，宛陈则除之，邪胜则虚之。"
  summary: 一切干预的核心原则——先判虚实方向，再选补泻操作。方向错了比不干预更糟。
  tags: [treatment-principle, excess-deficiency]

- id: p02
  title: 用针之要在于调气
  source_chapter: 刺节真邪第七十五
  source_quote: "用针之类，在于调气。"
  summary: 干预的根本目标是调气(恢复功能状态)，不是治形(处理表面症状)。
  tags: [core-principle, qi-regulation]

- id: p03
  title: 气至而有效
  source_chapter: 九针十二原第一
  source_quote: "刺之要，气至而有效，效之信，若风之吹云，明乎若见苍天。"
  summary: 干预有效的标志是"气至"——系统产生积极反应。效果应该是可感知、可验证的。
  tags: [effectiveness, feedback]

- id: p04
  title: 补泻有时
  source_chapter: 九针十二原第一、终始第九
  source_quote: "徐而疾则实，疾而徐则虚。"又"泻必用员……补必用方。"
  summary: 补法和泻法有具体的操作差异(速度、方向、手法)，不是笼统的"多和少"。
  tags: [technique, supplementation-drainage]

- id: p05
  title: 上工治未病
  source_chapter: 逆顺第五十五
  source_quote: "上工刺其未生者也；其次刺其未盛者也；其次刺其已衰者也。下工刺其方袭者也。"
  summary: 能力高下的判断标准是干预时机的早晚，不是技术手段的复杂程度。
  tags: [prevention, timing, quality]

- id: p06
  title: 持针之道坚者为宝
  source_chapter: 九针十二原第一
  source_quote: "持针之道，坚者为宝。正指直刺，无针左右。神在秋毫，属意病者。"
  summary: 操作时必须专注、稳定、精确。心神散乱则操作无效甚至有害。
  tags: [focus, precision, execution]

- id: p07
  title: 必先诊脉乃可以治
  source_chapter: 九针十二原第一、终始第九
  source_quote: "凡将用针，必先诊脉，视气之剧易，乃可以治也。"
  summary: 干预前必须先做诊断评估。不做评估就干预，如同盲人射箭。
  tags: [diagnosis-first, assessment]

- id: p08
  title: 无迎逢逢之气
  source_chapter: 逆顺第五十五
  source_quote: "兵法曰无迎逢逢之气，无击堂堂之阵。刺法曰：无刺熇熇之热，无刺漉漉之汗。"
  summary: 不要在问题最猛烈时正面硬攻，要等其势头衰退时再出手。
  tags: [timing, avoidance, military-analogy]

- id: p09
  title: 知调阴阳精气乃光
  source_chapter: 根结第五
  source_quote: "用针之要，在于知调阴与阳。调阴与阳，精气乃光，合形与气，使神内藏。"
  summary: 调节阴阳是恢复健康的核心手段，阴阳平衡则精神充沛、功能正常。
  tags: [yin-yang, balance, core-principle]

- id: p10
  title: 得其人乃传，非其人勿言
  source_chapter: 官能第七十三、禁服第四十八
  source_quote: "各得其能，方乃可行，其名乃彰。不得其人，其功不成。"
  summary: 知识和技术必须传给合适的人，否则不仅无效还会造成危害。
  tags: [knowledge-transfer, selection, responsibility]

- id: p11
  title: 视人五态乃治之
  source_chapter: 通天第七十二
  source_quote: "古之善用针艾者，视人五态乃治之。盛者泻之，虚者补之。"
  summary: 治疗方案必须因人而异。不同体质类型需要不同的干预策略。
  tags: [individualization, constitution]

- id: p12
  title: 邪之所凑其气必虚
  source_chapter: 百病始生第六十六
  source_quote: "风雨寒热不得虚，邪不能独伤人。卒然逢疾风暴雨而不病者，盖无虚，故邪不能独伤人。"
  summary: 外部因素只有在内部状态虚弱时才能造成伤害。"两虚相得乃客其形"。
  tags: [vulnerability, internal-external]

- id: p13
  title: 病各有宜各不同形
  source_chapter: 官针第七、九针论第七十八
  source_quote: "不得其用，病弗能移。疾浅针深，内伤良肉……病深针浅，病气不泻。"
  summary: 工具和方法必须匹配问题的性质和深度。深浅、大小不匹配都会导致失败。
  tags: [matching, appropriateness]

- id: p14
  title: 顺天之时病可与期
  source_chapter: 顺气一日分为四时第四十四
  source_quote: "顺天之时，而病可与期。顺者为工，逆者为粗。"
  summary: 治疗须顺应自然节律(四季、昼夜)。顺应者成功，违背者失败。
  tags: [seasonal, natural-rhythm]

- id: p15
  title: 五脏者所以藏精神
  source_chapter: 本神第八
  source_quote: "五脏主藏精者也，不可伤，伤则失守而阴虚；阴虚则无气，无气则死矣。"
  summary: 五脏不仅是生理器官，更是精神活动的载体。保护五脏就是保护精神根基。
  tags: [organ-spirit, protection, foundation]

- id: p16
  title: 以痛为输
  source_chapter: 经筋第十三
  source_quote: "治在燔针劫刺，以知为数，以痛为输。"
  summary: 当问题明确表现为疼痛时，痛处本身就是干预点。不必拘泥于固定位置。
  tags: [pain-point, pragmatic, intervention]

- id: p17
  title: 阴阳相随如环无端
  source_chapter: 营卫生会第十八、动输第六十二
  source_quote: "营卫之行也，上下相贯，如环之无端。"又"四末解则气从合，相输如环。"
  summary: 系统的运行是循环的、无始无终的。理解循环才能找到干预的切入点。
  tags: [cycle, circulation, systems]

- id: p18
  title: 审守其输调其虚实
  source_chapter: 海论第三十三
  source_quote: "审守其俞，而调其虚实，无犯其害，顺者得复，逆者必败。"
  summary: 调节关键节点(输)，避免造成新的伤害(无犯其害)。方向正确则恢复，方向错误则败坏。
  tags: [key-points, harm-avoidance, direction]

- id: p19
  title: 告之以其败导之以其便
  source_chapter: 师传第二十九
  source_quote: "告之以其败，语之以其善，导之以其所便，开之以其所苦。虽有无道之人，恶有不听者乎？"
  summary: 沟通四步法: 说明危害→讲清好处→引导可行路径→解除痛苦。适用于任何需要说服的场景。
  tags: [communication, persuasion, four-steps]

- id: p20
  title: 善治者治皮毛
  source_chapter: 阴阳反应篇(素问)、灵枢隐含
  source_quote: "圣人自治于未有形也，愚者遭其已成也。"(玉版第六十)
  summary: 最高明的处理是在问题尚未成型时就介入。"积微之所生"——大问题都从小问题积累而来。
  tags: [early-intervention, accumulation]
```
