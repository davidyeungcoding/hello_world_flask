from flask import Flask
from os import environ

app = Flask(__name__)

@app.route("/")
@app.route("/hello")
def say_hi():
    return "Hello World!"
    
@app.route("/hello/<name>")
def hi_person(name):
    return "Hello {}!".format(name.title())

@app.route("/jedi/<first>/<last>")
def jedi_name(first, last):
    return "Hello, {}{}".format(last.title()[:3], first[:2])

if __name__ == "__main__":
    app.run(host=environ['IP'],
            port=int(environ['PORT']))