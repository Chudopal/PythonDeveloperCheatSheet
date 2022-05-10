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


def username_greeting():
    name = input('Enter your name: ')
    print("Dear %s, happy to see u"%(name))

def menu():
    return(
        "-"*20 + "\n" +
        '1. Product catalog \n'
        '2. Order page \n'
        '3. Exit \n'
        )

def choice(shopping: int) -> None: 
    result = ''
    if shopping == 1:
        result = format_catalog()
    elif shopping == 2:
        result = order()
    elif shopping == 3:
        result = exit() 
    

def format_catalog():
    for product_name in PRODUCTS:
        print(product_name, '-', PRODUCTS[product_name])


def order():
    for product_name in PRODUCTS:
        print(product_name, '-', PRODUCTS[product_name])
    SBAG = list(map(str,input('Please add a product name to sbag: ').split())) 
    final_sum=0
    for i in SBAG:
        final_sum += PRODUCTS.get(i)
    print('Final purchase cost is {}.Thank you!'.format(final_sum))           

def exit():
    print(BYE)


def run():
    username_greeting()
    shopping = None
    while shopping != 3:
        print(menu())
        shopping = int(input('Choose an item: '))
        choice(shopping)

run()
