import uuid


class Person:
    
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.uuid = uuid.uuid4()
        self.age = age


class Task:

    def __init__(self, task_description: str, task_area: str, experience: int) -> None:
        self.task_description = task_description
        self.task_area = task_area
        self.experience = experience    


class Employee(Person):

    def __init__(self, name: str, age: int, role: str, employee_exp: str) -> None:
        super().__init__(name, age)
        self.role = role
        self.employee_exp = employee_exp

    def make_task(self, task: Task):
        if self.employee_exp >= task.experience and self.role == task.task_area:
            task_result = f'Task {task.task_description} is done!'
        else:
            task_result = f'Task {task.task_description} is not for me.'

        return task_result


employee = Employee('Vasily Madzhahedov', 12, 'Developer', 3)
print(employee.make_task(Task('Car repair', 'Mechanic', 1)))
print(employee.make_task(Task('Create web-service', 'Developer', 1)))
