# 1. Животный мир:
# - у собаки есть имя, возраст и любимая команда(например сидеть).
#     Собака может лаять, то есть выводить в консоль
#     "Hello, I'm {name}, and I'm woofing! My favorite command is {command}!"
# - у кота есть имя, возраст и любимое место .
#     Кот может мяукать, то есть выводить в консоль
#     "Hello, I'm {name}, and I'm meowing! My favorite place is {fav_place}!"
# - и у котов, и у собак есть метод presentate(),
# который выводит следующее сообщение:
#     'My name is {name}, my age is {age}'

class Animal:

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def presentate(self):
        print(f"My name is {self.name}, my age is {self.age}")


class Dog(Animal):

    def __init__(self, name: str, age: int, command: str):
        super().__init__(name, age)
        self.command = command

    def message(self):
        print(f"Hello, I'm {self.name}, and I'm woofing! My favorite command is {self.command}!")


class Cat(Animal):

    def __init__(self, name: str, age: int, fav_place: str):
        super().__init__(name, age)
        self.fav_place = fav_place

    def message(self):
        print(f"Hello, I'm {self.name}, and I'm meowing! My favorite place is {self.fav_place}!")


# 2. Система менеджмента сотрудников.
# - Человек имеет имя, uuid, возраст
# - Работник - это человек, у которого есть роль
#     в компании и стаж работы, работник может выполнять задачу,
#     если она его из его сферы и у него достаточно опыта для
#     выполнения задачи. Если сотрудник может выполнить задачу,
#     в консоль выводится:
#     Task {task_description} is done!
#     если выполнить не может, то
#     Task {task_description} is not for me.
# - Задача имеет описание, сферу(разработка, бухгалтерия, hr, кадры...),
#     а также уровень исполнителя, например 5 значит, что только работник
#     с опытом 5 лет может ее исполнить
# Опишите эту бизнес-логику в коде, можете добавить свои фичи =)

from uuid import uuid4


class Task:
    def __init__(self, description, sphere, work_exp_level):
        self.description = description
        self.sphere = sphere
        self.work_exp_level = work_exp_level


class Human:
    def __init__(self, name: str, age: int, uuid: str):
        self.name = name
        self.age = age
        self.uuid = uuid


class Worker(Human):
    def __init__(self, name: str, age: int, uuid: str, role: str, work_exp: int):
        super().__init__(name, age, uuid)
        self.role = role
        self.work_exp = work_exp

    def make_task(self):
        if (self.role = self.sphere) and (
                self.work_exp >= self.work_exp_level):  ## возможно правильно будет self.role = Task().sphere
            print(f"Task {self.description} is done!")
        else:
            print(f"Task {self.description} is not for me.")
