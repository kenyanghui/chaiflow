# 案例候选 — 《黄帝内经·灵枢》

> 由 case-extractor 提取，阶段 1.5 三重验证前。不做筛选，宁多勿漏。

```yaml
- id: c01
  title: 拔刺雪污解结决闭——久病可治
  source_chapter: 九针十二原第一
  type: positive_case
  summary: |
    黄帝问: 久病是否不可治? 岐伯以四个比喻回答:
    "刺虽久犹可拔也, 污虽久犹可雪也, 结虽久犹可解也, 闭虽久犹可决也。"
    善用针者取疾"犹拔刺也, 犹雪污也, 犹解结也, 犹决闭也"。
    "疾虽久犹可毕也, 言不可治者未得其术也"——问题不是不能解决, 而是没找到方法。
  extracted_insight: 任何久拖不决的问题都有解决可能, "不能解决"往往意味着"方法不对"。
  tags: [persistence, method, curable]

- id: c02
  title: 营卫失调导致老人失眠
  source_chapter: 营卫生会第十八
  type: positive_case
  summary: |
    老人夜不寐而少壮之人昼不眠, 原因在于营卫运行状态不同:
    壮者气血盛, 肌肉滑, 气道通, 营卫运行正常, 故"昼精而夜瞑"。
    老者气血衰, 肌肉枯, 气道涩, 营卫运行不畅, 故"昼不精, 夜不瞑"。
    这是将睡眠问题归因于气血运行状态(系统动力), 而非简单的"神经衰弱"。
  extracted_insight: 表面症状(失眠)的根因可能是系统动力衰退(营卫失调), 而非局部问题。
  tags: [sleep, aging, circulation, root-cause]

- id: c03
  title: 胃为五脏六腑之海
  source_chapter: 动输第六十二、平人绝谷第三十二
  type: positive_case
  summary: |
    "胃为五脏六腑之海, 其清气上注于肺, 肺气从太阴而行之。"
    胃是气血生化的源头, 胃气足则脉动不休, 胃气绝则人死。
    "故平人不食饮七日而死者, 小谷精气津液皆尽故也。"
    七日不食则死, 是因为胃中水谷消耗殆尽, 五脏六腑失去营养来源。
  extracted_insight: 系统的核心供应源(胃/供应链)决定整个系统的存亡。"断粮"是最致命的失败。
  tags: [supply, stomach, foundation, nutrition]

- id: c04
  title: 五脏各有小大坚脆偏倾——体质决定易病性
  source_chapter: 本藏第四十七
  type: positive_case
  summary: |
    五脏各有二十五种形态变化(小大、高下、坚脆、端正、偏倾×五),
    不同形态决定了不同的健康倾向:
    "五脏皆小者少病……五脏皆坚者无病, 五脏皆脆者不离于病。"
    外在可观测: 红色小理者心小, 白色小理者肺小, 青色小理者肝小……
    "视其外应以知其内藏则知所病矣。"
  extracted_insight: 先天禀赋决定抗病能力, 但可通过外在表征识别风险, 提前预防。
  tags: [constitution, predisposition, external-signs]

- id: c05
  title: 大惑论——视觉错觉的精神机制
  source_chapter: 大惑论第八十
  type: positive_case
  summary: |
    黄帝登高台时眩晕, 岐伯解释: 五脏六腑之精气皆上注于目。
    "邪中于项, 因逢其身之虚, 其入深, 则随眼系以入于脑。入于脑则脑转……目眩以转矣。"
    精散则"视歧见两物"。此外, "心有所喜神有所恶, 卒然相惑则精气乱"——
    心理冲突也会导致视觉错觉。
    "上气不足下气有余……故善忘也"——健忘是上气不足导致的。
  extracted_insight: 精神/认知问题(眩晕、复视、健忘、嗜睡)都有气血运行异常的物质基础。
  tags: [vision, cognition, spirit, mechanism]

- id: c06
  title: 情志伤脏的具体路径
  source_chapter: 本神第八
  type: positive_case
  summary: |
    五种情志各有损伤的脏腑和最终致命季节:
    怵惕思虑→伤心→死于冬; 愁忧不解→伤脾→死于春;
    悲哀动中→伤肝→死于秋; 喜乐无极→伤肺→死于夏;
    盛怒不止→伤肾→死于季夏; 恐惧不解→伤精→骨酸痿厥。
    每种情志过度都有明确的损伤路径和恶化终点。
  extracted_insight: 情绪管理不是软技能, 而是"五脏不受邪"的硬需求。每种情绪有特定的伤害路径。
  tags: [emotion, organ-damage, pathway]

- id: c07
  title: 肥瘦老少刺法不同
  source_chapter: 逆顺肥瘦第三十八
  type: positive_case
  summary: |
    肥人(年质壮大, 血气充盈): 深而留之。
    瘦人(皮薄色少, 血清气滑): 浅而疾之。
    常人(端正敦厚, 血气和调): 无失常数。
    壮士(重则气涩血浊: 深而留之; 劲则气滑血清: 浅而疾之)。
    婴儿(肉脆血少气弱): 以豪刺, 浅刺而疾拔针, 日再可也。
    同样的干预手段, 不同体质需要完全不同的参数设置。
  extracted_insight: "一刀切"的方案是失败之源。参数(深度/速度/频率)必须因人而异。
  tags: [personalization, parameters, body-type]

- id: c08
  title: 天年——人生十阶段
  source_chapter: 天年第五十四
  type: positive_case
  summary: |
    十岁好走, 二十好趋, 三十好步, 四十好坐, 五十肝衰目不明,
    六十心衰好卧, 七十脾虚皮肤枯, 八十肺衰言善误, 九十肾焦经脉空, 百岁终矣。
    每个阶段有明确的生理特点和行为倾向, 这是自然规律, 无法逆转但可以延缓。
    "五脏坚固, 血脉和调……故能长久"——长寿的根基在于五脏功能完好。
  extracted_insight: 理解生命周期的每个阶段特点, 才能在对的时间做对的事(养生重点随年龄变化)。
  tags: [lifecycle, aging, stages, longevity]

- id: c09
  title: 病气传变如多米诺骨牌
  source_chapter: 病传第四十二
  type: positive_case
  summary: |
    病先发于心→一日之肺→三日之肝→五日之脾→三日不已→死(冬夜半夏日中)。
    病先发于肺→三日之肝→一日之脾→五日之胃→十日不已→死。
    六种起点的传变路径都有记载, 每条路径有固定的天数和死亡时辰。
    "间一脏及二三四脏者, 乃可刺也"——只要没有传遍, 就还有治疗机会。
  extracted_insight: 问题扩散有规律可循, 理解规律就能预判走向, 提前阻断。
  tags: [progression, prediction, chain-reaction]

- id: c10
  title: 卫气行——精确到刻的运行时刻表
  source_chapter: 卫气行第七十六
  type: positive_case
  summary: |
    卫气运行有精确的时刻表: 水下一刻在太阳, 二刻在少阳, 三刻在阳明, 四刻在阴分,
    然后循环往复。一日一夜共百刻, 卫气行五十周。
    "谨候其时, 病可与期, 失时反候者, 百病不治。"
    "刺实者刺其来也, 刺虚者刺其去也"——在卫气到达时泻, 离开时补。
  extracted_insight: 精确的时间窗口可以大幅提升干预效果。"何时做"与"做什么"同等重要。
  tags: [timing, schedule, precision, circadian]

- id: c11
  title: 贼风——无形之邪的伏击机制
  source_chapter: 贼风第五十八
  type: positive_case
  summary: |
    有人不出门也生病, 岐伯解释: "此皆尝有所伤于湿气, 藏于血脉之中, 分肉之间,
    久留而不去。"旧邪潜伏在体内, "其有热则汗出, 汗出则受风, 虽不遇贼风邪气,
    必有因加而发焉。"
    "其所从来者微, 视之不见, 听而不闻, 故似鬼神。"
  extracted_insight: 许多"莫名其妙"的问题, 实际上是历史遗留隐患被新因素触发。旧债新还。
  tags: [latent-pathogen, trigger, hidden-cause]

- id: c12
  title: 阴阳不和则目不瞑——失眠的气机机制
  source_chapter: 大惑论第八十、邪客第七十一
  type: positive_case
  summary: |
    "卫气不得入于阴, 常留于阳……故目不瞑。"
    失眠是因为卫气(阳气)不能从体表进入体内(阴分), 阳气偏盛阴虚。
    治疗: "补其不足, 泻其有余, 调其虚实, 以通其道而去其邪。"
    半夏汤可通阴阳——"阴阳已通, 其卧立至"。
  extracted_insight: 睡眠问题的本质是阴阳通道不通, 恢复通路比镇静更根本。
  tags: [sleep, yin-yang, pathway, treatment]

- id: c13
  title: 经筋病——以痛为输的务实策略
  source_chapter: 经筋第十三
  type: positive_case
  summary: |
    十二经筋各有循行路线和病候, 但治疗原则统一: "治在燔针劫刺, 以知为数, 以痛为输。"
    不取固定穴位, 而是以痛点本身作为干预点。"以知为数"以见效为准, 不预设次数。
    口眼歪斜的治法: 用马膏涂急的一侧, 白酒和桂涂缓的一侧, 用桑钩固定——
    针对性处理"急"和"缓"两个对立面。
  extracted_insight: 当问题定位明确时, 直接在问题点干预即可, 不必过度系统化。实用主义优先。
  tags: [pragmatic, pain-point, treatment]

- id: c14
  title: 五脏气绝的连锁死亡
  source_chapter: 经脉第十
  type: positive_case
  summary: |
    手太阴气绝→皮毛焦→爪枯毛折→毛先死→两笃丁死(火胜金)。
    手少阴气绝→脉不通→血不流→面黑如漆柴→血先死→壬笃癸死(水胜火)。
    五阴气俱绝→目系转→志先死→远一日半死。
    六阳气绝→阴与阳相离→腠理发泄→绝汗乃出→旦占夕死, 夕占旦死。
  extracted_insight: 系统崩溃有明确的连锁信号, 识别早期信号是挽救的关键。
  tags: [organ-failure, chain-reaction, prognosis]

- id: c15
  title: 邪客五邪——痈疽寒热各有治法
  source_chapter: 刺节真邪第七十五
  type: positive_case
  summary: |
    五种邪气各有治法口诀:
    痈邪: "无迎陇, 易俗移性"——不正面硬攻, 改变环境使其散。
    大邪: "泄夺其有余, 乃益虚"——泻其盛处。
    小邪: "补其不足, 乃无害"——补虚扶正。
    热邪: "越而苍, 出游不归"——开门放邪外出。
    寒邪: "日以温, 徐往徐来, 致其神"——慢慢温养, 不可急攻。
  extracted_insight: 不同性质的问题需要完全不同的策略。不能一个方法打天下。
  tags: [differentiation, strategy, five-evils]
```
