"""1. Если переменная key равна 10,
выведите "Верно", если другому значению,
выведите "Не верно"
"""

key = int(input("Введите число: "))
if key == 10:
    response = "Верно"
else:
    response = "Не верно"

print(response)

"""2. Переменная num может принимать 4
значения: 1, 2, 3 или 4. Если она
имеет значение '1', то в переменную
result запишем 'зима', если имеет
значение '2' – 'весна' и так далее.
Если значения не 1,2,3,4, то вывести
"Нет такой поры года" и завершить
программу
"""
num = int(input("Введите число: ")) # можно брать из консоли
result = ""

if num == 1:
    result = "зима"
elif num == 2:
    result = "весна"
elif num == 3:
    result = "лето"
elif num == 4:
    result = "осень"
else:
    result = "нет такой поры года"

print(result.capitalize())

# Или можно сделать так:

seasons = {
    1: "зима",
    2: "весна",
    3: "лето",
    4: "осень"
}
result = seasons.get(num, "нет такой поры года")


print(result.capitalize())

"""3. В переменной month лежит какое-то
число из интервала от 1 до 12. Определите
в какую пору года попадает этот месяц
(зима, лето, весна, осень). Если число
меньше 1, то выведите "значение слишком
маленькое", если больше 12, "значение слишком
большое"
"""

month = int(input("Введите число: "))
result = ""

if month <= 2 or month == 12:
    result = "зима"
elif 3 <= month <= 5:
    result = "весна"
elif 6 <= month <= 8:
    result = "лето"
elif 9 <= result <= 11:
    result = "осень"
elif result < 1:
    result = "значение слишком маленькое"
else:
    result = "значение слишком большое"

print(result.upper())

# или можно сделать так

seasons_months_map = {
    "зима": (1, 2, 12),
    "весна": (3, 4, 5),
    "лето": (6, 7, 8),
    "осень": (9, 10, 11),
}
max_month = 12
min_month = 1

if month > max_month:
    result = "значение слишком большое"
elif month < min_month:
    result = "значение слишком маленькое"
else:
    for season, months in seasons_months_map.items():
        if month in months:
            result = season

print(result.upper())


"""4. Дана строка из 6-ти цифр. Проверьте,
что сумма первых трех цифр равняется сумме
вторых трех цифр. Если это так - выведите
'да', в противном случае выведите 'нет'."""

numbers_string = input("Выедите число с четным количеством цифр: ") #строку можно ввести. Строка вида "123456", сумма первых трех 1+2+3=6, вторых - 4+5+6=15
result = "" # по итогу должен быть да или нет

# данная программа работает для любых чисел с четным количеством цифр:

if len(numbers_string) % 2 != 0:
    result = "в числе нечетное количество цифр"
else:
    first_sum = 0
    second_sum = 0
    string_middle = int(len(numbers_string)/2)

    for index in range(0, string_middle):
        first_sum += int(numbers_string[index])
        second_sum += int(numbers_string[string_middle + index])

    if first_sum == second_sum:
        result = "да"
    else:
        result = "нет"

print(result.capitalize())


"""5. Выведите фразы "Greeting №number",
где number - это номер выведенного сообщения,
ровно столько раз, сколько скажет пользователь.
Желательно решить задачу через интерполяцию строк.
"""

greeting_max_number = int(input("Введите число: ")) # пользователь вводит, сколько раз вывести сообщения
greeting_template = "Greeting №{}"
result = []

for greeting_number in range(1, greeting_max_number + 1):
    result.append(greeting_template.format(greeting_number))

message = "\n".join(result)
print(message)

"""6. Необходимо вывести на экран таблицу умножения на 3:

3*1=3
3*2=6
3*3=9
3*4=12
3*5=15
3*6=18
3*7=21
3*8=24
3*9=27
3*10=30

Задачу так же желательно решить, используя интерполяцию строк.
"""

template = "{}*{}={}"
result_list = []
main_number = 3
max_number = 10
min_number = 1

for number in range(min_number, max_number + 1):
    result_list.append(
        template.format(main_number, number, main_number * number)
    )

