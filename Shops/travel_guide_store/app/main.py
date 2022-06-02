import json
from typing import List, Dict

class With_File_Working():

    def __init__(self, path : str, name: str) -> None:
        self._path = path
        self.name = name
        

    def read_file(self) -> List:    
        with open(self.adress) as file:
            data = json.load(file).get(self.name)
        return data


    def write_file(adress, data) -> None:    
        with open(adress, "w") as file:
            json.dump(data, file, indent=4) 


def user_menu() -> str:                                        
    return ("Выберете действие: \n" + 
        "1.  Посмотреть список туров \n" + 
        "2.  Положить выбранный тур в корзину\n" + 
        "3.  Проверить сумму товаров в корзине\n" +  
        "4.  Закончить работу\n"  ) 

def provide_data(data: List[Dict])-> Dict:                                  
    result = []
    for id in data:
        id = list(id.values())
        result.append(id)
    return result 

def provide_file(data):                                                 
    return [
        {
            "id": id, 
            "price": price
            } 
            for id, price in data
            ]     

def get_whole_data() -> Dict[str, List]:
    data = With_File_Working.read_file("app\guide_offer.json", "catalog")
    return data                                    

def get_menu()-> List:                                                         
    data = get_whole_data()
    return provide_data(data)

def show_cart():                                                        
    data = get_whole_data()
    return data.get("shopping_cart")    

def format_catalog(catalog: any)-> str:                              
    return "\n".join([f" Тур - {guide_id} - стоит {price} BYN" for guide_id, price in catalog]) 

def add_cart(catalog):                                                     
    result = None
    guide = input("Напишите выбранный тур: ") 
    for item in catalog: 
        if item[0] == guide:
            result = item
            break
    return result    
    
def summ_guide(sum_list: List):                                         
    total_sum = 0
    result = "" 
    for item in sum_list:
        result += item[0] + "\n"
        total_sum += item[1]
        result += f"Сумма покупок в корзине составляет: {total_sum} BYN" + "\n"
    return result       

def show_menu():                                                   
    data = get_menu()
    message = format_catalog(data)
    return message
    
def choose_guide():                                                
    cart = add_cart(get_menu())
    data = get_whole_data()
    data["shopping_cart"] = provide_data(data["shopping_cart"])
    data["shopping_cart"].append(cart)
    data["shopping_cart"] = provide_file(data["shopping_cart"])
    With_File_Working.write_file(data, "app\guide_offer.json")
    return "Товар добавлен в корзину"

def check_cart():                                                  
    return summ_guide(provide_data(show_cart()))

def make_choice (choice) -> str: 
    result = "" 
    if choice == 1: 
        result = show_menu()  
    elif choice == 2: 
        result =choose_guide() 
    elif choice == 3:
        result= check_cart()
    elif choice ==4: 
        pass
    else: 
        return user_menu()   
    return result  

def save_make_choice(choice):
    result = ""

    try:
        result = make_choice(choice = int(choice))
    except ValueError:
        result = "Вводите только цифры!" 
    except FileNotFoundError:
        result = "В магазине нет товаров"+ '\n'    
    return result   

def run() -> None: 
    choice = None
    while choice  !="4":     
        print(user_menu()) 
        choice = input("Введите пункт меню: ")
        print(save_make_choice(choice = choice)) 
     
run()