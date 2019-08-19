# 地点配置，可更改名称，不可直接更改地点数量
PLACES = ['机关城', '噬牙狱', '妃雪阁', '炎帝冢', '蜃楼', '皇宫', '镜湖医庄', '蜀山虞渊', '小圣贤庄']
DIRECTIONS = ['东', '南', '西', '北']

# 角色配置
ROLES = ['项少羽', '苍狼王', '焰灵姬', '骨妖', '墨鸦', '李斯', '卫庄', '雪女', '赤练', '少司命', '盖聂', '姬如千泷', '张良', '高渐离', '离舞', '端木蓉', '鬼谷子', '花影', '逍遥子', '荆天明', '焱妃', '颜路', '白凤', '荆轲', '星魂', '季布', '月神', '石兰', '钟离眜', '弄玉', '晓梦', '章邯', '蒙恬']
PASSWORDS = ['iq4458', 'qgbc48', 'k74107', '671126', 'lzl517', '790990', 'ipg653', '555436', 'mmgr23', '935865', 'ooi021', 'mb8960', '211516', '698082', '263621', '695337', 'vty509', 'h44075', 'xrh590', 'bchw03', 'vnv977', 'tcy541', 'ggbu05', 'psvn88', '214934', 'yi8149', 'nhyw69', 'uog726', 'sxo952', 'k44387', 'sc0049', 'szi891', 'n87499']
DIRECTOR_PASSWORD = 'yu92aq68'
AUDIENCE_PASSWORD = 'test'

# 道具配置
ITEM_HOT_AOE = ['[热群]水寒', '[热群]秋骊', '[热群]雪霁'] # AOE热武器（带持续伤害）
ITEM_HOT_AOE_DAMAGE = 40
ITEM_HOT_VITAL = ['[热狙]天问', '[热狙]鲨齿', '[热狙]赤霄', '[热狙]渊虹'] # 狙击类热武器
ITEM_HOT_VITAL_DAMAGE = 80
ITEM_HOT = ['[热]太阿', '[热]干将', '[热]莫邪', '[热]巨阙', '[热]琥珀', '[热]破阵霸王枪'] # 热武器
ITEM_HOT_DAMAGE = 40
ITEM_COLD = ['[冷]掩日', '[冷]惊鲵', '[冷]玄翦', '[冷]真刚', '[冷]断水', '[冷]乱神', '[冷]魍魉', '[冷]转魄', '[冷]灭魂', '[冷]羽刃', '[冷]瞬飞轮', '[冷]链蛇软剑', '[冷]寒蝉'] # 冷兵器
ITEM_COLD_DAMAGE = 20
ITEM_ENSURE = ['[高防]扶桑神木'] # 伤害减半
ITEM_PROTECT = ['[防]镇岳', '[防]纯钧', '[防]湛卢', '[防]霜魂', '[防]赤瞳', '[防]天照', '[防]黄金牡丹'] # 抵消10点伤害
ITEM_LOCATOR = ['[GPS]墨眉', '[GPS]非攻'] # 查看道具或人物所在地点（GPS）
ITEM_TELESCOPE = ['[侦]凌虚', '[侦]含光'] # 查看人物持有的道具（望远镜）
ITEM_LOCK = ['[锁]幻音宝盒'] # 锁区域行动（电击棒）
ITEM_SHOW = ['[公示]逆鳞'] # 大喇叭（公示器）
ITEM_BOMB = ['[炸]雷神锤', '[炸]麒麟刺', '[炸]鸩羽千夜'] # 暗杀系手榴弹
ITEM_KILL = ['[毒]残虹'] # 暗杀系氰化钾
ITEM_PERFECT_CURE = ['[HP100]碧血玉叶花'] #生命加满并抵消持续伤害
ITEM_CURE = ['[HP30]真人丹'] # 抵消持续伤害或生命+30
ITEM_BANDAGE = ['[HP10]清疏丹'] # 抵消持续伤害或生命+10
ITEM_ACTIVE = ['[MP100]离魂丹'] # 体力加满
ITEM_WATER = ['[MP50]御鬼丹'] # 体力+50

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
