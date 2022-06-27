import time
from uuid import uuid4


class Model:
    
    def __init__(self, brand: str, model: str) -> None:
        self.brand = brand
        self.model = model


class Engine:

    def __init__(self, vin: uuid4, power: float) -> None:
        self.vin = vin
        self.power = power


class Wheel:
    
    def __init__(self, material: str, season: str) -> None:
        self.material = material 
        self.season = season


class Body:

    def __init__(self, car_material: str, color: str) -> None:
        self.car_material = car_material
        self.color = color


class Car:

    def __init__(self, model: Model, engine: Engine, wheel: Wheel, body: Body) -> None:
        self.model = model
        self.engine = engine
        self.wheel = wheel
        self.body = body

    def get_car_info(self):
        return f'Brand : {self.model.brand}, Model : {self.model.model}, ' \
               f'wheels - {self.wheel.material} : {self.wheel.season}, {self.body.car_material}, ' \
               f'color - {self.body.color}. '

    def move_car(self):
        result_msg = "I'm starting.\n"
        total_time = 0
        distance = int(input('Enter distance :\n'))        

        for curenctDict in range(distance):
            result_msg += f'{curenctDict + 1} km\n'
            total_time += self.engine.power
            time.sleep(self.engine.power)

        result_msg += f"I'm stopping.\nTotal time - {total_time} s."
        return result_msg


def get_cars_list() -> list:
    cars_list = [
        Car(
            Model('Skoda', 'Octavia'),
            Engine(uuid4(), 0.1),
            Wheel('rubber', '4 winter'),
            Body('iron', 'blue')
        ),
        Car(
            Model('BMW', '316'),
            Engine(uuid4(), 0.5),
            Wheel('rubber', '4 summer'),
            Body('iron', 'black')
        ),
        Car(
            Model('Audi', 'A4'),
            Engine(uuid4(), 0.2),
            Wheel('rubber', '4 winter'),
            Body('iron', 'green')
        ),
        Car(
            Model('Lexus', 'ix'),
            Engine(uuid4(), 1),
            Wheel('rubber', '2 winter, 2 summer'),
            Body('iron', 'white')
        ),
        Car(
            Model('Mazda', '6'),
            Engine(uuid4(), 0.9),
            Wheel('rubber', '4 summer'),
            Body('iron', 'blue')
        )
    ]

    return cars_list


def run():
    cars_list = get_cars_list()
    cnt = 0
    for car in cars_list:
        cnt += 1
        print(car.move_car())
        print(f'{cnt}.', car.get_car_info())


run()
