print('HelloWorld')
bag = []
cars = [('Merc', 100),('BMW', 1000000),('Audi', 50),('VW', 20),('Ford', 10)]

def add_products(list):
        id = 0
        print('0 - Выход')
        for i in list:
            id += 1
            print(f'{id}.{i[0]} - ${i[1]}')
        while True:
            choice = int(input('Выберите товар: '))
            if choice == 0:
                break
            else:
                bag.append(list[choice - 1])
                print('Товар успешно добавлен в корзину.')

def show_bag():
    total = 0
    for i in bag:
        print(i[0])
        total += i[1]
    print(f'{total}$ - Общая сумма покупок')

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
            add_products(cars)
        elif choice == 2:
            show_bag()
        else:
            print('Неверный выбор')

add_products(cars)