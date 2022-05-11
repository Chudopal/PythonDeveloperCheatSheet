import json

path_json = '../shop_invent.json'


def shoping(path) -> None:

    with open(path, 'r', encoding='utf8') as file:
        data = json.load(file)

    for product, price in data.items():
        print(product, "-", price)
    price = 0
    while True:
        product = input ("Какой товар? ")
        if product == "0":
            break;
        number = int(input("Количество штук? "))
        price = price+data[product]*number
    print('Сумма:', price)

shoping(path_json)