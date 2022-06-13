import json
import psycopg2
from dataclasses import dataclass, asdict
from abc import ABC, abstractmethod


# ----------------- #
# Exceptions #
# ----------------- #

class NoSuchProductException(Exception):
    """raises when no required product at storage"""


# ----------------- #
# DATA ACCESS LAYER #
# ----------------- #

class StorageAdaptor(ABC):

    @abstractmethod
    def get_data(self) -> list[dict]:
        """returns all data from storage as list[dict]"""

    @abstractmethod
    def add_item(self, new_item: dict):
        """add data represented as dict object to storage"""

    @abstractmethod
    def remove_item(self, item: dict):
        """remove item from storage"""

    @abstractmethod
    def clear_data(self):
        """delete all the data from storage"""


class DBStorage:
    def __init__(self, **kwargs):
        self._host = kwargs.get('host', '127.0.0.1')
        self._user = kwargs.get('user', '')
        self._password = kwargs.get('password', '')
        self._dbname = kwargs.get('dbname')

    def execute(self, *sql_query: str) -> psycopg2.cursor:
        connector = psycopg2.connect(host=self._host, user=self._user, password=self._password, dbname=self._dbname)
        # connector = sqlite3.connect(self._dbname)
        cursor = connector.cursor()
        for item in sql_query:
            cursor.execute(item)
        connector.commit()
        return cursor


class JsonStorage:

    def __init__(self, file_name: str):
        self.file_name = file_name

    def read(self) -> list:
        try:
            with open(self.file_name, "r") as file:
                data = json.load(file)
        except OSError:
            data = []
        return data

    def save(self, data):
        with open(self.file_name, "w") as file:
            json.dump(data, file)


class DBStorageAdaptor(StorageAdaptor):
    def __init__(self, db_storage: DBStorage, table_name: str):
        self.db_storage = db_storage
        self.table_name = table_name

    def get_data(self) -> list[dict]:
        _SQL = """SELECT * FROM {table_name};""".format(table_name=self.table_name)
        db_response = self.db_storage.execute(_SQL)
        columns = [item[0] for item in db_response.description]
        data = [dict(zip(columns, row)) for row in db_response.fetchall()]
        return data

    def add_item(self, new_item: dict):
        _SQL = """INSERT INTO {table_name} VALUES ({values});"""
        self.db_storage.execute(_SQL)

    def remove_item(self, item: dict):
        _SQL = """DELETE FORM {table_name} WHERE {key}={value};"""
        self.db_storage.execute(_SQL)

    def clear_data(self):
        _SQL = """DELETE FROM {table_name};""".format(table_name=self.table_name)
        self.db_storage.execute(_SQL)


class JsonStorageAdaptor(StorageAdaptor):

    def __init__(self, stored_data: JsonStorage):
        self.stored_data = stored_data

    def get_data(self) -> list:
        return self.stored_data.read()

    def add_item(self, new_item: dict):
        data = self.get_data()
        data.append(new_item)
        self.stored_data.save(data)

    def remove_item(self, item: dict):
        data = self.get_data()
        data.remove(item)
        self.stored_data.save(data)

    def clear_data(self):
        self.stored_data.save([])


# ----------------- #
# DOMAIN LAYER #
# ----------------- #

@dataclass
class Product:
    pizza_id: int
    name: str
    category: str
    description: str
    price: float
    calories: int


@dataclass
class Order:
    name: str
    amount: int
    price: float
    calories: int


class OrdersHandler:

    def __init__(self, orders: StorageAdaptor):
        self.orders = orders

    def get_orders(self) -> list:
        return [Order(**order) for order in self.orders.get_data()]

    def add_order(self, order: Order):
        processed_order = asdict(order)
        self.orders.add_item(processed_order)

    def clear_order(self):
        self.orders.clear_data()


class ProductsHandler:

    def __init__(self, products: StorageAdaptor):
        self.products = products

    def get_all_products(self) -> list[Product]:
        return [Product(**product) for product in self.products.get_data()]

    def get_product(self, name: str) -> Product or None:
        result = None
        for product in self.get_all_products():
            if product.name == name:
                result = product
                break
        return result

    def remove_product(self, product: Product) -> None:
        self.products.remove_item(asdict(product))

    def add_product(self, new_product: Product) -> None:
        processed_product = asdict(new_product)
        self.products.add_item(processed_product)


