"""Программа для салона красоты (Лэшмейкера и бровиста).
Возможности:
- просмотреть все услуги
- добавить услугу в корзину
- посмотреть сумму выбранных услуг
"""

import json

# знаю что комменты нельзя. но мы же учимся:)

# функция которая показывает список услуг по ключу

def list_of_services():
    with open("app\list_services.json", encoding='utf-8') as file:
        data  = json.load(file)
    return data["list_of_services"]

# функция которая приводит и показывает список услуг в красивом виде

def edited_list_of_services(data):
    result = ''
    for i in data:
        result += (f"{i['service_number']}. {i['name_of_services']} - {i['price_of_service']}р.\n")
    return result
# print(edited_list_of_services(list_of_services()))

# функция которая показывает выбранные услуги и их стоимость

def basket_of_services():
    with open("app\services_basket.json", encoding='utf-8') as file:
        result  = json.load(file)
        r = ''
        counter = 0
        for i in result["list_of_services"]:
            counter += i['price_of_service']
            r += (f"{i['service_number']}. {i['name_of_services']} - {i['price_of_service']}р.\n")
    return r + f'Итого: {counter}'


# функция выбора услуг 

def adding_service():
    ...


# функция навигатор по меню

def make_main_choice(choice):
    result = ""
    if choice == 1:
        result = list_of_services()
    elif choice == 2:
        result = adding_service()
    elif choice == 3:
        result = basket_of_services()
    elif choice != 4:
        result = 'Неверный выбор'
    return result



# функция первого собщения меню

def menu():
    message = """
        1 - Посмотреть услуги
        2 - Выбор услуг
        3 - Посмотреть список выбранных услуг
        4 - Выход
    """ + "\n" + "Выберите действие: "
    return int(input(message))

