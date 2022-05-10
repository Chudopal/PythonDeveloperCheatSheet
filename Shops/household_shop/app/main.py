import json

BUY_PRODUCTS = dict()

def read_file(path, name):
    with open(path, encoding='utf-8') as file:
        data = json.load(file)
    return data.get(name)


def write_file(path, data):
    with open(path, 'w', encoding='utf-8') as file:
        json.dump(data, file)


def adaptor(data: list) -> dict:
    return {article.get('id'): article.get('price') for article in data}


def file_adaptor(data: dict) -> list:
    return [{'id': product_id, 'quantity': product_cnt} for product_id, product_cnt in data.items()]


def get_products_storage_from_list() -> dict:
    raw_data = read_file('storage.json', 'products')
    return adaptor(raw_data)


def get_users_prod_storage_from_dict() -> dict:
    return BUY_PRODUCTS


def update_product_from_dict(buy_dict: dict) -> None:
    BUY_PRODUCTS.update(buy_dict)


def add_buy_products(buy_dict: dict, add_func: callable):
    add_func(buy_dict)


def format_items(
        actions: dict,
        sep: str = ". ",
        sep_item: str = ";\n",
        end: str = ".\n"
) -> str:
    return f"{sep_item}".join([
        "{}{}{}".format(
            number, sep, action
        ) for number, action in actions.items()
    ]) + end


def get_menu_items() -> dict[int, str]:
    return {
        1: 'Список продуктов',
        2: 'Выбор продукта',
        3: 'Просмотреть корзину',
        4: 'Посчитать сумму',
        0: 'Exit',
    }


def get_buy_form() -> dict:
    return {
        "name": "Введите наименование товара: ",
        "quantity": "Введите кол-во товара: ",
    }


def get_phrase(key: str) -> dict[str, str]:
    phrases = {
        "choice": "Введите номер пункта меню: ",
        "continue": "Чтобы продолжить нажмите Enter.",
    }
    return {key: phrases.get(key)}


def validate_buy_product(buy_product: dict) -> dict:
    return {
        buy_product.get('name').capitalize(): int(buy_product.get('quantity', 1)),
    }


def validate_user_choice(choice: dict) -> dict:
    return {
        "choice": int(choice.get("choice"))
    }


def validate_product_list(product_list: dict) -> str:
    if not product_list:
        result = 'В магазине вообще голяк:(\n'
    else:
        result = format_items(product_list, sep=' - ', sep_item='р., ', end='р.\n')

    return result


def validate_buy_list(buy_list: dict) -> str:
    if not buy_list:
        result = 'Ваша корзина пуста\n'
    else:
        result = format_items(buy_list, sep=' - ', sep_item='шт., ', end='шт.\n')

    return result

def execute_console_output(*output_list: str) -> None:
    for output in output_list:
        print(output, end="", sep="")


def execute_console_input(**input_items: dict) -> any:
    return {
        key: input(form)
        for key, form in input_items.items()
    }


def get_sum_amt(buy_products: dict, product_list: dict) -> str:
    result_amt = int()
    for product_name, product_cnt in buy_products.items():
        result_amt += product_list.get(product_name) * product_cnt

    return f'Общая сумма = {result_amt}р.\n'


def menu_controller() -> dict:
    menu = format_items(get_menu_items())
    execute_console_output(menu)
    raw_choice = execute_console_input(
        **get_phrase("choice")
    )
    return validate_user_choice(
        raw_choice
    )


def get_all_products_controller() -> None:
    products = get_products_storage_from_list()
    execute_console_output(
        validate_product_list(products)
    )


def select_product_controller():
    form = get_buy_form()
    raw_buy_product = execute_console_input(**form)
    clean_buy_product = validate_buy_product(raw_buy_product)
    add_buy_products(clean_buy_product, update_product_from_dict)


def view_buy_products_controller():
    buy_list = get_users_prod_storage_from_dict()
    execute_console_output(
        validate_buy_list(buy_list)
    )


def get_sum_amt_controller():
    buy_list = get_users_prod_storage_from_dict()
    amt_result = get_sum_amt(buy_list, get_products_storage_from_list())
    write_file('buy_products.json', file_adaptor(buy_list))
    execute_console_output(
        amt_result
    )


def get_choices() -> dict[int, callable]:
    return {
        1: get_all_products_controller,
        2: select_product_controller,
        3: view_buy_products_controller,
        4: get_sum_amt_controller,
        0: quit
    }


def execute_choice(choice: int) -> None:
    choices = get_choices()
    choices.get(
        choice
    )()
    execute_console_input(**get_phrase("continue"))


def run():
    while True:
        choice = menu_controller()
        execute_choice(**choice)


run()
