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

from uuid import uuid4
import time


class Engine:
    type = None

    def __init__(self, power: float):
        self.serial_number = uuid4()
        self.power = power


class DieselEngine(Engine):
    type = "Diesel"


class GasolineEngine(Engine):
    type = "Gasoline"


class ElectricityEngine(Engine):
    type = "Electricity"


class Wheel:
    material = None
    description = None


class WinterWheel(Wheel):
    material = "Steel"
    description = "Winter"


class SummerWheel(Wheel):
    material = "Steel"
    description = "Summer"


class SportWheel(Wheel):
    material = "Carbon"
    description = "Sport"


class OffRoadWheel(Wheel):
    material = "Titan"
    description = "OffRoad"


class Body:
    def __init__(self, color: str):
        self.color = color


class HatchbackBody(Body):
    material = "Aluminium"
    type = "Hatchback"


class SportBody(Body):
    material = "Carbon"
    type = "Sport"


class OffRoadBody(Body):
    material = "Titan"
    type = "OffRoad"


class CoupeBody(Body):
    material = "Aluminium"
    type = "Coupe"


class WheelsSet:
    def __init__(self, *wheels: Wheel):
        self.wheels = wheels
        self.wheels_set = dict()
        self._format_wheels()

    def __repr__(self):
        return " ".join(f"{value} {key}" for key, value in self.wheels_set.items())

    def _format_wheels(self):
        for wheel in self.wheels:
            if not self.wheels_set.get(wheel.description):
                self.wheels_set[wheel.description] = 1
            else:
                self.wheels_set[wheel.description] += 1


class Vehicle:
    def __init__(self, model: str, body: Body, engine: Engine, wheels: WheelsSet):
        self.model = model
        self.body = body
        self.engine = engine
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


class VehicleCreator:
    def __init__(self):
        self.all_engines = {
            "Gasoline": GasolineEngine,
            "Diesel": DieselEngine,
            "Electric": ElectricityEngine
        }
        self.all_bodies = {
            "Hatch": HatchbackBody,
            "Sport": SportBody,
            "OffRoad": OffRoadBody,
            "Coupe": CoupeBody
        }
        self.all_wheels = {
            "Winter": WinterWheel,
            "Summer": SummerWheel,
            "Sport": SportWheel,
            "OffRoad": OffRoadWheel
        }

    def create_wheel_set(self, wheels: tuple[str]) -> WheelsSet:
        return WheelsSet(*[self.all_wheels.get(wheel)() for wheel in wheels])

    def create(self, model: str, body: str, color: str, engine: str, power: float, *wheels: str) -> Vehicle:
        return Vehicle(
            model,
            self.all_bodies.get(body)(color),
            self.all_engines.get(engine)(power),
            self.create_wheel_set(wheels)
        )


garage = [
    VehicleCreator().create('Jeep', 'OffRoad', 'Green', 'Diesel', 2, "OffRoad", "OffRoad", "OffRoad", "OffRoad"),
    VehicleCreator().create('Skoda', 'Sport', 'Green', 'Gasoline', 0.3, "Summer", "Summer", "Summer", "Summer"),
    VehicleCreator().create('BMW', 'Coupe', 'Black', 'Diesel', 1, "Summer", "Summer", "Winter", "Winter"),
    VehicleCreator().create('Audi', 'Hatch', 'Red', 'Gasoline', 1, "Sport", "Sport", "Sport", "Sport"),
    VehicleCreator().create('Tesla', 'Hatch', 'White', 'Electric', 0.6, "Summer", "Summer", "Summer", "Summer")
]

for car in garage:
    print(car)
    car.move(5)
