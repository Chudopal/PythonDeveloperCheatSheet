class Animal:

    def __init__ (self, name:str, age:int) -> None:
        self.name = name
        self.age = age

    def presentate (self):
        return f'My name is {self.name}, my age is {self.age}'

class Dog(Animal):

    def __init__ (self, name: str, age: int, command: str):
        self.name = name
        self.age = age
        self.command = command

    def make_sound (self):
        return f"Hello, I'm {self.name}, and I'm woofing! My favorite command is {self.command}!"


class Cat(Animal):

    def __init__ (self, name: str, age: int, fav_place: str):
        self.name = name
        self.age = age
        self.fav_place = fav_place

    def make_sound (self):
        return f"Hello, I'm {self.name}, and I'm meowing! My favorite place is {self.fav_place}!"