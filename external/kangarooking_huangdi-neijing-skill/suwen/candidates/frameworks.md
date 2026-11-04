# 框架候选 — 《黄帝内经·素问》

> 由 framework-extractor 提取，阶段 1.5 三重验证前。不做筛选，宁多勿漏。

```yaml
- id: f01
  title: 阴阳二分法
  type: framework
  source_chapter: 阴阳应象大论篇第五
  source_quote: |
    "阴阳者，天地之道也，万物之纲纪，变化之父母，生杀之本始，神明之府也。治病必求于本。"
  summary: |
    将一切事物按阴阳两极分类，形成二元对立统一的思维模型。任何现象都可归入阴或阳，
    且阴中有阳、阳中有阴，可无限细分。用阴阳视角分析问题，找到失衡的根源再施治。
    这是素问最核心的元思维框架，贯穿全书。
  tags: [yin-yang, dualism, meta-framework, diagnosis]

- id: f02
  title: 阴阳无限可分推理法
  type: framework
  source_chapter: 金匮真言论篇第四
  source_quote: |
    "阴中有阴，阳中有阳。平旦至日中，天之阳，阳中之阳也；日中至黄昏，天之阳，阳中之阴也；合夜至鸡鸣，天之阴，阴中之阴也；鸡鸣至平旦，天之阴，阴中之阳也。"
  summary: |
    阴阳不是静态二分，而是可递归细分的层次结构。先分大阴阳，再在每一侧继续分出阴阳，
    形成"阴中之阴""阳中之阴"等多层分析。这种递归细分法使分析精度不断提升，
    类似于现代分类学中的层次分类思维。
  tags: [yin-yang, recursive-analysis, classification, reasoning]

- id: f03
  title: 五行生克网络推理
  type: framework
  source_chapter: 藏气法时论篇第二十二
  source_quote: |
    "五行者，金木水火土也。更贵更贱，以知死生，以决成败，而定五脏之气，间甚之时，死生之期也。"
  summary: |
    将事物归入五行（木火土金水），利用五行间的相生相克关系构建网络推理模型。
    通过"至其所生而愈，至其所不胜而甚"的规律，预判疾病走势和预后。
    这是一种系统动力学思维，关注元素间的相互作用而非孤立属性。
  tags: [five-elements, network-thinking, prediction, system-dynamics]

- id: f04
  title: 标本缓急决策框架
  type: framework
  source_chapter: 标本病传论篇第六十五
  source_quote: |
    "知标本者，万举万当，不知标本，是谓妄行。先病而后逆者治其本，先逆而后病者治其本……先病而后生中满者治其标，先中满而后烦心者治其本。小大不利治其标，小大利治其本。"
  summary: |
    面对复杂问题时，区分"本"（根本原因/先发病）与"标"（表面症状/继发病），
    按"急则治标，缓则治本"的优先级决策。先病为本后病为标，但中满、二便不利等急症
    需优先处理。病发有余先治本后治标，病发不足先治标后治本。
    这是一个通用的优先级排序决策框架，不限于医学领域。
  tags: [priority, decision-making, root-cause, triage]

- id: f05
  title: 治未病预防策略
  type: framework
  source_chapter: 四气调神大论篇第二
  source_quote: |
    "是故圣人不治已病，治未病不治己乱、治未乱，此之谓也。夫病已成而后药之，乱己成而后治之，譬犹渴而穿井，斗而铸锥，不亦晚乎？"
  summary: |
    在问题尚未出现时就主动预防，而非等问题爆发后再应对。这包含两个层面：
    "未病先防"（在疾病未发生时预防）和"既病防变"（在疾病已发生后防止恶化）。
    核心思想是预防的ROI远高于治疗。适用于任何需要风险管理的领域。
  tags: [prevention, strategy, risk-management, proactive]

- id: f06
  title: 四时调养法
  type: framework
  source_chapter: 四气调神大论篇第二
  source_quote: |
    "春三月，此为发陈……夜卧早起，广步于庭，被发缓形，以使志生……逆之则伤肝；夏三月，此为蕃秀……夜卧早起，无厌于日……逆之则伤心；秋三月……早卧早起……逆之则伤肺；冬三月……早卧晚起，必待日光……逆之则伤肾。"
  summary: |
    将时间维度（四季）纳入决策，每个季节有对应的养生策略：春养生（顺应生发）、
    夏养长（顺应旺盛）、秋养收（顺应收敛）、冬养藏（顺应闭藏）。
    核心原则是"春夏养阳，秋冬养阴"。这是一种时间感知型决策框架，
    强调行为应与外部周期同步。
  tags: [seasonal, timing, adaptation, lifecycle]

- id: f07
  title: 正邪对比分析法
  type: framework
  source_chapter: 评热病论篇第三十三 / 刺法论篇第七十二
  source_quote: |
    "邪之所凑，其气必虚"；"正气存内，邪不可干"
  summary: |
    评估"正气"（抗病能力/系统韧性）与"邪气"（致病因素/外部压力）的力量对比，
    判断胜负走向。正气胜则不病，邪气胜则发病。治疗的核心是扶正祛邪。
    这是一种对抗性力量分析框架，适用于任何"防守vs攻击"的博弈场景。
  tags: [strength-assessment, resistance, balance, competitive-analysis]

- id: f08
  title: 天人合一系统思维
  type: framework
  source_chapter: 生气通天论篇第三
  source_quote: |
    "夫自古通天者，生之本，本于阴阳。天地之间，六合之内，其气九州、九窍、五脏十二节，皆通乎天气。"
  summary: |
    将人体视为天地自然的缩影，用宏观自然规律类比和推断人体内部的微观规律。
    人体结构与自然现象一一对应：天有四时，人有四脏；天有五行，人有五脏。
    这是一种类比推理框架，通过宏观理解来推断微观机制。
  tags: [analogy, holistic, systems-thinking, macro-micro]

- id: f09
  title: 以外测内推理法
  type: framework
  source_chapter: 脉要精微论篇第十七 / 五藏生成篇第十
  source_quote: |
    "切脉动静而视精明，察五色，观五脏有余不足，六腑强弱，形之盛衰，以此参伍，决死生之分。"
  summary: |
    通过观察外部可感知的信号（面色、脉象、声音、体态），推断内部不可直接观察的
    脏腑状态。面色五色对应五脏，脉象变化反映气血盛衰。
    这是一种间接推理框架，从可观测变量推断隐藏变量，类似于现代诊断学中的
    "proxy measurement"思维。
  tags: [observation, inference, proxy-measurement, diagnosis]

- id: f10
  title: 五味调和决策法
  type: framework
  source_chapter: 生气通天论篇第三
  source_quote: |
    "是故谨和五味，骨正筋柔，气血以流，腠理以密，如是则骨气以精。谨道如法，长有天命。"又"阴之所生，本在五味；阴之五宫，伤在五味。"
  summary: |
    将事物按五味（酸苦甘辛咸）分类，五味各归其脏，适量则养、过量则伤。
    核心是"调和"——不偏嗜任何一味，使五味均衡。
    这是一种均衡决策框架，适用于任何涉及多因素平衡的资源配置场景。
  tags: [balance, five-flavors, moderation, diet]

- id: f11
  title: 因地制宜分析法
  type: framework
  source_chapter: 异法方宜论篇第十二
  source_quote: |
    "医之治病也，一病而治各不同，皆愈何也？地势使然也。故东方之域……其治宜砭石；西方者……其治宜毒药；北方者……其治宜灸焫；南方者……其治宜微针；中央者……其治宜导引按蹻。故圣人杂合以治，各得其所宜。"
  summary: |
    同一个问题在不同地域环境下需要不同的解决方案。东方人多痈疡宜砭石，
    西方人病生于内宜毒药，北方人脏寒宜灸焫，南方人挛痹宜微针，中央人多痿厥宜导引。
    核心原则是"得病之情，知治之大体"，即理解问题的具体语境后选择最匹配的方案。
    适用于任何需要contextualize决策的场景。
  tags: [context, localization, adaptation,因地制宜]

- id: f12
  title: 脏腑传变预测法
  type: framework
  source_chapter: 玉机真藏论篇第十九
  source_quote: |
    "五脏受气于其所生，传之于其所胜，气舍于其所生，死于其所不胜。病之且死，必先传行，至其所不胜，病乃死。"
  summary: |
    疾病按五行相克顺序在脏腑间传递（肝→脾→肾→心→肺→肝），
    当传至"所不胜"之脏时最为危重。通过掌握传变规律，
    可以预判疾病将传至哪个脏腑，从而提前阻断。
    这是一种多米诺骨牌式的连锁反应预测模型。
  tags: [prediction, progression, chain-reaction, five-elements]

- id: f13
  title: 六经传变推理法
  type: framework
  source_chapter: 热论篇第三十一
  source_quote: |
    "伤寒一日，巨阳受之，故头项痛，腰脊强。二日阳明受之……三日少阳受之……四日太阴受之……五日少阴受之……六日厥阴受之。"
  summary: |
    外感疾病按六经（太阳→阳明→少阳→太阴→少阴→厥阴）的固定顺序逐层深入，
    从表到里、从阳到阴。每日传一经，症状可预测。
    这是一种阶段性演进推理框架，通过定位当前阶段预判下一阶段的发展。
    适用于任何有阶段性发展规律的问题。
  tags: [staging, progression, six-meridians, prediction]

- id: f14
  title: 虚实判断与补泻决策
  type: framework
  source_chapter: 通评虚实论篇第二十八
  source_quote: |
    "邪气盛则实，精气夺则虚。"
  summary: |
    首先判断问题是"实"（外部致病因素过盛）还是"虚"（内部正气不足），
    然后采取相反策略：实则泻之（消除多余），虚则补之（填补不足）。
    这是一种先定性后定量、方向相反的决策逻辑。
    实证用攻法，虚证用补法，虚实夹杂则攻补兼施。
  tags: [diagnosis, binary-decision, excess-deficiency, treatment]

- id: f15
  title: 寒热辨析框架
  type: framework
  source_chapter: 阴阳应象大论篇第五
  source_quote: |
    "阳胜则热，阴胜则寒。重寒则热，重热则寒。"
  summary: |
    将一切失衡归为寒热两端（阳盛则热，阴盛则寒），并认识到极端会向对立面转化
    （重寒则热，重热则寒——物极必反）。治疗时寒者热之、热者寒之，
    但需注意真寒假热、真热假寒的情况。这是一种辩证思维框架。
  tags: [cold-heat, dialectics, polarity, reversal]

- id: f16
  title: 情志-脏腑关联推理
  type: framework
  source_chapter: 阴阳应象大论篇第五
  source_quote: |
    "怒伤肝，悲胜怒；喜伤心，恐胜喜；思伤脾，怒胜思；忧伤肺，喜胜忧；恐伤肾，思胜恐。"
  summary: |
    五种情志（怒喜思忧恐）与五脏一一对应，过度的情志损伤对应的脏腑，
    但可以用相胜的情志来纠正（以情胜情）。例如怒伤肝但悲可胜怒。
    这是一种将心理与生理关联的交叉推理框架，也是最早的"情绪管理"方法论。
  tags: [emotion, five-elements, psychology, counterbalance]

- id: f17
  title: 升降出入运动分析
  type: framework
  source_chapter: 六微旨大论篇第六十八
  source_quote: |
    "出入废则神机化灭，升降息则气立孤危。故非出入，则无以生长壮老已；非升降，则无以生长化收藏。是以升降出入，无器不有。"
  summary: |
    一切生命活动的本质是气的升降出入四种运动形式。升（从下向上）、降（从上向下）、
    出（从内向外）、入（从外向内），四者协同维持生命运转，任何一种运动停滞都会导致
    疾病甚至死亡。这是一种运动学分析框架，用四个方向的运动来描述和诊断系统状态。
  tags: [movement, dynamics, qi, systems]

- id: f18
  title: 亢害承制调控法
  type: framework
  source_chapter: 六微旨大论篇第六十八
  source_quote: |
    "亢则害，承乃制，制则生化，外列盛衰，害则败乱，生化大病。"
  summary: |
    任何力量过度亢盛就会造成损害，必须有制约力量（承）来平衡，
    有了制约才能维持正常的生化运转。这是自然界自我调节的基本规律：
    过强则被抑制，过弱则被扶持。这类似于现代系统论中的负反馈调节。
  tags: [regulation, negative-feedback, balance, self-correction]

- id: f19
  title: 三部九候分层诊断法
  type: framework
  source_chapter: 三部九候论篇第二十
  source_quote: |
    "人有三部，部有三候，以决死生，以处百病，以调虚实，而除邪疾。上部天，两额之动脉……中部天，手太阴也……下部天，足厥阴也。"
  summary: |
    将人体分为上中下三部，每部又分天地人三候，共九个观测点。
    通过对比九个位置的状态差异（独大、独小、独疾、独迟等），
    精确定位问题所在。这是一种分层抽样+差异对比的诊断框架，
    类似于现代的"多维度检测定位"思维。
  tags: [triage, multi-point-assessment, localization, diagnosis]

- id: f20
  title: 病机十九条归纳推理
  type: framework
  source_chapter: 至真要大论篇第七十四
  source_quote: |
    "诸风掉眩，皆属于肝。诸寒收引，皆属于肾。诸气膹郁，皆属于肺。诸湿肿满，皆属于脾。诸热瞀瘈，皆属于火。诸痛痒疮，皆属于心。"
  summary: |
    将纷繁复杂的症状归纳为十九条病机规则，每条以"诸X皆属于Y"的格式呈现。
    看到特定症状群，就能快速归因到对应的脏腑或邪气。
    这是一种模式识别+快速归因的推理框架，将观察到的现象映射到已知分类。
  tags: [pattern-recognition, attribution, diagnosis, categorization]

- id: f21
  title: 正治反治策略框架
  type: framework
  source_chapter: 至真要大论篇第七十四
  source_quote: |
    "寒者热之，热者寒之，微者逆之，甚者从之……逆者正治，从者反治……热因寒用，寒因热用，塞因塞用，通因通用，必伏其所主，而先其所因。"
  summary: |
    面对问题时，常规情况用"正治"（寒用热药，热用寒药，直接对抗）；
    但当问题复杂到出现假象时（真寒假热、真热假寒），需用"反治"
    （顺从假象用药，但实际治疗的仍是本质）。关键在于"必伏其所主，而先其所因"——
    必须先找到真正的病因。这是一种"表象vs本质"的决策框架。
  tags: [strategy, counter-intuitive, root-cause, paradox]

- id: f22
  title: 比类推理法
  type: framework
  source_chapter: 示从容论篇第七十六
  source_quote: |
    "夫圣人之治病，循法守度，援物比类，化之冥冥，循上及下，何必守经。……不引比类，是知不明也。"
  summary: |
    用已知事物的规律来类比推论未知事物的规律。"援物比类"是将一个领域的知识
    迁移到另一个领域。例如从天地日月运行类比人体气血运行，
    从四时变化类比脏腑盛衰。这是一种类比推理（analogical reasoning）框架。
  tags: [analogy, transfer-learning, reasoning, cross-domain]

- id: f23
  title: 表里先后决策法
  type: framework
  source_chapter: 至真要大论篇第七十四
  source_quote: |
    "从内之外者调其内；从外之内者治其外；从内之外而盛于外者，先调其内而后治其外；从外之内而盛于内者，先治其外，而后调其内。"
  summary: |
    判断问题的来源方向（从内向外还是从外向内），以及当前的主要矛盾在何处，
    据此决定先治内还是先治外。如果问题始于内但主要表现于外，先治内后治外；
    反之亦然。这是一种"溯源+优先级"的组合决策框架。
  tags: [priority, sequence, root-source, decision-making]

- id: f24
  title: 同病异治与异病同治
  type: framework
  source_chapter: 异法方宜论篇第十二 / 病能论篇第四十六
  source_quote: |
    "此同名异等者也。夫痈气之息者，宜以针开除去之。夫气盛血聚者，宜石而泻之，此所谓同病异治也。"
  summary: |
    同样的疾病表现可能有不同的病机（同病异治），需要不同的方案；
    不同的疾病可能有相同的病机（异病同治），可以用相同的方案。
    关键不是看表面症状是否相同，而是看病机本质是否相同。
    这是一种"透过现象看本质"的分类决策框架。
  tags: [differentiation, essence-vs-phenomenon, treatment, classification]

- id: f25
  title: 扶正祛邪策略选择
  type: framework
  source_chapter: 离合真邪论篇第二十七
  source_quote: |
    "方其来也，必按而止之，止而取之，无逢其冲而泻之。……候邪不审，大气已过，泻之则真气脱，脱则不复，邪气复至，而病益蓄。"
  summary: |
    攻邪（祛邪）必须把握时机——邪气初来时可攻，邪气正盛时不可硬攻（无逢其冲），
    邪气已过时攻则伤正气。核心是在保护正气的前提下祛除邪气。
    这是一种时机敏感的"攻防节奏"决策框架，强调攻击的时机选择比攻击本身更重要。
  tags: [timing, attack-defense, risk, opportunity]

- id: f26
  title: 十二官系统协调模型
  type: framework
  source_chapter: 灵兰秘典论篇第八
  source_quote: |
    "心者，君主之官也，神明出焉。肺者，相傅之官，治节出焉。肝者，将军之官，谋虑出焉……凡此十二官者，不得相失也。故主明则下安……主不明则十二官危。"
  summary: |
    将人体十二个脏腑比作朝廷十二个官职，各司其职又相互协调。
    心为君主是核心领导，心明则全身安定，心乱则全系统崩溃。
    这是一种"核心依赖型系统"的组织管理思维——
    系统的多个子系统各负其责，但整体效能取决于核心节点的状态。
  tags: [organization, system-dependency, leadership, coordination]

- id: f27
  title: 气运周期预测法
  type: framework
  source_chapter: 天元纪大论篇第六十六
  source_quote: |
    "甲己之岁，土运统之；乙庚之岁，金运统之；丙辛之岁，水运统之；丁壬之岁，木运统之；戊癸之岁，火运统之。"
  summary: |
    基于天干地支的60年周期，推算每年的五运六气特征，预判该年的气候特点和
    流行病趋势。太过年和不及年各有不同的疾病谱。这是一种周期性预测框架，
    试图从大时间尺度上把握规律。虽然具体推算的准确性有争议，
    但其"从周期性规律预判未来"的思维方式具有方法论价值。
  tags: [prediction, cycle, time-series, epidemiology]

- id: f28
  title: 胜复循环推理
  type: framework
  source_chapter: 至真要大论篇第七十四
  source_quote: |
    "有胜则复，无胜则否。……胜至则复，无常数也，衰乃止耳。复已而胜，不复则害，此伤生也。"
  summary: |
    自然界存在"胜-复"循环：一种力量过胜，必然会引来报复性的克制力量（复气）。
    胜气越甚，复气越强；胜气微弱，复气也微。这是系统的自我调节机制。
    理解胜复循环，可以预判"物极必反"的转折点。
    这是一种周期性波动+均值回归的推理框架。
  tags: [cycle, overcorrection, mean-reversion, dynamics]

- id: f29
  title: 邪犯层次推理法
  type: framework
  source_chapter: 皮部论篇第五十六 / 缪刺论篇第六十三
  source_quote: |
    "邪之始入于皮毛也……其入于络也，则络脉盛色变；其入客于经也，则感虚乃陷下。其留于筋骨之间，寒多则筋挛骨痛，热多则筋弛骨消。"
  summary: |
    病邪侵入人体按固定层次从浅到深：皮毛→络脉→经脉→腑→脏。
    层次越深，病情越重。通过判断邪在何层，决定治疗方法和预后。
    这是一种"深度定位"推理框架，类似现代的"分层防御"思维。
  tags: [layer, depth-assessment, progression, defense-in-depth]

- id: f30
  title: 毒药用量递减法
  type: framework
  source_chapter: 五常政大论篇第七十
  source_quote: |
    "大毒治病，十去其六；常毒治病，十去其七；小毒治病，十去其八；无毒治病，十去其九。谷肉果菜，食养尽之，无使过之，伤其正也。"
  summary: |
    根据药物毒性的大小设定不同的治疗终止标准：毒性越大，见效即停越早；
    毒性越小，可以治疗更久。核心原则是"无使过之，伤其正也"——
    不可过度治疗以免伤害正气。剩余部分用食疗调养。
    这是一种"边际收益递减+止损"的决策框架。
  tags: [dosage, margin, stop-loss, risk-benefit]

- id: f31
  title: 形神合一评估法
  type: framework
  source_chapter: 上古天真论篇第一
  source_quote: |
    "上古之人，其知道者，法于阴阳，和于术数，食饮有节，起居有常，不妄作劳，故能形与神俱，而尽终其天年。"
  summary: |
    健康是"形"（身体）与"神"（精神）的统一状态。形神俱备才能长寿。
    只养形不养神，或只养神不养形，都不能达到完整健康。
    这是一种身心统一的评估框架，反对将身体和心理割裂看待。
  tags: [body-mind, holistic, assessment, unity]

- id: f32
  title: 求其属推理法
  type: framework
  source_chapter: 至真要大论篇第七十四
  source_quote: |
    "诸寒之而热者取之阴，热之而寒者取之阳，所谓求其属也。"
  summary: |
    当常规方法无效时（用寒药治热反而更热），需要"求其属"——
    重新审视问题的归属。表面是热证但用寒药无效，说明本质是阴虚发热，
    应补阴而非清热。这是一种"当A策略失败时，问题可能属于B类"的
    诊断性推理框架，强调对问题本质的持续追问。
  tags: [re-attribution, root-cause, failure-analysis, reframing]

- id: f33
  title: 五志胜克调节法
  type: framework
  source_chapter: 阴阳应象大论篇第五
  source_quote: |
    "怒伤肝，悲胜怒；喜伤心，恐胜喜；思伤脾，怒胜思；忧伤肺，喜胜忧；恐伤肾，思胜恐。"
  summary: |
    当一种情绪过度时，可以用与之相胜的另一种情绪来调节。悲可胜怒（金克木），
    恐可胜喜（水克火），怒可胜思（木克土），喜可胜忧（火克金），
    思可胜恐（土克水）。这是一种用系统内其他力量来制衡某个过度力量的调节策略。
  tags: [emotion-regulation, five-elements, counterbalance, psychology]

- id: f34
  title: 从容比类诊断法
  type: framework
  source_chapter: 疏五过论篇第七十七
  source_quote: |
    "善为脉者，必以比类奇恒，从容知之，为工而不知道，此诊之不足贵。"
  summary: |
    诊断时必须用"比类"（类比推理）和"奇恒"（辨别常与变）两种方法结合。
    比类是将当前病例与已知模式对比，奇恒是判断当前状态是正常变异还是真正异常。
    "从容"意味着不急于下结论，先全面收集信息再综合判断。
    这是一种审慎的综合诊断思维框架。
  tags: [diagnosis, comparison, anomaly-detection, deliberation]

- id: f35
  title: 上下病气反治法
  type: framework
  source_chapter: 五常政大论篇第七十
  source_quote: |
    "气反者，病在上，取之下；病在下，取之上；病在中，傍取之。"
  summary: |
    当常规的局部治疗无效时，采用空间上的反向策略：病在上部从下部治疗，
    病在下部从上部治疗，病在中部从两侧治疗。这是一种"间接路径"思维——
    当直接攻击目标无效时，从相反方向或侧面突破。
    类似于军事上的迂回策略。
  tags: [indirect-approach, spatial-reasoning, strategy, bypass]

- id: f36
  title: 阴阳开阖枢模型
  type: framework
  source_chapter: 阴阳离合篇第六
  source_quote: |
    "三阳之离合也：太阳为开，阳明为阖，少阳为枢。三阴之离合也，太阴为开，厥阴为阖，少阴为枢。"
  summary: |
    将三阴三阳各赋予"开、阖、枢"三种功能角色。开是向外释放，
    阖是向内收敛，枢是转动枢纽。三者配合才能正常运转。
    这是一种功能分工模型，适用于理解任何需要"输入-转换-输出"的系统。
  tags: [functional-model, triad, input-output, gate]

- id: f37
  title: 上工治未病层级评价
  type: framework
  source_chapter: 八正神明论篇第二十六 / 刺热篇第三十二
  source_quote: |
    "上工救其萌牙，必先见三部九候之气，尽调不败而救之，故曰上工。下工救其已成，救其已败。"又"病虽未发，见赤色者刺之，名曰治未病。"
  summary: |
    将医者能力分为上工和下工两级：上工在疾病萌芽阶段就识别并干预，
    下工等到疾病明显才应对。判断标准是干预时机的早晚，
    而非治疗手段的复杂程度。这是一种以"预防时机"为维度的
    能力评估和优先级框架——越早干预价值越高。
  tags: [assessment, tier, early-detection, prevention]

- id: f38
  title: 治病求本推理法
  type: framework
  source_chapter: 阴阳应象大论篇第五
  source_quote: |
    "治病必求于本。"
  summary: |
    一切治疗必须追溯根本原因。本在阴阳——所有疾病归根结底是阴阳失衡。
    不追问根本只治表面症状，等于扬汤止沸。这虽然只有四个字，
    但它是素问所有推理框架的元原则：先找到根本原因，再制定方案。
    类似于现代的"第一性原理"思维和"根因分析"(root cause analysis)。
  tags: [root-cause, first-principles, meta-principle, reasoning]

- id: f39
  title: 参伍合参综合诊断法
  type: framework
  source_chapter: 脉要精微论篇第十七
  source_quote: |
    "切脉动静而视精明，察五色，观五脏有余不足，六腑强弱，形之盛衰，以此参伍，决死生之分。"
  summary: |
    通过多种诊断方法（脉诊、色诊、问诊、望形）收集信息，然后"参伍"——
    将多源信息交叉比对、相互验证，综合判断。单一指标可能有误差，
    多指标交叉验证可提高判断的准确性。
    这是一种多源信息融合的决策框架。
  tags: [multi-source, cross-validation, diagnosis, fusion]

- id: f40
  title: 得神失神预后判断法
  type: framework
  source_chapter: 移精变气论篇第十三
  source_quote: |
    "得神者昌，失神者亡。"
  summary: |
    判断预后的终极标准是"神"——患者的整体精神状态和生命力。
    不管具体症状如何，"得神"（精神饱满、反应灵敏）预后良好，
    "失神"（精神萎靡、反应迟钝）预后凶险。
    这是一种从整体状态而非局部指标判断系统健康度的评估框架。
  tags: [prognosis, vitality, overall-assessment, spirit]

- id: f41
  title: 脉逆四时预警法
  type: framework
  source_chapter: 平人气象论篇第十八
  source_quote: |
    "脉从阴阳，病易已；脉逆阴阳，病难已；脉得四时之顺，曰病无他；脉反四时及不间脏曰难已。"
  summary: |
    脉象与季节相应为顺（春弦夏钩秋毛冬石），不相应为逆。
    顺者易治，逆者难治。这是一种将当前状态与预期基准对比的预警框架——
    如果观测值偏离了应有的季节性基准，说明系统处于异常状态。
    类似于现代的"偏差分析"(deviation analysis)。
  tags: [seasonal-benchmark, deviation, warning, prognosis]

- id: f42
  title: 五实五虚危症评估法
  type: framework
  source_chapter: 玉机真藏论篇第十九
  source_quote: |
    "脉盛，皮热，腹胀，前后不通，闷瞀，此谓五实。脉细，皮寒，气少，泄利前后，饮食不入，此谓五虚。……浆粥入胃，泄注止，则虚者活；身汗得后利，则实者活。"
  summary: |
    用五个指标快速评估危症：五实（五种过度亢盛的表现）和五虚（五种严重不足的表现）。
    五实五虚皆预后不良，但各有转机条件——虚者能进食止泻则活，
    实者能出汗通便则活。这是一种"危险评估+转机条件"的框架。
  tags: [critical-assessment, crisis, recovery-criteria, prognosis]

- id: f43
  title: 知犯何逆随证治之
  type: framework
  source_chapter: 举痛论篇第三十九
  source_quote: |
    "余知百病生于气也，怒则气上，喜则气缓，悲则气消，恐则气下，寒则气收，炅则气泄，惊则气乱，劳则气耗，思则气结。"
  summary: |
    九种因素（怒、喜、悲、恐、寒、炅、惊、劳、思）各有确定的气机反应模式。
    知道哪种因素导致了气机紊乱，就能针对性地纠正。
    这是一种"因果链映射"框架——特定输入必然产生特定输出，
    理解了映射关系就能精准干预。
  tags: [causation, mapping, emotion, nine-qi]
```
