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


def read_file(path):
    with open(path, encoding='utf-8') as json_file:
        data = json.load(json_file)
        return data


def write_file(path, data) -> None:
    with open(path, "w", encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4)


def adaptor(data: List[Dict]) -> List:
    result = []
    for product in data:
        product = list(product.values())
        result.append(product)
    return result


def file_adaptor(data):
    return [
        {
            "product": product,
            "cost": cost
        } for product, cost in data
    ]


def get_whole_data() -> Dict[str, List]:
    return read_file("app\storage.json")


def get_products() -> List:
    data = get_whole_data()
    return adaptor(data.get("products"))


def buy_goods() -> List:
    data = get_whole_data()
    return data.get("basket")


def format_product(product_list: any) -> str:
    return "\n".join([
        f"{index}.Товар {product} стоит {cost} рублей."
        for index, (product, cost)
        in enumerate(product_list)
    ])


def menu() -> str:
    return ("0. Выход\n" + 
    "1. Посмотреть все товары и цены на них\n" +
    "2. Выбрать товар\n" + 
    "3. Посмотреть сумму покупки." )


def add_purchase(product_list) -> List:
    result = None
    input_massage = input("Выберите товар: ")
    for product in product_list:
        if product[0] == input_massage:
            result = product
            break
    return result


def perchoice(product_list: List) -> List:
    total = 0
    result = ""
    for i in product_list:
        result += i[0] + '\n'
        total += i[1]
    result += f'{total} рублей - Общая сумма покупок' + "\n"
    return result


def show_products():
    product = get_products()
    message = format_product(product)
    return message


def choose_product():
    purchase = add_purchase(get_products())
    data = get_whole_data()
    data["basket"] = adaptor(data["basket"])
    data["basket"].append(purchase)
    data["basket"] = file_adaptor(data["basket"])
    write_file("app\storage.json", data)
    return "Товар добавлен в корзину"


def get_bill():
    return perchoice(
        adaptor(
            buy_goods()
        )
    )

def make_choice(choice) -> str:
    result = ""
    if choice == 1:        
        result = show_products()
    elif choice == 2:
        result = choose_product()
    elif choice == 3:
        result = get_bill()
    elif choice != 0:
        result = "Не корректный ввод. Попробуйте снова"
    else:
        return menu()
    return result


def safe_make_choice(choice):
    result = ""

    try:
        result = make_choice(choice=int(choice))
    except ValueError:
        result = "Вводите только цифры!"
    except FileNotFoundError:
        result = "В магазине нет товаров"

    return result


def run() -> None:    
    choice = None
    while choice != "0":
        print(menu())
        choice = input("Выберите пункт меню: ")
        print(safe_make_choice(choice=choice))


run() 