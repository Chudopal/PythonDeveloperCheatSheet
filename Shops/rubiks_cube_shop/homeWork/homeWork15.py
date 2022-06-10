"""
1. Животный мир:
- у собаки есть имя, возраст и любимая команда(например сидеть).
    Собака может лаять, то есть выводить в консоль
    "Hello, I'm {name}, and I'm woofing! My favorite command is {command}!"
- у кота есть имя, возраст и любимое место .
    Кот может мяукать, то есть выводить в консоль
    "Hello, I'm {name}, and I'm meowing! My favorite place is {fav_place}!"
- и у котов, и у собак есть метод presentate(),
который выводит следующее сообщение:
    'My name is {name}, my age is {age}'
Опишите это в коде.
"""


class Animal():
    
    def __init__(self, name: str, age: int) -> None:
        self._name = name
        self._age = age
        pass

    def presentate(self):
        print(f"My name is {self._name}, my age is {self._age}")


class Dog(Animal):
    
    def __init__(self, name: str, age: int, favorite_command: str) -> None:
        self._favorite_command = favorite_command
        super().__init__(name, age)

    def voice(self)->None:
        print(f"Hello, I'm {self._name}, and I'm woofing! My favorite command is {self._favorite_command}!")


class Cat(Animal):
    
    def __init__(self, name: str, age: int, favorite_place: str) -> None:
        self._favorite_place = favorite_place
        super().__init__(name, age)

    def voice(self)->None:
        print(f"Hello, I'm {self._name}, and I'm meowing! My favorite place is {self._favorite_place}!")


dog = Dog("Bobik", 3, "voice")
cat = Cat("Tima", 13, "palace")

dog.presentate()
cat.presentate()
dog.voice()
cat.voice()


"""
2. Система менеджмента сотрудников.
- Человек имеет имя, uuid, возраст
- Работник - это человек, у которого есть роль
    в компании и стаж работы, работник может выполнять задачу,
    если она его из его сферы и у него достаточно опыта для
    выполнения задачи. Если сотрудник может выполнить задачу,
    в консоль выводится:
    Task {task_description} is done!
    если выполнить не может, то
    Task {task_description} is not for me. 
- Задача имеет описание, сферу(разработка, бухгалтерия, hr, кадры...),
    а также уровень исполнителя, например 5 значит, что только работник
    с опытом 5 лет может ее исполнить
Опишите эту бизнес-логику в коде, можете добавить свои фичи =)
При желании можете сделать так, чтобы сотрудники брались из БД
"""

class People():
    
    def __init__(self, name: str, uuid: str, age: int) -> None:
        self._name  = name
        self._uuid = uuid
        self._age = age 


class Worker(People):

    def __init__(self, name: str, uuid: str, age: int, role: str, experiens: int) -> None:
        self._role = role
        self._experiens = experiens
        super().__init__(name, uuid, age)

    def check_task(self, task)->None:
        if task._service_sector == self._role and task._experiens <= self._experiens:
            print(f"Task {task._description} is done!")
        else:
            print(f"Task {task._description} is not for me.")



class Task():

    def __init__(self, description: str, service_sector: str, experiens: str) -> None:
        self._description = description
        self._service_sector = service_sector
        self._experiens = experiens


worker = Worker("Bob", "adsfasdf", 34, "developer", 3)
task = Task("Add OOP", "developer", 3)

worker.check_task(task)


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

import time
from urllib.parse import ParseResultBytes
import uuid


class Engine:
    
    def __init__(self, power: float) -> None:
        self._uuid = uuid.uuid4()
        self._power = power


class Wheels:
    
    def __init__(self, material: str, description: str) -> None:
        self._material = material
        self._description = description


class Corpus:
    
    def __init__(self, color: str, material: str) -> None:
        self._color = color 
        self._material = material


class Car:

    def __init__(self, model: str, engine: Engine, wheels: Wheels, corpus: Corpus) -> None:
        self._model = model
        self._engine = engine
        self._wheels = wheels
        self._corpus = corpus


class Action:

    def __init__(self) -> None:
        self._counter = 1

    def move(self, distanse: int, car: Car) -> None:
        self.start_move(car)
        total_time = self.drive(distanse, car) 
        self.finish_move(total_time)

    def print_car_info(self, car: Car)-> None:
        print(f"Model - {car._model}, wheels - {car._wheels._description}, corpus color - {car._corpus._color}.")

    def start_move(self, car: Car)->None:
        print(f"{self._counter}. ", end="")
        self.print_car_info(car)
        print("I'm starting.")

    def drive(self, distanse, car: Car)-> int:
        time_per1km =  1 / car._engine._power
        for i in range(distanse):
            time.sleep(time_per1km)
            print(f"{i+1} km")
        return time_per1km * distanse

    def finish_move(self, total_time)-> None:
        print("I'm stopping.")
        print(f"Total time - {total_time} s.")
        self._counter += 1


        

engine_05 = Engine(0.5)
engine_1 = Engine(1)
engine_2 = Engine(2)

wheels_2s2w = Wheels("rubber", "2 summer 2 winter")
wheels_4s = Wheels("rubber", "4 summer")
wheels_4w = Wheels("rubber", "4 winter")

corpus_red = Corpus("red", "aluminum")
corpus_green = Corpus("green", "aluminum")

