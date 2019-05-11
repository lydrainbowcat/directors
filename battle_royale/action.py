import threading
import random
import traceback
from data import roles, places, items
from user import get_id
import message

costs = {
    'move': 5,
    'search': 10,
    'pick': 5,
    'attack': 10,
    'equip': 0,
    'use': 0,
    'deliver': 5
}

feedbacks = {}

mutex = threading.Lock()
living = False

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
        role['strength'] -= costs['search']
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
        if set(['刃甲', '锁子甲', '板甲', '圆盾']) & set(target['hands']):
            value -= 10
        if '先锋盾' in target['hands']:
            value //= 2
    if continual:
        target['injured'] = 10
    target['life'] -= value
    message.add(get_id(target['name']), 1, '你被攻击，受到' + str(value) + '伤害')
    if target['life'] <= 0:
        target['life'] = 0
        target['able'] = False
        places[target['location']]['exists'].remove(target['name'])
        source['things'] = source['things'] + target['things']
        ret = '杀死了' + target['name'] + '，' + ('获得全部道具：' + ' '.join(target['things']) if len(target['things']) > 0 else '对方无道具')
        target['things'] = []
        target['hands'] = []
        return ret
    return ''

def do_attack(role, target):
    res = []
    if '黯灭' in role['hands']:
        for t in places[role['location']]['exists'][:]:
            if t in roles and t != role['name']:
                res.append(be_attacked(role, roles[t], 60, ignore_defend=True))
        role['hands'].remove('黯灭')
        role['things'].remove('黯灭')
    elif '漩涡' in role['hands']:
        for t in places[role['location']]['exists'][:]:
            if t in roles and t != role['name']:
                res.append(be_attacked(role, roles[t], 60, ignore_defend=True))
        role['hands'].remove('漩涡')
        role['things'].remove('漩涡')
    elif '圣者遗物' in role['hands']:
        res.append(be_attacked(role, target, 110, ignore_defend=True))
        role['hands'].remove('圣者遗物')
        role['things'].remove('圣者遗物')
    else:
        dec = 10
        district = False
        weapons = list(filter(lambda x: items.get(x, [9, 1])[0] <= 4 and items.get(x, [9, 1])[1] > 0, role['hands']))
        if len(weapons) > 0:
            weapon = weapons[0]
            items[weapon][1] -= 1
            if items[weapon][1] == 0:
                role['hands'].remove(weapon)
                role['things'].remove(weapon)
            if items[weapon][0] == 1:
                dec += 40
                district = True
            elif items[weapon][0] == 2:
                dec += 80
            elif items[weapon][0] == 3:
                dec += 40
            else:
                dec += 20
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
    if target['life'] <= 0 or target['life'] > 100:
        return '请勿鞭尸'
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

def change_life(role, value):
    death = []
    role['life'] += value
    if role['life'] <= 0:
        role['life'] = 0
        role['able'] = False
        places[role['location']]['exists'].remove(role['name'])
        places[role['location']]['exists'] += role['things']
        role['hands'] = []
        role['things'] = []
        death.append(role['name'])
    message.add(get_id(role['name']), 1, '你的生命值变化了' + str(value))
    return death

def use(role, item, target):
    if item not in role['hands']:
        return '未装备此道具'
    tp = items.get(item, [9, 1])[0]
    times = items.get(item, [9, 1])[1]
    if times <= 0:
        return '当夜次数已用尽'
    if tp <= 5:
        return '1~5类道具无需使用，拿在手里以后，直接搜索、攻击即可'
    elif tp <= 7:
        items[item][1] -= 1
        if item in ['慧光', '银月之晶']:
            if target == '':
                return '使用失败，未选择使用目标'
            for k, v in places.items():
                if v['able'] and target in v['exists']:
                    return k
            for k, v in roles.items():
                if target in v['things']:
                    return k + ' ' + v['location']
            return '场上无此道具'
        elif item in ['刷新球', '坚韧球']:
            if target == '':
                return '使用失败，未选择使用目标'
            return ' '.join(roles[target]['things']) if len(roles[target]['things']) > 0 else '对方无道具'
        elif item == '王冠':
            for t in places[role['location']]['exists'][:]:
                if t in roles and t != role['name']:
                    roles[t]['able'] = False
            return '使用成功'
        else:
            return '极限法球请QQ联系导演，下一日公示'
    elif tp == 8:
        death = []
        if item == '圣者遗物':
            death += change_life(roles[target], -100)
        elif item in ['黯灭', '漩涡']:
            for t in places[role['location']]['exists'][:]:
                if t in roles and t != role['name']:
                    death += change_life(roles[t], -50)
        role['hands'].remove(item)
        role['things'].remove(item)
        return '使用成功。' + ('杀死了' + ' '.join(death) + '，道具散落' if len(death) > 0 else '无人死亡')
    elif tp == 9:
        if item == '虚无宝石':
            role['strength'] += 50
            if role['strength'] > 100:
                role['strength'] = 100
        elif item == '振奋宝石':
            role['strength'] = 100
        elif item == '回复指环':
            if role['injured'] > 0:
                role['injured'] = 0
            else:
                role['life'] += 10
                if role['life'] > 100:
                    role['life'] = 100
        elif item == '治疗指环':
            if role['injured'] > 0:
                role['injured'] = 0
            else:
                role['life'] += 30
                if role['life'] > 100:
                    role['life'] = 100
        elif item == '恐鳖之心':
            role['injured'] = 0
            role['life'] = 100
        role['hands'].remove(item)
        role['things'].remove(item)
        return '使用成功'
    return '未定义的道具'

