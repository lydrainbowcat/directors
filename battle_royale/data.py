from constants import *
import random

def alive_roles():
    res = [v for k, v in roles.items() if v['life'] > 0 and v['life'] <= 100]
    res.sort(key=lambda x: x['order'])
    for role in res:
        role['vote'] = 1
        for item in role['hands']:
            role['vote'] += count_vote(item)
    return res

def count_vote(item):
    if len(items[item]) >= 3:
        return items[item][2]
    return 0

def enabled_places():
    res = [v for k, v in places.items() if v['able']]
    res.sort(key=lambda x: x['order'])
    return res

def all_items():
    return list(items.keys()) + ITEM_PERFECT_CURE + ITEM_CURE * 5 + ITEM_BANDAGE * 5 + ITEM_ACTIVE * 3 + ITEM_WATER * 6

# order: 显示顺序，exists: 当地散落的道具，able: 是否启用
places = {}
for i in range(0, len(PLACES) * 4):
    places[PLACES[i // 4] + DIRECTIONS[i % 4]] = { 'order': i + 1, 'exists': [], 'able': True }

# order: 显示顺序，able: 能否行动，life: 生命，strength: 体力，location: 位置，hands: 手中道具，things: 背包道具
roles = {
    '导演': { 'order': -1, 'life': 1000, 'strength': 100, 'hands': [], 'things': [], 'location': '主席台', 'able': False },
    '观众': { 'order': 0, 'life': 1000, 'strength': 100, 'hands': [], 'things': [], 'location': '看台', 'able': False }
}
for i in range(0, len(ROLES)):
    roles[ROLES[i]] = { 'order': i + 1, 'life': 100, 'strength': 100, 'hands': [], 'things': [], 'location': '', 'able': True }

# [类别，剩余次数]
items = {}
for i in ITEM_HOT_AOE:
    items[i] = [1, 5, 0]
for i in ITEM_HOT_VITAL:
    items[i] = [2, 5, 0]
for i in ITEM_HOT:
    items[i] = [3, 5, 0]
for i in ITEM_COLD:
    items[i] = [4, 100, 1]
for i in ITEM_PROTECT + ITEM_ENSURE:
    items[i] = [5, 100, 2]
for i in ITEM_LOCATOR:
    items[i] = [6, 1, 3]
for i in ITEM_TELESCOPE:
    items[i] = [6, 2, 3]
for i in ITEM_LOCK + ITEM_SHOW:
    items[i] = [7, 1, 3]
for i in ITEM_BOMB + ITEM_KILL:
    items[i] = [8, 1, 0]
for k, v in places.items():
    v['name'] = k

# 随机初始道具
for i in all_items():
    places[random.choice(list(places.keys()))]['exists'].append(i)

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

places = {'妃雪阁北': {'able': True, 'name': '妃雪阁北', 'exists': ['[冷]魍魉', '[炸]麒麟刺', '离舞'], 'order': 12}, '蜃楼南': {'able': True, 'name': '蜃楼南', 'exists': ['焰灵姬'], 'order': 18}, '镜湖医庄北': {'able': True, 'name': '镜湖医庄北', 'exists': ['[侦]含光'], 'order': 28}, '妃雪阁东': {'able': True, 'name': '妃雪阁东', 'exists': [], 'order': 9}, '皇宫北': {'able': True, 'name': '皇宫北', 'exists': [], 'order': 24}, '小圣贤庄西': {'able': True, 'name': '小圣贤庄西', 'exists': [], 'order': 35}, '噬牙狱南': {'able': True, 'name': '噬牙狱南', 'exists': ['[冷]瞬飞轮', '钟离眜'], 'order': 6}, '皇宫南': {'able': True, 'name': '皇宫南', 'exists': [], 'order': 22}, '蜃楼北': {'able': True, 'name': '蜃楼北', 'exists': [], 'order': 20}, '蜃楼西': {'able': True, 'name': '蜃楼西', 'exists': ['项少羽'], 'order': 19}, '炎帝冢北': {'able': True, 'name': '炎帝冢北', 'exists': ['[冷]乱神', '[防]湛卢', '焱妃'], 'order': 16}, '噬牙狱北': {'able': True, 'name': '噬牙狱北', 'exists': ['章邯', '荆轲'], 'order': 8}, '噬牙狱东': {'able': True, 'name': '噬牙狱东', 'exists': ['张良', '墨鸦'], 'order': 5}, '蜃楼东': {'able': True, 'name': '蜃楼东', 'exists': ['[炸]雷神锤', '[MP100]离魂丹', '石兰'], 'order': 17}, '妃雪阁西': {'able': True, 'name': '妃雪阁西', 'exists': ['赤练'], 'order': 11}, '机关城东': {'able': True, 'name': '机关城东', 'exists': ['少司命', '苍狼王', '雪女'], 'order': 1}, '皇宫西': {'able': True, 'name': '皇宫西', 'exists': ['白凤', '盖聂', '李斯'], 'order': 23}, '机关城北': {'able': True, 'name': '机关城北', 'exists': [], 'order': 4}, '蜀山虞渊北': {'able': True, 'name': '蜀山虞渊北', 'exists': ['高渐离'], 'order': 32}, '蜀山虞渊东': {'able': True, 'name': '蜀山虞渊东', 'exists': [], 'order': 29}, '皇宫东': {'able': True, 'name': '皇宫东', 'exists': [], 'order': 21}, '镜湖医庄东': {'able': True, 'name': '镜湖医庄东', 'exists': [], 'order': 25}, '炎帝冢东': {'able': True, 'name': '炎帝冢东', 'exists': ['[HP30]真人丹', '季布'], 'order': 13}, '蜀山虞渊西': {'able': True, 'name': '蜀山虞渊西', 'exists': [], 'order': 31}, '妃雪阁南': {'able': True, 'name': '妃雪阁南', 'exists': [], 'order': 10}, '机关城南': {'able': True, 'name': '机关城南', 'exists': ['[HP30]真人丹', '蒙恬'], 'order': 2}, '镜湖医庄南': {'able': True, 'name': '镜湖医庄南', 'exists': ['[热群]水寒', '[热]琥珀', '星魂'], 'order': 26}, '小圣贤庄北': {'able': True, 'name': '小圣贤庄北', 'exists': ['[冷]惊鲵', '花影'], 'order': 36}, '小圣贤庄南': {'able': True, 'name': '小圣贤庄南', 'exists': ['逍遥子'], 'order': 34}, '镜湖医庄西': {'able': True, 'name': '镜湖医庄西', 'exists': ['弄玉', '姬如千泷'], 'order': 27}, '机关城西': {'able': True, 'name': '机关城西', 'exists': [], 'order': 3}, '炎帝冢南': {'able': True, 'name': '炎帝冢南', 'exists': [], 'order': 14}, '蜀山虞渊南': {'able': True, 'name': '蜀山虞渊南', 'exists': ['荆天明'], 'order': 30}, '炎帝冢西': {'able': True, 'name': '炎帝冢西', 'exists': [], 'order': 15}, '噬牙狱西': {'able': True, 'name': '噬牙狱西', 'exists': ['卫庄', '颜路', '端木蓉'], 'order': 7}, '小圣贤庄东': {'able': True, 'name': '小圣贤庄东', 'exists': ['月神', '鬼谷子', '骨妖'], 'order': 33}}
roles = {'端木蓉': {'strength': 55, 'able': True, 'name': '端木蓉', 'injured': 0, 'order': 16, 'ts': 1566307706.1978798, 'deliver': 0, 'hands': ['[侦]凌虚'], 'things': ['[侦]凌虚'], 'life': 100, 'location': '噬牙狱西'}, '逍遥子': {'strength': 55, 'able': True, 'name': '逍遥子', 'injured': 0, 'order': 19, 'ts': 1566306931.522231, 'deliver': 0, 'hands': ['[热狙]鲨齿'], 'things': ['[热狙]鲨齿', '[热]破阵霸王枪'], 'life': 100, 'location': '小圣贤庄南'}, '月神': {'strength': 100, 'able': True, 'name': '月神', 'injured': 0, 'order': 27, 'ts': 0, 'deliver': 0, 'hands': [], 'things': [], 'life': 100, 'location': '小圣贤庄东'}, '晓梦': {'strength': 5, 'able': False, 'name': '晓梦', 'injured': 0, 'order': 31, 'ts': 1566307034.198642, 'deliver': 0, 'hands': [], 'things': [], 'life': 0, 'location': '小圣贤庄南'}, '盖聂': {'strength': 50, 'able': True, 'name': '盖聂', 'injured': 0, 'order': 11, 'ts': 1566307074.8034813, 'deliver': 0, 'hands': ['[冷]断水', '[毒]残虹'], 'things': ['[冷]断水', '[冷]寒蝉', '[毒]残虹'], 'life': 10, 'location': '皇宫西'}, '荆天明': {'strength': 50, 'able': True, 'name': '荆天明', 'injured': 0, 'order': 20, 'ts': 1566306867.9968097, 'deliver': 0, 'hands': ['[防]纯钧'], 'things': ['[防]纯钧'], 'life': 100, 'location': '蜀山虞渊南'}, '苍狼王': {'strength': 60, 'able': True, 'name': '苍狼王', 'injured': 0, 'order': 2, 'ts': 1566306781.6699536, 'deliver': 0, 'hands': ['[冷]真刚'], 'things': ['[冷]真刚', '[HP10]清疏丹'], 'life': 100, 'location': '机关城东'}, '姬如千泷': {'strength': 75, 'able': True, 'name': '姬如千泷', 'injured': 0, 'order': 12, 'ts': 1566306936.6675656, 'deliver': 0, 'hands': ['[防]赤瞳', '[热狙]天问'], 'things': ['[防]赤瞳', '[热狙]天问'], 'life': 100, 'location': '镜湖医庄西'}, '少司命': {'strength': 55, 'able': True, 'name': '少司命', 'injured': 0, 'order': 10, 'ts': 1566306940.6146357, 'deliver': 0, 'hands': ['[热]干将'], 'things': ['[热]干将'], 'life': 50, 'location': '机关城东'}, '赤练': {'strength': 85, 'able': True, 'name': '赤练', 'injured': 0, 'order': 9, 'ts': 1566307229.455646, 'deliver': 0, 'hands': ['[防]天照', '[冷]转魄'], 'things': ['[热]莫邪', '[HP30]真人丹', '[冷]转魄', '[防]天照'], 'life': 100, 'location': '妃雪阁西'}, '张良': {'strength': 75, 'able': True, 'name': '张良', 'injured': 0, 'order': 13, 'ts': 1566307118.784658, 'deliver': 0, 'hands': ['[高防]扶桑神木'], 'things': ['[高防]扶桑神木', '[公示]逆鳞'], 'life': 55, 'location': '噬牙狱东'}, '墨鸦': {'strength': 85, 'able': True, 'name': '墨鸦', 'injured': 0, 'order': 5, 'ts': 1566307602.257993, 'deliver': 0, 'hands': ['[冷]掩日', '[GPS]非攻'], 'things': ['[冷]掩日', '[GPS]非攻'], 'life': 100, 'location': '噬牙狱东'}, '焰灵姬': {'strength': 60, 'able': True, 'name': '焰灵姬', 'injured': 0, 'order': 3, 'ts': 1566307310.9222484, 'deliver': 0, 'hands': ['[热狙]赤霄'], 'things': ['[热狙]赤霄', '[冷]灭魂'], 'life': 70, 'location': '蜃楼南'}, '观众': {'strength': 100, 'able': False, 'name': '观众', 'injured': 0, 'order': 0, 'ts': 0, 'deliver': 0, 'hands': [], 'things': [], 'life': 1000, 'location': '看台'}, '季布': {'strength': 100, 'able': True, 'name': '季布', 'injured': 0, 'order': 26, 'ts': 0, 'deliver': 0, 'hands': [], 'things': [], 'life': 100, 'location': '炎帝冢东'}, '钟离眜': {'strength': 100, 'able': True, 'name': '钟离眜', 'injured': 0, 'order': 29, 'ts': 0, 'deliver': 0, 'hands': [], 'things': [], 'life': 50, 'location': '噬牙狱南'}, '焱妃': {'strength': 100, 'able': True, 'name': '焱妃', 'injured': 0, 'order': 21, 'ts': 0, 'deliver': 0, 'hands': [], 'things': [], 'life': 100, 'location': '炎帝冢北'}, '离舞': {'strength': 100, 'able': True, 'name': '离舞', 'injured': 0, 'order': 15, 'ts': 0, 'deliver': 0, 'hands': [], 'things': [], 'life': 100, 'location': '妃雪阁北'}, '白凤': {'strength': 60, 'able': True, 'name': '白凤', 'injured': 0, 'order': 23, 'ts': 1566306881.5038762, 'deliver': 0, 'hands': ['[热]巨阙'], 'things': ['[热]巨阙', '[热群]雪霁'], 'life': 40, 'location': '皇宫西'}, '花影': {'strength': 100, 'able': True, 'name': '花影', 'injured': 0, 'order': 18, 'ts': 0, 'deliver': 0, 'hands': [], 'things': [], 'life': 100, 'location': '小圣贤庄北'}, '李斯': {'strength': 50, 'able': True, 'name': '李斯', 'injured': 0, 'order': 6, 'ts': 1566307366.9068892, 'deliver': 0, 'hands': ['[防]霜魂'], 'things': ['[防]霜魂'], 'life': 80, 'location': '皇宫西'}, '骨妖': {'strength': 50, 'able': True, 'name': '骨妖', 'injured': 0, 'order': 4, 'ts': 1566306879.0726082, 'deliver': 0, 'hands': ['[冷]链蛇软剑'], 'things': ['[冷]链蛇软剑', '[HP10]清疏丹'], 'life': 100, 'location': '小圣贤庄东'}, '章邯': {'strength': 50, 'able': True, 'name': '章邯', 'injured': 0, 'order': 32, 'ts': 1566307679.7866042, 'deliver': 0, 'hands': ['[热群]秋骊'], 'things': ['[热]太阿', '[热群]秋骊'], 'life': 10, 'location': '噬牙狱北'}, '鬼谷子': {'strength': 50, 'able': True, 'name': '鬼谷子', 'injured': 0, 'order': 17, 'ts': 1566307766.3824043, 'deliver': 0, 'hands': ['[热狙]渊虹'], 'things': ['[HP10]清疏丹', '[冷]玄翦', '[热狙]渊虹'], 'life': 100, 'location': '小圣贤庄东'}, '导演': {'strength': 100, 'able': False, 'name': '导演', 'injured': 0, 'order': -1, 'ts': 0, 'deliver': 0, 'hands': [], 'things': [], 'life': 1000, 'location': '主席台'}, '高渐离': {'strength': 100, 'able': True, 'name': '高渐离', 'injured': 0, 'order': 14, 'ts': 0, 'deliver': 0, 'hands': [], 'things': [], 'life': 100, 'location': '蜀山虞渊北'}, '项少羽': {'strength': 75, 'able': True, 'name': '项少羽', 'injured': 0, 'order': 1, 'ts': 1566306700.819351, 'deliver': 0, 'hands': [], 'things': ['[HP30]真人丹', '[锁]幻音宝盒'], 'life': 100, 'location': '蜃楼西'}, '颜路': {'strength': 50, 'able': True, 'name': '颜路', 'injured': 0, 'order': 22, 'ts': 1566307517.51045, 'deliver': 0, 'hands': ['[防]镇岳'], 'things': ['[防]镇岳', '[防]黄金牡丹', '[GPS]墨眉'], 'life': 10, 'location': '噬牙狱西'}, '雪女': {'strength': 55, 'able': True, 'name': '雪女', 'injured': 0, 'order': 8, 'ts': 1566307175.9585614, 'deliver': 0, 'hands': [], 'things': [], 'life': 100, 'location': '机关城东'}, '卫庄': {'strength': 75, 'able': True, 'name': '卫庄', 'injured': 0, 'order': 7, 'ts': 1566306912.4869456, 'deliver': 0, 'hands': [], 'things': ['[HP100]碧血玉叶花', '[HP10]清疏丹'], 'life': 100, 'location': '噬牙狱西'}, '荆轲': {'strength': 50, 'able': True, 'name': '荆轲', 'injured': 0, 'order': 24, 'ts': 1566307281.3307323, 'deliver': 0, 'hands': ['[冷]羽刃'], 'things': ['[冷]羽刃'], 'life': 100, 'location': '噬牙狱北'}, '石兰': {'strength': 100, 'able': True, 'name': '石兰', 'injured': 0, 'order': 28, 'ts': 0, 'deliver': 0, 'hands': [], 'things': [], 'life': 100, 'location': '蜃楼东'}, '蒙恬': {'strength': 100, 'able': True, 'name': '蒙恬', 'injured': 0, 'order': 33, 'ts': 0, 'deliver': 0, 'hands': [], 'things': [], 'life': 100, 'location': '机关城南'}, '弄玉': {'strength': 100, 'able': True, 'name': '弄玉', 'injured': 0, 'order': 30, 'ts': 0, 'deliver': 0, 'hands': [], 'things': [], 'life': 100, 'location': '镜湖医庄西'}, '星魂': {'strength': 100, 'able': True, 'name': '星魂', 'injured': 0, 'order': 25, 'ts': 0, 'deliver': 0, 'hands': [], 'things': [], 'life': 100, 'location': '镜湖医庄南'}}
items = {'[GPS]非攻': [6, 1], '[热狙]鲨齿': [2, 3], '[高防]扶桑神木': [5, 100], '[防]镇岳': [5, 100], '[防]黄金牡丹': [5, 100], '[侦]含光': [6, 2], '[热]莫邪': [3, 1], '[热群]水寒': [1, 5], '[冷]玄翦': [4, 100], '[冷]寒蝉': [4, 100], '[防]霜魂': [5, 100], '[防]纯钧': [5, 100], '[防]天照': [5, 100], '[毒]残虹': [8, 1], '[冷]链蛇软剑': [4, 100], '[冷]惊鲵': [4, 100], '[热]破阵霸王枪': [3, 5], '[热狙]天问': [2, 5], '[热狙]渊虹': [2, 5], '[公示]逆鳞': [7, 1], '[热狙]赤霄': [2, 4], '[热群]雪霁': [1, 5], '[防]赤瞳': [5, 100], '[冷]魍魉': [4, 100], '[冷]瞬飞轮': [4, 100], '[冷]真刚': [4, 100], '[冷]灭魂': [4, 100], '[热]太阿': [3, 4], '[冷]转魄': [4, 100], '[冷]羽刃': [4, 99], '[炸]雷神锤': [8, 1], '[冷]断水': [4, 100], '[炸]麒麟刺': [8, 1], '[侦]凌虚': [6, 2], '[冷]乱神': [4, 100], '[防]湛卢': [5, 100], '[热]琥珀': [3, 5], '[热]巨阙': [3, 4], '[热]干将': [3, 5], '[锁]幻音宝盒': [7, 1], '[热群]秋骊': [1, 5], '[炸]鸩羽千夜': [8, 1], '[冷]掩日': [4, 100], '[GPS]墨眉': [6, 1]}
