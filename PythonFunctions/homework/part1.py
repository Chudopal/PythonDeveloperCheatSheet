"""1. Увеличте все элементы
следующей коллекции на 1"""
from typing import List


def cast_int(arg):
    return int(arg)+1

int_list = [1,2,"3",4,5,6,7,"5", "100"]
result_list = list(map(cast_int, int_list))
print(result_list)



"""2. Сложите все элементы
предыдущей коллекции(result_list)"""
list_sum = sum(result_list)

"""3. Напишите функцию, которая получает
список элементов(аргументом может быть
список как int_list из задания 1). Найдите
сумму всех элементов. И верните как результат
строку:
"Сумма элементов {все элементы списка через запятую} равно {сумма всех элементов}"
"""
def find_sum_and_format_message(int_list) -> str:
    return f"Сумма элементов {", ".join(map(str, int_list))} равно {sum(map(int, int_list))}"

"""4. Перепишите предыдущую функцию,
чтобы она принимала не лист, а
элементы поотдельности. Количество аргументов
должно быть неограниченно."""

def find_sum_and_format_message(*int_list) -> str:
    return f"Сумма элементов {", ".join(map(str, int_list))} равно {sum(map(int, int_list))}"

"""5. Напишите функцию, которая будет
последовательно перемножать элементы
2х коллекций.
Например a=[1,2,3], b=[3,4,5], то
результат функции - [3, 8, 15].
Предпологается, что коллекции имеют
одинаковое количество элементов."""
# добавить 2 варика
def mul(
    first_list: List[int],
    second_list: List[int]
) -> List[int] or None:
    result = []
    if len(first_list) == len(second_list):
        result = None
    for index  in range(0, len(first_list)):
        result.append(first_list[index] * second_list[index])
    return result

print(mul([1,2,3,4], [4,5,6,7]))
