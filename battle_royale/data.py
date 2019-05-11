# order: 显示顺序，exists: 当地散落的道具，able: 是否启用
places = {
    '墓地东': { 'order': 1, 'exists': [], 'able': True },
    '墓地南': { 'order': 2, 'exists': [], 'able': True },
    '墓地西': { 'order': 3, 'exists': [], 'able': True },
    '墓地北': { 'order': 4, 'exists': [], 'able': True },
    '医院东': { 'order': 5, 'exists': [], 'able': True },
    '医院南': { 'order': 6, 'exists': [], 'able': True },
    '医院西': { 'order': 7, 'exists': [], 'able': True },
    '医院北': { 'order': 8, 'exists': [], 'able': True },
    '海岸东': { 'order': 9, 'exists': [], 'able': True },
    '海岸南': { 'order': 10, 'exists': [], 'able': True },
    '海岸西': { 'order': 11, 'exists': [], 'able': True },
    '海岸北': { 'order': 12, 'exists': [], 'able': True },
    '工厂东': { 'order': 13, 'exists': [], 'able': True },
    '工厂南': { 'order': 14, 'exists': [], 'able': True },
    '工厂西': { 'order': 15, 'exists': [], 'able': True },
    '工厂北': { 'order': 16, 'exists': [], 'able': True },
    '树林东': { 'order': 17, 'exists': [], 'able': True },
    '树林南': { 'order': 18, 'exists': [], 'able': True },
    '树林西': { 'order': 19, 'exists': [], 'able': True },
    '树林北': { 'order': 20, 'exists': [], 'able': True },
    '邮局东': { 'order': 21, 'exists': [], 'able': True },
    '邮局南': { 'order': 22, 'exists': [], 'able': True },
    '邮局西': { 'order': 23, 'exists': [], 'able': True },
    '邮局北': { 'order': 24, 'exists': [], 'able': True },
    '机场东': { 'order': 25, 'exists': [], 'able': True },
    '机场西': { 'order': 26, 'exists': [], 'able': True },
    '机场南': { 'order': 27, 'exists': [], 'able': True },
    '机场北': { 'order': 28, 'exists': [], 'able': True },
    '学校东': { 'order': 29, 'exists': [], 'able': True },
    '学校南': { 'order': 30, 'exists': [], 'able': True },
    '学校西': { 'order': 31, 'exists': [], 'able': True },
    '学校北': { 'order': 32, 'exists': [], 'able': True },
    '住宅东': { 'order': 33, 'exists': [], 'able': True },
    '住宅南': { 'order': 34, 'exists': [], 'able': True },
    '住宅西': { 'order': 35, 'exists': [], 'able': True },
    '住宅北': { 'order': 36, 'exists': [], 'able': True }
}

