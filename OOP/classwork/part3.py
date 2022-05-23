class TooBigNumberException(Exception):
    pass

def div(a, b):
    result = None
    if a > 1_000_000_000:
        raise TooBigNumberException("Слишком большое число")
    try:
        result = round(a/b, 2)
    except ZeroDivisionError:
        result = "Поделить нельзя"
    return result


print(div(1_000_000_000_000,2))


print(div(1,3))
print(div(1,0))




c = 0

while c < len(a):
    print(a[c])
    c += 1

class Repository:

    def __init__(self):
        self.c = 0
        self._a = [1,2,3]

    def __iter__(self):
        return self

    def __next__(self):
        
        if self.c < len(self._a):        
            result = self._a[self.c]
            self.c += 1
        else:
            raise StopIteration

        return result


r = Repository()



for i in r:
    print(i)


a = [1,2,3]

for i in a:
    print(i)


def iterate(c):
    for i in c:
        print(i)
    print("_"*10)

a = [1,2,3]

c = [i**2 for i in a]
iterate(c)
iterate(c)

c = (i**2 for i in a)
a = list(c)
a = list(c)

iterate(a)
iterate(a)

def generate(start_list):
    for item in start_list:
        yield item ** 2

print(list(generate([1,2,3,4])))

print(list(generate([1,2,3,4])))


from dataclasses import dataclass
from uuid import uuid4, UUID


@dataclass
class User:
    name: str
    age: int
    user_uuid: UUID = uuid4()


class FormatService:

    def execute(self, user: User):
        result = f"Your name is {user.name}."
        result += f"Your age is {user.age}."
        result += f"You uuid is {user.user_uuid}."
        return result


service = FormatService()
user = User("Name", 18)
result = service.execute(user)


with open("1.txt") as file:
    text = file.read()

import re

incorrect_chars = r"[\%\&\@\#\-\^]"

text = re.sub(incorrect_chars,"",text)
print(text)


"""
Программа для больнице
Есть пациент
Есть доктор
Доктор выписывает поциенту диагноз
"""



from typing import List
from uuid import UUID
import json


class Persone:

    def __init__(
        self,
        age: int,
        name: str,
        uuid: UUID
    ):
        self._age = age
        self._name = name
        self._uuid = uuid 


class Diagnosis:
    
    def __init__(
        self,
        sick: str,
        description: str,
        patient: "Patient"
        ):
        self._sick = sick
        self._description = description
        self._patient = patient


class Doctor(Persone):
    
    def __init__(
        self,
        age: int,
        name: str,
        field: str,
        storage: "FileStorage", 
        ):
        self._storage = storage
        self._field = field
        super().__init__(age, name)

    def make_diagnosis(
        self, 
        patient: 'Patient',
        sick: str,
        description: str
        ) -> Diagnosis:

        diagnosis_list = self._storage.get()
        diagnosis = Diagnosis(
            patient=patient,
            sick=sick,
            description=description
        )
        diagnosis_list.append(diagnosis)
        self._storage.save(diagnosis)
        return diagnosis
    
    def get_json(self):
        return {
            "age" : self._age ,
            "name" : self._name ,
            "field" : self._field ,
        }


class Patient(Persone):

    def __init__(
        self,
        age: int,
        name: str,
        height: float,
        weight: float
        ):
        self._height = height
        self._weight = weight
        super().__init__(age, name)


class FileStorage:

    def __init__(
        self,
        path: str,
        key: str,
        model: type
        ):
        self._path = path
        self._key = key
        self._model = model

    def get(self) -> List:
        with open(self._path) as file:
            data = json.load(file).get(self._key)
        return [self._model(**item) for item in data]

    def save(self, data: List):
        data = [item.get_json() for item in data]
        with open(self._path) as file:
            raw_data = json.load(file)
            raw_data[self._key] = data
            json.dump(raw_data, file)


class SQLStorage():
    pass


class EventSourcingStorage():
    pass

patient_storage = FileStorage("1.json", "patients", Patient)
doctor_storage = FileStorage("1.json", "doctors", Doctor)


Doctor(..., storage=patient_storage)

class Clinic():
    pass


{
    "patients": [],
    "doctors": [],
    "diagnosis": [
        {
            "sick": "dfg",
            "description": "dgf",
            "patient_id": "dffgd"
        }
    ]
}


Diagnosis(
    **{
        "sick": "dfg",
        "description": "dgf",
        "patient_id": "dffgd"
    }
)


Diagnosis(sick="ddg", description="dfdf" )

