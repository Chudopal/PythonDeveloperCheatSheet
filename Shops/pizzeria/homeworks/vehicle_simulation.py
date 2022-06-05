"""
3. Автосимуляция:

- Машина состоит из двигателя, колес, корпуса, у машины есть модель.
    Машина может ехать определенное количество КМ, а именно выводить в консоль:

    I'm starting.
    1 km
    2 km
    3 km
    I'm stopping.
    Total time - 3 s.

    Проезд машины, если ей нужно проехать 3 км.
    Между каждым км проходит промежуток времени, который задает двигатель.
    В данном случае мощность двигателя - 1 с.
- Информация о машине выводится следующим образом:
    Model - BMW, wheels - 2 summer 2 winter, corpus color - grey.
    или
    Model - Audi, wheels - 4 winter, corpus color - red.
    Добавьте для этого специальный метод

- Двигатель имеет серийный номер(уникальный), и мощность(в нашем случае -
    это количество секунд, за которое проезжается 1 км), то есть,
    если мощность = 0.5, значит двигатель может преодолеть 1 км за полсекунды.

- Колеса имеют материал, и описание (Summer, Winter)

- Корпус имеет цвет и материал

Сделайте 5 машин, и запустите их так, чтобы выводилось следующее сообщение:

1. Model - Audi, wheels - 4 winter, corpus color - red.
    I'm starting.
    1 km
    2 km
    3 km
    I'm stopping.
    Total time - 3 s.
2. Model - BMW, wheels - 2 summer 2 winter, corpus color - grey.
    I'm starting.
    1 km
    2 km
    3 km
    I'm stopping.
    Total time - 1.5 s.

и так далее.

Чтобы сделать промежуток между киллометрами, используйте функцию:

import time
time.sleep(0.5) #остановит работу на 0.5 сек
"""

from dataclasses import dataclass
from uuid import uuid4
import time


@dataclass
class Engine:
    serial_number = uuid4()
    power: float


@dataclass
class Wheel:
    material: str
    season: str


@dataclass
class Body:
    color: str
    material: str


class WheelsSetCreator:
    def __init__(self, *wheels: Wheel):
        self.wheels = wheels
        self.wheels_set = dict()
        self._format_wheels()

    def __repr__(self):
        return " ".join(f"{value} {key}" for key, value in self.wheels_set.items())

    def _format_wheels(self):
        for wheel in self.wheels:
            if not self.wheels_set.get(wheel.season):
                self.wheels_set[wheel.season] = 1
            else:
                self.wheels_set[wheel.season] += 1


class Vehicle:
    def __init__(self, model: str, engine: Engine, body: Body, wheels: WheelsSetCreator):
        self.model = model
        self.engine = engine
        self.body = body
        self.wheels = wheels

    def __repr__(self):
        return f"Model - {self.model}, wheels - {self.wheels}, corpus color - {self.body.color}."

    def move(self, distance: float):
        traveled_distance = 0
        print("I'm starting.")
        while traveled_distance < distance:
            time.sleep(self.engine.power)
            traveled_distance += 1
            print(traveled_distance)
        print(f"Total time - {self.engine.power * distance}")


slow_engine = Engine(2)
fast_engine = Engine(1)
hyper_engine = Engine(0.3)

regular_body = Body("Green", "Aluminium")
sport_body = Body("Red", "Carbon")
off_road_body = Body("Blue", "Aluminium")

winter_wheel = Wheel("Steel", "Winter")
summer_wheel = Wheel("Steel", "Summer")
sport_wheel = Wheel("Carbon", "Summer")
off_road_wheel = Wheel("Titanium", "Off-road")

race_set = WheelsSetCreator(sport_wheel, sport_wheel, sport_wheel, sport_wheel)
winter_set = WheelsSetCreator(winter_wheel, winter_wheel, winter_wheel, winter_wheel)
summer_set = WheelsSetCreator(summer_wheel, summer_wheel, summer_wheel, summer_wheel)
off_road_set = WheelsSetCreator(off_road_wheel, off_road_wheel, off_road_wheel, off_road_wheel)
mix_set = WheelsSetCreator(winter_wheel, summer_wheel, winter_wheel, summer_wheel)

garage = [
    Vehicle('Jeep', slow_engine, off_road_body, off_road_set),
    Vehicle('Skoda', hyper_engine, sport_body, race_set),
    Vehicle('BMW', fast_engine, regular_body, mix_set),
    Vehicle('Audi', fast_engine, sport_body, summer_set),
    Vehicle('Mercedes', fast_engine, sport_body, winter_set)
]

for car in garage:
    print(car)
    car.move(5)
