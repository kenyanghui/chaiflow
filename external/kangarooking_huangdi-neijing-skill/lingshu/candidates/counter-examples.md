# 反例候选 — 《黄帝内经·灵枢》

> 由 counter-example-extractor 提取，阶段 1.5 三重验证前。不做筛选，宁多勿漏。

```yaml
- id: ce01
  title: 补泻方向错误则杀人
  source_chapter: 根结第五、九针十二原第一
  type: failure_mode
  source_quote: |
    "满而补之, 则阴阳四溢, 肠胃充郭, 肝肺内(月真), 阴阳相错。
    虚而泻之, 则经脉空虚, 血气竭枯, 肠胃(亻耳耳耳)辟, 皮肤薄着, 毛腠夭膲, 予之死期。"
  summary: |
    实证(有余)用了补法: 阴阳更加泛滥, 肠胃胀满, 肝肺充血, 阴阳错乱。
    虚证(不足)用了泻法: 经脉更空虚, 气血枯竭, 皮肤干瘪, 可判死期。
    方向错误比不干预更致命。
  warning: 虚实判断错误会导致方向相反的干预, 效果适得其反。
  tags: [wrong-direction, excess-deficiency, fatal]

- id: ce02
  title: 刺不知逆顺则杀人
  source_chapter: 根结第五
  type: failure_mode
  source_quote: |
    "刺不知逆顺, 真邪相搏。满而补之……虚而泻之……"
    "故曰: 上工平气, 中工乱脉, 下工绝气危生。故曰: 下工不可不慎也。"
  summary: |
    上工调平气机, 中工反而扰乱脉象, 下工直接断绝气机危及生命。
    操作者水平不足时, 干预本身成为伤害源。
  warning: 能力不足时的干预比不干预更危险。"庸医杀人"不是比喻。
  tags: [skill-level, harm, practitioner-quality]

- id: ce03
  title: 五脏气已绝而误刺则死
  source_chapter: 九针十二原第一
  type: failure_mode
  source_quote: |
    "五脏之气已绝于内, 而用针者反实其外, 是谓重竭, 重竭必死, 其死也静。
    五脏之气已绝于外, 而用针者反实其内, 是谓逆厥, 逆厥则必死, 其死也躁。"
  summary: |
    五脏气已绝于内(阴虚)却补外→"重竭"→静死。
    五脏气已绝于外(阳虚)却补内→"逆厥"→躁死。
    当系统已经衰竭时, 方向错误的干预直接导致死亡。
  warning: 系统衰竭时的干预方向至关重要, 反向操作直接致命。
  tags: [terminal, exhaustion, wrong-direction]

- id: ce04
  title: 针过深过浅皆有害
  source_chapter: 九针十二原第一、官针第七
  type: failure_mode
  source_quote: |
    "针太深则邪气反沉病益。"
    "疾浅针深, 内伤良肉, 皮肤为痈; 病深针浅, 病气不泻, 支为大脓。
    病小针大, 气泻太甚, 疾必为害; 病大针小, 气不泄泻, 亦复为败。"
  summary: |
    浅病深刺→伤好肉成痈; 深病浅刺→排不掉邪气成脓。
    小病用大针→泻气太甚伤人; 大病用小针→排不出邪气失败。
    工具和深度必须匹配问题。
  warning: 干预的强度和深度不匹配问题, 导致新的伤害或无效。
  tags: [depth-mismatch, tool-mismatch, iatrogenic]

- id: ce05
  title: 刺害中而不去则精泄
  source_chapter: 九针十二原第一、寒热病第二十一
  type: failure_mode
  source_quote: |
    "刺之害中而不去则精泄; 害中而去则致气。精泄则病益甚而恇, 致气则生为痈疡。"
  summary: |
    刺中要害但留针太久→精气外泄, 病情加重。
    刺中要害但拔针太快→气滞局部, 形成痈疡。
    时间参数(留针长短)同样是干预成败的关键。
  warning: 干预持续时间不当会导致反效果——太久则耗损, 太短则淤滞。
  tags: [duration, retention, over-intervention]

- id: ce06
  title: 夺阴者死夺阳者狂
  source_chapter: 九针十二原第一
  type: failure_mode
  source_quote: |
    "取五脉者死, 取三脉者恇; 夺阴者死, 夺阳者狂, 针害毕矣。"
  summary: |
    过度泻五脏之脉→死; 泻三阳脉→恐惧不安。
    过度夺阴(血/津液)→死; 过度夺阳(气)→狂躁。
    有明确的不可逾越的红线。
  warning: 存在不可逆的底线, 超过则系统崩溃。干预有绝对禁忌。
  tags: [red-line, irreversible, absolute-contraindication]

- id: ce07
  title: 热病九不可刺
  source_chapter: 热病第二十三
  type: failure_mode
  source_quote: |
    "热病不可刺者有九: 一曰汗不出大颧发赤……二曰泄而腹满甚……三曰目不明热不已……
    四曰老人婴儿热而腹满……五曰汗不出呕下血……六曰舌本烂热不已……
    七曰咳而衄汗不出……八曰髓热者死……九曰热而痉者死。腰折, 齿噤也。"
  summary: |
    热病中有九种情况绝对不可针刺, 涉及汗不出、腹满、目不明、出血、舌烂、
    髓热、痉厥等危重表现。这些是系统已接近崩溃的信号, 干预反而加速死亡。
  warning: 某些状态下任何干预都是危险的, 此时"不做"比"做"更明智。
  tags: [absolute-contraindication, critical-state, do-not-treat]

- id: ce08
  title: 五夺不可泻
  source_chapter: 五禁第六十一
  type: failure_mode
  source_quote: |
    "形肉已夺, 一夺也; 大夺血之后, 二夺也; 大汗出之后, 三夺也;
    大泄之后, 四夺也; 新产及大血之后, 五夺也。此皆不可泻。"
  summary: |
    五种极度虚弱的状态(形肉消瘦、大量失血、大汗、大泻、产后大出血),
    绝对不可用泻法, 因为系统已无余可泻, 泻则崩溃。
  warning: 当系统资源已耗尽时, "减法"操作是致命的。
  tags: [exhaustion, no-drainage, contraindication]

- id: ce09
  title: 五逆——病脉不符
  source_chapter: 五禁第六十一
  type: failure_mode
  source_quote: |
    "热病脉静, 汗已出脉盛躁, 一逆也; 病泄脉洪大, 二逆也;
    着痹不移肉破身热脉偏绝, 三逆也; 淫而夺形身热色天然白, 四逆也;
    寒热夺形脉坚搏, 五逆也。"
  summary: |
    五种病与脉不一致的情况(热病反见静脉、泄泻反见洪脉等),
    说明系统已完全紊乱, 预后极差。
  warning: 当观测指标与实际情况完全矛盾时, 说明系统已严重失序。
  tags: [contradiction, paradox, poor-prognosis]

- id: ce10
  title: 真心痛——旦发夕死
  source_chapter: 厥病第二十四
  type: failure_mode
  source_quote: |
    "真心痛, 手足清至节, 心痛甚, 日发夕死, 夕发旦死。"
    又"真头痛, 头痛甚, 脑尽痛, 手足寒至节, 死不治。"
  summary: |
    真心痛和真头痛是两种无法治愈的急症, 手足冰冷到关节, 朝发夕死。
    这是灵枢承认"有不治之症"的诚实之处——不是所有问题都能解决。
  warning: 必须承认能力边界。有些问题确实是不可逆的, 识别比盲目干预更重要。
  tags: [terminal, incurable, boundary]

- id: ce11
  title: 同病异因——不可一概而论
  source_chapter: 五变第四十六
  type: failure_mode
  source_quote: |
    "一时遇风, 同时得病, 其病各异。"又"木之阴阳, 尚有坚脆, 况于人乎?"
  summary: |
    同样的外部条件(暴风骤雨), 同时受邪的人会得不同的病,
    因为各人体质不同(如树木有坚脆)。
    "犯者得之, 避者得无殆"——但即使是同样的犯者, 结果也不同。
  warning: 不可根据外部条件简单推判结果, 个体差异是关键变量。
  tags: [individual-variation, same-cause-different-effect]

- id: ce12
  title: 上工平气中工乱脉下工绝气
  source_chapter: 根结第五
  type: failure_mode
  source_quote: "上工平气, 中工乱脉, 下工绝气危生。"
  summary: |
    中等水平的操作者(中工)会把脉象搞乱——干预了但方向不对, 制造了新的紊乱。
    下等水平的操作者(下工)直接断绝气机危及生命。
  warning: 能力不足的干预不仅无效, 还会制造新问题。
  tags: [skill-level, iatrogenic, harm-from-intervention]
```
