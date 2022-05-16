BYE = 'Waiting for you again:)' 

import json

def write_file(data, filename):
    with open(filename, "w") as file:
        json.dump(data, file)


def read_file(filename):
    with open(filename) as file:
       data = json.load(file)
    return data


def add_info_file(filename, product):
    data = read_file(filename)
    data.append(product) 
    write_file(data, filename)


def clean_file(filename):
    write_file([], "app/sbag.json")


def format_catalog_dict(filename):
    data = read_file(filename)
    for key, value in data.items():
        print(key, ':', value, sep='')


def format_catalog_list(filename):
    data = read_file(filename)
    for i in data:
        print(i, sep='')


def print_hello_username():
    name = input('Enter your name: ')
    print("Dear %s, happy to see u"%(name))


def get_menu():
    return(
        "-"*20 + "\n" +
        '1. Product catalog \n'
        '2. Order page \n'
        '3. S-Bag \n'
        '4. Clean S-Bag \n'
        '5. Exit \n'
        )


def make_choice(shopping: int) -> None: 
    if shopping == 1:
        format_catalog_dict("app/products.json")
    elif shopping == 2:
        make_order()
    elif shopping == 3:
        show_sbag()   
    elif shopping == 4: 
        clean_file("app/sbag.json")
    elif shopping == 5:
        exit() 


def add_item():
    product = input('Please add a product name to sbag(one by one): ')
    add_info_file("app/sbag.json", product)
    print('Product added to SBAG. To add more back to order page')


def make_order():
    read_file("app/products.json")
    add_item()  


def count_sbag_sum():
    final_sum=0
    for i in read_file("app/sbag.json"):
        final_sum += read_file("app/products.json").get(i)
    print('Final purchase cost is {}.Thank you!'.format(final_sum))


def show_sbag():
    format_catalog_list("app/sbag.json")
    count_sbag_sum()


def exit():
    print(BYE)


def run():
    print_hello_username()
    shopping = None
    while shopping != 5:
        print(get_menu())
        shopping = int(input('Choose an item: '))
        make_choice(shopping)


run()