# order: 显示顺序，exists: 当地散落的道具，able: 是否启用
places = {
    '哼哼井东': { 'order': 1, 'exists': ['板甲', '振奋宝石'], 'able': True },
    '哼哼井南': { 'order': 2, 'exists': ['代达罗斯之殇', '回复指环'], 'able': True },
    '哼哼井西': { 'order': 3, 'exists': ['标枪'], 'able': True },
    '哼哼井北': { 'order': 4, 'exists': ['圆盾'], 'able': True },
    '达达城东': { 'order': 5, 'exists': ['狂战斧', '阔剑'], 'able': True },
    '达达城南': { 'order': 6, 'exists': ['锁子甲'], 'able': True },
    '达达城西': { 'order': 7, 'exists': ['恶魔刀锋'], 'able': True },
    '达达城北': { 'order': 8, 'exists': ['掠夺者之斧'], 'able': True },
    '丹丹堡东': { 'order': 9, 'exists': ['慧光', '虚无宝石'], 'able': True },
    '丹丹堡南': { 'order': 10, 'exists': ['金箍棒', '虚无宝石'], 'able': True },
    '丹丹堡西': { 'order': 11, 'exists': ['短棍'], 'able': True },
    '丹丹堡北': { 'order': 12, 'exists': ['漩涡'], 'able': True },
    '沙沙寨东': { 'order': 13, 'exists': ['圣剑'], 'able': True },
    '沙沙寨南': { 'order': 14, 'exists': ['振奋宝石', '回复指环'], 'able': True },
    '沙沙寨西': { 'order': 15, 'exists': ['先锋盾'], 'able': True },
    '沙沙寨北': { 'order': 16, 'exists': ['水晶剑'], 'able': True },
    '苏苏林东': { 'order': 17, 'exists': ['坚韧球'], 'able': True },
    '苏苏林南': { 'order': 18, 'exists': ['攻击之爪'], 'able': True },
    '苏苏林西': { 'order': 19, 'exists': ['黯灭', '虚无宝石'], 'able': True },
    '苏苏林北': { 'order': 20, 'exists': ['治疗指环'], 'able': True },
    '格格屋东': { 'order': 21, 'exists': ['雷神之锤'], 'able': True },
    '格格屋南': { 'order': 22, 'exists': ['治疗指环', '虚无宝石'], 'able': True },
    '格格屋西': { 'order': 23, 'exists': ['达贡之神力', '吸血面具'], 'able': True },
    '格格屋北': { 'order': 24, 'exists': ['王冠'], 'able': True },
    '月月丛东': { 'order': 25, 'exists': ['极限法球'], 'able': True },
    '月月丛西': { 'order': 26, 'exists': ['邪恶镰刀'], 'able': True },
    '月月丛南': { 'order': 27, 'exists': ['银月之晶', '回复指环'], 'able': True },
    '月月丛北': { 'order': 28, 'exists': ['神秘法杖', '圣者遗物', '回复指环'], 'able': True },
    '加加岛东': { 'order': 29, 'exists': ['刷新球'], 'able': True },
    '加加岛南': { 'order': 30, 'exists': ['跳刀', '秘银锤'], 'able': True },
    '加加岛西': { 'order': 31, 'exists': ['恐鳖之心'], 'able': True },
    '加加岛北': { 'order': 32, 'exists': ['刃甲', '虚无宝石'], 'able': True }
}

