from flask import Flask


app = Flask(__name__)

@app.route("/")
@app.route("/hello")
def index():
    return f"Hello world"


@app.route("/hello/<string:name>/age/<int:age>")
def user(name: str, age: int):
    return f"Hello {name.capitalize()}! Your age is {age}!"

<<<<<<< HEAD

app.run(port=5000, debug=True)
=======
 
app.run(port=5000, debug=True)
>>>>>>> 9b79568823889bc36e819d31de8236786f5a6f05
