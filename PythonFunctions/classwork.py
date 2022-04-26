"""Встроенные функции работы над коллекциями"""


def foo(item):
    return int(item)

def bar(item):
    return item > 2

print(foo(100))
print(foo("100"))


print(bar(1))

print(bar(3))

int_list = [1,"2", 3, "4"]

#                     [3,4]              [1,2,3,4]
clear_int_list = list(filter(bar, map(foo, int_list)))
print(int_list)
print(clear_int_list)

from typing import Dict, Tuple, Union

def choose_season(
    number: int, 
    seasons_map: Dict[Tuple[int], Union[str, int]]
):
    result = ""
    if number > 12:
        result = "Too big"
    elif number < 1:
        result = "Too small"
    else:
        for term, season in seasons_map.items():
            if number in term:
                result = season
                break
    return result


print(choose_season(
    8,{
    (1, 2, 12): "Winter",
    (3, 4, 5): "Spring",
    (6, 7): "Summer",
    (8): "Late summer",
    (9): "Early autumn",
    (10, 11): "Autumn",
    }
))

print("d", "k", "m", sep="...")

a = 5

def format(second, first, end, sep):
    print(a)
    result = f"{first}{sep}{second}{end}"
    return result



print(
    format(sep="!!!", end="$", first=1, second=2)
)

"""Функции & Процедуры"""


"""Типизация"""


def format(*items, end: str="\n", sep: str=" ") -> str:
    core = sep.join(
        map(str, items)
    )
    result = core + end
    return result


print(
    format("1", "2", 3, '4', sep="#")
)


# 9999 & 9999
a = "99998888666"
b = "99999886"

c = list(filter(lambda x: x in a, b))
print(c)


"""Генераторы списков"""
