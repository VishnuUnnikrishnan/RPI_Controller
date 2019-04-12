'''


'''
from modules.modulesMaster import display
from flask import Flask, request, send_from_directory, render_template

app = Flask(__name__, static_url_path='')
disp = display()   

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('static/js', path)

@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('static/css', path)

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