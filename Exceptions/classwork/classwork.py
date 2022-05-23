a = [1,2,3]
index = None

try:
    index  = int(input("Enter index: "))
except ValueError as e:
    print(e)

result = 10

try:
    result = a[index]
except IndexError as e:
    print(e)
except TypeError as e:
    print(e)


print(f"Your values is {result}")


import json

try:
    file = open("1.json")
    file.read() # ошибка!
except FileNotFoundError as e:

    with open("1.json") as file:
        data = json.load(file)

finally:
    file.close()

print(data)


def foo():
    1/0


def bar():
    foo()


def fun():
    bar()


try:
    fun()
except ZeroDivisionError as e:
    print("На ноль делить нельзя!")


# ДОБАВЛЕНИЕ ИСКЛЮЧЕНИЙ В ПРИМЕР С ПРОШЛОГО ЗАНЯТИЯ


class AgeTooSmallException(Exception):
    pass


class TooLongNameException(Exception):
    pass


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property # getter
    def name(self):
        return self._name
    
    @name.setter # setter
    def name(self, name):
        if len(name) > 10:
            raise TooLongNameException(
                "Имя должно быть меньше 10 символов"
            )
        self._name = name
    

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if age < 18:
            raise AgeTooSmallException(
                "Пользователь должен быть старше 18"
            )
        self._age = age

    def __str__(self):
        return f"name - {self._name}, age - {self._age}"

    def __add__(self, persone):
        return self._age + persone._age


try:
    p = Person("BOBsdfghjkjhgfdsdfghjkjhgfd", 18)
except AgeTooSmallException as e:
    print(e)
except TooLongNameException as e:
    print(e)

p.name = "BOBBOBBOBBOBBOBBOBBOB"
print(p.name)
p1 = Person("Alice", 10)

print(p+p1)



# ДЕЛАЛИ ПОСЛЕ ЗАНЯТИЯ



from dataclasses import dataclass
from abc import ABC, abstractmethod


@dataclass
class Dog():
    name: str
    age: int


class Repository(ABC):

    @abstractmethod
    def save(dog: Dog):
        """This method should save a dog."""


class Interface(ABC):

    @abstractmethod
    def send(message: str):
        """This method represents data."""


class DogRepository:

    def __init__(self, repository: Repository, interface: Interface):
        self.repository = repository
        self.interface = interface

    def create(self, name, age) -> Dog:

        dog = Dog(name, age)
        self.repository.save(dog)
        self.interface.send("Dog created")


class JSONRepository(Repository):

    def __init__(self, json_file_path):
        self.json_file_path

    def save(dog: Dog):
        ...



class DBRepository(Repository):

    def __init__(self, connection):
        self.connection

    def save(dog: Dog):
        ...

class ConsoleInterface(Interface):

    def send(message: str):
        print(message)


class TelegramInterface(Interface):

    def __init__(self, token: str):
        self.token


    def send(message: str):
        ...


repository = DogRepository(JSONRepository("vvv"), TelegramInterface())