# The "Hello World" of Flask <http://flask.pocoo.org/>
# Usage: FLASK_APP=hello-flask.py flask run

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"


