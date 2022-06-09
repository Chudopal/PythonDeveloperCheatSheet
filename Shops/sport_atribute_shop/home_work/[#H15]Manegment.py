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


from uuid import UUID, uuid4


class People:

    def __init__(self, name: str, uuid: UUID, age: int) -> None:
        self.name = name
        self.uuid = uuid4()
        self.age = age


class Worker(People):

    def __init__(
        self,
        name: str,
        uuid: UUID,
        age: int,
        sphere: str,
        work_experience: str
) -> None:
        super().__init__(name, uuid, age)
        self.sphere = sphere
        self.work_experience = work_experience


class Task:

    def __init__(self, description: str,
    sphere: str,
    experience: int,
    task_description: str,
    worker: Worker
    ) -> None:
        self.description = description
        self.sphere = sphere
        self.experience = experience
        self.task_description = task_description
        self.worker = worker

    def get_positive_task(self):
        return f"Task {self.task_description} is done!"

    def get_negative_task(self):
        return f"Task {self.task_description} is not for me."

    def get_task(self):
        if (self.worker.work_experience >= self.experience) and (self.worker.sphere == self.sphere):
            self.get_positive_task()
        else: 
            self.get_negative_task()

