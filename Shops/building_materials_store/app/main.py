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

# SHOP = {
#     'apple': 5,
#     'orange' : 7,
#     'tomato' : 4,
#     'potato' : 2,
# }
# buy_product = []

import json
from typing import List, Dict


def read_file(path, name) -> List:    #чтение json файла
    with open(path) as file:
        data = json.load(file)
    return data.get(name)

def write_file(path, data) -> None:  #запись json файла
    with open(path, 'w') as file:
        json.dump(data, file)


def adaptor(data: List) -> Dict:  #конвертация листа в словарь
    result = {}
    for materials in data:
        result[materials.get('material_name')] = materials.get('cost')
    return result


def save_adaptor(data: Dict) -> List: # конвертация словаря в лист
    result = []
    for material_name, material_cost in data.items():
        result.append(
            {"material_name": material_name,
             "cost": material_cost}
        )
    return result



def get_all_product() -> List:    #показывает все материалы магазина
    data = read_file('storage_building.json', 'materials')
    return adaptor(data)


def get_buy_materials() -> List:    #показывает выбранные в корзину материалы
    data = read_file('buy_materials.json', 'materials')
    return adaptor(data)


def add_product(product_name: str) -> None:    #добавляет товар в корзину!!! NO WORK
    # buy_product.append(SHOP.get(product_name))
    save_adaptor()
    write_file('buy_materials.json', save_adaptor(get_all_product()))

def get_buy_product() -> List:        #показывает сумму покупки!!! NO WORK сделается после add_product
    total_price = sum(buy_product)
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
    '3 - посмотреть сумму покупки(сумма цен выбранных товаров)\n' +
    '4 - завершить покупку.'
    )


def make_choice(choice: int):                #пока вообще не трогал
    if choice == 1:
        product = get_all_product()
        message = format_product(product)
        result = message
    elif choice == 2:
        product_name = input('Введите желаемый товар: ')
        result = add_product(product_name)
    elif choice == 3:
        result = get_buy_product()

    return result


def run() -> None:
    choice = None
    while choice != 4:
        print(menu())
        choice = int(input('Введите пункт меню: '))
        message = make_choice(choice)
        print(message)

run()




