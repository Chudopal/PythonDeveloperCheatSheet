import json

from typing import List, Dict
 
def read_file(adress, name) -> List:    #функция позволяет читать данные из файла
    with open(adress) as file:
        data = json.load(file)
    return data.get(name)

# def write_file(adress, data) -> None:     #функция записывает данные в файл
#     with open(adress, "w") as file:
#         json.dump(data, file)    

def provide_data(data: List)-> Dict:      #функция приводит данные к выводу в виде списка
    result = {}
    for guide in data:
        result[guide.get("id")] = guide.get("price")
    return result 

def provide_file(data: Dict, item: str):      #функция приводит данные файла к визуальному порядку (без скобок) 
    result = {"catalog":get_menu(), "shopping_cart":take_guide()}
    guides=[]   
    for guide_id, guide_price in data.items():
        guides.append({"id": guide_id, "price":guide_price})
    result[item]=guides
    return result     

def get_menu()-> List:              #функция вызывает каталог туров с  ценами
    data = read_file("app\guide_offer.json", "catalog")
    return provide_data(data)

def take_guide()-> List:             #функция вызывает корзину покупателя
    data = read_file("app\guide_offer.json", "shopping_cart")
    return provide_data(data) 

def user_menu() -> str:              #функция выводит меню действий
    return ("Выберете действие: \n" + 
        "1.  Посмотреть список туров \n" + 
        "2.  Положить выбранный тур в корзину\n" +  
        "3.  Проверить сумму заказа\n"  ) 
 
def format_catalog(guide_list: Dict)-> str:  #функция при выбора меню просмотра выводит списком красивым
    return "\n".join([f"{guide_id} cost {guide} BYN" for guide_id, guide in guide_list.items()]) 
 

def add_cart():
    with open("app\guide_offer.json") as file: 
        content = json.load(file)
        guide_id = input("Напишите выбранный маршрут: ")
        for guide_id, price_id in catalog.item():
            content.get("shopping_cart").append({"id": guide_id, "price": price_id}) # добавили новую информацию к существующей
    with open("app\guide_offer.json", "w") as file: 
        json.dump(content, file, indent=3)
#     
#     guide_content = get_menu().get(guide_id)
#     choise_guide = take_guide(guide_id)
#     data = provide_file(choise_guide, "shopping_cart")
#     write_file("app\guide_offer.json", data)


# def start_shopping (guide_id): #функция для добавления тура в корзину
#     #  your_ch2 = input("Напишите выбранный продукт: ")
#     # for x in your_ch2: 
#     #     fill_cart.append(str(your_ch2)) 
#     #     return "\n".join([f" {your_ch2} добавлен в Вашу корзину" for your_ch2 in fill_cart]) 
 
def make_choice (choice: int): 
    result = "" 
    if choice == 1: 
        guides = get_menu() 
        message = format_catalog(guides)
        result = message  
    elif choice == 2: 
        output = add_cart() 
        # message = start_shopping(shopping_cart) 
        # result = message 
    elif choice == 3:
        guides= take_guide() 
        message = format_catalog(guides)   
        result = message   
    return result     
         
 
def run() -> None: 
    choice = None 
    while choice == 1 or 2 or 3:     
        print(user_menu()) 
        choice = int(input("Введите пункт меню: ")) 
        message = make_choice(choice) 
        print(message) 
     
       
run()