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
from typing import Dict
from flask import Flask
from flask import jsonify


app = Flask(__name__)


def get_cars():
    with open("storage.json") as file:
        data = json.load(file).get("2_task").get("cars")
    return data

def get_car(data: Dict)-> list: 
    return [
        {"id": car.get("id", {}),
        "price_usd": car.get("price", {}).get("amount", {}),
        "brand": car.get("properties", {})[0].get("value", {}),
        "model": car.get("properties", {})[1].get("value", {}),
        "generation": car.get("properties", {})[2].get("value", {}),
        "year": car.get("properties", {})[3].get("value", {}),
        "rain_detector": car.get("properties", {})[4].get("value", {}),
        "interior_material": car.get("properties", {})[5].get("value", {}),
        "created_advert": car.get("publishedAt", {})
        } for car in data
    ] 

@app.route("/cars")
def get_cars_view():
    car = get_cars()
    cars = get_car(car)
    return jsonify(
        {
            "cars_number": len(cars),
            "cars": cars       
        }
    )

app.run(port=5000)