class Shop:

    def __init__(self, goods: StorageAdaptor, orders: StorageAdaptor):
        self.products = ProductsHandler(goods)
        self.orders = OrdersHandler(orders)

    def make_order(self, product: str, amount: int):
        product_in_storage = self.products.get_product(product)
        try:
            order = Order(name=product_in_storage.name,
                          amount=amount,
                          price=product_in_storage.price * amount,
                          calories=product_in_storage.calories * amount)
            self.orders.add_order(order)
        except AttributeError:
            raise NoSuchProductException

    def cancel_order(self):
        self.orders.clear_order()

    def get_orders(self) -> list:
        return self.orders.get_orders()

    def get_products(self) -> list:
        return self.products.get_all_products()

    def total_sum(self) -> float:
        total_sum = 0
        for order in self.get_orders():
            total_sum += order.price
        return total_sum

    def total_calories(self) -> int:
        total_calories = 0
        for order in self.get_orders():
            total_calories += order.calories
        return total_calories


# ----------------- #
# INTERFACE LAYER #
# ----------------- #

class AppView(ABC):

    @abstractmethod
    def get_menu(self) -> str:
        """
         returns application menu
        """

    @abstractmethod
    def get_input_message(self, key: str) -> dict[str: str]:
        """
        returns a message for input() __prompt argument
        """

    @abstractmethod
    def get_error_message(self, key: str) -> dict[str: str]:
        """
        returns error message
        """

    @abstractmethod
    def get_success_message(self, key: str, arg: str = ''):
        """
        returns success message
        """

    @abstractmethod
    def format_products_list(self, products: list[Product]) -> str:
        """
        returns formatted products list as string
        """

    @abstractmethod
    def format_orders_list(self, orders: list[Order], total_sum: float) -> str:
        """
        returns formatted orders list as string
        """


class IOController(ABC):

    @abstractmethod
    def execute_input(self, **input_items: dict) -> dict:
        """
        executes input() function with input_items as __prompt arg.
        """

    @abstractmethod
    def execute_output(self, *output_items: str):
        """
        executes print() function
        """

    @abstractmethod
    def validate_input(self, raw_input: dict[str: str]) -> dict:
        """
        validates input string
        """

    @abstractmethod
    def validate_order_input(self, raw_input: dict[str: str]) -> dict:
        """
        validates order input
        """

    @abstractmethod
    def validate_product_input(self, raw_input: dict[str: str]) -> dict:
        """
        validates product input
        """


class ConsoleAppView(AppView):

    def get_menu(self) -> str:
        return '-' * 30 + '\nPlease choose an action:\n' \
                          '1. List of pizzas\n' \
                          '2. Order pizza\n' \
                          '3. Show order\n' \
                          '4. Clear orders\n' \
                          '5. Quit program'

    def get_input_message(self, key: str) -> dict[str, str]:
        messages = {
            "action": ">>> ",
            "make_order": "What pizza would you like to order? (pizza [amount]): ",
            "add_pizza": "Add pizza: (category, name, price, calories, [description]) ",
            "remove_pizza": "What pizza would you want to remove from storage (name): "
        }
        return {key: messages.get(key)}

    def get_error_message(self, error: str) -> str:
        errors = {
            'action_error': 'You choose wrong action. Try again',
            'no_pizza_error': 'We don`t have that pizza, please try again',
            'no_orders_error': 'You haven`t order any pizza yet',
            'value_error': "You entered incorrect value, please try again"
        }
        return errors.get(error)

    def get_success_message(self, message: str, arg: str = '') -> str:
        messages = {
            'delete_success': 'Your order has been canceled!',
            'order_success': f'"{arg}" pizza added to your order',
            'add_success': f'"{arg}" pizza added to storage',
            'remove_success': f'"{arg}" pizza removed from storage'
        }
        return messages.get(message)

    def format_products_list(self, products_list: list[Product]) -> str:
        template = '- {pizza}: {description} ({calories} kcal) - {price} в‚¬\n'
        result = '\nToday on sale:\n'
        categories = {product.category for product in products_list}
        for category in categories:
            result += category + '\n'
            for product in products_list:
                if product.category == category:
                    result += template.format(pizza=product.name,
                                              description=product.description,
                                              calories=product.calories,
                                              price=product.price)
        return result

    def format_orders_list(self, orders_list: list[Order], total_sum: float) -> str:
        template = '{pizza} x {amount}: {price:.2f}\n'
        result = '\nYour order:\n'
        for product in orders_list:
            result += template.format(pizza=product.name,
                                      amount=product.amount,
                                      price=product.price)
        result += f'\nTOTAL SUM: {total_sum:.2f}'
        return result

    @staticmethod
    def get_order_form() -> dict:
        return {
            'name': 'What pizza would you like to order: ',
            'amount': 'And how many: '
        }


