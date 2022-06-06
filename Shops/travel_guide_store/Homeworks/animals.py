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

"""
class Animals ():
    def __init__ (self, name, age):
        self.name = name
        self.age = age

    def presentate(self):
        print(f'My name is {self.name}, my age is {self.age}')


class Cat(Animals):
    def __init__(self, name:str, age: int, fav_place: str):
        self.fav_place = fav_place
        super().__init__(name=name, age=age)

    def introduce(self):
        print(f"Hello, I'm {self.name}, and I'm meowing! My favorite place is {self.fav_place}!")


class Dog(Animals):
    def __init__(self, name:str, age:int, command:str):
        self.command = command
        super().__init__(name=name, age=age)

    def introduce(self):
        print(f"Hello, I'm {self.name}, and I'm woofing! My favorite command is {self.command}!")

# проверка
cat1 = Cat("Tom", 3, "window")
dog1 = Dog("Duk", 5, "Take it!")
print(cat1.introduce())
print(dog1.introduce())
cat2=Cat("Mishel", 5, "bed")
print(cat2.presentate())