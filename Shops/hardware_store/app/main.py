import json
from typing import List, Dict


PATH_JSON = '../shop_invent.json'
WRITE_JSON = '../shopping_card.json'


class JsonFileHandler:

    def __init__(self, path: str):
        self.path = path

    def write_file(self, data) -> None:
        with open(self.path, 'w') as file:
            json.dump(data, file)

    def read_file(self) -> List:
        with open(self.path, 'r', encoding='utf8') as file:
            return json.load(file)


class ActionStore:

    BUY_PRODUCTS = []
    SHOP = {}

    shop_invent = JsonFileHandler(PATH_JSON)
    shopping_card = JsonFileHandler(WRITE_JSON)

    def get_all_product(self) -> Dict:
        if not self.SHOP:
            self.SHOP.update(self.shop_invent.read_file())
        return self.SHOP

    def add_product(self, product_name: str) -> None:
        self.BUY_PRODUCTS.append(self.get_all_product().get(product_name))
        self.shopping_card.write_file(self.BUY_PRODUCTS)

    def get_buy_product(self) -> List:
        total_price = sum(self.BUY_PRODUCTS)
        result = (f'Your purchase amount is {total_price} dollars')
        return result

    def format_product(self, product_list: Dict) -> str:
        return '\n'.join([
            f'{product_name} - {cost} dollars'
            for product_name, cost in product_list.items()
        ])

    def clear_buy_products(self):
        self.BUY_PRODUCTS.clear()
        self.shopping_card.write_file(self.BUY_PRODUCTS)

    def check_product(self, product_name):
        return self.get_all_product().get(product_name)

shop = ActionStore()


def menu() -> str:
    return (
    '~'*100 + '\n'
    '1 - View all products and their prices\n' +
    '2 - select product\n' +
    '3 - view purchase amount\n' +
    '4 - complete your purchases.\n' +
    '5 - Close shop'
    )


def make_choice(choice: int):
    result = ""
    if choice == 1:
        products = shop.get_all_product()
        message = shop.format_product(products)
        result = message
    elif choice == 2:
        products = input("select product: ")
        if shop.check_product(products) == None:
            result = 'You have entered a non-existent product, please repeat'
        else:
            shop.add_product(products)
            result = f'you have selected a {products} product'
    elif choice == 3:
        result = shop.get_buy_product()
    elif choice == 4:
        result = shop.get_buy_product()
        shop.clear_buy_products()
    elif (choice < 1) or (choice > 5):
        result = 'Enter a number from 1 to 5'
    elif choice == 5:
        result = 'Shop is closed, see you soon!'

    return result


def run() -> None:
    choice = None
    while choice != 5:
        print(menu())
        try:
            choice = int(input('Enter menu item: '))
            message = make_choice(choice)
            print(message)
        except ValueError:
            print("You have entered a string, enter a number!")


run()