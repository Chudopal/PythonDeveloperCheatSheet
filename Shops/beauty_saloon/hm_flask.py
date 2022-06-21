from flask import Flask


app = Flask(__name__)

@app.route("/")
@app.route("/hello")
def index():
    return f"Hello world"


@app.route("/hello/<string:name>/age/<int:age>")
def user(name: str, age: int):
    return f"Hello {name.capitalize()}! Your age is {age}!"

 
app.run(port=5000, debug=True)
