class Car:

    def __init__(self, speed, people_number):
        self.speed = speed
        self.people_number = people_number

    def move(self):
        print(f"MOVE. SPEED IS {self.speed}")


this_car = Car(speed=120, people_number=4)
this_car1 = Car(speed=90, people_number=4)
this_car2 = Car(speed=200, people_number=4)

this_car.move()
this_car1.move()
this_car2.move()


import json

class JsonFileHandler:

    def __init__(self, path: str):
        self.path = path

    def save(self, data):
        with open(self.path, "w") as file:
            json.dump(data, file, indent=4) 

    def read(self):
        with open(self.path) as file:
            data = json.load(file)
        return data


class Car():

    def __init__(self, price, name):
        self.price = price
        self.name = name
    
    def get_json(self):
        return {
            "price": self.price,
            "name": self.name
        }


json_handler = JsonFileHandler("storage.json")

data = {
    "a": 1
}

json_handler.save(data)

print(json_handler.read())


class Cat:

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def make_sound(self):
        return f"Meow. Hello my name" \
            f" is {self.name} and my color"\
            f" is {self.color}"


cat = Cat("Barsik", "green")
sound = cat.make_sound()
print(sound)

cat1 = Cat("Ball", "red")
sound = cat1.make_sound()
print(sound)


class Order:

    def __init__(self):
        self.products = list()

    def add_product(self, product):
        self.products.append(product)

    def calculate_price(self) -> int:
        price = 0
        for product in self.products:
            price += product.get("price")
        return price

    def get_json(self):
        return {
            "products": self.products
        }


order = Order()
json_handler = JsonFileHandler("1.json")

order.add_product({"name": "A", "price": 10})
order.add_product({"name": "A", "price": 10})
order.add_product({"name": "A", "price": 10})

order.add_product({"name": "B", "price": 20})
order.add_product({"name": "B", "price": 20})
order.add_product({"name": "B", "price": 20})

print(order.calculate_price())

json_handler.save(order.get_json())


class Animal:

    def __init__(self, speed):
        self.speed = speed

    def walk(self):
        print(f"My speed is {self.speed}")


class Cat(Animal):

    def __init__(self, name, speed):
        self.name = name
        super().__init__(speed)

    def walk(self):
        print(f"I'm cat.")
        super().walk()


class Dog(Animal):

    def __init__(self, name, speed):
        self.name = name
        super().__init__(speed)
    
    def run(self):
        print(f"I'm running. My speed is {self.speed * 2}")


# cat = Cat("Bob", 4)
# cat.walk()

dog = Dog("Sharick", 5)
dog.walk()
dog.run()


a = list()

class Car():

    def __init__(self, speed):
        self._max_speed = 10
        self.set_speed(speed)

    def set_speed(self, speed):
        if speed <= self._max_speed:
            self._speed = speed
        else:
            self._speed = self._max_speed

    def move(self):
        self._start()
        self._drive()
        self._stop()
    
    def _start(self):
        for i in range(self._speed + 1):
            print(i)

    def _drive(self):
        print(f"Driving, speed is {self._speed}")

    def _stop(self):
        for i in range(self._speed, -1, -1):
            print(i)


car = Car(20)
car.move()

class Animal:

    def __init__(self, speed):
        self.speed = speed

    def walk(self):
        print(f"My speed is {self.speed}")


class Cat(Animal):

    def __init__(self, name, speed):
        self.name = name
        super().__init__(speed)
    
    def make_sound(self):
        print("Meow")


class Dog(Animal):

    def __init__(self, name, speed):
        self.name = name
        super().__init__(speed)
    
    def make_sound(self):
        print("Woof")


def record(item):
    item.make_sound()

cat = Cat("Bob",5)
dog = Dog("Did",7)

record(cat)
record(dog)

import json

class JsonFileHandler:

    def __init__(self, path: str):
        self.path = path

    def save(self, data):
        with open(self.path, "w") as file:
            json.dump(data, file, indent=4) 

    def read(self):
        with open(self.path) as file:
            data = json.load(file)
        return data



class GlobalStorageHandler():
    
    def __init__(self, storage):
        self._storage = storage
    
    def save(self, data):
        self._storage.append(data)
    
    def read(self):
        return self._storage





STORAGE = list()

def process(data, handler):
    # some logic
    handler.save(data)

handler = JsonFileHandler("1.json")
data = {"a": 1}
global_handler = GlobalStorageHandler(STORAGE)

print(STORAGE)
process(data, handler)
print(STORAGE)