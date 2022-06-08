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


class People:

    def __init__(self, name: str, uuid: str, age: int) -> None:
        self.name = name
        self.uuid = uuid
        self.age = age


class Worker(People):

    def __init__(
        self,
        name: str,
        uuid: str,
        age: int,
        job: str,
        work_experience: str,
        task_description: str
) -> None:
        super().__init__(name, uuid, age)
        self.job = job
        self.work_experience = work_experience
        self.task_description = task_description

    def get_positive_task(self):
        return f"Task {self.task_description} is done!"

    def get_negative_task(self):
        return f"Task {self.task_description} is not for me."


class Task:

    def __init__(self, description: str, sphere: str, experience: int) -> None:
        self.description = description
        self.sphere = sphere
        self.experience = experience

    
class Management:
    pass 