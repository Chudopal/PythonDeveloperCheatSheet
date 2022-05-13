import json


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

    def add_item(self, new_item: dict):
        stored_data = self.get_data()
        stored_data.update(new_item)
        self.data.save(stored_data)

    def remove_item(self, category: str, item: str):
        stored_data = self.get_data()
        stored_data.get(category).pop(item)
        self.data.save(stored_data)

    def add_item_category(self, new_category: dict[str: dict]):
        self.add_item(new_category)

    def remove_item_category(self, category: str):
        stored_data = self.get_data()
        stored_data.pop(category)
        self.data.save(stored_data)

    def clear_data(self):
        self.data.save({})


# ----------------- #
# DOMAIN LAYER #
# ----------------- #

class Product:

    def __init__(self, category: str, name: str, price: float, description: str):
        self.category = category
        self.name = name
        self.price = price
        self.description = description

    def get_info(self) -> dict[str: any]:
        return {
            'name': self.name,
            'category': self.category,
            'price': self.price,
            'description': self.description
        }


class PizzaProduct(Product):
    def __init__(self, category: str, name: str, price: float, calories: int, description: str = ''):
        self.calories = calories
        super().__init__(category, name, price, description)

    def get_info(self) -> dict[str: any]:
        return {
            'name': self.name,
            'category': self.category,
            'price': self.price,
            'description': self.description,
            'calories': self.calories
        }


class OrdersHandler:

    def __init__(self, orders: Storage):
        self.orders = orders

    def get_orders(self) -> dict:
        return self.orders.get_data()

    def add_order(self, item: str, amount: int, price: float):
        processed_order = self._process_order(item, amount, price)
        self.orders.add_item(processed_order)

    def clear_order(self):
        self.orders.clear_data()

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
        product_category = product.category
        new_product = {
            product.name: {
                'price': product.price,
                'description': product.description
            }
        }
        self.products.get(product_category).update(new_product)
        self.data_at_storage.add_item(self.products)

    def remove_product(self, product: Product):
        self.products.get(product.category).pop(product.name)
        self.data_at_storage.remove_item(product.category, product.name)

    def remove_category(self, category: str):
        pass

    def get_products_in_category(self, category: str) -> dict:
        return self.products.get(category)

    def get_product(self, name: str) -> dict:
        product = None
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


class PizzaProductsHandler(ProductsHandler):

    def get_calories(self, pizza: str) -> int:
        return self.get_product(pizza).get('calories')

    def get_description(self, pizza: str) -> str:
        return self.get_product(pizza).get('description')

    def add_product(self, product: PizzaProduct):
        product_category = product.category
        new_product = {
            product.name.upper(): {
                'price': product.price,
                'calories': product.calories,
                'description': product.description
            }
        }
        self.products.get(product_category).update(new_product)
        self.data_at_storage.add_item(self.products)

    def remove_product(self, product: list):
        self.products.get(product[0].upper()).pop(product[1].upper())
        self.data_at_storage.remove_item(product[0], product[1])

    def add_category(self, category: str):
        self.products[category.upper()] = {}
        self.data_at_storage.add_item_category({category.upper(): {}})


class Shop:

    def __init__(self, goods: Storage, orders: Storage):
        self.goods = PizzaProductsHandler(goods)
        self.orders = OrdersHandler(orders)

    def make_order(self, product_name: str, amount: int) -> bool:
        price = self.goods.get_price(product_name)
        if price:
            self.orders.add_order(product_name, amount, price)
            success = True
        else:
            success = False

        return success

    def cancel_order(self):
        self.orders.clear_order()

    def get_orders(self) -> dict:
        return self.orders.get_orders()

    def get_goods(self) -> dict:
        return self.goods.get_all_products()

    def total_sum(self) -> float:
        total_sum = 0
        for order in self.get_orders().values():
            total_sum += order.get('price')
        return total_sum


