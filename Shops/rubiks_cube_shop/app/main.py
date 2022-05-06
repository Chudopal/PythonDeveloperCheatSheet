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


"""
Что хорошо:
- хорошо сделано переиспользование менюшки
- классно, что добавил возможность выхода
- классно, что сделал аннотации

Что стоило бы исправить:
- отделить принты и инпуты от бизнес-логики
- странное добавление продуктов, с таким
    подходом будет сложно добавлять новые
    фичи в программу. Лучше сделай отдельную
    структуру в которой будешь хранить покупки
- желательно, чтобы программа запускалась вызовом
    одной функции, типа main()
"""

PRODUCT_RANGE = {
    "Apple": 1500,
    "Samsung": 1200,
    "HONOR": 1000,
    "Nokia": 700
}


def menu()->None: 
    massage = ("1. Товары и их цены\n" +
        "2. Выбрать товар\n" +
        "3. Посмотреть сумму покупки\n" +
        "4. Выход")
    print(massage)
   



def massage_product_range(product_range: dict)->str: # логика высчитывания и подстановка в темплейт - это разное
    tamplate = "{} стоит {}\n"
    result = "\n"
    for product_name, price in product_range.items():
        result += tamplate.format(product_name, price)
    return result


def choose_product(product_range: dict)->int: 
    name_product  = input("Введите название подуката:") 
    price = product_range.get(name_product)
    return price, name_product


def massage_purchase(list_purchase: dict, sum_purchases: int)->str:
    tamplate = "{} x {}, "
    result = "Ваши покупки "
    for product_name, number in list_purchase.items(): # можно сделать мапом
        result += tamplate.format(product_name, number)
    result += "на сумму " + str(sum_purchases)
    return result


def main(): # слишком много логики, можно упростить
    sum_purchases = 0
    list_purchase = {}
    choose = 1
    while choose != 4: 
        if choose > 4 or choose < 1: 
            choose = int(input("Данного действия не существует, попробуйте заново:"))
        else:
            menu()
            choose = int(input("Выберите действие:"))
        if choose == 1:
            massage = massage_product_range(PRODUCT_RANGE)
            print(massage)
        elif choose == 2:
            price, name_product = choose_product(PRODUCT_RANGE)
            if price == None:
                print("Такого товара не существует!") 
            else: # выглядит как часть логики, которую можно вынести в функцию
                sum_purchases += price 
                count = list_purchase.get(name_product) # вложенность слишком большая
                if count == None:
                    list_purchase[name_product] = 1
                else:
                    list_purchase[name_product] += 1
        elif choose == 3:
            massage = massage_purchase(list_purchase, sum_purchases)
            print(massage)


main()

