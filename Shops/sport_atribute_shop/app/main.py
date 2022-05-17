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



def read_file(path, name):
    with open(path, encoding='utf-8') as json_file:
        data = json.load(json_file)
        return data.get(name)



def write_file(path, data) -> None:
    with open(path, "w", encoding='utf-8') as json_file:
        json.dump(data, json_file)
        


def adaptor(data: Dict) -> List:
    result = []
    for product in data:
        product = list(product.values())
        result.append(product)
    return result
        

def file_adaptor(data: List) -> Dict:
    result = {
        "products": get_products(),
        "basket" : buy_goods()
    }
    for product, cost in data.items():
        result.append({
            "product" : product,
            "cost" : cost
        })
    return result



def get_products() -> List:
    data = read_file("app\storage.json", "products")
    return adaptor(data)
    


def buy_goods() -> List:
    data = read_file("app\storage.json", "basket")
    return data



def format_product(product_list: any) -> str:
    return "\n".join([f"{product[0]}.Товар {product[1][0]} стоит {product[1][-1]} рублей." for product in enumerate(product_list, 1)])



def menu() -> str:
    return ("0. Выход\n" + 
    "1. Посмотреть все товары и цены на них\n" +
    "2. Выбрать товар\n" + 
    "3. Посмотреть сумму покупки.")



def make_choice(product_list) -> List:
    result = []
    input_massage = input("Выберите товар: ")
    for product in product_list:
        if product[0] == input_massage:
            result.append(product)
    print(result)
    return result        


def perchoice(product_list: List) -> List:
    total = 0
    result = ""
    for i in product_list:
        result += i[0] + '\n'
        total += i[1]
    result = result + f'{total} рублей - Общая сумма покупок' + "\n"
    return result
    



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
            make_choice(get_products())
            print("Товар добавлен в корзину")
        elif choice == 3:
            perchoice(make_choice(get_products()))
        elif choice == 0:
            print("Спасибо за покупку")
            break
        else:
            print("Не корректный ввод. Попробуйте снова")

run()
