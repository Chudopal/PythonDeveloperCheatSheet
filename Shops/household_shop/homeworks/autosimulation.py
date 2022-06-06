import time
from uuid import uuid4


class Model:
    
    def __init__(self, brand: str, model: str) -> None:
        self.brand = brand
        self.model = model


class Engine(Model):
    
    def __init__(self, brand: str, model: str, vin: uuid4, power: float) -> None:
        super().__init__(brand, model)
        self.vin = vin
        self.power = power


class Wheel(Engine):
    
    def __init__(self, brand: str, model: str, vin: uuid4, power: float, material: str, season: str) -> None:
        super().__init__(brand, model, vin, power)
        self.material = material 
        self.season = season

    def move_car(self):
        result_msg = "I'm starting.\n"
        total_time = 0
        distance = int(input('Enter distance :\n'))

        for curenctDict in range(0, distance):
            result_msg += f'{curenctDict + 1} km\n'
            total_time += self.power 
            time.sleep(self.power)
        result_msg += f"I'm stopping.\nTotal time - {total_time} s."

        return result_msg


class SkeletonCar(Wheel):

    def __init__(self, brand: str, model: str, vin: uuid4, power: float, material: str, season: str, car_material: str, color: str) -> None:
        super().__init__(brand, model, vin, power, material, season)
        self.car_material = car_material
        self.color = color

    def get_car_info(self):
        return f'Brand : {self.brand}, Model : {self.model}, wheels - {self.material} : {self.season}, {self.car_material}, color - {self.color}.'


def get_cars_list() -> list:
    cars_list = [
        SkeletonCar('Skoda', 'Octavia', uuid4(), 0.1, 'rubber', '4 winter', 'iron', 'blue'),
        SkeletonCar('BMW', '316', uuid4(), 0.5, 'rubber', '4 summer', 'iron', 'black'),
        SkeletonCar('Audi', 'A4', uuid4(), 0.2, 'rubber', '4 winter', 'iron', 'green'),
        SkeletonCar('Lexus', 'ix', uuid4(), 1, 'rubber', '2 winter, 2 summer', 'iron', 'white'),
        SkeletonCar('Mazda', '6', uuid4(), 0.9, 'rubber', '4 winter', 'iron', 'blue'),
    ]

    return cars_list


def run():
    cars_list = get_cars_list()
    cnt = 0
    for car in cars_list:
        cnt += 1
        print(f'{cnt}.', car.get_car_info())
        print(car.move_car())


run()