# order: 显示顺序，able: 能否行动，life: 生命，strength: 体力，location: 位置，hands: 手中道具，things: 背包道具
roles = {
    '导演': { 'order': -1, 'life': 1000, 'strength': 100, 'hands': [], 'things': [], 'location': '主席台', 'able': False },
    '观众': { 'order': 0, 'life': 1000, 'strength': 100, 'hands': [], 'things': [], 'location': '看台', 'able': False },
    '风行者': { 'order': 1, 'life': 100, 'strength': 100, 'hands': [], 'things': [], 'location': '', 'able': True },
    '变体精灵': { 'order': 2, 'life': 100, 'strength': 100, 'hands': [], 'things': [], 'location': '', 'able': True },
    '死亡骑士': { 'order': 3, 'life': 100, 'strength': 100, 'hands': [], 'things': [], 'location': '', 'able': True },
    '沙王': { 'order': 4, 'life': 100, 'strength': 100, 'hands': [], 'things': [], 'location': '', 'able': True },
    '水晶室女': { 'order': 5, 'life': 100, 'strength': 100, 'hands': [], 'things': [], 'location': '', 'able': True },
    '精灵守卫': { 'order': 6, 'life': 100, 'strength': 100, 'hands': [], 'things': [], 'location': '', 'able': True },
    '龙骑士': { 'order': 7, 'life': 100, 'strength': 100, 'hands': [], 'things': [], 'location': '', 'able': True },
    '敌法师': { 'order': 8, 'life': 100, 'strength': 100, 'hands': [], 'things': [], 'location': '', 'able': True },
    '灵魂守卫': { 'order': 9, 'life': 100, 'strength': 100, 'hands': [], 'things': [], 'location': '', 'able': True },
    '海军上将': { 'order': 10, 'life': 100, 'strength': 100, 'hands': [], 'things': [], 'location': '', 'able': True },
    '幻影刺客': { 'order': 11, 'life': 100, 'strength': 100, 'hands': [], 'things': [], 'location': '', 'able': True },
    '月之女祭司': { 'order': 12, 'life': 100, 'strength': 100, 'hands': [], 'things': [], 'location': '', 'able': True },
    '谜团': { 'order': 13, 'life': 100, 'strength': 100, 'hands': [], 'things': [], 'location': '', 'able': True },
    '狙击手': { 'order': 14, 'life': 100, 'strength': 100, 'hands': [], 'things': [], 'location': '', 'able': True },
    '卓尔游侠': { 'order': 15, 'life': 100, 'strength': 100, 'hands': [], 'things': [], 'location': '', 'able': True },
    '巫医': { 'order': 16, 'life': 100, 'strength': 100, 'hands': [], 'things': [], 'location': '', 'able': True },
    '月之骑士': { 'order': 17, 'life': 100, 'strength': 100, 'hands': [], 'things': [], 'location': '', 'able': True },
    '秀逗魔导士': { 'order': 18, 'life': 100, 'strength': 100, 'hands': [], 'things': [], 'location': '', 'able': True },
    '圣堂刺客': { 'order': 19, 'life': 100, 'strength': 100, 'hands': [], 'things': [], 'location': '', 'able': True },
    '精灵龙': { 'order': 20, 'life': 100, 'strength': 100, 'hands': [], 'things': [], 'location': '', 'able': True },
    '小小': { 'order': 21, 'life': 100, 'strength': 100, 'hands': [], 'things': [], 'location': '', 'able': True },
    '巨牙海民': { 'order': 22, 'life': 100, 'strength': 100, 'hands': [], 'things': [], 'location': '', 'able': True },
    '光之守卫': { 'order': 23, 'life': 100, 'strength': 100, 'hands': [], 'things': [], 'location': '', 'able': True },
    '魅惑魔女': { 'order': 24, 'life': 100, 'strength': 100, 'hands': [], 'things': [], 'location': '', 'able': True },
    '鱼人夜行者': { 'order': 25, 'life': 100, 'strength': 100, 'hands': [], 'things': [], 'location': '', 'able': True },
    '狼人': { 'order': 26, 'life': 100, 'strength': 100, 'hands': [], 'things': [], 'location': '', 'able': True },
    '影魔': { 'order': 27, 'life': 100, 'strength': 100, 'hands': [], 'things': [], 'location': '', 'able': True },
}

# [类别，剩余次数]
items = {
    '狂战斧': [1,5],
    '雷神之锤': [1,5],
    '金箍棒': [1,5],
    '代达罗斯之殇': [2,5],
    '达贡之神力': [2,5],
    '圣剑': [2,5],
    '恶魔刀锋': [3,5],
    '水晶剑': [3,5],
    '邪恶镰刀': [3,5],
    '掠夺者之斧': [3,5],
    '标枪': [4,100],
    '攻击之爪': [4,100],
    '短棍': [4,100],
    '阔剑': [4,100],
    '跳刀': [4,100],
    '秘银锤': [4,100],
    '吸血面具': [4,100],
    '神秘法杖': [4,100],
    '刃甲': [5,100],
    '锁子甲': [5,100],
    '板甲': [5,100],
    '圆盾': [5,100],
    '先锋盾': [5,100],
    '慧光': [6,1],
    '银月之晶': [6,1],
    '刷新球': [6,2],
    '坚韧球': [6,2],
    # '法师长袍': [7,1],
    # '抗魔斗篷': [7,1],
    '王冠': [7,1],
    '极限法球': [7,1],
    '黯灭': [8,1],
    '漩涡': [8,1],
    '圣者遗物': [8,1]
}

for k, v in places.items():
    v['name'] = k

for k, v in roles.items():
    v['name'] = k
    v['injured'] = v.get('injured', 0)
    v['deliver'] = v.get('deliver', 0)
    if v['able'] and len(v['location']) > 0:
        try:
            places[v['location']]['exists'].remove(k)
        except:
            pass
        places[v['location']]['exists'].append(k)
    if v['life'] <= 0:
        v['hands'] = []
        v['things'] = []
    v['ts'] = 0

def alive_roles():
    res = [v for k, v in roles.items() if v['life'] > 0 and v['life'] <= 100]
    res.sort(key=lambda x: x['order'])
    return res

def enabled_places():
    res = [v for k, v in places.items() if v['able']]
    res.sort(key=lambda x: x['order'])
    return res

def all_items():
    return list(items.keys()) + ['虚无宝石', '振奋宝石', '回复指环', '治疗指环', '恐鳖之心']
