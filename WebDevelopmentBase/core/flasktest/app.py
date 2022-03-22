from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/<name>")
def hello_world(name):
    age = request.args.get("age", '')
    surname = request.args.get("surname", '')
    return f"<p>Hello, {name} {surname}! Your age is {age}</p>"