car1 = Car("BMW", engine_05, wheels_2s2w, corpus_green)
car2 = Car("Audi", engine_1, wheels_4s, corpus_red)
car3 = Car("Geely", engine_2, wheels_4w, corpus_green)
car4 = Car("Ford", engine_05, wheels_2s2w, corpus_red)
car5 = Car("Renault", engine_1, wheels_4w, corpus_green)

action = Action()

# action.move(3, car1)
# action.move(2, car2)
# action.move(5, car3)
# action.move(3, car4)
# action.move(4, car5)







"""
4(EXTRA). Матрица
Город - площадка размера N на N
Агенты - перемещаются по городу(случайным образом),
    если будет на одной клетке с избранным, то избранный умрет
Избранный - просто перемещается по городу(случайным образом)
Агенты и избранный могут перемещаться: влево, вправо, вверх,
    вниз по сетке, если кто-то из них дошел до края сетки,
    то направление объекта меняется на противоположное.
Количество агентов и размер города задается через консоль.
Работает программа следующим образом:
выводится в консоль сетка N на N, где случайным образом
указано положение агентов и избранного, например:
C--
-A-
A--
потом итерация
-С-
A--
-A-
потом итерация
A--
-C-
--A
потом агент и избранный пересеклись:
-A-
--(C/A)
---
и воводится сообщение
Chosen is dead. Number of iterations - 4.
Так же можно сделать и с сеткой 5 на 5 или 10 на 10
- Каждая итерация выводится на экран.
- Время между итерациями - 0.5 сек.
Задержку между итерациями делаем через time:
import time
time.sleep(0.5) #остановит работу на 0.5 сек
Случайное перемещение можно сделать через random:
import random
random.randint(1, 4) # случайное число от 1 до 4 (включая 1 и 4)
"""
import random

class Interface:
    
    def input_size_map(self)->int:
        try:
            size_map = int(input("Enter map size:"))
        except:
            print("It is not a number!")
            size_map = self.input_size_map()
        return size_map

    def input_agents(self, size: int)->int:
        try:
            agents = int(input("Enter the number of agents:"))
        except:
            print("It is not a number!")
            agents = self.input_agents(size)
        agents = self.check_agents(agents, size)
        return agents

    def check_agents(self, agents: int, size: int)->int:
        corect_agents = agents
        if agents >= (size * size):
            print("Too many agents!")
            corect_agents = self.input_agents(size)
        return corect_agents

    def print_map(self, map: list)-> None:
        for row in map:
            print(' '.join([str(elem) for elem in row]))
        print("")
    

class Game: 
    
    def __init__(self, interface : Interface) -> None:
        self._interface = interface
        self._size = self._interface.input_size_map()
        self._agents = self._interface.input_agents(self._size)
        self._map = [["-"] * self._size for i in range(self._size)]
        self._position_agent = [[0, 0]] * self._agents 
        self._position_elected = [0, 0]
        self._stop = True
        self._counter = 0

    def start_game(self)->None:
        self.init_pos_agent()
        self.init_pos_elected()
        self._interface.print_map(self._map)
        self.run()
 
    def init_pos_agent(self):
        for i in range(len(self._position_agent)):
            pos = self.random_pos()
            self._position_agent[i] = pos
            self._map[pos[0]][pos[1]] = "A"

    def init_pos_elected(self)->list:
        pos = self.random_pos()
        if pos in self._position_agent:
            pos = self.init_pos_elected()
        self._map[pos[0]][pos[1]] = "C"
        self._position_elected = pos
        return pos

    def move(self):
        self.clear_map()
        self.new_pos_agent()
        self.new_pos_elected()
        self.set_new_pos()

    def clear_map(self):
        for i in range(self._size):
            for j in range(self._size):
                self._map[i][j] = "-"

    def new_pos_agent(self):
        for i in range(len(self._position_agent)):
            pos = self.check_pos(self._position_agent[i])
            self._position_agent[i] = pos

    def new_pos_elected(self):
        pos = self.check_pos(self._position_elected)
        self._position_elected = pos
    
    def check_pos(self, pos: list)->list:
        direction = random.randint(1, 4)
        if direction == 1:
            if pos[0] == 0:
                pos[0] += 1
            else:
                pos[0] -= 1
        elif direction == 2:
            if pos[1] == 0:
                pos[1] += 1
            else:
                pos[1] -= 1
        elif direction == 3:
            if pos[0] == self._size - 1:
                pos[0] -= 1
            else:
                pos[0] += 1
        elif direction == 4:
            if pos[1] == self._size - 1:
                pos[1] -= 1
            else:
                pos[1] += 1
        return pos

    def set_new_pos(self):
        for pos in self._position_agent:
            self._map[pos[0]][pos[1]] = "A"
        self._map[self._position_elected[0]][self._position_elected[1]] = "C"

    def random_pos(self):
        return [random.randint(0, self._size - 1), random.randint(0, self._size - 1)]

    def run(self):
        while self._stop:
            time.sleep(3)
            self.move()
            self._counter += 1
            self._interface.print_map(self._map)
            if self._position_elected in self._position_agent:
                self._stop = False
                self._map[self._position_elected[0]][self._position_elected[1]] = "(C/A)" 
                self._interface.print_map(self._map)
                print(f"Chosen is dead. Number of iterations - {self._counter}.")


interface = Interface()
game = Game(interface)
game.start_game()