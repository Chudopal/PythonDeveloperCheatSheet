import json


# ---------------- #
# STORAGES #
# ---------------- #

# at external files now

# ----------------- #
# DATA ACCESS LAYER #
# ----------------- #

class FilesHandler:

    def __init__(self, file_name: str, path: str = ""):
        self.path = path
        self.file_name = file_name

    def read(self) -> dict:
        try:
            with open(self.path + self.file_name, "r") as file:
                data = json.load(file)
        except OSError:
            data = {}
        return data

    def save(self, data):
        with open(self.path + self.file_name, "w") as file:
            json.dump(data, file)


class Storage:

    def __init__(self, data: FilesHandler):
        self.data = data

    def get_data(self) -> dict:
        return self.data.read()

    def add_item(self, new_item):
        stored_data = self.get_data()
        stored_data.update(new_item)
        self.data.save(stored_data)

    def remove_item(self, item):
        stored_data = self.get_data()
        stored_data.pop(item)
        self.data.save(stored_data)


# ----------------- #
# DOMAIN LAYER #
# ----------------- #

class Product:

    def __init__(self, category: str, name: str, price: float):
        self.category = category
        self.name = name
        self.price = price

    def get_name(self) -> str:
        return self.name

    def get_price(self) -> float:
        return self.price

    def product_info(self) -> list[str, dict]:
        return [self.category, {
            self.name: {
                'price': self.price
            }
        }
                ]


class Pizza(Product):
    def __init__(self, category: str, name: str, price: float, calories: int, description: str = ''):
        self.calories = calories
        self.description = description
        super().__init__(category, name, price)

    def product_info(self) -> list[str, dict]:
        return [self.category, {
            self.name: {
                'price': self.price,
                'calories': self.calories,
                'description': self.description
            }
        }
                ]


class OrdersHandler:

    def __init__(self, orders: Storage):
        self.orders = orders

    def get_orders(self) -> dict:
        return self.orders.get_data()

    def add_order(self, item: str, amount: int, price: float):
        processed_order = self._process_order(item, amount, price)
        self.orders.add_item(processed_order)

    def _process_order(self, item: str, amount: int, price: float) -> dict[str: dict[str: float, str: int]]:
        item_from_orders = self._get_item(item)
        new_amount = item_from_orders.get('amount') + amount
        new_price = price * new_amount
        return {item: {'price': new_price, 'amount': new_amount}}

    def _get_item(self, item: str) -> dict[str: float, str: int]:
        orders = self.get_orders()
        default_item = {'price': 0, 'amount': 0}
        return orders.get(item, default_item)


class ProductsHandler:

    def __init__(self, products: Storage):
        self.products = products.get_data()
        self.data_at_storage = products

    def get_all_products(self) -> dict:
        return self.products

    def add_product(self, product: Product):
        product_category = product.product_info()[0]
        product_data = product.product_info()[1]
        self.products.get(product_category).update(product_data)
        self.data_at_storage.add_item(self.products)

    def remove_product(self, product: Product):
        self.products.get(product.product_info()[0]).pop(product.get_name())
        self.data_at_storage.remove_item(product.get_name())

    def remove_category(self, category: str):
        pass

    def get_products_in_category(self, category: str) -> dict:
        return self.products.get(category)

    def get_product(self, name: str) -> dict:
        product = None
        # filter(lambda x: x.get(name), self.products.values())
        for category in self.products.values():
            product = category.get(name)
            if product:
                break
        return product

    def get_product_by_category(self, category: str, name: str) -> dict:
        return self.products.get(category).get(name)

    def get_price(self, product_name: str) -> any:
        product = self.get_product(product_name)
        if product:
            result = product.get('price')
        else:
            result = None
        return result


class PizzasStorageHandler(ProductsHandler):

    def get_calories(self, product: str) -> int:
        return self.get_product(product).get('calories')

    def get_description(self, product: str) -> str:
        return self.get_product(product).get('description')


class Shop:

    def __init__(self, goods: Storage, orders: Storage):
        self.goods = ProductsHandler(goods)
        self.orders = OrdersHandler(orders)

    def make_order(self, product_name: str, amount: int) -> bool:
        price = self.goods.get_price(product_name)
        if price:
            self.orders.add_order(product_name, amount, price)
            success = True
        else:
            success = False

        return success

    def get_orders(self) -> dict:
        return self.orders.get_orders()

    def get_goods(self) -> dict:
        return self.goods.get_all_products()

    def total_sum(self) -> float:
        total_sum = 0
        for order in self.get_orders().values():
            total_sum += order.get('price')
        return total_sum


class ShopAdmin(Shop):

    def add_product(self, product: Product):
        self.goods.add_product(product)

    def remove_product(self, product: Product):
        self.goods.remove_product(product)


# ----------------- #
# INTERFACE LAYER #
# ----------------- #

