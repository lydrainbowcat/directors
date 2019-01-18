import threading
import random
import traceback
from data import roles, places, items

costs = {
    'move': 5,
    'search': 10,
    'pick': 5,
    'attack': 20,
    'equip': 0,
    'use': 0
}

feedbacks = {}

mutex = threading.Lock()

def move(role, to):
    if to not in places:
        return '移动失败'
    dst = places[to]
    if not dst['able']:
        return '移动失败'
    if to == role['location']:
        return '无需移动'
    src = places[role['location']]
    role['location'] = to
    src['exists'].remove(role['name'])
    dst['exists'].append(role['name'])
    role['strength'] -= costs['move']
    return '移动成功'

def search(role):
    feedbacks[role['name']] = ''
    place = places[role['location']]
    if len(place['exists']) == 1:
        return '空'
    res = random.choice(list(filter(lambda x: x != role['name'], place['exists'])))
    feedbacks[role['name']] = res
    role['strength'] -= costs['search']
    return res

def pick(role):
    fb = feedbacks.get(role['name'], '')
    feedbacks[role['name']] = ''
    place = places[role['location']]
    if fb == '' or fb in roles or fb not in place['exists']:
        return '捡拾失败'
    place['exists'].remove(fb)
    role['things'].append(fb)
    role['strength'] -= costs['pick']
    return '捡拾成功'

def be_attacked(source, target, value, ignore_defend=False, continual=False):
    if not ignore_defend:
        if '锅盖' in target['hands']:
            value -= 10
        if '防弹衣' in target['hands']:
            value //= 2
    if continual:
        target['injured'] = 10
    target['life'] -= value
    if target['life'] <= 0:
        target['life'] = 0
        target['able'] = False
        places[target['location']]['exists'].remove(target['name'])
        source['things'] = source['things'] + target['things']
        return '杀死了' + target['name'] + '，获得全部道具：' + ' '.join(target['things'])
    return ''

def do_attack(role, target):
    res = []
    if '手榴弹' in role['hands']:
        for t in places[role['location']]['exists'][:]:
            if t in roles and t != role['name']:
                res.append(be_attacked(role, roles[t], 60, ignore_defend=True))
        role['hands'].remove('手榴弹')
        role['things'].remove('手榴弹')
    elif '氰化钾' in role['hands']:
        res.append(be_attacked(role, target, 110, ignore_defend=True))
        role['hands'].remove('氰化钾')
        role['things'].remove('氰化钾')
    else:
        dec = 10
        district = False
        weapons = list(filter(lambda x: items.get(x, [9, 1])[0] <= 4, role['hands']))
        if len(weapons) > 0:
            weapon = weapons[0]
            items[weapon][1] -= 1
            if items[weapon][1] == 0:
                role['hands'].remove(weapon)
                role['things'].remove(weapon)
            if items[weapon][0] == 1:
                dec += 50
                district = True
            elif items[weapon][0] == 2:
                dec += 100
            elif items[weapon][0] == 3:
                dec += 50
            else:
                dec += 30
        if district:
            for t in places[role['location']]['exists'][:]:
                if t in roles and t != role['name']:
                    res.append(be_attacked(role, roles[t], dec, continual=True))
        else:
            res.append(be_attacked(role, target, dec))
    res = list(filter(lambda x: len(x) > 0, res))
    return '攻击成功。' + '。'.join(res)

def attack(role):
    fb = feedbacks.get(role['name'], '')
    feedbacks[role['name']] = ''
    place = places[role['location']]
    if fb == '' or fb not in roles or fb not in place['exists']:
        return '攻击失败'
    target = roles[fb]
    res = do_attack(role, target)
    role['strength'] -= costs['attack']
    return res

def is_same_type(item1, item2):
    t1 = 1 if items.get(item1, [9, 1])[0] <= 4 else 0
    t2 = 1 if items.get(item2, [9, 1])[0] <= 4 else 0
    return t1 == t2

def equip(role, item):
    if item not in role['things']:
        return '无此道具'
    role['hands'] = list(filter(lambda x: not is_same_type(item, x), role['hands']))
    role['hands'].append(item)
    return '装备成功'

def use(role, item):
    if item not in role['hands']:
        return '未装备此道具'
    tp = items.get(item, [9, 1])[0]
    if tp <= 5:
        return '1~5类道具无法使用'
    elif tp == 9:
        if item == '矿泉水':
            role['strength'] += 50
            if role['strength'] > 100:
                role['strength'] = 100
        elif item == '绷带':
            if role['injured'] > 0:
                role['injured'] = 0
            else:
                role['life'] += 10
                if role['life'] > 100:
                    role['life'] = 100
        elif item == '急救包':
            role['life'] += 50
            if role['life'] > 100:
                role['life'] = 100
        role['hands'].remove(item)
        role['things'].remove(item)
        return '使用成功'
    else:
        return '6-8类道具请对话导演人工结算'

def act(role, action, params):
    cost = costs.get(action, -1)
    if cost < 0:
        return '未定义的行动'
    mutex.acquire()
    msg = ''
    res = ''
    try:
        if cost > role['strength']:
            msg = '演员试图行动'
            res = '体力不足'
        elif not role['able']:
            msg = '演员试图行动'
            res = '禁止行动'
        elif action == 'move':
            msg = '移动' + params[0]
            res = move(role, params[0])
        elif action == 'search':
            msg = '搜索'
            res = search(role)
        elif action == 'pick':
            msg = '捡拾'
            res = pick(role)
        elif action == 'attack':
            msg = '攻击'
            res = attack(role)
        elif action == 'equip':
            msg = '装备' + params[1]
            res = equip(role, params[1])
        elif action == 'use':
            msg = '使用' + params[2]
            res = use(role, params[2])
    except Exception as e:
        res = str(e)
        traceback.print_exc()
    mutex.release()
    return msg + '。反馈：' + res

def act_admin(action, params):
    res = ''
    try:
        if action == 'life':
            target = params.get('life_target')
            role = roles[target]
            value = int(params.get('life_value'))
            role['life'] += value
            if role['life'] <= 0:
                role['life'] = 0
                role['able'] = False
                places[role['location']]['exists'].remove(target)
                places[role['location']]['exists'] += role['things']
        elif action == 'strength':
            target = params.get('strength_target')
            role = roles[target]
            value = int(params.get('strength_value'))
            roles[target]['strength'] += value
        elif action == 'electronic':
            target = params.get('electronic_target')
            role = roles[target]
            for t in places[role['location']]['exists'][:]:
                if t in roles and t != target:
                    roles[t]['able'] = False
        elif action == 'rope':
            target = params.get('rope_target')
            role = roles[target]
            roles[target]['able'] = False
        elif action == 'unrope':
            target = params.get('unrope_target')
            role = roles[target]
            roles[target]['able'] = True
    except Exception as e:
        res = str(e)
        traceback.print_exc()
