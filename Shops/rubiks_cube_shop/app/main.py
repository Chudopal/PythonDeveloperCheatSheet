import json
import psycopg2


class FileProcessing():

    def __init__(self, path : str) -> None:
        self._path = path

    def read(self) -> list:
        with open(self._path) as file:
            try:
                result = json.load(file)
            except:
                self.write([])
        return result

    def write(self, data : list) -> None:
        with open(self._path, "w") as file:
            json.dump(data, file)

    def insert_purchase(self, name , price)->None:
        purchase = self.read()
        purchase[name]= {"counter":1, "price":price}
        self.write(purchase)
        
    def update_purchase(self, name)->None:
        purchase = self.read()
        purchase[name]["counter"] += 1
        self.write(purchase)


class SQLProcessing():
    
    def __init__(self, dbname: str, user: str,
            password: str, host: str, port: int, name_tab: str) -> None:
        self._connection = psycopg2.connect(
            dbname = dbname,
            user = user,
            password=password,
            host= host,
            port = port)
        self._name_tab = name_tab
        self._cursor = self._connection.cursor()

    def read(self)->dict:
        self._cursor.execute("""
        SELECT * FROM {};
        """.format(self._name_tab))
        result = self._cursor.fetchall()
        if self._name_tab == "product":
            result = self.conv_product(result)
        elif self._name_tab == "purchase":
            result = self.conv_purchase(result)
        return result

    def insert_purchase(self, name , price)->None:
        self._cursor.execute("""
        INSERT INTO purchase(name, price, counter) VALUES('{}', {}, 1);
        """.format(name, price))
        self._connection.commit()


    def update_purchase(self, name)->None:
        self._cursor.execute("""
        UPDATE purchase SET counter =counter + 1 WHERE name = '{}';
        """.format(name))
        self._connection.commit()

    def conv_product(self, data: list)->dict:
        result = {}
        for product in data:
            result[product[0]] = product[1]
        return result

    def conv_purchase(self, data: list)->dict:
        result = {}
        for product in data:
            result[product[0]] = {"price":product[1], "counter":product[2]}
        return result


class Console:
    
    def select_choose(self, choose: int) -> int:
        if choose > 4 or choose < 1: 
            choose = self.check_input("?????????????? ???????????????? ???? ????????????????????, ???????????????????? ????????????:")
        else:
            self.menu()
            choose = self.check_input("???????????????? ????????????????:")
        return choose

    def check_input(self, massage: str)->int:
        try:
            choose = int(input(massage))
        except:
            choose = self.check_input("???????????????????? ?????? ??????:")
        return choose

    def menu(self)->None: 
        massage = ("1. ???????????? ?? ???? ????????\n" +
            "2. ?????????????? ??????????\n" +
            "3. ???????????????????? ?????????? ??????????????\n" +
            "4. ??????????")
        print(massage)


class Seller():
    
    def massage_product_range(self, product_range: dict)->str: 
        tamplate = "{} ?????????? {}\n"
        result = "\n"
        for product_name, price in product_range.items():
            result += tamplate.format(product_name, price)
        return result

    def massage_purchase(self, list_purchase: dict, sum_purchases: int)->str:
        tamplate = "{} x {}, "
        result = "???????? ?????????????? "
        for product_name, number in list_purchase.items(): # ?????????? ?????????????? ??????????
            result += tamplate.format(product_name, number["counter"])
        result += "???? ?????????? " + str(sum_purchases)
        return result

    def sum_purchase(self, list_purchase: dict) -> int:
        result = 0
        for product_info in list_purchase.values():
            result += product_info["counter"] * product_info["price"]
        return result


class Buyer():

    def update_purchase(self, purchase_product_range, product_range) -> str:
        purchase = purchase_product_range.read()
        list_product = product_range.read()
        price, name_product = self.choose_product(list_product)
        if price == None:
            massage = "???????????? ???????????? ???? ????????????????????!\n"
        else:   
            self.add_product(purchase_product_range, name_product, price)
            massage = "?????????? ????????????????!\n"
        return massage

    def add_product (self, purchase_product_range, name_product : str, price : int) -> dict:
        purchase = purchase_product_range.read()
        count = purchase.get(name_product)
        if count == None:
            purchase_product_range.insert_purchase(name_product, price)
        else:
            purchase_product_range.update_purchase(name_product)
        

    def choose_product(self, product_range: dict)->int: 
        name_product  = input("?????????????? ???????????????? ????????????????:") 
        price = product_range.get(name_product)
        return price, name_product


class Shop():
    
    def __init__(self, product_range: FileProcessing, purchase_product_range: FileProcessing,
                    console: Console, seller: Seller, buyer: Buyer) -> None:
        self. _product_range = product_range
        self._purchase_product_range = purchase_product_range
        self._console = console
        self._seller = seller
        self._buyer = buyer
        self._choose = 1

    def main(self): 
        while self._choose != 4: 
            self._choose = self._console.select_choose(self._choose) 
            print(self.select_action(self._choose))

    def select_action(self, choose: int) -> str:
        massage = ""
        if choose == 1:
            massage = self._seller.massage_product_range(self._product_range.read())
        elif choose == 2:
            massage = self._buyer.update_purchase(self._purchase_product_range, self._product_range)
        elif choose == 3:
            massage = self._seller.massage_purchase(self._purchase_product_range.read(), 
                self._seller.sum_purchase(self._purchase_product_range.read()))
        return massage

# product_range = FileProcessing("Shops/rubiks_cube_shop/app/rubiks_cube_product_range.json")# - ?????? ???????????? ?? ?????????????? 
# purchase_product_range = FileProcessing("Shops/rubiks_cube_shop/app/purchase_range.json")

product_range = SQLProcessing(
    dbname = 'shop',
    user = 'jiaxer',
    password = "dk2509fl",
    host = "localhost",
    port = 5432,
    name_tab = "product")

purchase_product_range= SQLProcessing(
    dbname = 'shop',
    user = 'jiaxer',
    password = "dk2509fl",
    host = "localhost",
    port = 5432,
    name_tab = "purchase")

console = Console()
seller = Seller()
buyer = Buyer()
shop = Shop(product_range, purchase_product_range, console, seller, buyer)
shop.main()




