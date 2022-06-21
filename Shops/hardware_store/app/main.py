import json
from typing import List, Dict
from abc import ABC, abstractmethod
import psycopg2
from contextlib import closing
from psycopg2.extras import DictCursor


class StorageHandler(ABC):

    @abstractmethod
    def add_items(self, path, new_items):
        pass

    @abstractmethod
    def get_data(self, path) -> List:
        pass

    @abstractmethod
    def remove_all(self, path):
        pass


class Storage():

    def __init__(self, strategy: StorageHandler, path: str) -> None:
        self._strategy = strategy
        self._path = path

    @property
    def strategy(self) -> StorageHandler:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: StorageHandler) -> None:
        self._strategy = strategy

    def add_items(self, new_items) -> None:
        self._strategy.add_items(self._path, new_items)

    def get_data(self) -> List:
        return self._strategy.get_data(self._path)

    def remove_all(self) -> None:
        self._strategy.remove_all(self._path)


class DataBaseHandler(StorageHandler):

    def __init__(self, connection_config):
        self._connection_config = connection_config

    def execute(self, sql_query):
        with closing(psycopg2.connect(self._connection_config)) as conn:
            with conn.cursor(cursor_factory=DictCursor) as cursor:
                cursor.execute(sql_query)


    def write(self, path, data) -> None:
        with open(path, 'w') as file:
            json.dump(data, file)

    def read(self, path) -> List:
        with open(path, 'r', encoding='utf8') as file:
            return json.load(file)


class ShopService:
    BUY_PRODUCTS = []
    SHOP = {}

    def __init__(self, shop_invent_path: str, shopping_card_path: str):
        self._shop_invent_storage = Storage(DataBaseHandler(), shop_invent_path)
        self._shopping_card_storage = Storage(DataBaseHandler(), shopping_card_path)

    def get_all_product(self) -> Dict:
        if not self.SHOP:
            self.SHOP.update(self._shop_invent_storage.read())
        return self.SHOP

    def add_product(self, product_name: str) -> None:
        self.BUY_PRODUCTS.append(self.get_all_product().get(product_name))
        self._shopping_card_storage.write(self.BUY_PRODUCTS)

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
        self._shopping_card_storage.write(self.BUY_PRODUCTS)

    def check_product(self, product_name):
        return self.get_all_product().get(product_name)


class Shop:

    def __init__(self, shop_service) -> None:
        self._shop_service = shop_service

    def show_menu(self) -> None:
        print(
            '~' * 100 + '\n'
                        '1 - View all products and their prices\n' +
            '2 - select product\n' +
            '3 - view purchase amount\n' +
            '4 - complete your purchases.\n' +
            '5 - Close shop'
        )

    def make_choice(self, choice: int):
        result = ""
        if choice == 1:
            products = self._shop_service.get_all_product()
            message = self._shop_service.format_product(products)
            result = message
        elif choice == 2:
            products = input("select product: ")
            if self._shop_service.check_product(products) == None:
                result = 'You have entered a non-existent product, please repeat'
            else:
                self._shop_service.add_product(products)
                result = f'you have selected a {products} product'
        elif choice == 3:
            result = self._shop_service.get_buy_product()
        elif choice == 4:
            result = self._shop_service.get_buy_product()
            self._shop_service.clear_buy_products()
        elif (choice < 1) or (choice > 5):
            result = 'Enter a number from 1 to 5'
        elif choice == 5:
            result = 'Shop is closed, see you soon!'
        return result


def run() -> None:
    shop_invent_path = '../shop_invent.json'
    shopping_card_path = '../shopping_card.json'
    shop = Shop(ShopService(shop_invent_path, shopping_card_path))
    choice = None
    while choice != 5:
        shop.show_menu()
        try:
            choice = int(input('Enter menu item: '))
            message = shop.make_choice(choice)
            print(message)
        except ValueError:
            print("You have entered a string, enter a number!")


run()
