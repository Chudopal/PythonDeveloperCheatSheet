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


cat = Cat('barsik', 15, 'kjhyh')
cat.make_sound()


ROUND((SUM(price*amount)*(18/100))/1+(18/100),2)