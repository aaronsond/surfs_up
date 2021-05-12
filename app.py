from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
        return 'Sup, World'

@app.route("/three")
def test():
        return 'I do not understand magic methods, AKA Dunder'