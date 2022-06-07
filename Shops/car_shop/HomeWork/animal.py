class Animal:


    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


class Dog(Animal):


    def __init__(self, name: str, age: int, favorite_command: str):
        self.favorite_command = favorite_command
        super().__init__(name, age)
        

    
    def make_command(self):
            print(f"Hello, I'm {self.name}, and I'm woofing! My favorite command is {self.favorite_command}!")



class Cat(Animal):


    def __init__(self, name: str, age: int, favorite_place: str):
        self.favorite_place = favorite_place
        super().__init__(name, age)


    def favorite_place(self):
        print(f"Hello, I'm {self.name}, and I'm meowing! My favorite place is {self.favorite_place}!")
        

cat = Cat('Barsik', 2, 'Table')
cat.favorite_place()
        
dog = Dog('Sharik', 5, 'Sit')
dog.make_command()
