CATALOG = {
"White tea": 2,
"Green tea": 3,
"Red tea": 1,
"Black tea": 4
}


ADD_CATALOG = []


def get_all_catalog():
    return CATALOG

def get_new_catalog():
    return ADD_CATALOG
 
def format():
    ...


def add_product(add):
    product_name = input("What do you want to buy? ") 
    for i in product_name: 
        add.append(product_name)
        return "Product added in bag"

        
    
def summa(sum_list):
    coast_list= [] 
    for x in ADD_CATALOG: 
        for item in CATALOG.keys(): 
            if x == item: 
                y = CATALOG[item] 
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
        result = add_product(ADD_CATALOG)
        # print(ADD_CATALOG)
    elif choice == 3:
        products = summa(ADD_CATALOG)
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