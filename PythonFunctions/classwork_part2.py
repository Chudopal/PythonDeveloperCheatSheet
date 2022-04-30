# def foo(arg: any) -> int:
#     return int(arg) + 1


from typing import Dict


random_list = [1,2,3,"5"]
result = list(map(lambda arg: int(arg)+1, random_list))
# print(result)


users = [
    {
        "name": "Alex",
        "age": 22,
    },
    {
        "name": "Bob",
        "age": 10,
    },
    {
        "name": "Alice",
        "age": 20,
    },
]

# def filter_adult(p: Dict) -> bool:
#     result = p.get("age",0) >= 18
#     return result

# f = lambda p: p.get("age") >= 18
# adults = list(filter(f, users))
# print(adults)
# a = [1,2,3,4, "5"]
# a_plus_1 = [int(item) + 1 for item in a]

# a_plus_1 = (int(item) + 1 for item in a if item > 3)

# print("HERE")
# print(a_plus_1)


# print(a_plus_1)

def foo1(arg):
    return int(arg) + 1

def foo2(arg):
    return int(arg) + 2

def foo3(arg):
    return int(arg) + 3

def foo4(arg):
    return int(arg) + 4

def foo(arg):
    return f"{arg} не обрабатывается"

a = 4

choices = {
    1: foo1,
    2: foo2,
    3: foo3,
}

choices[4] = foo4

# print(
#     choices.get(a, foo)(a)
# )

# if a == 1:
#     r = foo1(a)
# elif a == 2:
#     r = foo2(a)
# elif a == 3:
#     r = foo3(a)
# else:
#     r = foo(a)

# defs = [foo1, foo2, foo3]

# for d in defs:
#     print(d(1))

# defs_map

# def my_print(smth: any) -> None:

#     def separate() -> None:
#         print("-"*80)
    
#     separate()
#     print(smth)
#     separate()

from typing import Callable


# def separate(func):

#     def inner(*args, **kwargs):
#         print('-'*80)
#         func(*args, **kwargs) # здесь вызов me_print_2
#         print('-'*80)

#     return inner

# def separate_by_star(func):

#     def inner(*args, **kwargs):
#         print("*"*80)
#         func(*args, **kwargs)
#         print("*"*80)
    
#     return inner


# @separate
# @separate_by_star
# def my_print_2(smth, s1,s2,s3):
#     print(smth,s1,s2,s3)


# my_print_2("hello", 234,545,656)


#my_print_2("Hello",1,2,3)


# def separate(sep="^"):

#     def wrapper(func):

#         def inner(*args, **kwargs):
#             print(sep*80)
#             func(*args, **kwargs)
#             print(sep*80)

#         return inner

#     return wrapper


# @separate(":")
# def my_print_2(smth, s1,s2,s3):
#     print(smth,s1,s2,s3)

# separate(":")(my_print_2)("ognwrgnwr", 123,234,2345)


# my_print_2("ognwrgnwr", 123,234,2345)

# def sum_1(a):
#     return a+1

# def sum_2(a):
#     return a+2

# def sum_3(a):
#     return a+3


def sum_factory(b, c):

    def sum_n(a):
        return a + b + c

    return sum_n

sum_1 = sum_factory(1)
print(sum_1(10))

sum_2 = sum_factory(2)
print(sum_2(10))

sum_3 = sum_factory(3)
print(sum_3(10))
