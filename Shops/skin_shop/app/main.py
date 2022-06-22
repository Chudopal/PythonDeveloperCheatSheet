# """5. Напишите программу магазина.
# Покупатели могут покупать какие-то продукты в магазине.

# Возможности покупателя:
# - посмотреть все товары и цены на них
# - выбрать товар
# - посмотреть сумму покупки(сумма цен выбранных товаров)
# Взаимодействие происходит через консоль.

# Товары храните просто в какой-нибудь из коллекций.
# Выбор товара - это ввод пользователем строки названия товара
# """

import json

products = [
    ("Rogozhka",100),
    ("Velour",200),
    ("Vicrovelour",300),
    ("Shenil",400),
]

order = []

def read_file(filename: str) -> dict:
    
    with open(filename) as file:
        data = json.load(file)
    return data


# № function 1
def get_all_products() -> list:
     data = read_file('Shops\skin_shop\\app\storage.json')
     id = 0
     result = ''
     for product in data.get('products'):
         print(product)
         id += 1
         #result += f'{id}.{product[0]} : {product[1]}$' + "\n"

     return result

# № function 2
def add_product(product_id: int) ->str:

     order.append(products[product_id - 1])
     result = f'Вы выбрали {products[product_id - 1][0]} стоимость {products[product_id - 1][1]}$' + "\n"
     return result 

# № function 3
def get_sum_price() -> str:
    sum = 0
    for order_item in order:
     sum += order_item[1]
    return sum 


def managment_func(num_func: int):
    result = ""
    if num_func == 1:
        result = get_all_products()
    elif num_func == 2:
        product_id = int(input(get_all_products() + 'Введите номер продукта: '))
        result = add_product(product_id)
    elif num_func == 3:
        result = f'Сумма покупки {get_sum_price()}$'
    else:
        result = 'Введены неверные значения'

    return result

def menu():
    menu = """
        0 - Выход
        1 - Посмотреть товары
        2 - Добавить в корзину
        3 - Посмотреть корзину
    """ + "\n" + "Выберите действие: "
    return menu


def run() -> None:
    choice = ""
    while choice != 'Выход':
        choice = int(input(menu()))
        message = managment_func(choice)
        print(message)

run()


   