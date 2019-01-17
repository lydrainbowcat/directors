from flask import Flask
from flask import request, redirect, url_for, render_template
from user import encrypt, decrypt, is_director, has_user, get_id
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
        to = request.args.get('to', '')
        content = request.args.get('content', '')
        messages = message.all()
        return render_template('view_all.html', messages=messages, send_url='/api/send/'+key, to=to, content=content)
    else:
        content = request.args.get('content', '')
        messages = message.get(user)
        disabled = len(messages) > 0 and is_director(messages[-1]['to'])
        return render_template('view.html', messages=message.get(user), send_url='/api/send/'+key, content=content, disabled=disabled)

@app.route('/api/send/<key>', methods=['POST'])
def send_message(key):
    try:
        user = decrypt(key)
        if not has_user(user):
            raise
    except:
        return redirect(url_for('index'))

    content = request.form.get('content', '')
    if len(content) > 0:
        if is_director(user):
            dst = request.form.get('to', '')
            message.add(get_id(dst), 1, content)
        else:
            message.add(user, 0, content)
    return redirect(url_for('view_messages', key=key))
