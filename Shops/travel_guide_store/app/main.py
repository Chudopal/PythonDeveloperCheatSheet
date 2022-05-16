import json

from typing import List, Dict

SHOPPING_RESULT = []

def user_menu() -> str:              
    return ("Выберете действие: \n" + 
        "1.  Посмотреть список туров \n" + 
        "2.  Положить выбранный тур в корзину\n" +  
        "3.  Проверить корзину\n" +
        "4.  Проверить сумму товаров в корзине\n" +  
        "5.  Закончить работу\n"  ) 

def read_file(adress, name) -> List:    #функция позволяет читать данные из файла
    with open(adress) as file:
        data = json.load(file)
    return data.get(name)

def write_file(adress, data) -> None:     #функция записывает данные в файл
    with open(adress, "w") as file:
        json.dump(data, file)    

def provide_data(data: List)-> Dict:      #функция приводит данные к выводу в виде списка
    result = {}
    for guide in data:
        result[guide.get("id")] = guide.get("price")
    return result 

def provide_file(data: Dict, item: str):      #функция приводит данные файла к визуальному порядку (без скобок) 
    result = {"catalog":get_menu()}
    items=[]   
    for guide_id, guide_price in data.items():
       items.append({"id": guide_id, "price":guide_price})
    result[item]=items
    return result     

def get_menu()-> List:              #функция вызывает каталог туров с  ценами
    data = read_file("app\guide_offer.json", "catalog")
    return provide_data(data)

def take_guide()-> List:             #функция вызывает корзину покупателя
    data = read_file("app\shopping_cart.json", "offer_sum")
    return data 

def format_catalog(guide_list: Dict)-> str:  #функция при выбора меню просмотра выводит списком красивым
    return "\n".join([f"{guide_id} cost {guide} BYN" for guide_id, guide in guide_list.items()]) 

def format_cart(cart_list: Dict): #приводит в порядок корзину покупателя
    return "\n".join([f"Your choice guide: {guide_id} cost {guide} BYN and added in shopping_cart" for guide_id, guide in cart_list.items()])

def add_cart(choice_id: str):
    cart = get_menu(format_catalog())
    for items in cart:
        item_cost = items["price"]
        item_id = items["id"]
        if choice_id == item_id:
            result = {item_id: item_cost}
            SHOPPING_RESULT.append(result) 
    cart = write_file("app\shopping_cart.json", SHOPPING_RESULT)   
  
    
        
def make_choice (choice: int): 
    result = "" 
    if choice == 1: 
        guides = get_menu()
        message = format_catalog(guides)
        result = message  
    elif choice == 2: 
        choice_id= input("Enter your choice, please: ") 
        result =add_cart(choice_id) 
        
    elif choice == 3:
        guides= take_guide() 
        message = format_catalog(guides)   
        result = message  
    elif choice == 4: 
        return result     
         
 
def run() -> None: 
    choice = None
    while choice  !=5:     
        print(user_menu()) 
        choice = int(input("Введите пункт меню: ")) 
        message = make_choice(choice) 
        print(message) 
     
       
run()