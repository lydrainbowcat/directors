import base64

users = {
    'cy941h': '导演',
    'test': '观众',
    'hur227': '风行者',
    '200338': '变体精灵',
    '421905': '死亡骑士',
    'pdtu74': '沙王',
    'ozmz67': '水晶室女',
    'cvxg35': '精灵守卫',
    'oo8817': '龙骑士',
    'a30360': '敌法师',
    'dtk482': '灵魂守卫',
    'g52595': '海军上将',
    '289844': '幻影刺客',
    'w50977': '月之女祭司',
    'i43478': '谜团',
    'ngpb62': '狙击手',
    'f39307': '卓尔游侠',
    't24415': '巫医',
    '688016': '月之骑士',
    'y72930': '秀逗魔导士',
    'g59861': '圣堂刺客',
    'v33661': '精灵龙',
    'yyv937': '小小',
    'fmc149': '巨牙海民',
    '465811': '光之守卫',
    'dwr212': '魅惑魔女',
    'vzsu98': '鱼人夜行者',
    '891709': '狼人',
    'azz019': '影魔',
}

user_ids = {
    '导演': 'cy941h',
    '观众': 'test',
    '风行者': 'hur227',
    '变体精灵': '200338',
    '死亡骑士': '421905',
    '沙王': 'pdtu74',
    '水晶室女': 'ozmz67',
    '精灵守卫': 'cvxg35',
    '龙骑士': 'oo8817',
    '敌法师': 'a30360',
    '灵魂守卫': 'dtk482',
    '海军上将': 'g52595',
    '幻影刺客': '289844',
    '月之女祭司': 'w50977',
    '谜团': 'i43478',
    '狙击手': 'ngpb62',
    '卓尔游侠': 'f39307',
    '巫医': 't24415',
    '月之骑士': '688016',
    '秀逗魔导士': 'y72930',
    '圣堂刺客': 'g59861',
    '精灵龙': 'v33661',
    '小小': 'yyv937',
    '巨牙海民': 'fmc149',
    '光之守卫': '465811',
    '魅惑魔女': 'dwr212',
    '鱼人夜行者': 'vzsu98',
    '狼人': '891709',
    '影魔': 'azz019',
}

def encrypt(key):
    return base64.urlsafe_b64encode(key.encode('ascii')).decode('ascii')

def decrypt(key):
    return base64.urlsafe_b64decode(key.encode('ascii')).decode('ascii')

def has_user(user):
    return user in users

def is_director(user):
    return user == '导演' or users.get(user, '') == '导演'

def get_id(name):
    name = name.strip()
    return user_ids.get(name, '')
