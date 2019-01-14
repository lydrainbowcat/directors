import base64

users = {
    'last2660': '导演',
    'test': '观众'
}

user_ids = {
    '导演': 'last2660',
    '观众': 'test'
}

def encrypt(key):
    return base64.urlsafe_b64encode(key.encode('ascii')).decode('ascii')

def decrypt(key):
    return base64.urlsafe_b64decode(key.encode('ascii')).decode('ascii')

def has_user(user):
    return user in users

def is_director(user):
    return users[user] == '导演'

def get_id(name):
    name = name.strip()
    return user_ids.get(name, '')
