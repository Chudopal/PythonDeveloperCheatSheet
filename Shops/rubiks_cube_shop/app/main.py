from itertools import product
import json

# PRODUCT_RANGE = {
#     "3x3": 1500,
#     "4x4": 1200,
#     "5x5": 1000,
#     "2x2": 700
# }



class FileProcessing():

    def __init__(self, path : str) -> None:
        self._path = path


    def read(self) -> list:
        with open(self._path) as file:
            result = json.load(file)
        return result

    
    def write(self, data : list) -> None:
        with open(self._path, "w") as file:
            json.dump(data, file)
        


def menu()->None: 
    massage = ("1. Товары и их цены\n" +
        "2. Выбрать товар\n" +
        "3. Посмотреть сумму покупки\n" +
        "4. Выход")
    print(massage)
   

def massage_product_range(product_range: dict)->str: 
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
        result += tamplate.format(product_name, number["counter"])
    result += "на сумму " + str(sum_purchases)
    return result


def add_purchase(purchase : dict, list_product: dict) -> dict:
    price, name_product = choose_product(list_product)
    if price == None:
        print("Такого товара не существует!") 
    else:   
        count = purchase.get(name_product) # вложенность слишком большая
    if count == None:
        purchase[name_product]= {"counter":1, "price":price}
    else:
        purchase[name_product]["counter"] += 1
    return purchase


def sum_purchase(list_purchase: dict) -> int:
    result = 0
    for product_info in list_purchase.values(): # можно сделать мапом
        result += product_info["counter"] * product_info["price"]
    return result


def main(): # слишком много логики, можно упростить
    product_rang = FileProcessing("app/rubiks_cube_product_range.json")
    purchase_product_range = FileProcessing("app/purchase_range.json")
    list_product = product_rang.read()
    sum_purchases = 0
    choose = 1
    while choose != 4: 
        if choose > 4 or choose < 1: 
            choose = int(input("Данного действия не существует, попробуйте заново:"))
        else:
            menu()
            choose = int(input("Выберите действие:"))
        if choose == 1:
            massage = massage_product_range(product_rang.read())
            print(massage)
        elif choose == 2:
            list_purchase = purchase_product_range.read()
            list_purchase = add_purchase(list_purchase, list_product)
            purchase_product_range.write(list_purchase)
        elif choose == 3:
            list_purchase = purchase_product_range.read()
            massage = massage_purchase(list_purchase, sum_purchase(list_purchase))
            print(massage)

main()

# shop = Shop()
# shop.main()


