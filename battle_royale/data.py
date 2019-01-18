places = {
    '墓地东': { 'order': 1, 'exists': [], 'able': True },
    '墓地南': { 'order': 2, 'exists': ['手榴弹'], 'able': True },
    '墓地西': { 'order': 3, 'exists': [], 'able': True },
    '墓地北': { 'order': 4, 'exists': [], 'able': True },
    '医院东': { 'order': 5, 'exists': [], 'able': True },
    '医院南': { 'order': 6, 'exists': [], 'able': True },
    '医院西': { 'order': 7, 'exists': [], 'able': True },
    '医院北': { 'order': 8, 'exists': [], 'able': True },
    '海岸东': { 'order': 9, 'exists': [], 'able': False },
    '海岸南': { 'order': 10, 'exists': [], 'able': False },
    '海岸西': { 'order': 11, 'exists': [], 'able': False },
    '海岸北': { 'order': 12, 'exists': [], 'able': False },
    '工厂东': { 'order': 13, 'exists': [], 'able': True },
    '工厂南': { 'order': 14, 'exists': [], 'able': True },
    '工厂西': { 'order': 15, 'exists': ['手榴弹'], 'able': True },
    '工厂北': { 'order': 16, 'exists': [], 'able': True },
    '树林东': { 'order': 17, 'exists': [], 'able': True },
    '树林南': { 'order': 18, 'exists': ['手榴弹'], 'able': True },
    '树林西': { 'order': 19, 'exists': [], 'able': True },
    '树林北': { 'order': 20, 'exists': [], 'able': True },
    '邮局东': { 'order': 21, 'exists': [], 'able': False },
    '邮局南': { 'order': 22, 'exists': [], 'able': False },
    '邮局西': { 'order': 23, 'exists': [], 'able': False },
    '邮局北': { 'order': 24, 'exists': [], 'able': False },
    '机场东': { 'order': 25, 'exists': [], 'able': True },
    '机场西': { 'order': 26, 'exists': [], 'able': True },
    '机场南': { 'order': 27, 'exists': [], 'able': True },
    '机场北': { 'order': 28, 'exists': [], 'able': True },
    '学校东': { 'order': 29, 'exists': ['手榴弹'], 'able': True },
    '学校南': { 'order': 30, 'exists': [], 'able': True },
    '学校西': { 'order': 31, 'exists': [], 'able': True },
    '学校北': { 'order': 32, 'exists': [], 'able': True },
    '住宅东': { 'order': 33, 'exists': [], 'able': True },
    '住宅南': { 'order': 34, 'exists': [], 'able': True },
    '住宅西': { 'order': 35, 'exists': [], 'able': True },
    '住宅北': { 'order': 36, 'exists': [], 'able': True }
}

