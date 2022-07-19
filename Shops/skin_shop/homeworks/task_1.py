from flask import Flask


app = Flask(__name__)


@app.route("/hello/alex/age/100")
def index():
    return "Hello Alex! Your age is 100!"


@app.route("/hello/bob/age/1")
def aboud():
    return "Hello Bob! Your age is 1!"

app.run(port=4000)