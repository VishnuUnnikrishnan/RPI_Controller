
from flask_sockets import Sockets
from modules.modulesMaster import display
from flask import Flask, request, send_from_directory, render_template

app = Flask(__name__)
sockets = Sockets(app)
disp = display()   

@sockets.route('/message')
def messages(ws):
    disp.setLink(ws)
    while not ws.closed:
        message = ws.receive()

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('static/js', path)

@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('static/css', path) 

@app.route('/svg/<path:path>')
def send_svg(path):
    return send_from_directory('static/svg', path) 

@app.route("/modules")
def modules():
    return disp.createOutput()

@app.route("/modules/<path:path>")
def moduleClicks(path):    
    if path in disp.paths:
        item = disp.paths[int(path)]
        module = disp.buttonModules[item]
        module.onClick()
    else:
        return "error"

@app.route("/")
def intro():
    return render_template('base.html')