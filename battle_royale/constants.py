# 地点配置，可更改名称，不可直接更改地点数量
PLACES = ['哼哼井', '达达城', '丹丹堡', '沙沙寨', '苏苏林', '格格屋', '月月丛', '加加岛']
DIRECTIONS = ['东', '南', '西', '北']

# 角色配置
ROLES = ['风行者', '变体精灵', '死亡骑士', '沙王', '水晶室女', '精灵守卫', '龙骑士', '敌法师', '灵魂守卫', '海军上将', '幻影刺客', '月之女祭司', '谜团', '狙击手', '卓尔游侠', '巫医', '月之骑士', '秀逗魔导士', '圣堂刺客', '精灵龙', '小小', '巨牙海民', '光之守卫', '魅惑魔女', '鱼人夜行者', '狼人', '影魔']
PASSWORDS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27']
DIRECTOR_PASSWORD = 'cy941h'
AUDIENCE_PASSWORD = 'test'

# 道具配置
ITEM_HOT_AOE = ['狂战斧', '雷神之锤', '金箍棒'] # AOE热武器（带持续伤害）
ITEM_HOT_AOE_DAMAGE = 40
ITEM_HOT_VITAL = ['代达罗斯之殇', '达贡之神力', '圣剑'] # 狙击类热武器
ITEM_HOT_VITAL_DAMAGE = 80
ITEM_HOT = ['恶魔刀锋', '水晶剑', '邪恶镰刀', '掠夺者之斧'] # 热武器
ITEM_HOT_DAMAGE = 40
ITEM_COLD = ['标枪', '攻击之爪', '短棍', '阔剑', '跳刀', '秘银锤', '吸血面具', '神秘法杖'] # 冷兵器
ITEM_COLD_DAMAGE = 20
ITEM_ENSURE = ['先锋盾'] # 伤害减半
ITEM_PROTECT = ['刃甲', '锁子甲', '板甲', '圆盾'] # 抵消10点伤害
ITEM_LOCATOR = ['慧光', '银月之晶'] # 查看道具或人物所在地点（GPS）
ITEM_TELESCOPE = ['刷新球', '坚韧球'] # 查看人物持有的道具（望远镜）
ITEM_LOCK = ['王冠'] # 锁区域行动（电击棒）
ITEM_SHOW = ['极限法球'] # 大喇叭（公示器）
ITEM_BOMB = ['黯灭', '漩涡'] # 暗杀系手榴弹
ITEM_KILL = ['圣者遗物'] # 暗杀系氰化钾
ITEM_PERFECT_CURE = ['恐鳖之心'] #生命加满并抵消持续伤害
ITEM_CURE = ['治疗指环'] # 抵消持续伤害或生命+30
ITEM_BANDAGE = ['回复指环'] # 抵消持续伤害或生命+10
ITEM_ACTIVE = ['振奋宝石'] # 体力加满
ITEM_WATER = ['虚无宝石'] # 体力+50

# Actions
MOVE = 'move'
SEARCH = 'search'
PICK = 'pick'
ATTACK = 'attack'
EQUIP = 'equip'
USE = 'use'
THROW = 'throw'
DELIVER = 'deliver'

# 体力消耗配置
COSTS = {
    MOVE: 5, SEARCH: 10, PICK: 5, ATTACK: 10, EQUIP: 0, USE: 0, THROW: 0, DELIVER: 5
}
