from typing import List, Dict
from abc import ABC, abstractmethod
from psycopg2 import sql
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

    def __init__(self, strategy: StorageHandler, table_name: str) -> None:
        self._strategy = strategy
        self._table_name = table_name

    @property
    def strategy(self) -> StorageHandler:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: StorageHandler) -> None:
        self._strategy = strategy

    def add_items(self, new_items) -> None:
        self._strategy.add_items(self._table_name, new_items)

    def get_data(self) -> List:
        return self._strategy.get_data(self._table_name)

    def remove_all(self) -> None:
        self._strategy.remove_all(self._table_name)


class DataBaseHandler(StorageHandler):

    def __init__(self, dbname: str, user: str,
            password: str, host: str) -> None:
        self._dbname = dbname
        self._user = user
        self._password = password
        self._host = host

    def get_data(self) -> List:
        sql_query = self._select_query()
        db_response = self.db_storage.execute(sql_query)
        columns = [item[0] for item in db_response.description]
        data = [dict(zip(columns, row)) for row in db_response.fetchall()]
        return data

    def add_items(self, item: dict):
        sql_query = self._insert_query(item)
        self.db_storage.execute(sql_query)

    def remove_all(self, item: dict):
        sql_query = self._delete_query(item)
        self.db_storage.execute(sql_query)

    def execute(self, sql_query):
        with closing(psycopg2.connect(dbname=self._dbname, user=self._user,
                              password=self._password, host=self._host)) as conn:
            with conn.cursor(cursor_factory=DictCursor) as cursor:
                cursor.execute(sql_query)
                conn.commit()
                return cursor


class DBStorageAdaptor(StorageHandler):

    def __init__(self, db_storage: DataBaseHandler, table_name: str):
        self.db_storage = db_storage
        self.table_name = table_name

    def _select_query(self, columns: list = None, filer_params: dict = None) -> psycopg2.sql:
        if columns:
            query = sql.SQL("SELECT {columns} FROM {table}").format(
                table=sql.SQL(self.table_name),
                columns=sql.SQL(", ").join([sql.Identifier(col) for col in columns])
            )
        else:
            query = sql.SQL("SELECT * FROM {table}").format(
                table=sql.SQL(self.table_name)
            )

        if filer_params:
            query += self._format_where_params(filer_params)
        query += sql.SQL(";")

        return {"query": query, "vars": filer_params}

    def _insert_query(self, variables: dict) -> psycopg2.sql:
        query = sql.SQL("INSERT INTO {table} ({columns}) VALUES ({values})").format(
            table=sql.SQL(self.table_name),
            columns=sql.SQL(", ").join([sql.Identifier(col) for col in variables.keys()]),
            values=sql.SQL(", ").join([sql.Placeholder(val) for val in variables.keys()])
        )
        query += sql.SQL(";")

        return {"query": query, "vars": variables}

    def _delete_query(self, filer_params: dict = None) -> psycopg2.sql:
        query = sql.SQL("DELETE FROM {table}").format(
            table=sql.SQL(self.table_name),
        )

        if filer_params:
            query += self._format_where_params(filer_params)
        query += sql.SQL(";")

        return {"query": query, "vars": filer_params}

    def _format_where_params(self, variables: dict) -> psycopg2.sql:
        return sql.SQL(" WHERE ") + sql.SQL(" AND ").join([sql.SQL("{}={}").format(
            sql.Identifier(identifier), sql.Placeholder(identifier)) for identifier in variables])


class ShopService:
    BUY_PRODUCTS = []
    SHOP = {}

    def __init__(self, shop_invent_table_name: str, shopping_card_table_name: str):
        self._shop_invent_storage = Storage(DataBaseHandler('banking_system', 'postgres',
                                                            'mypassword', 'host'), shop_invent_table_name)
        self._shopping_card_storage = Storage(DataBaseHandler('banking_system', 'postgres',
                                                              'mypassword', 'host'), shopping_card_table_name)

    def get_all_product(self) -> Dict:
        if not self.SHOP:
            self.SHOP.update(self._shop_invent_storage.get_data())
        return self.SHOP

    def add_product(self, product_name: str) -> None:
        self.BUY_PRODUCTS.append(self.get_all_product().get(product_name))
        self._shopping_card_storage.add_items(self.BUY_PRODUCTS)

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
    shopping_card_table_name = 'shopping_card'
    shop = Shop(ShopService(shop_invent_table_name, shopping_card_table_name))
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
