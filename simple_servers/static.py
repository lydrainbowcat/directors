from flask import Flask
from flask import render_template
from gevent.pywsgi import WSGIServer

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('ch.html')

http_server = WSGIServer(('', 83), app)
http_server.serve_forever()
