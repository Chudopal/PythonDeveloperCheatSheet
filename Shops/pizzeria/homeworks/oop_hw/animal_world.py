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


class Animal:

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def presentate(self):
        print(f'My name is {self.name}, my age is {self.age}')


class Dog(Animal):

    def __init__(self, name: str, age: int, fav_command: str):
        self.fav_command = fav_command
        super().__init__(name, age)

    def make_sound(self):
        print(f"Hello, I'm {self.name}, and I'm woofing! My favorite command is {self.fav_command}!")


class Cat(Animal):

    def __init__(self, name: str, age: int, fav_place: str):
        self.fav_place = fav_place
        super().__init__(name, age)

    def make_sound(self):
        print(f"Hello, I'm {self.name}, and I'm meowing! My favorite place is {self.fav_place}!")
