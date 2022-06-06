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

    def make_woof(self):
        return f"Hello, I'm {self.name}, and I'm woofing! My favorite command is {self.command}!"


class Cat(Animal):
    
    def __init__(self, name: str, age: int, fav_place: str) -> None:
        super().__init__(name, age)
        self.fav_place = fav_place

    def make_meow(self):
        return f"Hello, I'm {self.name}, and I'm meowing! My favorite place is {self.fav_place}!"


cat = Cat('Мурзилка', 12, 'Лоток')
dog = Dog('Бублик', 4, 'Ести')
print(cat.make_meow())
print(dog.make_woof())
