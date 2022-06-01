import json


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


class Console:
    

    def select_choose(self, choose: int) -> int:
        if choose > 4 or choose < 1: 
            choose = int(input("Данного действия не существует, попробуйте заново:"))
        else:
            self.menu()
            choose = int(input("Выберите действие:"))
        return choose


    def menu(self)->None: 
        massage = ("1. Товары и их цены\n" +
            "2. Выбрать товар\n" +
            "3. Посмотреть сумму покупки\n" +
            "4. Выход")
        print(massage)


class Seller():
    
    def massage_product_range(self, product_range: dict)->str: 
        tamplate = "{} стоит {}\n"
        result = "\n"
        for product_name, price in product_range.items():
            result += tamplate.format(product_name, price)
        return result


    def massage_purchase(self, list_purchase: dict, sum_purchases: int)->str:
        tamplate = "{} x {}, "
        result = "Ваши покупки "
        for product_name, number in list_purchase.items(): # можно сделать мапом
            result += tamplate.format(product_name, number["counter"])
        result += "на сумму " + str(sum_purchases)
        return result


    def sum_purchase(self, list_purchase: dict) -> int:
        result = 0
        for product_info in list_purchase.values():
            result += product_info["counter"] * product_info["price"]
        return result



class Buyer():

    
    def update_purchase(self, purchase : dict, list_product: dict) -> dict and str:
        price, name_product = self.choose_product(list_product)
        if price == None:
            massage = "Такого товара не существует!\n"
        else:   
            purchase = self.add_product(purchase, list_product, name_product, price)
            massage = "Товар добавлен!\n"
        return purchase, massage


    def add_product (self, purchase : dict, list_product: dict, name_product : str, price : int) -> dict:
        count = purchase.get(name_product)
        if count == None:
            purchase[name_product]= {"counter":1, "price":price}
        else:
            purchase[name_product]["counter"] += 1
        return purchase


    def choose_product(self, product_range: dict)->int: 
        name_product  = input("Введите название подуката:") 
        price = product_range.get(name_product)
        return price, name_product


class Shop(FileProcessing, Console, Seller, Buyer):
    

    def __init__(self, product_range: FileProcessing, purchase_product_range: FileProcessing) -> None:
        self. _product_range = product_range
        self._purchase_product_range = purchase_product_range
        self._choose = 1


    def main(self): 
        while self._choose != 4: 
            self._choose = self.select_choose(self._choose) 
            print(self.select_action(self._choose))
        

    def add_purchase(self) -> str:
        list_purchase = self._purchase_product_range.read()
        list_purchase, massage = self.update_purchase(self._purchase_product_range.read(), self._product_range.read())
        purchase_product_range.write(list_purchase)
        return massage


    def select_action(self, choose: int) -> str:
        massage = ""
        if choose == 1:
            massage = self.massage_product_range(self._product_range.read())
        elif choose == 2:
            massage = self.add_purchase()
        elif choose == 3:
            massage = self.massage_purchase(self._purchase_product_range.read(), 
                self.sum_purchase(self._purchase_product_range.read()))
        return massage


product_range = FileProcessing("app/rubiks_cube_product_range.json")
purchase_product_range = FileProcessing("app/purchase_range.json")
shop = Shop(product_range, purchase_product_range)
shop.main()




