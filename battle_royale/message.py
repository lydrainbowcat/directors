import time
from user import users

messages = {user: [] for user in users.keys()}

def add(user, direction, content):
    if user not in messages:
        return
    ts = time.time()
    read_ts = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(ts))
    print(read_ts, users[user], direction, content)
    messages[user].append({
        'timestamp': -ts,
        "time": read_ts,
        'content': content,
        'from': users[user] if direction == 0 else '导演',
        'to': users[user] if direction == 1 else '导演'
    })

def get(user):
    if user not in messages:
        return []
    return messages[user]

def all():
    res = []
    for user, msgs in messages.items():
        res.extend(msgs)
    res.sort(key=lambda m: m['timestamp'])
    return res

def clear():
    messages = {user: [] for user in users.keys()}