roles = {
    '导演': { 'order': -1, 'life': 1000, 'strength': 100, 'location': '主席台', 'things': [], 'hands': [], 'able': False },
    '观众': { 'order': 0, 'life': 1000, 'strength': 100, 'location': '看台', 'things': [], 'hands': [], 'able': False },
    '黑长博': { 'order': 1, 'life': 90, 'strength': 80, 'hands': [], 'things': ['绷带'], 'location': '树林西', 'able': True },
    '藤吉文世': { 'order': 2, 'life': 0, 'strength': 100, 'location': '出局', 'things': [], 'hands': [], 'able': False },
    '松井知里': { 'order': 3, 'life': 0, 'strength': 100, 'location': '出局', 'things': [], 'hands': [], 'able': False },
    '相马光子': { 'order': 4, 'life': 100, 'strength': 100, 'hands': ['GPS2'], 'things': ['GPS2'], 'location': '住宅东', 'able': True },
    '琴弹加代子': { 'order': 5, 'life': 100, 'strength': 85, 'hands': ['步枪'], 'things': ['步枪', '矿泉水'], 'location': '墓地南', 'able': True },
    '中川有香': { 'order': 6, 'life': 60, 'injured': 10, 'strength': 100, 'hands': [], 'things': [], 'location': '医院南', 'able': True },
    '濑户丰': { 'order': 7, 'life': 40, 'strength': 95, 'hands': ['手枪1'], 'things': ['手枪1'], 'location': '墓地南', 'able': True },
    '南佳织': { 'order': 8, 'life': 60, 'strength': 100, 'hands': [], 'things': [], 'location': '机场东', 'able': True },
    '元渊恭一': { 'order': 9, 'life': 100, 'strength': 100, 'hands': [], 'things': [], 'location': '树林南', 'able': True },
    '矢作好美': { 'order': 10, 'life': 0, 'strength': 100, 'location': '出局', 'things': [], 'hands': [], 'able': False },
    '日下由美子': { 'order': 11, 'life': 100, 'strength': 100, 'hands': [], 'things': [], 'location': '工厂西', 'able': True },
    '川田章吾': { 'order': 12, 'life': 100, 'strength': 100, 'hands': [], 'things': [], 'location': '医院东', 'able': True },
    '三村信史': { 'order': 13, 'life': 100, 'strength': 100, 'hands': ['双截棍'], 'things': ['矿泉水', '双截棍', '瑞士军刀'], 'location': '机场西', 'able': True },
    '稻田瑞穗': { 'order': 14, 'life': 100, 'strength': 55, 'hands': ['手枪4'], 'things': ['矿泉水', '手枪4'], 'location': '学校北', 'able': True },
    '沼井充': { 'order': 15, 'life': 100, 'strength': 60, 'hands': ['冰镐'], 'things': ['冰镐'], 'location': '树林西', 'able': True },
    '大木立道': { 'order': 16, 'life': 0, 'strength': 100, 'location': '出局', 'things': [], 'hands': [], 'able': False },
    '山本和彦': { 'order': 17, 'life': 100, 'strength': 100, 'hands': ['金属球棒'], 'things': ['金属球棒'], 'location': '墓地东', 'able': True },
    '月冈彰': { 'order': 18, 'life': 100, 'strength': 70, 'hands': [], 'things': ['矿泉水'], 'location': '树林南', 'able': True },
    '饭岛敬太': { 'order': 19, 'life': 100, 'strength': 95, 'hands': ['绳子'], 'things': ['绳子'], 'location': '住宅北', 'able': True },
    '国信庆时': { 'order': 20, 'life': 40, 'injured': 10, 'strength': 100, 'hands': [], 'things': [], 'location': '墓地北', 'able': True },
    '织田敏宪': { 'order': 21, 'life': 100, 'strength': 100, 'hands': [], 'things': [], 'location': '机场西', 'able': True },
    '笹川龙平': { 'order': 22, 'life': 40, 'injured': 10, 'strength': 100, 'hands': [], 'things': [], 'location': '墓地北', 'able': True },
    '野田聪美': { 'order': 23, 'life': 100, 'strength': 95, 'hands': ['手枪2'], 'things': ['板砖', '矿泉水', '手枪2'], 'location': '树林南', 'able': True },
    '中川典子': { 'order': 24, 'life': 60, 'strength': 100, 'hands': ['菜刀'], 'things': ['菜刀'], 'location': '机场西', 'able': True },
    '赤松义生': { 'order': 25, 'life': 10, 'strength': 100, 'hands': ['电击棒'], 'things': ['电击棒'], 'location': '工厂西', 'able': True },
    '小川樱': { 'order': 26, 'life': 40, 'strength': 100, 'hands': ['拳击手套'], 'things': ['拳击手套'], 'location': '住宅东', 'able': True },
    '仓元洋二': { 'order': 27, 'life': 100, 'strength': 100, 'hands': ['GPS1'], 'things': ['氰化钾', 'GPS1', '急救包'], 'location': '工厂西', 'able': True },
    '榊祐子': { 'order': 28, 'life': 100, 'strength': 90, 'hands': ['十字弓'], 'things': ['十字弓'], 'location': '工厂南', 'able': True },
    '新井田和志': { 'order': 29, 'life': 80, 'strength': 80, 'hands': [], 'things': ['矿泉水'], 'location': '住宅东', 'able': True },
    '泷口优一郎': { 'order': 30, 'life': 100, 'strength': 60, 'hands': [], 'things': ['矿泉水'], 'location': '墓地南', 'able': True },
    '金井泉': { 'order': 31, 'life': 100, 'strength': 100, 'hands': ['斧头'], 'things': ['斧头'], 'location': '学校北', 'able': True },
    '天堂真弓': { 'order': 32, 'life': 100, 'strength': 100, 'hands': [], 'things': [], 'location': '工厂南', 'able': True },
    '清水比吕乃': { 'order': 33, 'life': 40, 'injured': 10, 'strength': 100, 'hands': ['望远镜2'], 'things': ['扬声器', '望远镜2'], 'location': '住宅东', 'able': True },
    '旗上忠胜': { 'order': 34, 'life': 60, 'strength': 95, 'hands': ['日本刀'], 'things': ['日本刀'], 'location': '住宅东', 'able': True },
    '千草贵子': { 'order': 35, 'life': 70, 'strength': 100, 'hands': ['霰弹枪'], 'things': ['霰弹枪'], 'location': '医院西', 'able': True },
    '七原秋也': { 'order': 36, 'life': 100, 'strength': 100, 'hands': ['锅盖', '狙击枪'], 'things': ['锅盖', '绷带', '狙击枪', '望远镜1'], 'location': '住宅东', 'able': True },
    '江藤惠': { 'order': 37, 'life': 0, 'strength': 100, 'location': '出局', 'things': [], 'hands': [], 'able': False },
    '桐山和雄': { 'order': 38, 'life': 100, 'strength': 100, 'hands': ['手枪3', '防弹衣'], 'things': ['手枪3', '绷带', '防弹衣'], 'location': '墓地南', 'able': True },
    '杉村弘树': { 'order': 39, 'life': 100, 'strength': 100, 'hands': [], 'things': [], 'location': '工厂东', 'able': True },
    '北野雪子': { 'order': 40, 'life': 0, 'strength': 100, 'location': '出局', 'things': [], 'hands': [], 'able': False },
    '谷泽遥': { 'order': 41, 'life': 100, 'strength': 100, 'hands': [], 'things': [], 'location': '树林南', 'able': True },
    '内海幸枝': { 'order': 42, 'life': 100, 'strength': 65, 'hands': ['冲锋枪'], 'things': ['冲锋枪'], 'location': '墓地北', 'able': True }
}

items = {
    '霰弹枪': [1,5],
    '冲锋枪': [1,3],
    '狙击枪': [2,5],
    '步枪': [2,2],
    '手枪1': [3,5],
    '手枪2': [3,5],
    '手枪3': [3,4],
    '手枪4': [3,4],
    '十字弓': [4,10000],
    '斧头': [4,10000],
    '瑞士军刀': [4,10000],
    '拳击手套': [4,10000],
    '菜刀': [4,10000],
    '日本刀': [4,10000],
    '双节棍': [4,10000],
    '金属球棒': [4,10000],
    '板砖': [4,10000],
    '冰镐': [4,10000],
    '锅盖': [5,10000],
    '防弹衣': [5,10000],
    'GPS1': [6,1],
    'GPS2': [6,1],
    '望远镜1': [6,1],
    '望远镜2': [6,1],
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
    if v['able']:
        places[v['location']]['exists'].append(k)

def alive_roles():
    res = [v for k, v in roles.items() if v['life'] > 0 and v['life'] <= 100]
    res.sort(key=lambda x: x['order'])
    return res

def enabled_places():
    res = [v for k, v in places.items() if v['able']]
    res.sort(key=lambda x: x['order'])
    return res
