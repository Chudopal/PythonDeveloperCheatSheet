import json

from typing import List, Dict

SHOPPING_RESULT = []
COAST_LIST= []
DICT = {}

def user_menu() -> str:              
    return ("Выберете действие: \n" + 
        "1.  Посмотреть список туров \n" + 
        "2.  Положить выбранный тур в корзину\n" + 
        "3.  Проверить сумму товаров в корзине\n" +  
        "4.  Проверить корзину\n" +
        "5.  Закончить работу\n"  ) 

def read_file(adress, name) -> List:    
    with open(adress) as file:
        data = json.load(file)
    return data.get(name)

def read_cart(adress) -> List:   
    with open(adress) as file:
        data = json.load(file)
    return data

def write_file(adress, data) -> None:    
    with open(adress, "w") as file:
        json.dump(data, file)    

def provide_data(data: List)-> Dict:      
    result = {}
    for guide in data:
        result[guide.get("id")] = guide.get("price")
    return result 

def provide_file(data: Dict, item: str):     
    result = {"catalog":get_menu()}
    items=[]   
    for guide_id, guide_price in data.items():
       items.append({"id": guide_id, "price":guide_price})
    result[item]=items
    return result     

def get_menu()-> List:              
    data = read_file("app\guide_offer.json", "catalog")
    return provide_data(data)

def take_guide()-> List:             
    data = read_file("app\shopping_cart.json", "cart")
    return data 

def format_catalog(guide_list: Dict)-> str:  
    return "\n".join([f"{guide_id} cost {guide} BYN" for guide_id, guide in guide_list.items()]) 

def format_cart(cart_list: Dict): 
    return "\n".join([f"Your choice guide: {guide_id} cost {guide} BYN and added in shopping_cart" for guide_id, guide in cart_list.items()])

def add_cart(choice_id: str):
    cart = get_menu()
    part = format_catalog(cart)
    guide = input("Напишите выбранный тур: ") 
    for item in guide: 
        choice_id.append(str(guide)) 
        return "\n".join([f" Тур - {guide} - добавлен в Вашу корзину" for guide in choice_id]) 
    
  
def summ_guide(sum_list):
    catalog = get_menu() 
    # coast_list= [] 
    for part in SHOPPING_RESULT: 
        for item in catalog.keys(): 
            if part == item: 
                price = catalog[item] 
                COAST_LIST.append(price)             
    sum_list = sum(COAST_LIST) 
    return "\n". join([f"Сумма покупок в корзине составляет: {sum_list} BYN"])    

def show_cart():
    list1 = SHOPPING_RESULT
    list2 = COAST_LIST
    for item in range(0, len(list1)):
        DICT[list1[item]] = list2[item]
        write_file("app\shopping_cart.json", DICT)
    

def make_choice (choice: int): 
    result = "" 
    if choice == 1: 
        guides = get_menu()
        message = format_catalog(guides)
        result = message  
    elif choice == 2: 
        result =add_cart(SHOPPING_RESULT) 
    elif choice == 3:
        guides= summ_guide(SHOPPING_RESULT) 
        result = guides 
        
    elif choice == 4:
        guides = show_cart()
        message = read_cart("app\shopping_cart.json")
        result = message
    elif choice ==5: 
        pass
       
    return result     
         

def run() -> None: 
    choice = None
    while choice  !=5:     
        print(user_menu()) 
        choice = int(input("Введите пункт меню: ")) 
        message = make_choice(choice) 
        print(message) 
     
run()