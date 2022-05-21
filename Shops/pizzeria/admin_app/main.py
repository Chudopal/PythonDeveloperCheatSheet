import json
from pathlib import Path
from dataclasses import dataclass, asdict
from abc import ABC, abstractmethod


# ----------------- #
# DATA ACCESS LAYER #
# ----------------- #
class StorageHandler(ABC):

    @abstractmethod
    def read(self):
        """reads data from storage"""

    @abstractmethod
    def save(self, data):
        """save data to storage"""


class JsonStorageHandler(StorageHandler):

    def __init__(self, file_name: str):
        self.__base_dir = Path(__file__).resolve().parent.parent
        self.file_name = str(self.__base_dir.joinpath('app', file_name))

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


class StorageAdaptor:

    def __init__(self, stored_data: StorageHandler):
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

    def make_order(self, product: str, amount: int) -> bool:
        product_in_storage = self.products.get_product(product)
        if product_in_storage:
            order = Order(name=product_in_storage.name,
                          amount=amount,
                          price=product_in_storage.price * amount,
                          calories=product_in_storage.calories * amount)
            self.orders.add_order(order)
            success = True
        else:
            success = False
        return success

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


class AdminShop(Shop):

    def add_product(self, product: Product):
        self.products.add_product(product)

    def remove_product(self, product_name: str) -> bool:
        product_to_remove = self.products.get_product(product_name)
        if product_to_remove:
            self.products.remove_product(product_to_remove)
            return True
        else:
            return False


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
        executes print() function with output_items as args
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
        template = '- {pizza}: {description} ({calories} kcal) - {price} €\n'
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


class ConsoleAdminView(ConsoleAppView):

    def get_menu(self) -> str:
        return '-' * 30 + '\nPlease choose an action:\n' \
                          '1. List of pizzas\n' \
                          '2. Order pizza\n' \
                          '3. Show order\n' \
                          '4. Clear orders\n' \
                          '5. Add pizza to storage\n' \
                          '6. Remove pizza from storage\n' \
                          '7. Quit program'

    @staticmethod
    def get_pizza_form() -> dict:
        return {
            'name': 'Pizzas name: ',
            'category': 'Category: ',
            'price': 'Price: ',
            'calories': 'Calories: ',
            'description': 'Description [optional]: '
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
            result = self.pizzeria.make_order(**processed_input)
            if result:
                output = self.view.get_success_message('order_success', processed_input.get("product"))
            else:
                output = self.view.get_error_message('no_pizza_error')
        except ValueError:
            output = self.view.get_error_message('value_error')
        self.io.execute_output(output)

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


class AdminShopApplication(ShopApplication):

    def __init__(self, shop: AdminShop, io: ConsoleIOController, view: ConsoleAdminView):
        super().__init__(shop, io, view)
        self.pizzeria = shop
        self.view = view
        self.io = io

    def _get_action(self) -> dict[int, callable]:
        return {
            1: self.show_all_pizzas_controller,
            2: self.order_pizza_controller,
            3: self.show_orders_controller,
            4: self.clear_orders_controller,
            5: self.add_new_pizza_controller,
            6: self.remove_pizza_controller,
            7: quit
        }

    def add_new_pizza_controller(self):
        raw_input = self.io.execute_input(**self.view.get_pizza_form())
        try:
            processed_input = self.io.validate_product_input(raw_input)
            self.pizzeria.add_product(Product(**processed_input))
            self.io.execute_output(self.view.get_success_message('add_success', processed_input.get('name')))
        except ValueError:
            self.io.execute_output(self.view.get_error_message('value_error'))

    def remove_pizza_controller(self):
        raw_input = self.io.execute_input(**self.view.get_input_message('remove_pizza'))
        processed_input = self.io.validate_input(raw_input)
        result = self.pizzeria.remove_product(processed_input.get('name'))
        if result:
            self.io.execute_output(self.view.get_success_message('remove_success', processed_input.get('name')))
        else:
            self.io.execute_output(self.view.get_error_message('no_pizza_error'))

    @staticmethod
    def _create_pizza(new_pizza: dict) -> Product:
        return Product(**new_pizza)


if __name__ == '__main__':
    pizza_storage = StorageAdaptor(JsonStorageHandler("pizzas.json"))
    orders_storage = StorageAdaptor(JsonStorageHandler("ordered_pizzas.json"))
    mega_pizzeria = AdminShop(pizza_storage, orders_storage)
    app = AdminShopApplication(mega_pizzeria, ConsoleIOController(), ConsoleAdminView())
    app.run_app()
