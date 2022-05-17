class Animal:
    def make_sound(self):
        print("Sound")


class Cat(Animal):

    def make_sound(self):
        print("Meow")

    def walk(self):
        print("I'm walking")


class Dog(Animal):
    def make_sound(self):
        print("Woof")


class WalkingMixIn():
    def walk(self):
        print("I'm walking now")


class CatDog(WalkingMixIn ,Dog, Cat):
    pass


print(CatDog.mro())



class Shop:

    products = ["rice", "eggs"]

    def __init__(self, name: str, square: int):
        self._name = name
        self._square = square


    def describe(self):
        print(self._name, self._square, self.products)


    @classmethod
    def format_products(cls):
        return "\n".join(cls.products)


    def print_hello():
        print("HEllo")
    
    def sell(self):
        print(self.__name)


s = Shop("Magnit", 100)
s.describe()
print(s.products)
s.products.append("Append")
s.describe()


s1 = Shop("Sosedi", 20)
print(s1.format_products())

print(Shop.format_products())
Shop("Sosedi", 20).print_hello()

print(Shop.products)
Shop.describe()


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
except TooLongNameExcaption as e:
    print(e)

p.name = "BOBBOBBOBBOBBOBBOBBOB"
print(p.name)
p1 = Person("Alice", 10)

print(p+p1)



from dataclasses import dataclass, field




@dataclass()
class Bill:

    price: int
    amount: int

    def get_json(self):
        return self.__dict__


b = Bill(100, 10)
print(b.get_json())


from uuid import uuid4

class Bill():

    def __init__(self):
        self.bill_uuid = str(uuid4())


print(Bill().bill)


def main_menu():
    choice = None
    while choice != 0:
        print("""
        0 - Выход
        1 - Посмотреть товары/Добавить в корзину
        2 - Посмотреть корзину
        """)
        choice = int(input('Выберите действие: '))
        
        if choice == 1:
            print("ff")
        elif choice == 2:
            print("ddd")
        elif choice not in [0,1,2]:
            print('Неверный выбор')

    print('Пока')
main_menu()