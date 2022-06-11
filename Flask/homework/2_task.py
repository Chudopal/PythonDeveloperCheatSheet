"""
Запустите приложение, посмотрите, как оно сейчас работает
Сделайте так, чтобы при переходе по
localhost:5000/cars

Выводился json следующего формата:
{
    "cars_number": 25,
    "cars": [
        {
            "id": 101068323,
            "price_usd": 22300,
            "brand": "Nissan",
            "model": "Leaf",
            "generation": "II",
            "year": "2017",
            "rain_detector": true,
            "interior_material": "ткань",
            "created_advert": "2022-05-01T18:59:04+0000"
        },
        ...
    ]
}

(extra) Дабавьте фильтрацию через адресную строку по всем этим параметрам.
"""

import json
from flask import Flask
from flask import jsonify


app = Flask(__name__)


def get_cars():
    with open("storage.json") as file:
        data = json.load(file).get("2_task").get("cars")
    return data


@app.route("/cars")
def get_cars_view():
    cars = get_cars()
    return jsonify(cars)

app.run(port=5000)