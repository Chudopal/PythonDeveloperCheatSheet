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
from flask import request

app = Flask(__name__)


class CarsStorage:

    def __init__(self, path):
        self.path = path
        self.data = self.read()

    def find_cars(self, **kwargs) -> list:
        response = self.get_all_cars().get("cars")
        if kwargs:
            for key, value in kwargs.items():
                response = list(filter(lambda car: str(car.get(key)).lower() == str(value).lower(), response))
        return response

    def get_car_by_id(self, car_id):
        return self.find_cars(car_id=str(car_id))

    def get_all_cars(self):
        result = {"cars_number": len(self.data)}
        cars = []
        for car in self.data:
            car_data = {
                "id": car.get("id"),
                f"price_{car.get('price').get('currency')}": car.get("price").get("amount"),
                "created_advert": car.get("publishedAt")
            }

            car_data.update(
                {car_property.get('name'): car_property.get("value") for car_property in car.get('properties')}
            )
            cars.append(car_data)
        result.update({"cars": cars})

        return result

    def save(self):
        with open(self.path, "w") as file:
            json.dump(file, self.data)

    def read(self):
        with open(self.path) as file:
            data = json.load(file).get("2_task").get("cars")
        return data


context = CarsStorage("storage.json")


@app.route("/cars/", methods=["GET"])
def get_cars_view():
    return jsonify(context.find_cars(**request.args))


app.run(port=5000)
