"""Программа для салона красоты (Лэшмейкера и бровиста).
Возможности:
- просмотреть все услуги
- добавить услугу в корзину
- посмотреть сумму выбранных услуг
"""

import json

def list_of_services():
    with open("app\list_services.json", encoding='utf-8') as file:
        data  = json.load(file)
    return data["list_of_services"]


def edited_list_of_services(data):
    result = ''
    for i in data:
        result += (f"{i['service_number']}. {i['name_of_services']} - {i['price_of_service']}р.\n")
    return result    
    

def basket_of_services():
    with open("app\services_basket.json", encoding='utf-8') as file:
        data  = json.load(file)
    return data["list_of_services"]


def summa(data):
    counter = 0
    for i in data:
       counter += i['price_of_service']
    return f'Сумма всех услуг = {counter}р.'   


def format_basket(data):
    return edited_list_of_services(data) + summa(data)


def adding_service():
    print(edited_list_of_services(list_of_services()))
    choice = int(input("Выберите услугу:"))
    services = list_of_services()
    basket = basket_of_services()
    basket.append(services[choice -1 ])
    basket = {"list_of_services":basket}
    with open("app\services_basket.json", "w") as file:
        json.dump(basket, file)
    return ("Услуга успешно добавлена")


def make_main_choice(choice):
    result = ""
    if choice == 1:
        articles = list_of_services()
        message = edited_list_of_services(articles)
        result = message
    elif choice == 2:
        result = adding_service()
    elif choice == 3:
        articles = basket_of_services()
        message = format_basket((articles))
        result = message
    elif choice != 4:
        result = 'Неверный выбор'
    return result


def menu():
    message = """
        1 - Посмотреть услуги
        2 - Выбор услуг
        3 - Посмотреть список и стоимость выбранных услуг
        4 - Выход
    """ + "\n"
    return message
    

def run() -> None:
    choice = None
    while choice != 4:
        print(menu())
        choice = int(input("Введите пункт меню: "))
        message = make_main_choice(choice)
        print(message)

run()