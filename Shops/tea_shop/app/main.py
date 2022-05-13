import json



def get_all_catalog():
    data = read_file("app\catalog.json", "catalog")
    return data
    


def read_file(path, name):
    with open(path) as file:
        data = json.load(file)
    return data.get(name)


def write_file(path, data):
    with open(path, "w") as file:
        data = json.dump(data, file)


def get_new_catalog():
    data = read_file("app\catalog.json", "add_catalog")
    return data
 
 
def format():
    ...


def add_product(add):
    product_name = input("What do you want to buy? ") 
    for i in product_name: 
        add.append(product_name)
        return "Product added in bag"

        
    
def summa(sum_list):
    coast_list= [] 
    for x in get_new_catalog: 
        for item in get_all_catalog.keys(): 
            if x == item: 
                y = get_all_catalog[item] 
                coast_list.append(y) 


                sum_list = sum(coast_list) 

    return sum_list 


def menu():
    return(
        "*"*50 + "\n" +
        "1. Viewing catalog\n" +
        "2. Add product\n" + 
        "3. Calculate the amount"
    )


def make_choice(choice: int): 
    result = ""
    products= ""
    if choice == 1:
        products = get_all_catalog() 
        result = products
    elif choice == 2:
        product =  get_new_catalog
        result = add_product(get_new_catalog())
        # print(ADD_CATALOG)
    elif choice == 3:
        products = summa(get_new_catalog())
        result = products
    return result


def run():
    choice = None 
    while choice != 4:
        print(menu())
        choice = int(input("Input number: ")) 
        message = make_choice(choice) 
        print(message)


run()