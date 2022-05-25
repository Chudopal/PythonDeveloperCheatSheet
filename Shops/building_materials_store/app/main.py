"""5. Напишите программу магазина.
Покупатели могут покупать какие-то продукты в магазине.
Возможности покупателя:
- посмотреть все товары и цены на них
- выбрать товар
- посмотреть сумму покупки(сумма цен выбранных товаров)
Взаимодействие происходит через консоль.
Товары храните просто в какой-нибудь из коллекций.
Выбор товара - это ввод пользователем строки названия товара
"""

import json
from typing import List, Dict


class JsonHandler:
    def __init__(self, path, name, data):
        self.path = path
        self.name = name
        self.data = data

    def read_file(self, name) -> List:  # чтение json файла
        with open(self.path) as file:
            data = json.load(file)
        return data.get(self.name)

    def read_buy_file(self, path) -> List:  # чтение json файла
        with open(self.path) as file:
            data = json.load(file)
        return data

    def write_file(self, data) -> None:  # запись json файла
        with open(self.path, 'w') as file:
            json.dump(data, file, indent=4)


class FileManager:

    def get_all_product(self) -> List:  # показывает все материалы магазина
        data = JsonHandler("storage_building.json", "materials").read_file()
        return data

    def save_buy_product(self, buy_product):  # сохраняет добавленный товар в корзине
        data = JsonHandler('buy_materials.json').write_file(buy_product)
        return "Товар успешно сохранён в корзину!"


class ServiceFun:
    def __init__(self, product_name, data, product_list):
        self.product_name = product_name
        self.data = data
        self.product_list = product_list

    buy_product = []

    def adaptor(self, data: List) -> Dict:  # конвертация листа в словарь
        result = {}
        for materials in data:
            result[materials.get('material_name')] = materials.get('cost')
        return result

    def add_product(self, product_name: str) -> None:  # добавляет товар в корзину
        catalog = FileManager.get_all_product()
        for material in catalog:
            item_cost = material['cost']
            item_material = material['material_name']
            if product_name == item_material:
                result = {item_material: item_cost}
                ServiceFun.buy_product.append(result)
        return "Спасибо! Товар добавлен в корзину!"

    def get_buy_product(self) -> List:  # показывает сумму покупки
        result_list = []
        for material in ServiceFun.buy_product:
            result = list(material.values())
            for material in result:
                result_list.append(material)
        total_price = sum(result_list)
        result = (f'Ваша сумма покупки составляет {total_price} руб')
        return result

    def format_product(self, product_list: Dict) -> str:
        return '\n'.join([
            f'{product_name} - {cost} руб'
            for product_name, cost in product_list.items()
        ])


class SHOP:
    def __init__(self, choice):
        self.choice = choice

    def menu() -> str:
        return (
                '<>' * 80 + '\n'
                            '1 - посмотреть все товары и цены на них\n' +
                '2 - выбрать товар\n' +
                '3 - сохранить выбранные товары в корзине\n' +
                '4 - посмотреть сумму покупки(сумма цен выбранных товаров)\n' +
                '5 - завершить покупку.'
        )

    def make_choice(choice: int):
        if choice == 1:
            print('СПИСОК ДОСТУПНЫХ ТОВАРОВ:')
            product = ServiceFun().adaptor(FileManager().get_all_product())
            message = ServiceFun().format_product(product)
            result = message
        elif choice == 2:
            product_name = input('Введите желаемый товар: ')
            result = ServiceFun().add_product(product_name)
        elif choice == 3:
            result = FileManager().save_buy_product(ServiceFun().buy_product)
        elif choice == 4:
            result = ServiceFun().get_buy_product()
        elif choice == 5:
            result = "Спасибо, за покупку!"
        return result


def run() -> None:
    choice = None
    while choice != 5:
        print(SHOP.menu())
        try:
            choice = int(input('Введите пункт меню: '))
            message = SHOP.make_choice(choice)
            print(message)
        except ValueError:
            print("Введите целое число от 1 до 5!")


run()