# ----------------- #
# CONTROLLER LAYER #
# ----------------- #

class ConsoleIOController(IOController):

    def execute_output(self, *output_items):
        for item in output_items:
            print(item, sep="", end='\n')

    def execute_input(self, **input_items: dict) -> dict:
        return {key: input(message) for key, message in input_items.items()}

    def validate_input(self, raw_input: dict[str: str]) -> dict:
        return {
            'name': raw_input.get('remove_pizza').strip().title()
        }

    def validate_order_input(self, raw_input: dict[str: str]) -> dict:
        return {
            'product': raw_input.get('name').strip().title(),
            'amount': int(raw_input.get('amount'))
        }

    def validate_product_input(self, raw_input: dict[str]) -> dict:
        return {
            'name': raw_input.get('name', 'Default name').strip().title(),
            'category': raw_input.get('category', 'Default category').strip().capitalize(),
            'description': raw_input.get('description', "").strip().lower(),
            'price': float(raw_input.get('price', 0)),
            'calories': int(raw_input.get('calories', 0))
        }


class ShopApplication:

    def __init__(self, shop: Shop, io: ConsoleIOController, view: ConsoleAppView):
        self.pizzeria = shop
        self.view = view
        self.io = io

    def show_all_pizzas_controller(self):
        all_pizzas = self.pizzeria.get_products()
        result = self.view.format_products_list(all_pizzas)
        self.io.execute_output(result)

    def order_pizza_controller(self):
        raw_input = self.io.execute_input(**self.view.get_order_form())
        try:
            processed_input = self.io.validate_order_input(raw_input)
            self.pizzeria.make_order(**processed_input)
            result = self.view.get_success_message('order_success', processed_input.get("product"))
        except NoSuchProductException:
            result = self.view.get_error_message('no_pizza_error')
        except ValueError:
            result = self.view.get_error_message('value_error')
        self.io.execute_output(result)

    def show_orders_controller(self):
        orders = self.pizzeria.get_orders()
        total_sum = self.pizzeria.total_sum()
        result = self._check_orders(orders, total_sum)
        self.io.execute_output(result)

    def clear_orders_controller(self):
        self.pizzeria.cancel_order()
        self.io.execute_output(self.view.get_success_message("delete_success"))

    def run_app(self):
        while True:
            self.io.execute_output(self.view.get_menu())
            action = self._menu_input_controller()
            self._get_action().get(action, self._show_error_message)()

    def _get_action(self) -> dict[int, callable]:
        return {
            1: self.show_all_pizzas_controller,
            2: self.order_pizza_controller,
            3: self.show_orders_controller,
            4: self.clear_orders_controller,
            5: quit
        }

    def _show_error_message(self, error: str = 'action_error'):
        error_message = self.view.get_error_message(error)
        self.io.execute_output(error_message)

    def _menu_input_controller(self) -> int:
        user_input = self.io.execute_input(**self.view.get_input_message('action'))
        try:
            action = int(user_input.get('action'))
        except ValueError:
            action = 0
        return action

    def _check_orders(self, orders: list, total_sum: float) -> str:
        if orders:
            result = self.view.format_orders_list(orders, total_sum)
        else:
            result = self.view.get_error_message('no_orders_error')
        return result


if __name__ == '__main__':
    database = DBStorage(dbname="pizzeria.db")
    pizzas_storage = DBStorageAdaptor(
        db_storage=database,
        table_name="pizzas"
    )
    orders_storage = DBStorageAdaptor(
        db_storage=database,
        table_name="orders"
    )
    mega_pizzeria = Shop(pizzas_storage, orders_storage)
    app = ShopApplication(mega_pizzeria, ConsoleIOController(), ConsoleAppView())
    app.run_app()
