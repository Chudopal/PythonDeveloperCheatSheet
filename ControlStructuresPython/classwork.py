# -*- coding: utf-8 -*-
"""Операции над множествами"""
from unicodedata import name


a = {1,2,3}
b = {2,3,4}

"""Разность"""
c = a - b
#print(c)

"""Пересечение"""
c = a & b
#print(c)

"""Объединение"""
c = a | b
#print(c)

"""Симметрическая разность"""
c = a ^ b

"""Словари"""
name_age_map = {
    "Alice": 10
}

"""Данные в словарях: чтение, добавление, изменение, удаление"""
# print(name_age_map["Alice"])

name_age_map["Alice"] = 11
# print(name_age_map["Alice"])

name_age_map["Bob"] = 0
# print(name_age_map)

name_age_map.pop("Bob")
#print(name_age_map)

cargos = {
    10: "Samsung",
    10: "Apple"
}

#print(cargos)


# print(hash(5))
# print(hash("str"))

# print(hash((1, 2, 3)))

#print(hash([1, 2, 3]))

a_dict = {
    (1,2,3): "one two ..."
}

#print(a_dict)

# a_dict = {
#     list((1, 2, 3)): "one two ..."
# }

#print(hash("str"))

last_digit = {'samsung': 1, 'apple': 5}
last_digit['samsung'] = 10
# print(last_digit['apple'])
last_digit.pop('samsung')

container = {'phones': ['samsung', 'LG']}
container['phones'][1]

"""Получение ключей"""
name_age_map = {
    "Alice": 10,
    "Bob": 12,
}
#print(list(name_age_map.keys()))  # ["Alice", "Bob"]
#print(list(name_age_map.values())) # [10, 12]
#
#print(dict(zip(["Alice", "Bob"], [10, 12])))


name_age_map = {
    "Alice": 10,
    "Bob": 12,
}



age = name_age_map.get("Mike", 10)
#print(age)


user_info = {
    "is_active": True,
    "id": 1,
    "name": "Alex",
    "permissions": [
            "read", "write", "execute"
    ],
    "job_info": {
        "position": "developer",
        "experience": 3,
        "stuff_and_number": {
            "monitors": 2,
            "mouse": 1,
            "laptops": 2
        }
    }
}

#print(user_info.get("permissions")[2])


{
    "position": "developer",
    "experience": 3,
    "stuff_and_number": {
        "monitors": 2,
        "mouse": 1,
        "laptops": 2
    }
}

{
    "monitors": 2,
    "mouse": 1,
    "laptops": 2
}

job_info = user_info["job_info"]
stuff_and_number = job_info["stuff_and_number"]
monitors = stuff_and_number["monitors"]
#print(monitors)

"""Вложенные словари"""


"""Операторы сравнения"""




"""Операторы ветвления"""



a = 5
b = 5

# if a < b:
#     print("In condition")
# print("Without condition")

age = int(input("Enter ur age: "))

# if age > 18:
#     print("Allow")
#     if age > 65:
#         print("You're too old")

# if age >= 18:
#     print("Allow")
# else:
#     print("Access denied")

# if age < 18 or age > 60:
#     print("denied")
# else:
#     ...

if age <= 10:
    print("Тебе 1-й десяток")
elif (10 < age <= 20):
    print("Тебе 2-й десяток")
else:
    print("Тебе больше 2-х десятков")



"""Цикл while"""


"""Цикл for"""