class AdminShop(Shop):

    def add_product(self, product: Product or PizzaProduct):
        if self.goods.get_products_in_category(product.category):
            self.goods.add_product(product)
        else:
            self.goods.add_category(product.category)
            self.goods.add_product(product)

    def remove_product(self, product: list):
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
    def get_input_message(key: str) -> str:
        messages = {
            "action": ">>> ",
            "make_order": "What pizza would you like to order? (pizza [amount]): ",
            "add_pizza": "Add pizza: (category, name, price, calories, [description]) ",
            "remove_pizza": "What pizza would you want to remove from storage (category, name): "
        }
        return messages.get(key)

    @staticmethod
    def get_error_message(error: str) -> str:
        errors = {
            'action_error': 'You choose wrong action. Try again',
            'no_pizza_error': 'We don`t have that pizza, please try again',
            'no_orders_error': 'You haven`t order any pizza yet'
        }
        return errors.get(error)

    @staticmethod
    def get_success_message(message: str, arg: str = '') -> str:
        messages = {
            'delete_success': 'Your order has been cleared!',
            'order_success': f'{arg} pizza added to your order',
            'add_success': f'{arg} pizza added to storage',
            'remove_success': f'{arg} pizza removed from storage'
        }
        return messages.get(message)

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

    @staticmethod
    def show_menu() -> str:
        return '-' * 30 + '\nPlease choose an action:\n' \
                          '1. List of pizzas\n' \
                          '2. Order pizza\n' \
                          '3. Show order\n' \
                          '4. Clear orders\n' \
                          '5. Add pizza to storage\n' \
                          '6. Remove pizza from storage\n' \
                          '7. Quit program'


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

    @staticmethod
    def validate_admin_input(raw_admin_input: str) -> list:
        admin_input = raw_admin_input.strip().split(",")
        admin_input[0] = admin_input[0].upper()
        admin_input[1] = admin_input[1].upper()
        return admin_input


class ShopApplication:

    def __init__(self, shop: Shop):
        self.pizzeria = shop
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

    def _menu_input_controller(self) -> int:
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
            output = self.console.get_success_message('order_success', order.get("product"))
        else:
            output = self.console.get_error_message('no_pizza_error')
        self.io.print_output(output)

    def show_orders_controller(self):
        orders = self.pizzeria.get_orders()
        total_sum = self.pizzeria.total_sum()
        result = self._check_orders(orders, total_sum)
        self.io.print_output(result)

    def clear_orders_controller(self):
        self.pizzeria.cancel_order()

    def run_app(self):
        while True:
            self.io.print_output(self.console.show_menu())
            action = self._menu_input_controller()
            self._get_action().get(action, self._show_error_message)()


class AdminShopApplication(ShopApplication):

    def __init__(self, shop: AdminShop):
        super().__init__(shop)
        self.console = AdminConsoleView
        self.pizzeria = shop

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

    def run_app(self):
        while True:
            self.io.print_output(self.console.show_menu())
            action = self._menu_input_controller()
            self._get_action().get(action, self._show_error_message)()

    def add_new_pizza_controller(self):
        raw_admin_input = self.io.receive_input(self.console.get_input_message('add_pizza'))
        admin_input = self.io.validate_admin_input(raw_admin_input)
        pizza = self._create_pizza(admin_input)
        self.pizzeria.add_product(pizza)
        self.io.print_output(self.console.get_success_message('add_success', pizza.name))

    def remove_pizza_controller(self):
        raw_admin_input = self.io.receive_input(self.console.get_input_message('remove_pizza'))
        admin_input = self.io.validate_admin_input(raw_admin_input)
        self.pizzeria.remove_product(admin_input)
        self.io.print_output(self.console.get_success_message('remove_success', admin_input[1]))

    @staticmethod
    def _create_pizza(raw_data: list) -> PizzaProduct:
        return PizzaProduct(*raw_data)


if __name__ == '__main__':
    pizza_storage = Storage(FilesHandler("pizzas.json"))
    orders_storage = Storage(FilesHandler("ordered_pizzas.json"))
    mega_pizzeria = AdminShop(pizza_storage, orders_storage)
    app = AdminShopApplication(mega_pizzeria)
    app.run_app()
