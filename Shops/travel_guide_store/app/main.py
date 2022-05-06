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
from typing import List, Dict 
 
 
menu_Shop = {  #меню магазина с ценами 
    "Ананас": 15, 
    "Яйца": 5, 
    "Молоко": 3, 
    "Хлеб": 3, 
    "Арбуз": 8 
} 
 
shopping_cart = list() #корзина покупателя 
 
def get_menu()-> List: 
    return menu_Shop 
 
def make_choice()-> List: 
    return shopping_cart 
 
 
def user_menu() -> str: # доступные действия покупателя 
    return ("Выберете действие в магазине: \n" + 
        "1.  Посмотреть список продуктов\n" + 
        "2.  Положить продукт в корзину\n" +  
        "3.  Проверить сумму заказа\n"  ) 
 
def show_menu(menushop: Dict)-> str: # номер меню 1 - показать список продуктов 
    # key1 = menu_Shop.values() 
    # goods_id = menu_Shop.keys() 
    return "\n".join([f"{goods_id}  {key1}" for goods_id, key1 in menushop.items()]) 
 
def start_shopping (fill_cart): #номер меню 2 - положить продукт в корзину 
    your_ch2 = input("Напишите выбранный продукт: ") 
    for x in your_ch2: 
        fill_cart.append(str(your_ch2)) 
        return "\n".join([f" {your_ch2} добавлен в Вашу корзину" for your_ch2 in fill_cart]) 
 
def check_cart(sum_list): #номер меню 3 - показать сумму заказа 
    coast_list= [] 
    for x in shopping_cart: 
        for item in menu_Shop.keys(): 
            if x == item: 
                y = menu_Shop[item] 
                coast_list.append(y)             
    sum_list = sum(coast_list) 
         
    return sum_list 
 
 
def choice_do (choice: int): 
    result = "" 
    if choice == 1: 
        vyvod = get_menu() 
        messagi = show_menu(menu_Shop) 
        result = messagi  
    elif choice == 2: 
        vyvod = make_choice() 
        messagi = start_shopping(shopping_cart) 
        result = messagi 
    elif choice == 3: 
        messagi = check_cart(shopping_cart)   
        result = messagi   
    return result     
         
 
def run() -> None: 
    choice = None 
    while choice == 1 or 2 or 3:     
        print(user_menu()) 
        choice = int(input("Введите пункт меню: ")) 
        messagi = choice_do(choice) 
        print(messagi) 
     
 
         
 
run()