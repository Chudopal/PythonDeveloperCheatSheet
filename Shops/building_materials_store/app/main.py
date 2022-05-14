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
from typing import List, Dict


def read_file(path, name) -> List:    #чтение json файла
    with open(path) as file:
        data = json.load(file)
    return data.get(name)


def read_buy_file(path) -> List:    #чтение json файла
    with open(path) as file:
        data = json.load(file)
    return data


def write_file(path, data) -> None:  #запись json файла
    with open(path, 'w') as file:
        json.dump(data, file)


def adaptor(data: List) -> Dict:  #конвертация листа в словарь
    result = {}
    for materials in data:
        result[materials.get('material_name')] = materials.get('cost')
    return result


def get_all_product() -> List:    #показывает все материалы магазина
    data = read_file('storage_building.json', 'materials')
    return data


def get_buy_materials() -> List:    #показывает выбранные в корзину материалы
    data = read_buy_file('buy_materials.json')
    return data
print(get_buy_materials())


buy_product = []
def save_buy_product(buy_product):
    data = write_file('buy_materials.json', buy_product)


def add_product(product_name: str) -> None:    #добавляет товар в корзину
    catalog = get_all_product()
    for i in catalog:
        item_cost = i['cost']
        item_material = i['material_name']
        if product_name == item_material:
            result = dict.fromkeys([item_material], item_cost)
            buy_product.append(result)


def get_buy_product() -> List:        #показывает сумму покупки
    result_list = []
    for i in buy_product:
        result = list(i.values())
        for i in result:
            result_list.append(i)
    total_price = sum(result_list)
    result = (f'Ваша сумма покупки составляет {total_price} руб')
    return result


def format_product(product_list: Dict) -> str:
    return '\n'.join([
        f'{product_name} - {cost} руб'
        for product_name, cost in product_list.items()
    ])


def menu() -> str:
    return (
    '<>'*80 + '\n'
    '1 - посмотреть все товары и цены на них\n' +
    '2 - выбрать товар\n' +
    '3 - сохранить выбранные товары в корзине\n' +
    '4 - посмотреть сумму покупки(сумма цен выбранных товаров)\n' +
    '5 - завершить покупку.'
    )


def make_choice(choice: int):
    if choice == 1:
        product = adaptor(get_all_product())
        message = format_product(product)
        result = message
    elif choice == 2:
        product_name = input('Введите желаемый товар: ')
        result = add_product(product_name)
    elif choice ==3:
        result = save_buy_product(buy_product)
    elif choice == 4:
        result = get_buy_product()
    return result


def run() -> None:
    choice = None
    while choice != 5:
        print(menu())
        choice = int(input('Введите пункт меню: '))
        message = make_choice(choice)
        print(message)

run()




