import json

path_json = '../shop_invent.json'

buy_products = []

from typing import List, Dict

SHOP = []

def get_all_product() -> List:
    return SHOP

def read_file() -> List:
    with open(path_json, 'r', encoding='utf8') as file:
        return  json.load(file)

def add_product(product_name: str) -> None:
    buy_products.append(SHOP.get(product_name))

def get_buy_product() -> List:
    total_price = sum(buy_products)
    result = (f'Your purchase amount is {total_price} dollars')
    return result

def format_product(product_list: Dict) -> str:
    return '\n'.join([
        f'{product_name} - {cost} dollars'
        for product_name, cost in product_list.items()
    ])

def menu() -> str:
    return (
    '~'*100 + '\n'
    '1 - View all products and their prices\n' +
    '2 - select product\n' +
    '3 - view purchase amount\n' +
    '4 - complete your purchases.'
    )

def make_choice(choice: int):
    result = ""
    if choice == 1:
        products = get_all_product()
        message = format_product(products)
        result = message
    elif choice == 2:
        products = input("select product: ")
        add_product(products)
        result = 'you have selected a product'
    elif choice == 3:
        result = get_buy_product()
    elif choice == 4:
        result = get_buy_product()
        buy_products.clear()
    return result

SHOP = read_file()

def run() -> None:
    choice = None
    while choice != 5:
        print(menu())
        choice = int(input('Enter menu item: '))
        message = make_choice(choice)
        print(message)

run()