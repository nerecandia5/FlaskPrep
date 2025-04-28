from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/saludo")
def Hola_chau():
    return "<p>Hola, chau!</p>"

@app.route("/partido") 
def River_Boca():
    return "<p> River, Boca!</p>"

@app.route("/partido/<string:e1>/<string:e2>")
def partido (e1,e2):
    return f"{e1} vs {e2}"

