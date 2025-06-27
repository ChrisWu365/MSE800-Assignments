'''
Activity W12-1: Develop an initial web App using Flask
'''
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/username/<username>")
def learn(username):
    return f"{username} is learning Flask! That's amazing!!!"

if __name__ == "__main__":
    app.run(debug=True)