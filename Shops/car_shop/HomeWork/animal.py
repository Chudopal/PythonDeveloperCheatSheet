class Animal:


    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    
    def presentate(self):
        print(f"My name is {self.name}, my age is {self.age}")


class Dog(Animal):


    def __init__(self, name: str, age: int, favorite_command: str):
        self.favorite_command = favorite_command
        super().__init__(name, age)
        

    
    def make_command(self):
            print(f"Hello, I'm {self.name}, and I'm woofing! My favorite command is {self.favorite_command}!")



class Cat(Animal):


    def __init__(self, name: str, age: int, fav_place: str):
        self.fav_place = fav_place
        super().__init__(name, age)


    def sit_favorite_place(self):
        print(f"Hello, I'm {self.name}, and I'm meowing! My favorite place is {self.fav_place}!")
        

cat = Cat('Barsik', 2, 'Table')
cat.sit_favorite_place()
cat.presentate()
        
dog = Dog('Sharik', 5, 'Sit')
dog.make_command()
dog.presentate()