class ConsoleView:

    @staticmethod
    def show_menu() -> str:
        return '-' * 30 + '\nPlease choose an action:\n' \
                          '1. List of pizzas\n' \
                          '2. Order pizza\n' \
                          '3. Show order\n' \
                          '4. Clear orders\n' \
                          '5. Quit program'

    @staticmethod
    def get_error_message(error: str) -> str:
        errors = {
            'action_error': 'You choose wrong action. Try again',
            'no_pizza_error': 'We don`t have that pizza, please try again',
            'no_orders_error': 'You haven`t order any pizza yet'
        }
        return errors.get(error)

    @staticmethod
    def get_input_message(key: str) -> str:
        messages = {
            "action": ">>> ",
            "make_order": "What pizza would you like to order? (pizza [amount]): "
        }
        return messages.get(key)

    @staticmethod
    def validate_order(order: list[str]) -> dict:
        quantity = 1
        if order[-1].isdigit():
            quantity = int(order[-1])
            product = ' '.join(order[:-1])
        else:
            product = ' '.join(order)

        return {'product': product, 'quantity': quantity}

    @staticmethod
    def format_pizzas_list(pizzas_list: dict[str: dict[str: any]]) -> str:
        template = '* {product}: {description} ({calories} kcal) - {price} €\n'
        result = '\nToday on sale:\n'
        for category, pizzas in pizzas_list.items():
            result += category + '\n'
            for pizza, pizza_data in pizzas.items():
                result += template.format(product=pizza,
                                          description=pizza_data.get('description'),
                                          calories=pizza_data.get('calories'),
                                          price=pizza_data.get('price'))
        return result

    @staticmethod
    def format_orders_list(orders_list: dict[str: dict[str: float, str: int]], total_sum: float) -> str:
        template = '{pizza} x {amount}: {price:.2f}\n'
        result = '\nYour order:\n'
        for pizza_name, pizza_data in orders_list.items():
            result += template.format(pizza=pizza_name,
                                      amount=pizza_data.get('amount'),
                                      price=pizza_data.get('price'))
        result += f'\nTOTAL SUM: {total_sum:.2f}'
        return result


class AdminConsoleView(ConsoleView):

    def show_menu(self) -> str:
        return '-' * 30 + '\nPlease choose an action:\n' \
                          '1. List of pizzas\n' \
                          '2. Order pizza\n' \
                          '3. Show order\n' \
                          '4. Clear orders\n' \
                          '5. Add pizza to storage' \
                          '6. Remove pizza from storage' \
                          '7. Quit program'

    @staticmethod
    def get_input_message(key: str) -> str:
        messages = {
            "action": ">>> ",
            "make_order": "What pizza would you like to order? (pizza [amount]): ",
            "add_pizza": "Add pizza: (category, name, price, calories, [description]) ",
            "remove_pizza": "What pizza would you want to remove from storage: "
        }
        return messages.get(key)


# ----------------- #
# CONTROLLER LAYER #
# ----------------- #

class IOController:
    @staticmethod
    def print_output(*output_items: str):
        for item in output_items:
            print(item, sep="")

    @staticmethod
    def receive_input(input_phrase: str) -> str:
        return input(input_phrase)

    @staticmethod
    def validate_user_action(raw_user_action: str) -> int:
        try:
            user_action = int(raw_user_action)
        except ValueError:
            user_action = 0
        return user_action

    @staticmethod
    def validate_user_input(raw_user_input: str) -> list:
        user_input = raw_user_input.strip().upper().split(" ")
        return user_input


class ShopApplication:

    def __init__(self, pizzas: str = "pizzas.json", orders: str = "ordered_pizzas.json"):
        self.orders_storage = Storage(FilesHandler(orders))
        self.pizzas_storage = Storage(FilesHandler(pizzas))
        self.pizzeria = Shop(self.pizzas_storage, self.orders_storage)
        self.console = ConsoleView
        self.io = IOController

    def _get_action(self) -> dict[int, callable]:
        return {
            1: self.show_all_pizzas_controller,
            2: self.order_pizza_controller,
            3: self.show_orders_controller,
            4: self.clear_orders_controller,
            5: quit
        }

    @staticmethod
    def _check_orders(orders: dict, total_sum: float) -> str:
        if orders:
            result = ConsoleView.format_orders_list(orders, total_sum)
        else:
            result = ConsoleView.get_error_message('no_orders_error')

        return result

    def _show_error_message(self, error: str = 'action_error'):
        error_message = self.console.get_error_message(error)
        self.io.print_output(error_message)

    def menu_input_controller(self) -> int:
        raw_user_input = self.io.receive_input(self.console.get_input_message('action'))
        return self.io.validate_user_action(raw_user_input)

    def show_all_pizzas_controller(self):
        all_pizzas = self.pizzeria.get_goods()
        result = self.console.format_pizzas_list(all_pizzas)
        self.io.print_output(result)

    def order_pizza_controller(self):
        raw_user_input = self.io.receive_input(self.console.get_input_message('make_order'))
        user_input = self.io.validate_user_input(raw_user_input)
        order = self.console.validate_order(user_input)
        result = self.pizzeria.make_order(order.get('product'), order.get('quantity'))
        if result:
            output = f'{order.get("product")} pizza added to your order'
        else:
            output = self.console.get_error_message('no_pizza_error')
        self.io.print_output(output)

    def show_orders_controller(self):
        orders = self.pizzeria.get_orders()
        total_sum = self.pizzeria.total_sum()
        result = self._check_orders(orders, total_sum)
        self.io.print_output(result)

    def clear_orders_controller(self):
        pass

    def run_app(self):
        while True:
            self.io.print_output(self.console.show_menu())
            action = self.menu_input_controller()
            self._get_action().get(action, self._show_error_message)()


class AdminShopApplication(ShopApplication):
    pass


if __name__ == '__main__':
    mega_pizzeria = ShopApplication()
    mega_pizzeria.run_app()
