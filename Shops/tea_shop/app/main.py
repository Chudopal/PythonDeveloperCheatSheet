import json


add_catalog = []


def read_file(path, name):
    with open(path) as file:
        data = json.load(file)
    return data.get(name)


def write_file(path, data):
    with open(path, "w") as file:
        data = json.dump(data, file)


def format_file(data):  
    result = {}
    for products in data:
        result[products.get("product_name")] = products.get("price")
    return result


def get_all_catalog():
    data = read_file("app\catalog.json", "catalog")
    return data


def get_new_catalog(add_catalog):
    data = write_file("app\Add_catalog.json", add_catalog)
    
 
def format(product_list):
    return "\n".join([
        f"{product_name} costs {price} BYN" for product_name, price in product_list.items()
    ])


def add_product(product_name):
    catalog = get_all_catalog()
    for product in catalog:
        item_price = product["price"]
        item_product = product["product_name"]
        if product_name == item_product:
            result = {item_product: item_price}
            add_catalog.append(result)
            return "Product added in bag"
        
    
def summa():
    coast_list= [] 
    for product in add_catalog:
        result = list(product.values())
        for product in result:
            coast_list.append(product)
    total_sum = sum(coast_list)
    return total_sum
   

def menu():
    return(
        "*"*50 + "\n" +
        "1. Viewing catalog\n" +
        "2. Add product\n" + 
        "3. Calculate the amount\n" +
        "4. Exit"
    )


def make_choice(choice: int): 
    result = ""
    if choice == 1:
        product = format_file(get_all_catalog())
        message = format(product)
        result = message
    elif choice == 2:
        product_name = input("What do you want to buy? ") 
        result = add_product(product_name)
        # print(add_catalog)
    elif choice == 3:
        result = summa()
    return result


def run():
    choice = None 
    while choice != 4:
        print(menu())
        choice = int(input("*"*50 + "\n" +"Input number: ")) 
        message = make_choice(choice) 
        print(message)


run()