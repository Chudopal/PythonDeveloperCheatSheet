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

import json
from typing import Dict, List


# PRODUCTS = [
#         ["Мяч", 100],
#         ["Бутсы", 200],
#         ["Гетры", 15],
#         ["Шорты", 60],
#         ["Майка", 70], 
#         ["Щетки", 25]
# ]
BASKET = []

def format_product(product_list: any) -> List:
    return "\n".join([f"{product[0]}.Товар {product[1][0]} стоит {product[1][-1]} рублей." for product in enumerate(product_list, 1)])

def menu() -> str:
    return ("0. Выход\n" + 
    "1. Посмотреть все товары и цены на них\n" +
    "2. Выбрать товар\n" + 
    "3. Посмотреть сумму покупки.")

def get_products() -> str:
    with open("app\storage.json") as json_file:
        data = json.load(json_file)
        return data.get("products")

def adaptor(data: Dict) -> List:
    result = []
    for product in data:
        result = list(product.items())
    return result

print(adaptor(get_products()))

def make_choice(product_list) -> List:
    input_massage = input("Выберите товар: ")
    for product in product_list:
        if product[0] == input_massage:
            BASKET.append(product)
    

def perchoice():
    total = 0
    result = ""
    for i in BASKET:
        result += i[0] + '\n'
        total += i[1]
    result = result + f'{total} рублей - Общая сумма покупок' + "\n"
    print(result)

def run() -> None:    
    choice = None
    while choice != 0:
        print(menu())
        choice = int(input("Выберите пункт меню: "))
        if choice == 1:
            product = get_products()
            massage = format_product(product)
            print(massage)
        elif choice == 2:
            make_choice(PRODUCTS)
            print("Товар добавлен в корзину")
            
        elif choice == 3:
            perchoice()
        elif choice == 0:
            print("Спасибо за покупку")
            break
        else:
            print("Не корректный ввод. Попробуйте снова")

run()
