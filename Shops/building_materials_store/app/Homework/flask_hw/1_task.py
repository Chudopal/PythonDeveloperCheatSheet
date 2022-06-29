"""
Сделайте так, чтобы при переходе на страницу
localhost:5000/hello/alex/age/100
На странице повлялся текст:
Hello Alex! Your age is 100!
А при переходе на
localhost:5000/hello/bob/age/1
Hello Bob! Your age is 1!
"""

from flask import Flask


app = Flask(__name__)


@app.route("/hello/<string:name>/age/<int:age>")
def index(name: str, age: int):
    return f"Hello {name}! Your age is {age}!"


app.run(port=5000)




