# id
stuff_number = 5
dep_number = 5
print("stuff number addr", id(stuff_number))
print("dep number addr", id(dep_number))
dep_number += 1
print("dep number addr second", id(dep_number))

# функции ввода вывода
name = input("Enter your name: ")
age = input("Enter your age: ")

print("Hello", name, end="! ", sep=',...')
print("Your age is", age)

# программа спрашивает три раза
# цену продуктов, после суммирует это
# и выводит сообщение (сумма трех твоих покупок: 
# перечисляет цены этих покупок
# равна )
price1 = input("Введите стоимость первого товара ")
price2 = input("Введите стоимость второго товара ")
price3 = input("Введите стоимость третьего товара ")
product_sum = int(price1)+int(price2)+int(price3)
print("Сумма трех твоих покупок", end=" ")
print(price1, price2, price3,  sep="! ", end=" ")
print("равна", product_sum)


#коллекции

phone_price = 13.4
headphones_price = 2.1
tv_price = 15.2
microwave_price = 3.5

price_list = [phone_price, headphones_price, tv_price, microwave_price]




price_list = [13.4, 2.1, 15.2, 3.5]

phone_price, headphones_price, tv_price, microwave_price = price_list

print(phone_price)
print(headphones_price)



print(price_list)

price_list[0] = 10

print(price_list)

price_list[0] = price_list[0] + 10


print(price_list)
names = ["Oleg", "Andrey", "Vlad"]
print(names[1])
names[2] = "Sasha"
print(names)



names.append("Sergei")

print(names)

names.pop()

print(names)

names_z70 = ["Ilya", "Egor", "Vlad"]
names_z71 = ["Olia", "Misha", "Vlad"]

names = names_z70 + names_z71

person_number = len(names)

print(person_number)


box_one = ["phone", 'tv','pc','note']

print(box_one[-2])


# Множества

card_numbers = {1,2,3}

card_numbers.add(4)
card_numbers.add(4)
card_numbers.add(3)
card_numbers.add(3)

print(card_numbers)


card_numbers = [1, 2, 3, 4,4,4,4,5,5,5,5,5]

unique_card_numbers = set(card_numbers)

print(unique_card_numbers)

unique_card_numbers.remove(1)

print(unique_card_numbers)

len(unique_card_numbers)



departments = ("developers", "sales", "QA")

students = ["Petr", "Masha"]

people = list(students)

students.pop()

print(students)
print(people)
"""Программа магазин
Имееться 2 массива, массиы с наименованиями
и массами. Сущ общий массив магазина и сущ масси
прилавка"""

shop_catalog = ["meat", "tamatos"]
shop_weights = [15,20]

shop_face = [list(shop_catalog), list(shop_weights)]

shop_face[0].pop()
shop_face[1].pop()
print(shop_face)
print(shop_catalog, shop_weights)
