# 地点配置
PLACES = ['码头', '工厂', '贫民窟', '旅馆', '教堂', '市政厅', '消防局', '池塘', '住宅区', '灯塔', '小巷', '学校', '隧道', '山道', '寺庙', '靶场', '医院', '森林', '海滩', '墓园', '井']
DIRECTIONS = ['东', '南', '西', '北']
DIRECTIONS_ENABLED = False # 是否启用方位

# 角色配置
ROLES = ['溪风', '慕容紫英', '夏侯瑾轩', '赵灵儿', '龙溟', '楚寒镜', '明绣', '闲卿', '凌波', '徐长卿', '林月如', '沈欺霜', '景天', '龙葵', '龙阳', '唐钰', '阿奴', '青儿', '云天河', '草谷', '酒剑仙', '唐雪见', '苏媚', '云霆', '王小虎', '楚碧痕', '重楼', '唐雨柔', '姜云凡', '小蛮', '韩菱纱', '女苑']
PASSWORDS = ['gzkw51', 'x68295', 'ecb740', 'f72869', 'w91792', 'fnnv10', '666730', 'ml0809', 'z65583', '286034', 'o48277', '685125', 'xh7025', 'pc6638', 'lw9528', 'w69823', 'r29040', 'bdfw85', 'q75297', 'cyy052', 'szg571', '958201', 'vzr223', 'hik272', 'gexb00', '506219', 'a40717', 'xpka61', 'mf2620', 'qt9968', 'wsx43r', '898725']
DIRECTOR_PASSWORD = 'ang708j3'
AUDIENCE_PASSWORD = 'test'

# 道具配置
# 可通过在道具和人物名称中增加"<职业>"来限制人物可使用的道具
# 人物的职业后面可以增加一个字，例如标有<弓箭>的武器可对应标有<弓箭>或<弓箭手>的人物
# 例如"[冷]<弓箭>诸葛连弩"只能被"酌杯<弓箭手>"使用，不能被"小妤<投掷手>"和"取酒"使用
ITEM_HOT_AOE = ['[热群]雷灵珠', '[热群]火灵珠', '[热群]土灵珠'] # AOE热武器（带持续伤害）
ITEM_HOT_AOE_DAMAGE = 40
ITEM_HOT_VITAL = ['[热狙]七巧弓', '[热狙]火神弓', '[热狙]幽冥弓', '[热狙]射日弓'] # 狙击类热武器
ITEM_HOT_VITAL_DAMAGE = 80
ITEM_HOT = ['[热]降魔杖', '[热]灵泉杖', '[热]桃木杖', '[热]轰雷杖', '[热]鬼头杖', '[热]天蛇杖'] # 热武器
ITEM_HOT_DAMAGE = 40
ITEM_COLD = ['[冷]青锋剑', '[冷]越女剑', '[冷]龙泉剑', '[冷]无尘剑', '[冷]七星剑', '[冷]天绝剑', '[冷]太极剑', '[冷]凌风剑', '[冷]星辰剑', '[冷]镇妖剑', '[冷]望舒剑', '[冷]羲和剑', '[冷]玄铁剑'] # 冷兵器
ITEM_COLD_DAMAGE = 20
ITEM_ENSURE = ['[高防]广袖流仙裙'] # 伤害减半
ITEM_PROTECT = ['[防]璇龟甲', '[防]软藤甲', '[防]碧鳞甲', '[防]翼云甲', '[防]护胸甲', '[防]青铜甲', '[防]磷光甲'] # 抵消10点伤害
ITEM_PROTECT_VALUE = 10 # 防具抵御的伤害量
ITEM_LOCATOR = ['[GPS]灵心符', '[GPS]天师符'] # 查看道具所在地点（GPS）
ITEM_TELESCOPE = ['[侦]八卦镜', '[侦]乾坤镜'] # 查看人物持有的道具（望远镜）
ITEM_LOCK = ['[锁]女娲玉'] # 锁区域行动（电击棒）
ITEM_SHOW = ['[扬声]极目水'] # 大喇叭（公示器）
ITEM_BOMB = ['[炸]血海棠', '[炸]孔雀胆', '[炸]断肠草'] # 暗杀系手榴弹
ITEM_KILL = ['[毒]无影毒'] # 暗杀系氰化钾
ITEM_PERFECT_CURE = ['[HP100]天香续命露'] #生命加满并抵消持续伤害
ITEM_CURE = ['[HP30]舍利子'] # 抵消持续伤害或生命+30
ITEM_BANDAGE = ['[HP10]雪莲子'] # 抵消持续伤害或生命+10
ITEM_ACTIVE = ['[MP100]还神丹'] # 体力加满
ITEM_WATER = ['[MP50]行军丹'] # 体力+50

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
