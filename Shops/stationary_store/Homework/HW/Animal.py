class Animal:

    def __init__ (self, name:str, age:int) -> None:
        self.name = name
        self.age = age

    def presentate (self):
        return f'My name is {self.name}, my age is {self.age}'

class Dog:

    def __init__ (self, dog: Animal, command: str):
        self.dog = dog
        self.command = command

    def bark (self):
        return f"Hello, I'm {dog.name}, and I'm woofing! My favorite command is {self.command}!"


class Cat:

    def __init__ (self, cat: Animal, fav_place: str):
        self.cat = cat
        self.fav_place = fav_place

    def mew (self):
        return f"Hello, I'm {cat.name}, and I'm meowing! My favorite place is {self.fav_place}!"


dog = Animal ("Movie", 2)
cat = Animal ("Molly", 2)
movie = Dog(dog,"sit")
molly = Cat(cat,"armchair")