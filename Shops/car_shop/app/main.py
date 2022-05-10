import json


with open('my_cars.json', 'r') as f:
    my_cars = json.load(f)
    

with open('bag.json', 'r') as f:
    bag = json.load(f)


def choice_cars():
    while True:
        count = 0
        for i in my_cars['cars']:
            count += 1
            tamplate = f'{count}. model: {i["model"]}, price: ${i["price"]}'
            print(tamplate)
        print('0 - Назад')
        choice = add_to_bag()
        if choice == 0:
            break


def add_to_bag():
    choice = int(input('Выберите номер авто:'))
    if choice != 0:     
        bag['cars'].append(my_cars['cars'][choice - 1])
        save_bag()
    return choice


def save_bag():
    with open('bag.json', 'w') as f:
        json.dump(bag, f)


def show_bag():
    while True:
        total = 0
        count = 0
        for i in bag['cars']:
            count += 1
            total += i["price"]
            tamplate = f'{count}. model: {i["model"]}, price: ${i["price"]}'
            print(tamplate)
        print(f'Общая стоимость: ${total}')
        print('''
        0 - Вернуться в меню
        ''')
        choice = del_bag()
        if choice == 0:
            break


def del_bag():
    choice = int(input('Выберите авто для удаления: '))
    if choice != 0:
        del bag['cars'][choice - 1]
        print('Авто успешно удалено!')
        save_bag()
    return choice


def mine_menu():
    while True:
        print("""
        0 - Выход
        1 - Посмотреть товары/Добавить в корзину
        2 - Посмотреть корзину
        """)
        choice = int(input('Выберите действие: '))
        if choice == 0:
            break
        elif choice == 1:
            choice_cars()
        elif choice == 2:
            show_bag()
        else:
            print('Неверный выбор')

mine_menu()
