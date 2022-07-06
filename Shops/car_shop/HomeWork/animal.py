# #Task 1
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



#Task 2
from uuid import uuid4

class User:

    def __init__(self, name: str, age: int):
        self.name = name
        self.uuid = uuid4()
        self.age = age


class Task:

    def __init__(self, description: str, sphere: str, experience: int):
        self.description = description
        self.sphere = sphere
        self.experience = experience


class Employee(User):

    def __init__(self, name: str, age:int, sphere: str, experience:int):
        self.sphere = sphere
        self.experience = experience
        super().__init__(name, age)

    
    def task_execution(self, task: Task):
        if (self.experience >= task.experience) and (self.sphere == task.sphere):
            print(f"Task {task.description} is done!")
        else:
            print(f"Task {task.description} is not for me. ")


employee = Employee('Bob', 20, 'developer', 5)
task = Task('add OOP', 'developer', 5)

employee.task_execution(task)