def deliver(role, target, content):
    res = ''
    if len(content) > 0 and len(target) > 0 or target not in roles:
        if role['deliver'] == 0:
            role['deliver'] = 1
            role['strength'] -= 5
            message.add(get_id(target), 1, role['name'] + '传音给你：' + content)
            res = '传音成功'
        else:
            res = '传音失败，当夜次数已用尽'
    else:
        res = '传音失败，无效的对象或消息'
    return res

def act(role, action, params):
    global living
    if not living:
        return '行动未开始'
    cost = costs.get(action, -1)
    if cost < 0:
        return '未定义的行动'
    mutex.acquire()
    msg = ''
    res = ''
    try:
        if not role['able']:
            msg = '演员试图行动'
            res = '你被禁止行动'
        elif cost > role['strength']:
            msg = '演员试图行动'
            res = '体力不足'
        elif action == 'move':
            msg = '移动' + params.get('move_to', '')
            res = move(role, params.get('move_to', ''))
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
            msg = '装备' + params.get('equip_item', '')
            res = equip(role, params.get('equip_item', ''))
        elif action == 'use':
            msg = '使用' + params.get('use_item', '')
            target = ''
            target_role = params.get('use_item_target_role', '')
            if target_role != '':
                msg += '，目标' + target_role
                target = target_role
            target_item = params.get('use_item_target_item', '')
            if target_item != '':
                msg += '，查看' + target_item
                target = target_item
            res = use(role, params.get('use_item', ''), target)
        elif action == 'deliver':
            target = params.get('deliver_target', '')
            content = params.get('deliver_content', '')
            msg = '传音' + target + '：' + content
            res = deliver(role, target, content)
    except Exception as e:
        res = str(e)
        traceback.print_exc()
    mutex.release()
    return msg + '。反馈：' + res

def act_admin(action, params):
    global living
    res = ''
    mutex.acquire()
    try:
        if action == 'life':
            target = params.get('life_target')
            role = roles[target]
            value = int(params.get('life_value'))
            change_life(role, value)
        elif action == 'strength':
            target = params.get('strength_target')
            value = int(params.get('strength_value'))
            roles[target]['strength'] += value
        elif action == 'rope':
            target = params.get('rope_target')
            roles[target]['able'] = False
        elif action == 'unrope':
            target = params.get('unrope_target')
            roles[target]['able'] = True
        elif action == 'start':
            living = True
        elif action == 'end':
            living = False
            for k, v in roles.items():
                if v['life'] > 0 and v['life'] <= 100:
                    v['able'] = True
                    v['deliver'] = 0
                    v['strength'] += 50
                    if v['strength'] > 100:
                        v['strength'] = 100
                    if v['injured']:
                        change_life(v, -10)
            items['慧光'][1] = 1
            items['银月之晶'][1] = 1
            items['刷新球'][1] = 2
            items['坚韧球'][1] = 2
            items['王冠'][1] = 1
            items['极限法球'][1] = 1
        elif action == 'save':
            print(places)
            print(roles)
            print(items)
            print(message.messages)
        elif action == 'drop':
            what = params.get('drop_item')
            where = params.get('drop_place')
            places[where]['exists'].append(what)
        elif action == 'destroy':
            target = params.get('destroy_place')
            places[target]['able'] = False
            places[target]['exists'] = []
        elif action == 'move':
            who = params.get('move_target')
            where = params.get('move_place')
            try:
                dst = places[where]
                src = places[roles[who]['location']]
                roles[who]['location'] = where
                src['exists'].remove(who)
                dst['exists'].append(who)
            except:
                pass
        elif action == 'give':
            who = params.get('give_target')
            what = params.get('give_item')
            try:
                if what in roles[who]['things']:
                    roles[who]['things'].remove(what)
                    roles[who]['hands'].remove(what)
                else:
                    roles[who]['things'].append(what)
            except:
                pass
    except Exception as e:
        res = str(e)
        traceback.print_exc()
    mutex.release()
