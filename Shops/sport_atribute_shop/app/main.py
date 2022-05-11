"""5. Напишите программу магазина.
Покупатели могут покупать какие-то продукты в магазине.
Возможности покупателя:
- посмотреть все товары и цены на них
- выбрать товар
- посмотреть сумму покупки(сумма цен выбранных товаров)
Взаимодействие происходит через консоль.
Товары храните просто в какой-нибудь из коллекций.
Выбор товара - это ввод пользователем строки названия товара
"""

from typing import List


PRODUCT = [
        ("Мяч", 100),
        ("Бутсы", 200),
        ("Гетры", 15),
        ("Шорты", 60),
        ("Майка", 70), 
        ("Щетки", 25)
]


def format_product(product_list: any) -> str:
    return ([f"Товар {product[0]} стоит {product[1]}" for product in product_list])

def menu() -> str:
    return ("1. Посмотреть все товары и цены на них\n" +
    "2. Выбрать товар\n" + 
    "3. Посмотреть сумму покупки.")

def look() -> List:
    return PRODUCT
    

def choices():
    ...

def perchoice():
    ...

def run() -> None:
    print(menu())
    choice = None
    while True:
        choice = int(input("Выберите пункт меню: "))
        if choice == 1:
            product = look()
            massage = format_product(product)
            print(massage)
        elif choice == 2:
            product = int(input("Выберите товар: "))
            choices(product)
        elif choice == 3:
            perchoice()
        else:
            print("Не корректный ввод. Попробуйте снова")

run()
