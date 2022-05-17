import json

def get_cars_from_file():
    with open('my_cars.json', 'r') as f:
        my_cars = json.load(f)
    return my_cars
        
        
def get_cars_bag():
    with open('bag.json', 'r') as f:
        bag = json.load(f)
    return bag


def choice_cars():
    choice = None
    while choice != 0:
        for i in enumerate(get_cars_from_file()['cars'], 1):
            tamplate = f'{i[0]}. model: {i[1]["model"]}, price: ${i[1]["price"]}'
            print(tamplate)
        print('0 - Назад')
        choice = add_to_bag()



def add_to_bag():
    choice = int(input('Выберите номер авто:'))
    if choice != 0:
        cars = get_cars_bag()
        cars['cars'].append(get_cars_from_file()['cars'][choice - 1])
        save_bag(cars)
    return choice


def save_bag(cars):
    with open('bag.json', 'w') as f:
        json.dump(cars, f)


def show_bag():
    choice = None
    while choice != 0:
        total = 0
        count = 0
        for i in get_cars_bag()['cars']:
            count += 1
            total += i["price"]
            tamplate = f'{count}. model: {i["model"]}, price: ${i["price"]}'
            print(tamplate)
        print(f'Общая стоимость: ${total}')
        print('''
        0 - Вернуться в меню
        ''')
        choice = del_bag()


def del_bag():
    choice = int(input('Выберите авто для удаления: '))
    if choice != 0:
        bag = get_cars_bag()
        bag.get("cars").pop(choice - 1)
        print('Авто успешно удалено!')
        save_bag(bag)
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
            choice_cars()
        elif choice == 2:
            show_bag()
        elif choice == 0:
            print('Пока')
        else:
            print('Неверный выбор')

main_menu()
