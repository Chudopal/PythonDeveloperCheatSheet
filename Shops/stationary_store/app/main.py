PRODUCTS = {
    'pencil':2, 
    'pen':3, 
    'felt_pen':3,
    'paper':5,
    'eraser':2, 
    'stickers':1
    }

SBAG = []
BYE = 'Waiting for you again:)' 


def print_hello_username():
    name = input('Enter your name: ')
    print("Dear %s, happy to see u"%(name))


def get_menu():
    return(
        "-"*20 + "\n" +
        '1. Product catalog \n'
        '2. Order page \n'
        '3. S-Bag \n'
        '4. Exit \n'
        )


def make_choice(shopping: int) -> None: 
    if shopping == 1:
        format_catalog()
    elif shopping == 2:
        make_order()
    elif shopping == 3:
        show_sbag()   
    elif shopping == 4:
        exit() 
    

def format_catalog():
    for product_name in PRODUCTS:
        print(product_name, '-', PRODUCTS[product_name])


def add_item():
    product = input('Please add a product name to sbag(one by one): ')
    SBAG.append(product)
    print('Products added to SBAG. To add more back to order page')


def make_order():
    format_catalog()
    add_item()  


def count_sbag_sum():
    final_sum=0
    for i in SBAG:
        final_sum += PRODUCTS.get(i)
    print('Final purchase cost is {}.Thank you!'.format(final_sum))


def show_sbag():
    print(*SBAG)
    count_sbag_sum()


def exit():
    print(BYE)


def run():
    print_hello_username()
    shopping = None
    while shopping != 4:
        print(get_menu())
        shopping = int(input('Choose an item: '))
        make_choice(shopping)


run()