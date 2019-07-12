from flask import Flask
from flask import redirect
from gevent.pywsgi import WSGIServer

app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return redirect('http://www.lydshy.com:3389/' + path, code=302)

http_server = WSGIServer(('', 80), app)
http_server.serve_forever()
