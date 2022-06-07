import json
from typing import List, Dict

def print_hello_username():
    name = input('Enter your name: ')
    print("Dear %s, happy to see u"%(name))
    
def exit():
    print('Waiting for you again:)')


class JsonStorageHandler:
    """работа с хранилищем данных"""

    def __init__(self, path):
        self.path = path

    def write_file(self, data) -> None:
        with open(self.path, "w") as file:
            json.dump(data, file)

    def read_file(self) -> List:
        with open(self.path) as file:
            result = json.load(file)
        return result


    def add_info_file(self, product: str):
        catalog = JsonStorageHandler("products.json").read_file()
        data = JsonStorageHandler(self.path).read_file()
        if product in catalog:
            data.append(product) 
        else:
            print("Please, choose a product from catalog!")
        JsonStorageHandler(self.path).write_file(data)


class DataHandler:
    """адаптация вывода информации"""

    def __init__(self, path):
        self.path = path

    def format_catalog_dict(self) -> Dict:
        data = JsonStorageHandler(self.path).read_file()
        for key, value in data.items():
            print(key, ':', value, sep='')

    def format_catalog_list(self) -> List:
        data = JsonStorageHandler(self.path).read_file()
        for i in data:
            print(i, sep='')


class Order:
    """управление заказом"""

    def __init__(self, products_storage_path, sbag_storage_path):
        self._products_storage_path  = JsonStorageHandler(products_storage_path)
        self._sbag_storage_path = JsonStorageHandler(sbag_storage_path)


    def add_item_sbag(self) -> str:
        catalog = self._products_storage_path.read_file()
        data = self._sbag_storage_path.read_file()
        product = input('Please add a product name to sbag(one by one): ')
        if product in catalog:
            data.append(product)
            self._sbag_storage_path.write_file(data)
            print('Product added to SBAG. To add more back to order page')  
        else:
            print("Please, choose a product from catalog!")


    def count_sbag_sum(self) -> str:
        final_sum=0
        for i in self._sbag_storage_path.read_file():
            final_sum += self._products_storage_path.read_file().get(i)
        print('Final purchase cost is {}.Thank you!'.format(final_sum))

    def show_sbag(self)-> List:
        DataHandler("sbag.json").format_catalog_list()
        self.count_sbag_sum()

    def clear_sbag(self)-> None:
        self._sbag_storage_path.write_file([])


class Console:
    """действия через меню магазина"""

    def __init__(self, order):
        self.order = order

    def get_menu(self):
        print(
            "-"*20 + "\n" +
            '1. Product catalog \n'
            '2. Order page \n'
            '3. S-Bag \n'
            '4. Clear S-Bag \n'
            '5. Exit \n'
        )
  
    def make_choice(self,choice: int): 
        if  choice == 1:
            DataHandler("products.json").format_catalog_dict()
        elif choice == 2:
            self.order.add_item_sbag()  
        elif choice == 3:
            self.order.show_sbag()  
        elif choice == 4: 
            self.order.clear_sbag()
        elif choice == 5:
            exit() 


def run()-> None:
    """запуск"""

    print_hello_username()
    products_storage_path = "products.json"
    sbag_storage_path = "sbag.json"
    console = Console(Order(products_storage_path, sbag_storage_path))
    choice = None
    while choice != 5:
        console.get_menu()
        try:
            choice = int(input("Choose an item: "))
            console.make_choice(choice) 
        except ValueError:
            print("Enter a number from 1 to 5!")