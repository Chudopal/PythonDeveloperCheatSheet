"""Программа для салона красоты (Лэшмейкера и бровиста).
Возможности:
- просмотреть все услуги
- добавить услугу в корзину
"""

import json


def list_of_services():
    with open("app\list_services.json", encoding='utf-8') as file:
        result  = json.load(file)
        r = ''
        for i in result["list_of_services"]:
            r += (f"{i['service_number']}. {i['name_of_services']} - {i['price_of_service']}р.\n")
    return r
    

