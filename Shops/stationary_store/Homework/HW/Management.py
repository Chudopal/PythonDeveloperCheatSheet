import uuid

class Task:
    
    def __init__ (self, description: str, department: str, employee_experience: int):
        self.description = description
        self.department = department
        self.employee_experience = employee_experience


class Human:

    def __init__ (self, name: str, age: int):
        self.name = name
        self.uuid = uuid.uuid4()
        self.age = age


class Employee:

    def __init__ (self, experience: int, department:str, empl_dep: Human):
        self.experience = experience
        self.department = department
        self.empl_dep = empl_dep


    def complete_task (self, task:Task):
        if self.experience >= task.employee_experience and self.department == task.department:
            return f'Task {task.description} is done!'
        else:
            return f'Task {task.description} is not for me.'
        



empl_dev = Human("Kostya", 31)

kostya = Employee(3, "development", empl_dev)

task_one = Task("task", "development", 5)

print(Employee.complete_task(kostya, task_one))

