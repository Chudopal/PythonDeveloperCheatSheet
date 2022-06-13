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
    with open("2_task_storage.json") as file:
        data = json.load(file)
    return data


@app.route("/cars")
def get_cars_view():
    cars = get_cars()
    return jsonify(cars)


#extra In progress
# @app.route("/cars/<option>", methods=["GET"])
# def get_options(option):
#     response = get_cars().get('cars')
#
#     id = request.args.get("id")
#     price_usd = request.args.get("price_usd")
#     brand = request.args.get("brand")
#     model = request.args.get("model")
#     generation = request.args.get("generation")
#     year = request.args.get("year")
#     rain_detector = request.args.get("rain_detector")
#     interior_material = request.args.get("interior_material")
#     created_advert = request.args.get("created_advert")
# .......
#     response = UserStorage('1.json').find_users(name=name, job=job)
#     return jsonify(list(response))


app.run(port=5000)