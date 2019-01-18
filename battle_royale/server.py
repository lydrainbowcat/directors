from flask import Flask
from flask import request, redirect, url_for, render_template
from user import users, encrypt, decrypt, is_director, has_user, get_id
from data import roles, places, alive_roles, enabled_places
from action import act
import message

app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return 'Hello, World!'

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/api/login', methods=['POST'])
def login():
    id = request.form.get('id', '')
    return redirect(url_for('view_messages', key=encrypt(id)))

@app.route('/api/view/<key>')
def view_messages(key):
    try:
        user = decrypt(key)
        if not has_user(user):
            raise
    except:
        return redirect(url_for('index'))

    if is_director(user):
        messages = message.all()
        return render_template('view_all.html', messages=messages, send_url='/api/send/'+key,
                               roles=alive_roles(), places=enabled_places())

    else:
        messages = message.get(user)
        role = roles[users[user]]
        return render_template('view.html', messages=messages, send_url='/api/send/'+key,
                               role=role, places=enabled_places())

@app.route('/api/send/<key>', methods=['POST'])
def send_message(key):
    try:
        user = decrypt(key)
        if not has_user(user):
            raise
    except:
        return redirect(url_for('index'))

    action = request.form.get('action', '')
    if action != 'send':
        role = roles[users[user]]
        params = []
        params.append(request.form.get('move_to', ''))
        params.append(request.form.get('equip_item', ''))
        params.append(request.form.get('use_item', ''))
        content = act(role, action, params)
        message.add(user, 2, content)
    else:
        content = request.form.get('content', '')
        if len(content) > 0:
            if is_director(user):
                dst = request.form.get('to', '')
                message.add(get_id(dst), 1, content)
            else:
                message.add(user, 0, content)
    return redirect(url_for('view_messages', key=key))
