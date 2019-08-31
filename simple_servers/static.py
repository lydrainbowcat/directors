from flask import Flask
from flask import render_template
from gevent.pywsgi import WSGIServer

app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return render_template('ch.html')

http_server = WSGIServer(('', 83), app)
http_server.serve_forever()
