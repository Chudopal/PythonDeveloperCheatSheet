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

from uuid import uuid4
from dataclasses import dataclass


@dataclass
class Task:
    description: str
    field: str
    experience: int


class Human:

    def __init__(self, uuid: str, name: str, age: int):
        self.uuid = uuid
        self.name = name
        self.age = age


class Worker(Human):

    def __init__(self, uuid: str, name: str, age: int, field_of_activity: str, experience: int):
        self.field_of_activity = field_of_activity
        self.experience = experience
        super().__init__(uuid, name, age)

    def check_task(self, task: Task):
        if (task.experience <= self.experience) and (task.field == self.field_of_activity):
            print(f"Task {task.description} is done!")
        else:
            print(f"Task {task.description} is not for me.")
