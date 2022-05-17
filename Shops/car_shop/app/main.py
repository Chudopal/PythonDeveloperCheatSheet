import json

class Stock:
    def __init__(self, my_cars, bag, cars):
        self.my_cars = my_cars
        self.bag = bag
        self.cars = cars


    def get_cars_from_file():
        with open('my_cars.json', 'r') as f:
            my_cars = json.load(f)
        return my_cars
            
            
    def get_cars_bag():
        with open('bag.json', 'r') as f:
            bag = json.load(f)
        return bag


    def save_bag(cars):
        with open('bag.json', 'w') as f:
            json.dump(cars, f)

class Shop:
    def __init__(self, cars, total, bag):
        self.cars = cars
        self.total = total
        self.bad = bag


    def choice_cars():
        choice = None
        while choice != 0:
            message = ""
            for i in enumerate(Stock.get_cars_from_file()['cars'], 1):
                tamplate = f'{i[0]}. model: {i[1]["model"]}, price: ${i[1]["price"]}'
                message += tamplate + '\n'
            message += "0 - Назад"
            print(message)
            choice = Shop.add_to_bag()



    def add_to_bag():
        choice = int(input('Выберите номер авто:'))
        if choice != 0:
            cars = Stock.get_cars_bag()
            cars['cars'].append(Stock.get_cars_from_file()['cars'][choice - 1])
            Shop.save_bag(cars)
        return choice


    def show_bag():
        choice = None
        while choice != 0:
            total = 0
            count = 0
            for i in Stock.get_cars_bag()['cars']:
                count += 1
                total += i["price"]
                tamplate = f'{count}. model: {i["model"]}, price: ${i["price"]}'
                print(tamplate)
            print(f'Общая стоимость: ${total}')
            print('''
            0 - Вернуться в меню
            ''')
            choice = Shop.del_bag()


    def del_bag():
        choice = int(input('Выберите авто для удаления: '))
        if choice != 0:
            bag = Stock.get_cars_bag()
            bag.get("cars").pop(choice - 1)
            print('Авто успешно удалено!')
            Shop.save_bag(bag)
        return choice


def main_menu():
    choice = None
    while choice != 0:
        print("""
        0 - Выход
        1 - Посмотреть товары/Добавить в корзину
        2 - Посмотреть корзину
        """)
        choice = int(input('Выберите действие: '))
        
        if choice == 1:
            Shop.choice_cars()
        elif choice == 2:
            Shop.show_bag()
        elif choice not in [0,1,2]:
            print('Неверный выбор')

    print('Пока')

main_menu()
