import json
from flask import Flask
from flask import jsonify


app = Flask(__name__)


def get_cars():
    with open("storage.json") as file:
        data = json.load(file).get("flask2").get("cars")
    return data


def get_info(data: dict):
    return [
        {
            'id': car.get('id', {}),
            'price_usd': car.get('price', {}).get('amount', {}),
            'brand': car.get('properties', {})[0].get('value', {}),
            'model': car.get('properties', {})[1].get('value', {}),
            'generation': car.get('properties', {})[2].get('value', {}),
            'year': car.get('properties', {})[3].get('value', {}),
            'rain_detector': car.get('properties', {})[4].get('value', {}),
            'created_advert': car.get('publishedAt', {})
        } for car in data
    ]


@app.route("/cars")
def get_cars_view():
    cars_info = get_cars()
    data = get_info(cars_info)

    return jsonify(
        {
            "cars_number": len(data),
            "cars": data       
        }
    )


app.run(port=5000)