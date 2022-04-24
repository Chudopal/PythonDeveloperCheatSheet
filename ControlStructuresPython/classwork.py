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

if a < b:
    print("In condition")
print("Without condition")

age = int(input("Enter ur age: "))

if age > 18:
    print("Allow")
    if age > 65:
        print("You're too old")

if age >= 18:
    print("Allow")
else:
    print("Access denied")

if age < 18 or age > 60:
    print("denied")
else:
    ...

if age <= 10:
    print("Тебе 1-й десяток")
elif (10 < age <= 20):
    print("Тебе 2-й десяток")
else:
    print("Тебе больше 2-х десятков")


"""Цикл while"""
max_count = int(input("Enter value: ")) # 5
counter = 0


while (counter < max_count):
    print("Hello")
    counter += 1
    if counter >= 5:
        break

print("bye")

names = ["Bob", "Alice", "Nika"]
i = 0

while i < len(names):
    print(names[i])
    i += 1

"""Цикл for"""

names_ages = {"Bob": 10, "Alice": 12, "Nika": 3}

for name, age in names_ages.items():
    print(name, "is", age)

names = ["Bob", "Alice", "Nika", "Dora"]

for _ in range(10):
   print("Hello")

print('Entry name')
print('Do you want to entry name?')
answer = input()

if answer =='Yes':
    name = input('entry name')
    print('hello',name)
elif answer == 'No':
    print('Ok!')
else:
    while answer !='Yes' and answer !='No':
        answer=input('Do you want entry name')
        if answer == 'Yes':
            name = input('entry name')
            print('hello', name)
        elif answer == 'No':
            print('Ok!')


answer = None
positive_answers = ("yes", "Yes", "y", "Y", "yep")
negative_answers = ("No", "no", "N", "n", "nope")
correct_answers = negative_answers + positive_answers

while not answer in correct_answers:
    answer = input("Do you want to entry name?: ")

    if answer in positive_answers:
        name = input("Entry name: ")
        print("Hello", name, sep=", ", end="!\n")
    elif answer in negative_answers:
        print("Ok.")
    else:
        print("I don't understand you")


"""Строки"""
answer = input("Enter answer: ")

modify_answer = answer.lower()
modify_answer = answer.upper()
modify_answer = answer.capitalize()
modify_answer = answer.replace("a", "IIIIII")

print(modify_answer, answer)

name = "Bob"
age = 125678654.45456754


tamplate = "%s is %s, and he is awesome!"
result = tamplate % (name, age)

print(result)


name = "Bob"
age = 10

template = "{} is {}"
result = template.format(name, age)

result = f"{name} is {age}"

print(result)


name_age_map = {"Alex": 10, "Bob": 2}
result = ''
template = "{} is {}\n"


def print_format_str(name: str, age: int):
    result = f"{name} is {age}\n"
    print(result)


for name, age in name_age_map.items():
    print_format_str(name, age)

print("Bye")

# print(result)
