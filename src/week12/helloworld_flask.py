'''
Activity W12-1: Develop an initial web App using Flask
'''
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"