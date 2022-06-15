BAG = []
Products = [
    ("Aravia care set", 20),
    ("Filorga care set", 40),
    ("Payot care set", 205),
    ("Decleor care set", 50),
    ("Clinique care set", 250),
    ("Cellcosmet care set", 60),
    ("Eldan care set", 55),
    ("Janssen Cosmetics care set", 350),
    ("Biodroga care set", 120),
    ("Klapp care set", 145),
    ("Gerard's care set", 290),
]


def format_products(Products) -> str:
    id = 0
    result = '0 - Выход\n'
    for i in Products:
        id += 1
        result += f'{id}.{i[0]} - ${i[1]}' + "\n"
    return result + "Выберите товар: "


def show_BAG():
    total = 0
    result = ""
    for i in BAG:
        result += i[0] + '\n'
        total += i[1]

    result = result + f'{total}$ - Общая сумма покупок' + "\n"
    return result


def make_main_choice(choice):
    result = ""
    if choice == 1:
        result = show_products(Products)
    elif choice == 2:
        result = add_products(Products)
    elif choice == 3:
        result = show_BAG()   
    elif choice != 0:
        result = 'Неверный выбор'
    return result


def add_products(Products):
    message = format_products(Products)
    result = launch(add_product, input_message=message)
    return result


def add_product(choice):
    BAG.append(Products[choice - 1])
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
        1 - Посмотреть каталог
        2 - Добавить в корзину
        3 - Проверить корзину
    """ + "\n" + "Выберите действие: "
    launch(make_main_choice, input_message=message)


run()