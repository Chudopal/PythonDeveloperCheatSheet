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


...

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