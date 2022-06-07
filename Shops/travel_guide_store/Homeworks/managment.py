"""2. Система менеджмента сотрудников.
- Человек имеет имя, uuid, возраст
- Работник - это человек, у которого есть роль
    в компании и стаж работы, работник может выполнять задачу,
    если она его из его сферы и у него достаточно опыта для
    выполнения задачи. Если сотрудник может выполнить задачу,
    в консоль выводится:
    Task {task_description} is done!
    если выполнить не может, то
    Task {task_description} is not for me. 
- Задача имеет описание, сферу(разработка, бухгалтерия, hr, кадры...),
    а также уровень исполнителя, например 5 значит, что только работник
    с опытом 5 лет может ее исполнить"""

from uuid import uuid4

class Person:
    def __init__ (self, uuid:uuid4(), name: str, age: int):
        self.uuid = uuid4()
        self.name = name
        self.age = age
        
class Task:
    def __init__ (self, description:str, sector:str, level:int):
        self.description = description
        self.sector = sector
        self.level = level

class Employee(Person):
    def __init__ (self, name:str, age: int, role: str, experience: int, sector: str):
        super().__init__(self, name, age)
        self.role = role
        self.experience = experience
        self.sector = sector
        

    def operation(self, task: Task):
        result = ""
        if (self.experience >= task.level) and (self.sector == task.sector):
            result = f'Task {task.description} is done!'
        else:
            result = f'Task {task.description} is not for me.'
        return result


# проверка
chel1 = Employee( "Petr", 39, "Master", 18, "STO")
print(chel1.operation(Task("Починить авто", "STO", 15)))
print(chel1.operation(Task("Починить авто", "IT", 3)))
print(chel1.uuid)