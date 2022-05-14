import json
from typing import List, Dict

PATH_JSON = '../shop_invent.json'
WRITE_JSON = '../shopping_card.json'

BUY_PRODUCTS = []

SHOP = {}


def get_all_product() -> Dict:
    if not SHOP:
        SHOP.update(read_file())
    return SHOP


def read_file() -> List:
    with open(PATH_JSON, 'r', encoding='utf8') as file:
        return json.load(file)


def write_file(path, data) -> None:
    with open(path, 'w') as file:
        json.dump(data, file)


def add_product(product_name: str) -> None:
    BUY_PRODUCTS.append(get_all_product().get(product_name))
    write_file(WRITE_JSON, BUY_PRODUCTS)


def get_buy_product() -> List:
    total_price = sum(BUY_PRODUCTS)
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
        BUY_PRODUCTS.clear()
    return result


def run() -> None:
    choice = None
    while choice != 5:
        print(menu())
        choice = int(input('Enter menu item: '))
        message = make_choice(choice)
        print(message)

run()