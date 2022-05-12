
BAG = []
CLOTHES = [
    ('Dress', 250),
    ('Skirt', 120),
    ('Trousers', 85),
    ('Shorts', 70),
    ('Jumper', 100)
]


def format_products(clothes) -> str:
    id = 0
    result = '0 - Выход\n'
    for i in clothes:
        id += 1
        result += f'{id}.{i[0]} - rub {i[1]}' + "\n"
    return result + "Выберите товар: "


def show_BAG():
    total = 0
    result = ""
    for i in BAG:
        result += i[0] + '\n'
        total += i[1]

    result = result + f'{total}rub - Общая сумма покупок' + "\n"
    return result


def make_main_choice(choice):
    result = ""
    if choice == 1:
        result = add_products(CLOTHES)
    elif choice == 2:
        result = show_BAG()
    elif choice != 0:
        result = 'Неверный выбор'
    return result


def add_products(clothes):
    message = format_products(clothes)
    result = launch(add_product, input_message=message)
    return result


def add_product(choice):
    BAG.append(CLOTHES[choice - 1])
    return 'Товар успешно добавлен в корзину.'


def launch(func, input_message):
    choice = None
    while choice != 0:
        choice = int(input(input_message))
        message = func(choice)
        print(message)


def run():
    message = """
        0 - Выход
        1 - Посмотреть товары/Добавить в корзину
        2 - Посмотреть корзину
    """ + "\n" + "Выберите действие: "
    launch(make_main_choice, input_message=message)


run()