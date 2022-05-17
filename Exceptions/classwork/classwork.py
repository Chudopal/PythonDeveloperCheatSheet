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


class WrongInput(Exception):
    pass

product_list = [1,2,3,4]
order_list = []


index  = int(input("Enter index: ")) # неправильный ввод


def add_product(index):
    order_list.append(product_list[index]) # нет индекса
    
add_product("egg")
print(order_list)

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