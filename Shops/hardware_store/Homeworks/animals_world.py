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

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def presentate(self):
        return f'My name is {self.name}, my age is {self.age}'


class Dog(Animal):

    def __init__(self, name: str, age: int, command: str) -> None:
        super().__init__(name, age)
        self.command = command

    def make_sound(self):
        return f"Hello, I'm {self.name}, and I'm woofing! My favorite command is {self.command}!"


class Cat(Animal):

    def __init__(self, name: str, age: int, fav_place: str) -> None:
        super().__init__(name, age)
        self.fav_place = fav_place

    def make_sound(self):
        return f"Hello, I'm {self.name}, and I'm meowing! My favorite place is {self.fav_place}!"


cat = Cat('Murka', 4, 'windowsill')
dog = Dog('Bonni', 4, 'sit')
print(cat.make_sound())
print(dog.make_sound())