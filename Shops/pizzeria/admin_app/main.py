from pathlib import Path
from Shops.pizzeria.app import main as base


class JsonStorageHandler(base.JsonStorageHandler):

    def __init__(self, file_name: str):
        self.__base_dir = Path(__file__).resolve().parent.parent
        self.file_name = str(self.__base_dir.joinpath('app', file_name))


class AdminShop(base.Shop):

    def add_product(self, product: base.Product):
        self.products.add_product(product)

    def remove_product(self, product_name: str) -> bool:
        product_to_remove = self.products.get_product(product_name)
        if product_to_remove:
            self.products.remove_product(product_to_remove)
            return True
        else:
            return False


class ConsoleAdminView(base.ConsoleAppView):

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


class AdminShopApplication(base.ShopApplication):

    def __init__(self, shop: AdminShop, io: base.ConsoleIOController, view: ConsoleAdminView):
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
            self.pizzeria.add_product(base.Product(**processed_input))
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
    def _create_pizza(new_pizza: dict) -> base.Product:
        return base.Product(**new_pizza)


if __name__ == '__main__':
    pizza_storage = base.StorageAdaptor(JsonStorageHandler("pizzas.json"))
    orders_storage = base.StorageAdaptor(JsonStorageHandler("ordered_pizzas.json"))
    mega_pizzeria = AdminShop(pizza_storage, orders_storage)
    app = AdminShopApplication(mega_pizzeria, base.ConsoleIOController(), ConsoleAdminView())
    app.run_app()