# order: 显示顺序，able: 能否行动，life: 生命，strength: 体力，location: 位置，hands: 手中道具，things: 背包道具
roles = {
    '导演': { 'order': -1, 'life': 1000, 'strength': 100, 'hands': [], 'things': [], 'location': '主席台', 'able': False },
    '观众': { 'order': 0, 'life': 1000, 'strength': 100, 'hands': [], 'things': [], 'location': '看台', 'able': False },
    '黑长博': { 'order': 1, 'life': 100, 'strength': 100, 'hands': [], 'things': [], 'location': '学校东', 'able': True },
    '藤吉文世': { 'order': 2, 'life': 100, 'strength': 100, 'hands': [], 'things': [], 'location': '学校东', 'able': True },
    '松井知里': { 'order': 3, 'life': 100, 'strength': 100, 'hands': [], 'things': [], 'location': '学校东', 'able': True },
    '相马光子': { 'order': 4, 'life': 100, 'strength': 100, 'hands': [], 'things': [], 'location': '学校东', 'able': True },
    '琴弹加代子': { 'order': 5, 'life': 100, 'strength': 100, 'hands': [], 'things': [], 'location': '学校东', 'able': True },
    '中川有香': { 'order': 6, 'life': 100, 'strength': 100, 'hands': [], 'things': [], 'location': '学校东', 'able': True },
    '濑户丰': { 'order': 7, 'life': 100, 'strength': 100, 'hands': [], 'things': [], 'location': '学校东', 'able': True },
    '南佳织': { 'order': 8, 'life': 100, 'strength': 100, 'hands': [], 'things': [], 'location': '学校东', 'able': True },
    '元渊恭一': { 'order': 9, 'life': 100, 'strength': 100, 'hands': [], 'things': [], 'location': '学校东', 'able': True },
    '矢作好美': { 'order': 10, 'life': 100, 'strength': 100, 'hands': [], 'things': [], 'location': '学校东', 'able': True },
    '日下由美子': { 'order': 11, 'life': 100, 'strength': 100, 'hands': [], 'things': [], 'location': '学校东', 'able': True },
    '川田章吾': { 'order': 12, 'life': 100, 'strength': 100, 'hands': [], 'things': [], 'location': '学校东', 'able': True },
    '三村信史': { 'order': 13, 'life': 100, 'strength': 100, 'hands': [], 'things': [], 'location': '学校东', 'able': True },
    '稻田瑞穗': { 'order': 14, 'life': 100, 'strength': 100, 'hands': [], 'things': [], 'location': '学校东', 'able': True },
    '沼井充': { 'order': 15, 'life': 100, 'strength': 100, 'hands': [], 'things': [], 'location': '学校东', 'able': True },
    '大木立道': { 'order': 16, 'life': 100, 'strength': 100, 'hands': [], 'things': [], 'location': '学校东', 'able': True },
    '山本和彦': { 'order': 17, 'life': 100, 'strength': 100, 'hands': [], 'things': [], 'location': '学校东', 'able': True },
    '月冈彰': { 'order': 18, 'life': 100, 'strength': 100, 'hands': [], 'things': [], 'location': '学校东', 'able': True },
    '饭岛敬太': { 'order': 19, 'life': 100, 'strength': 100, 'hands': [], 'things': [], 'location': '学校东', 'able': True },
    '国信庆时': { 'order': 20, 'life': 100, 'strength': 100, 'hands': [], 'things': [], 'location': '学校东', 'able': True },
    '织田敏宪': { 'order': 21, 'life': 100, 'strength': 100, 'hands': [], 'things': [], 'location': '学校东', 'able': True },
    '笹川龙平': { 'order': 22, 'life': 100, 'strength': 100, 'hands': [], 'things': [], 'location': '学校东', 'able': True },
    '野田聪美': { 'order': 23, 'life': 100, 'strength': 100, 'hands': [], 'things': [], 'location': '学校东', 'able': True },
    '中川典子': { 'order': 24, 'life': 100, 'strength': 100, 'hands': [], 'things': [], 'location': '学校东', 'able': True },
    '赤松义生': { 'order': 25, 'life': 100, 'strength': 100, 'hands': [], 'things': [], 'location': '学校东', 'able': True },
    '小川樱': { 'order': 26, 'life': 100, 'strength': 100, 'hands': [], 'things': [], 'location': '学校东', 'able': True },
    '仓元洋二': { 'order': 27, 'life': 100, 'strength': 100, 'hands': [], 'things': [], 'location': '学校东', 'able': True },
    '榊祐子': { 'order': 28, 'life': 100, 'strength': 100, 'hands': [], 'things': [], 'location': '学校东', 'able': True },
    '新井田和志': { 'order': 29, 'life': 100, 'strength': 100, 'hands': [], 'things': [], 'location': '学校东', 'able': True },
    '泷口优一郎': { 'order': 30, 'life': 100, 'strength': 100, 'hands': [], 'things': [], 'location': '学校东', 'able': True },
    '金井泉': { 'order': 31, 'life': 100, 'strength': 100, 'hands': [], 'things': [], 'location': '学校东', 'able': True },
    '天堂真弓': { 'order': 32, 'life': 100, 'strength': 100, 'hands': [], 'things': [], 'location': '学校东', 'able': True },
    '清水比吕乃': { 'order': 33, 'life': 100, 'strength': 100, 'hands': [], 'things': [], 'location': '学校东', 'able': True },
    '旗上忠胜': { 'order': 34, 'life': 100, 'strength': 100, 'hands': [], 'things': [], 'location': '学校东', 'able': True },
    '千草贵子': { 'order': 35, 'life': 100, 'strength': 100, 'hands': [], 'things': [], 'location': '学校东', 'able': True },
    '七原秋也': { 'order': 36, 'life': 100, 'strength': 100, 'hands': [], 'things': [], 'location': '学校东', 'able': True },
    '江藤惠': { 'order': 37, 'life': 100, 'strength': 100, 'hands': [], 'things': [], 'location': '学校东', 'able': True },
    '桐山和雄': { 'order': 38, 'life': 100, 'strength': 100, 'hands': [], 'things': [], 'location': '学校东', 'able': True },
    '杉村弘树': { 'order': 39, 'life': 100, 'strength': 100, 'hands': [], 'things': [], 'location': '学校东', 'able': True },
    '北野雪子': { 'order': 40, 'life': 100, 'strength': 100, 'hands': [], 'things': [], 'location': '学校东', 'able': True },
    '谷泽遥': { 'order': 41, 'life': 100, 'strength': 100, 'hands': [], 'things': [], 'location': '学校东', 'able': True },
    '内海幸枝': { 'order': 42, 'life': 100, 'strength': 100, 'hands': [], 'things': [], 'location': '学校东', 'able': True }
}

# [类别，剩余次数]
items = {
    '霰弹枪': [1,5],
    '冲锋枪': [1,5],
    '狙击枪': [2,5],
    '步枪': [2,5],
    '手枪1': [3,5],
    '手枪2': [3,5],
    '手枪3': [3,5],
    '手枪4': [3,5],
    '十字弓': [4,100],
    '斧头': [4,100],
    '瑞士军刀': [4,100],
    '拳击手套': [4,100],
    '菜刀': [4,100],
    '日本刀': [4,100],
    '双截棍': [4,100],
    '金属球棒': [4,100],
    '板砖': [4,100],
    '冰镐': [4,100],
    '锅盖': [5,100],
    '防弹衣': [5,100],
    'GPS1': [6,1],
    'GPS2': [6,1],
    '望远镜1': [6,2],
    '望远镜2': [6,2],
    '绳子': [7,1],
    '电击棒': [7,1],
    '扬声器': [7,1],
    '手榴弹': [8,1],
    '氰化钾': [8,1]
}

for k, v in places.items():
    v['name'] = k

for k, v in roles.items():
    v['name'] = k
    v['injured'] = v.get('injured', 0)
    v['deliver'] = v.get('deliver', 0)
    if v['able']:
        try:
            places[v['location']]['exists'].remove(k)
        except:
            pass
        places[v['location']]['exists'].append(k)
    if v['life'] <= 0:
        v['hands'] = []
        v['things'] = []

def alive_roles():
    res = [v for k, v in roles.items() if v['life'] > 0 and v['life'] <= 100]
    res.sort(key=lambda x: x['order'])
    return res

def enabled_places():
    res = [v for k, v in places.items() if v['able']]
    res.sort(key=lambda x: x['order'])
    return res

def all_items():
    return list(items.keys()) + ['急救包', '绷带', '矿泉水']
