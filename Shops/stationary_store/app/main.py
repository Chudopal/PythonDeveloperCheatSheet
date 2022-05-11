PRODUCTS = {
    'pencil':2, 
    'pen':3, 
    'felt_pen':3,
    'paper':5,
    'eraser':2, 
    'stickers':1
    }

SBAG = () 
BYE = 'Waiting for you again:)' 


def hello_username():
    name = input('Enter your name: ')
    print("Dear %s, happy to see u"%(name))

def get_menu():
    return(
        "-"*20 + "\n" +
        '1. Product catalog \n'
        '2. Order page \n'
        '3. Exit \n'
        )

def make_choice(shopping: int) -> None: 
    if shopping == 1:
        format_catalog()
    elif shopping == 2:
        make_order()
    elif shopping == 3:
        exit() 
    

def format_catalog():
    for product_name in PRODUCTS:
        print(product_name, '-', PRODUCTS[product_name])

def count_sbag_sum():
    SBAG = list(input('Please add a product name to sbag: ').split())
    final_sum=0
    for i in SBAG:
        final_sum += PRODUCTS.get(i)
    print('Final purchase cost is {}.Thank you!'.format(final_sum))


def make_order():
    format_catalog()
    count_sbag_sum()         

def exit():
    print(BYE)


def run():
    hello_username()
    shopping = None
    while shopping != 3:
        print(get_menu())
        shopping = int(input('Choose an item: '))
        make_choice(shopping)

run()