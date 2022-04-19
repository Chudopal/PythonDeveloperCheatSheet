# 1. Напишите программу, которая получает от пользователя имя, его вес и рост.
# И выводит следующее сообщение: "Привет username! Твой имт - bmi!"
# ИМТ = m/(h**2), где: m — масса тела в киллограммах, h — рост в метрах.
from tkinter import W


username = input("Введи свое имя: ")
weight = float(input("Введи свой вес в кг: "))
height = float(input("Введи свой рост в метрах: "))
bmi = weight/(height**2)
print("Привет, ", username, "!" " Твой имт - ", bmi, "!", sep='')

# 2. Сделайте программу, которая будет запрашивать имя, страну, город, улицу и дом пользователя. 
# А потом выводить сообщение
# "username живет по слудующему адресу: country, town, street, home. Спасибо за доверие, username!"
# Решите задачу, не используя конкатенацию строк!

username: str = input("Введи свое имя: ")
country: str = input("Введи свою страну: ")
town: str = input("Введи свой город: ")
street: str = input("Введи свою улицу: ")
home: str = input("Введи свой дом: ")

print(username, "живет по следующему адресу", end=" ", sep=" ")
print(country, town, home, sep=', ', end=".")
print("Спасибо за доверие", username, sep=", ", end="!")


# 3. Выберите структуру данных для задач разработчиков,
# с условием того, что должна быть возможность легко
# добавлять задачи и удалять их (примеры задач:
# "поменять цвет кнопки ввод", "поменять цвет кнопки отправить"),
# после добавьте еще 2 задачи, удалите самую первую и 
# выведите последнюю добавленную задачу.

tasks = [
    "поменять цвет кнопки ввод",
    "поменять цвет кнопки отправить",
]
tasks.append("поменять шрифт")
tasks.append("отцентрировать содержимое")
tasks.pop(0)
print(tasks[-1])


# 4. Упакуйте следующие элементы в коллекцию,
# с условием того что email должен быть уникальным.
# После, добавьте еще 2 email-a и удалите email "test@test.com"
user_email1 = "test@test.com"
user_email2 = "qwerty@qwerty.com"

emails = {user_email1, user_email2}
emails.add("test1@vvv")
emails.add("test1@vv1")
emails.remove(user_email1)



# 5. Вы пишите программу, для слияния 2-х IT-компаний.
# Слияние компаний подразумевает и слияние отдетлов.
# Однако в итоговой компании должны отсуствовать
# повторяющиеся отделы, а также должна отсуствовать
# возможность как-либо изменять финальные отделы.
companies_departments = [
    ["development", "QA", "sales", "marketing"], # департаменты первой компании
    ["devops", "QA", "management", "development"] # департаменты второй компании
]

merged_departments = tuple(
    set(
        companies_departments[0] +
        companies_departments[1]
        )
    ) # подберите подходящую структуру данных


# 6. Сделайте следующее сообщение в одну строку:
# "У пользователя Kolia имеются следующие права: read, write, execute!"
username = "Kolia"
permissions = ["read", "write", "execute"]

read, write, execute = permissions

print("У пользователя", username, "имеются следующие права:", end=" ")
print(read, write, execute, sep=", ", end="!\n")


# 7. Вычислите сколько в среднем сотрудников в каждом отдетеле
employees = ["Alex", "Tania", "Andry", "Vlad", "Alina", "Vika"]
departments_number = "3"

avg_employees_per_dep = len(employees) / int(departments_number)


# 8. (extra) 
# Найдите ошибки в следующей программе и исправьте их
users = {1,2,3,4,5,6,7}
# Всем пользователям выдали разрешение на запись
users_with_write_perm = set(users)
# Появились новые пользователи:
users.add(8)
users.add(9)
# Им так же выдали разрешение на запись
users_with_write_perm.add(8)
users_with_write_perm.add(9)
# Потом прошло какое-то время и решили
# забрать у нескольких пользователей разрешение на запись
users_with_write_perm.remove(1)
users_with_write_perm.remove(2)
users_with_write_perm.remove(3)
users_with_write_perm.remove(4)

# а потом решили посчитать, сколько процентов пользователей имеют разрешение на запись:
percentage_with_perm = len(users_with_write_perm)/len(users) * 100 #подставьте корректную формулу
print(percentage_with_perm)
# сделайте так, чтобы программа работала
# и верно считала процент людей с разрешением на запись


