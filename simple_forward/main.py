from flask import Flask
from flask import redirect
from gevent.pywsgi import WSGIServer

app = Flask(__name__)

@app.route('/')
def index():
    return redirect('https://github.com/lydrainbowcat/tedukuri')

http_server = WSGIServer(('', 8000), app)
http_server.serve_forever()
