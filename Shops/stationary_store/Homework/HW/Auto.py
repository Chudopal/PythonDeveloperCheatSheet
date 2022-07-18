import time
from uuid import uuid4


class Car:

    def __init__(self, engine: str, wheels: str, corpus: str, model: str) -> None:
        self.engine = engine
        self.wheels = wheels
        self.corpus = corpus
        self.model = model
   
    def print_car_info(self):
        return f'Model - {self.model}, wheels - {self.wheels.description}, corpus color - {self.corpus.color}.'

    def move (self):
        total_time = 0
        distance = int(input("Enter number of kilometers: "))
        total_time_engine = self.engine.power * distance
        print("I'm starting.")
        while total_time <= distance:
            print(total_time)
            total_time += 1
            time.sleep(0.5)
        print("I'm stopping.")
        return f'Total time - {total_time_engine} s.'


class Wheels:

    def __init__(self, material:str, description: str) -> None:
        self.material = material
        self.description = description


class Corpus:

    def __init__(self, material:str, color: str) -> None:
        self.material = material
        self.color = color


class Engine:

    def __init__(self, power: float) -> None:
        self.sn = uuid4()
        self.power = power

wheels_set_1 = Wheels("rubber", "2 summer 2 winter")
wheels_set_2 = Wheels("rubber", "4 summer")
wheels_set_3 = Wheels("rubber", "4 winter")


corpus_type_1 = Corpus("steel", "grey")
corpus_type_2 = Corpus("steel", "green")
corpus_type_3 = Corpus("steel", "blue")
corpus_type_4 = Corpus("steel", "red")
corpus_type_5 = Corpus("steel", "black")


engine_05 = Engine(0.5)
engine_1 = Engine(1)
engine_2 = Engine(2)


car_1 = Car(engine_2, wheels_set_1, corpus_type_1, "BMW")
car_2 = Car(engine_2, wheels_set_1, corpus_type_2, "Audi")
car_3 = Car(engine_1, wheels_set_2, corpus_type_3, "KIA")
car_4 = Car(engine_1, wheels_set_2, corpus_type_4, "Honda")
car_5 = Car(engine_05, wheels_set_1, corpus_type_5, "Opel")