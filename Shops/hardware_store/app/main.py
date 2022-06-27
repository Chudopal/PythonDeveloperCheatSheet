from typing import List, Dict
from abc import ABC, abstractmethod
from psycopg2 import sql
import psycopg2


class StorageHandler(ABC):

    @abstractmethod
    def add_item(self, new_item):
        pass

    @abstractmethod
    def get_data(self) -> List:
        pass

    @abstractmethod
    def remove_all(self):
        pass


class Storage():

    def __init__(self, strategy: StorageHandler) -> None:
        self._strategy = strategy

    @property
    def strategy(self) -> StorageHandler:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: StorageHandler) -> None:
        self._strategy = strategy

    def add_item(self, new_item) -> None:
        self._strategy.add_item(new_item)

    def get_data(self) -> List:
        return self._strategy.get_data()

    def remove_all(self) -> None:
        self._strategy.remove_all()


class DataBaseHandler(StorageHandler):

    def __init__(self, dbname: str, user: str,
                 password: str, host: str, table_name: str) -> None:
        self._dbname = dbname
        self._user = user
        self._password = password
        self._host = host
        self._table_name = table_name

    def get_data(self) -> Dict:
        sql_query = self._select_query()
        db_response = self.execute(sql_query)
        return db_response.fetchall()

    def add_item(self, item: dict):
        sql_query = self._insert_query(item)
        self.execute(sql_query)

    def remove_all(self):
        sql_query = self._delete_query()
        self.execute(sql_query)

    def execute(self, sql_query):
        connector = psycopg2.connect(host=self._host, user=self._user, password=self._password, dbname=self._dbname)
        cursor = connector.cursor()
        cursor.execute(sql_query)
        connector.commit()
        return cursor

    def _select_query(self) -> psycopg2.sql:
        query = sql.SQL("SELECT * FROM {table}").format(
            table=sql.SQL(self._table_name))
        query += sql.SQL(";")
        return query

    def _insert_query(self, variables: dict) -> psycopg2.sql:
        query = sql.SQL("INSERT INTO {table} ({columns}) VALUES ({values})").format(
            table=sql.SQL(self._table_name),
            columns=sql.SQL(", ").join([sql.Identifier(col) for col in variables.keys()]),
            values=sql.SQL(", ").join([sql.Literal(val) for val in variables.values()])
        )
        query += sql.SQL(";")
        return query

    def _delete_query(self) -> psycopg2.sql:
        query = sql.SQL("DELETE FROM {table}").format(
            table=sql.SQL(self._table_name),
        )
        query += sql.SQL(";")
        return query


class ShopService:
    SHOP = {}

    def __init__(self, dbname: str, user: str,
                 password: str, host: str,
                 shop_invent_table_name: str, shopping_card_table_name: str):
        self._shop_invent_storage = Storage(DataBaseHandler(dbname, user,
                                                            password, host, shop_invent_table_name))
        self._shopping_card_storage = Storage(DataBaseHandler(dbname, user,
                                                              password, host, shopping_card_table_name))

    def get_all_product(self) -> Dict:
        if not self.SHOP:
            all_product = self._shop_invent_storage.get_data()
            all_product_dict = {x[1]: x for x in all_product}
            self.SHOP.update(all_product_dict)
        return self.SHOP

    def add_product(self, product_name: str) -> None:
        price = self.get_all_product().get(product_name)[2]
        self._shopping_card_storage.add_item({'price': price})

    def get_buy_product(self) -> List:
        shopping_cart = self._shopping_card_storage.get_data()
        prices = list(map(lambda x: x[1], shopping_cart))
        result = prices
        return result

    def format_product(self, product_list: Dict) -> str:
        return '\n'.join([
            f'{product_name} - {product[2]} dollars'
            for product_name, product in product_list.items()
        ])

    def clear_buy_products(self):
        self._shopping_card_storage.remove_all()

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
    shop_invent_table_name = 'shop_invent'
    shopping_card_table_name = 'shopping_cart'
    shop = Shop(ShopService('banking_system', 'postgres',
                            'mypassword', 'localhost', shop_invent_table_name, shopping_card_table_name))
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
