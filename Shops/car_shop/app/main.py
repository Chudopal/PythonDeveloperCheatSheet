import json
from unittest import result

class Stock:
    def __init__(self, filepath):
        self.filepath = filepath

    def get_cars(self):
        with open(self.filepath, 'r') as f:
            my_cars = json.load(f)
        return my_cars

    def save_bag(self, cars):
        with open(self.filepath, 'w') as f:
            json.dump(cars, f)

class Shop:
    def __init__(self, cars_stock, bag_stock):
        self.cars_stock = cars_stock
        self.bag_stock = bag_stock

    def choice_cars(self):
        choice = None
        while choice != '0':
            message = ""
            for i in enumerate(self.cars_stock.get_cars()['cars'], 1):
                tamplate = f'{i[0]}. model: {i[1]["model"]}, price: ${i[1]["price"]}'
                message += tamplate + '\n'
            message += "0 - Назад"
            print(message)
            choice = self.add_to_bag()
            print(choice)



    def add_to_bag(self):
        choice = input('Выберите номер авто: ')
        if choice != '0':
            cars = self.bag_stock.get_cars()
            result = ''
            try:
                cars['cars'].append(self.cars_stock.get_cars()['cars'][int(choice) - 1])
                self.bag_stock.save_bag(cars)
            except IndexError as e:
                result = 'Выберите авто из указанного списка!'
            except ValueError as e:
                result = 'Введите конкретное числовое значение!'
            return result
        return choice


    def show_bag(self):
        choice = None
        while choice != '0':
            total = 0
            count = 0
            cars = self.bag_stock.get_cars()
            for i in cars.get("cars", []):
                count += 1
                total += i["price"]
                tamplate = f'{count}. model: {i["model"]}, price: ${i["price"]}'
                print(tamplate)
            print(f'Общая стоимость: ${total}')
            print('''
            0 - Вернуться в меню
            ''')
            choice = self.del_bag()
            print(choice)


    def del_bag(self):
        choice = (input('Выберите авто для удаления: '))
        if choice != '0':
            bag = self.bag_stock.get_cars()
            result = ''
            try:
                bag.get("cars").pop(int(choice) - 1)
            except IndexError as e:
                result = 'Данного авто нет в вашей корзине!'
            except ValueError:
                result = 'Введите номер авто для удаления, если таковой имеется!'
            self.bag_stock.save_bag(bag)
            print('Авто успешно удалено!')
            return result
        return choice


def main_menu():
    choice = None
    cars_stock = Stock("my_cars.json")
    bag_stock = Stock("bag.json")
    shop = Shop(cars_stock=cars_stock, bag_stock=bag_stock)
    while choice != 0:
        print("""
        0 - Выход
        1 - Посмотреть товары/Добавить в корзину
        2 - Посмотреть корзину
        """)
        choice = int(input('Выберите действие: '))
        
        if choice == 1:
            shop.choice_cars()
        elif choice == 2:
            shop.show_bag()
        elif choice not in [0,1,2]:
            print('Неверный выбор! Попробуйте еще раз.')

    print('Пока')


def add_exception():
    try:
        main_menu()
    except ValueError as e:
        print('Введите конкретный пункт из меню!')
        main_menu()


add_exception()