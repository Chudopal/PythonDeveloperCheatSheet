from typing import List, Dict 
 
 
MENU_SHOP = {  
    "Ананас": 15, 
    "Яйца": 5, 
    "Молоко": 3, 
    "Хлеб": 3, 
    "Арбуз": 8 
} 
 
SHOPPING_CART = list()  
 
def get_menu()-> List: 
    return MENU_SHOP 
 
def make_choice()-> List: 
    return SHOPPING_CART 
 
 
def user_menu() -> str: 
    return ("Выберете действие в магазине: \n" + 
        "1.  Посмотреть список продуктов\n" + 
        "2.  Положить продукт в корзину\n" +  
        "3.  Проверить сумму заказа\n"  ) 
 
def show_menu(menushop: Dict)-> str:  
       return "\n".join([f"{goods_id}  {key1}" for goods_id, key1 in menushop.items()]) 
 
def start_shopping (fill_cart): 
    your_ch2 = input("Напишите выбранный продукт: ") 
    for x in your_ch2: 
        fill_cart.append(str(your_ch2)) 
        return "\n".join([f" {your_ch2} добавлен в Вашу корзину" for your_ch2 in fill_cart]) 
 
def check_cart(sum_list): 
    coast_list= [] 
    for x in SHOPPING_CART: 
        for item in MENU_SHOP.keys(): 
            if x == item: 
                y = MENU_SHOP[item] 
                coast_list.append(y)             
    sum_list = sum(coast_list) 
         
    return sum_list 
 
 
def choice_do (choice: int): 
    result = "" 
    if choice == 1: 
        output = get_menu() 
        message = show_menu(MENU_SHOP) 
        result = message  
    elif choice == 2: 
        output = make_choice() 
        message = start_shopping(SHOPPING_CART) 
        result = message 
    elif choice == 3: 
        message = check_cart(SHOPPING_CART)   
        result = message   
    return result     
         
 
def run() -> None: 
    choice = None 
    while choice == 1 or 2 or 3:     
        print(user_menu()) 
        choice = int(input("Введите пункт меню: ")) 
        message = choice_do(choice) 
        print(message) 
     
       
run()