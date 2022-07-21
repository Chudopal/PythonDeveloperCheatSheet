import json
from flask import Flask
from flask import jsonify


app = Flask(__name__)


def get_cars():
    with open("2_task_storage.json") as file:
        data = json.load(file)
    return data


@app.route("/")
@app.route("/cars")
def get_cars_view():
    cars = get_cars()
    return jsonify(cars)

app.run(port=5000, debug=True)