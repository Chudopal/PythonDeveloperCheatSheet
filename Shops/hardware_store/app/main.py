def shoping():

    price_list = {"рис": 5, "яйца": 4, "леденец": 3}
    for product, price in price_list.items():
        print(product, "-", price)
    price = 0
    while True:
        product = input ("Какой товар? ")
        if product == "0":
            break;
        number = int(input("Количество штук? "))
        price = price+price_list[product]*number
    print('Сумма:', price)

shoping()