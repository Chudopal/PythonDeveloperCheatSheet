import json


# ---------------- #
# STORAGES #
# ---------------- #

# at external files now

# ----------------- #
# DATA ACCESS LAYER #
# ----------------- #

def read_file(filename: str, path: str = '') -> dict:
    try:
        with open(path + filename) as file:
            data = json.load(file)
    except OSError:
        data = {}
    return data


def write_file(data: dict, filename: str, path: str = '') -> None:
    with open(path + filename, "w") as file:
        json.dump(data, file)


def get_pizzas_from_storage() -> dict[str: dict]:
    return read_file('pizzas.json')


def get_orders_from_storage() -> dict[str: dict]:
    return read_file('ordered_pizzas.json')


def update_orders(pizzas: dict) -> None:
    orders = read_file('ordered_pizzas.json')
    orders.update(pizzas)
    write_file(orders, 'ordered_pizzas.json')


# ----------------- #
# DOMAIN LAYER #
# ----------------- #


def get_product_price(pizza: str) -> any:
    pizzas = get_pizzas_from_storage()
    price = None
    for category in pizzas.values():
        price = category.get(pizza)
        if price:
            break
    return price


def get_pizza_from_purchases(pizza: str) -> dict:
    orders = get_orders_from_storage()
    default_order = {'amount': 0, 'price': 0}
    return orders.get(pizza, default_order)


def get_amount_of_pizza(pizza: dict[str: float]) -> float:
    return pizza.get('amount')


def get_price_of_pizza(pizza: dict[str: float]) -> float:
    return pizza.get('price')


def add_pizza_to_orders(pizza: str, amount: int, price: float):
    pizza_form_orders = get_pizza_from_purchases(pizza)
    new_amount = get_amount_of_pizza(pizza_form_orders) + amount
    new_price = get_price_of_pizza(pizza_form_orders) + price
    update_orders({pizza: {'price': new_price, 'amount': new_amount}})


def get_orders() -> list:
    orders = get_orders_from_storage()
    return [
        [
            pizza,
            amount_price.get('amount'),
            amount_price.get('price')
        ]
        for pizza, amount_price in orders.items()
    ]


def count_sum_of_orders() -> float:
    orders = get_orders_from_storage()
    total_price = 0
    for amount_price in orders.values():
        total_price += amount_price.get('price')
    return total_price


# ----------------- #
# INTERFACE LAYER #
# ----------------- #

def menu_view() -> str:
    return '-' * 30 + '\nPlease choose an action:\n' \
           '1. List of pizzas\n' \
           '2. Order pizza\n' \
           '3. Show order\n' \
           '4. Clear orders\n' \
           '5. Quit program'


def get_error_message(error: str) -> str:
    errors = {
        'action_error': 'You choose wrong action. Try again',
        'no_pizza_error': 'We don`t have that pizza, please try again',
        'no_orders_error': 'You haven`t order any pizza yet'
    }
    return errors.get(error)


def input_messages(key: str) -> str:
    messages = {
        "action": ">>> ",
        "make_order": "What pizza would you like to order? (pizza [amount]): "
    }
    return messages.get(key)


def format_pizzas_list(pizzas_list: dict[str: dict]) -> str:
    template = '- {product} {price}\n'
    result = '\nToday on sale:\n'
    for category, pizzas in pizzas_list.items():
        result += category + '\n'
        for product, price in pizzas.items():
            result += template.format(product=product, price=price)
    return result


def format_orders_list(orders_list: list[list[str, str, str]], total_sum: float) -> str:
    template = '{pizza} x {amount}: {price:.2f}\n'
    result = '\nYour order:\n'
    for pizza in orders_list:
        result += template.format(pizza=pizza[0],
                                  amount=pizza[1],
                                  price=pizza[2])
    result += f'\nTOTAL SUM: {total_sum:.2f}'
    return result


def check_orders(orders: list, total_sum: float) -> str:
    if orders:
        result = format_orders_list(orders, total_sum)
    else:
        result = get_error_message('no_orders_error')

    return result


def check_pizza(pizza: str, amount: int) -> str:
    pizza_price = get_product_price(pizza)
    if pizza_price:
        add_pizza_to_orders(pizza, amount, pizza_price)
        result = f'{pizza} pizza added to your order'
    else:
        result = get_error_message('no_pizza_error')

    return result


def print_output(*output_items: str):
    for item in output_items:
        print(item, sep="")


def receive_input(input_phrase: str) -> str:
    return input(input_phrase)


def validate_user_action(raw_user_action: str) -> int:
    try:
        user_action = int(raw_user_action)
    except ValueError:
        user_action = 0
    return user_action


def validate_order(order: list[str]) -> dict:
    quantity = 1
    if order[-1].isdigit():
        quantity = int(order[-1])
        pizza = ' '.join(order[:-1])
    else:
        pizza = ' '.join(order)

    return {'pizza': pizza, 'quantity': quantity}


def validate_user_input(raw_user_input: str) -> dict:
    user_input = raw_user_input.strip().upper().split(" ")
    return validate_order(user_input)


# ----------------- #
# CONTROLLER LAYER #
# ----------------- #


def menu_input_controller() -> int:
    raw_user_input = receive_input(input_messages('action'))
    return validate_user_action(raw_user_input)


def show_error_message(error: str = 'action_error'):
    error_message = get_error_message(error)
    print_output(error_message)


def show_all_pizzas_controller():
    pizzas = get_pizzas_from_storage()
    result = format_pizzas_list(pizzas)
    print_output(result)


def order_pizza_controller():
    raw_user_input = receive_input(input_messages('make_order'))
    user_input = validate_user_input(raw_user_input)
    order = check_pizza(user_input.get('pizza'), user_input.get('quantity'))
    print_output(order)


def show_orders_controller():
    orders = get_orders()
    total_sum = count_sum_of_orders()
    result = check_orders(orders, total_sum)
    print_output(result)


def clear_orders_controller():
    pass


ACTIONS = {
    1: show_all_pizzas_controller,
    2: order_pizza_controller,
    3: show_orders_controller,
    4: clear_orders_controller,
    5: quit
}


def run_app():
    while True:
        print_output(menu_view())
        action = menu_input_controller()
        ACTIONS.get(action, show_error_message)()


if __name__ == '__main__':
    run_app()
