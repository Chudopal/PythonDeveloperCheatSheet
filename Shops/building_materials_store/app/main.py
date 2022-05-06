"""
Кашевский Никита
5. Напишите программу магазина.
Покупатели могут покупать какие-то продукты в магазине.
Возможности покупателя:
- посмотреть все товары и цены на них
- выбрать товар
- посмотреть сумму покупки(сумма цен выбранных товаров)
Взаимодействие происходит через консоль.
Товары храните просто в какой-нибудь из коллекций.
Выбор товара - это ввод пользователем строки названия товара
"""
print('Hello World')
SHOP = {
    'apple': 5,
    'orange' : 7,
    'tomato' : 4,
    'potato' : 2,
}
buy_product = []
from typing import List, Dict

def get_all_product() -> List:
    return SHOP

def add_product(product_name: str) -> None:
    buy_product.append(SHOP.get(product_name))

def get_buy_product() -> List:
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

def make_choice(choice: int):
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




