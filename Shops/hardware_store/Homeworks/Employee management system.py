"""
2. Система менеджмента сотрудников.
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
    с опытом 5 лет может ее исполнить
Опишите эту бизнес-логику в коде, можете добавить свои фичи =)
При желании можете сделать так, чтобы сотрудники брались из БД
"""

import uuid


class Human:

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.uuid = uuid.uuid4()
        self.age = age


class Task:

    def __init__(self, description: str, area: str, exp: int) -> None:
        self.description = description
        self.area = area
        self.exp = exp


class Employee(Human):

    def __init__(self, name: str, age: int, role: str, employee_exp: str) -> None:
        super().__init__(name, age)
        self.role = role
        self.employee_exp = employee_exp

    def make_object(self, task: Task):
        if self.employee_exp >= task.exp and self.role == task.area:
            result = f'Task {task.description} is done!'
        else:
            result = f'Task {task.description} is not for me.'

        return result


employee = Employee('Nikita Gorohin ', 56, 'Businessman', 5)
print(employee.make_object(Task('treat people', 'Doc', 1)))
print(employee.make_object(Task('business analyst', 'Businessman', 4)))