message = "\n".join(result_list)

print(message)

"""7. (extra) Даны два числа.
Определить цифры, входящие в запись
как первого так и второго числа.
Для 125 и 5627 - это 2 и 5,
Для 99999 и 999 - это только 9"""

first = "89795"
second = "29745"

result_set = set(first) & set(second)

message = ", ".join(result_set)

print(message)

"""8. Отгадать целое число,
которое "загадал" компьютер в определенном диапазоне.
Пользователь вводит число, если число больше, чем загаданное,
то компьютер пишет "меньше", если меньше загаданного, то "больше".
И так до тех пор, пока пользователь не угадает число."""
import random

secret_number = random.randint(0, 100)

users_number = None

while users_number != secret_number:
    users_number = int(input("Введите число: "))
    if users_number < secret_number:
        print("больше")
    elif users_number > secret_number:
        print("меньше")

print("Вы угадали")

"""9. Найдите сумму чисел в структуре.
"""
numbers_list = [1, 2, 3,"4",
                5, 6, 7, 43,
                "5788", 432,
                "56654", 45,
                111, 223, 12]

result = 0
for number in numbers_list:
    result += int(number)

print(result)


"""10. Выведите сумму всех значений словаря."""
name_age_map = {"Bob": 3, "Alice": 2}

result = 0

for value in name_age_map.values():
    result += int(value)

print(result)


"""11. Сделайте операции с уже полюбившимся словарем =)."""
team_info = team_info = {
    "squadName": "Super hero squad",
    "homeTown": "Metro City",
    "formed": 2022,
    "secretBase": "Super tower",
    "active": True,
    "members": [
        {
            "name": "Molecule Man",
            "age": 29,
            "secretIdentity": "Dan Jukes",
            "powers": [
                "Radiation resistance",
                "Turning tiny",
                "Radiation blast"
            ]
        },
        {
            "name": "Madame Uppercut",
            "age": 39,
            "secretIdentity": "Jane Wilson",
            "powers": [
                "Million tonne punch",
                "Damage resistance",
                "Superhuman reflexes"
            ]
        },
        {
            "name": "Eternal Flame",
            "age": 1000000,
            "secretIdentity": "Unknown",
            "powers": [
                "Immortality",
                "Heat Immunity",
                "Inferno",
                "Teleportation",
                "Interdimensional travel"
            ]
        }
    ]
}

# 11.1 посчитайте средний возраст всех участников,
# не используя конкретные индексы
age_sum = 0

for member in team_info.get("members", []):
    age_sum += member.get("age")

average_age = age_sum / len(team_info.get("members", 1))
message = "Average age is {:.2f}".format(average_age)

print(message) 



# 11.2 Посчитайте среднее количество
# количество суперсил у героев.

powers_sum = 0

for member in team_info.get("members", []):
    powers_sum += len(member.get("powers"))

average_powers_count = powers_sum / len(team_info.get("members", 1))
message = "Average power count is {:.2f}".format(average_powers_count)

print(message) 


# 11.2 Выведите собщение "hero_name is hero_age",
# где hero_name - имя героя, hero_age - его возраст.
# Если возраст больше среднего, то вывести на
# отдельной строке сообщение: "He is very old",
# если возраст меньше среднего, то вывести "He is young"

age_info = []
message_template = "{} is {}.\n{}"

for member in team_info.get("members"):
    if member.get("age") > average_age: # взял из 11.1
        age_message = "He is very old"
    else:
        age_message = "He is young"

    age_info.append(message_template.format(
        member.get("name"),
        member.get("age"),
        age_message
    ))

final_message = "\n".join(age_info)
print(final_message)

"""12. Перепишите программу, которую мы писали
раньше так, чтобы остался только один print.
"""

username: str = input("Введи свое имя: ")
country: str = input("Введи свою страну: ")
town: str = input("Введи свой город: ")
street: str = input("Введи свою улицу: ")
home: str = input("Введи свой дом: ")

message_template = "{} живет по следующему адресу {}, {}, {}, {}. Спасибо за доверие, {}!"

message = message_template.format(username, country, town, street, home, username)