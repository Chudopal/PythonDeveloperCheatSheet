# 1.Возведите 2 в 1024 степень

res: int = 2 ** 1024

# 2.Сделайте так, чтобы код работал, 
# не меняя объявление переменных и расставьте скобки,
# чтобы вычислялась средняя зарплата всех отделов:

developer_department_salary = 1700
qa_department_salary = 1400
accountant_department_salary = 1500
departments_number = "3"

avg_salary = (developer_department_salary
    + qa_department_salary
    + accountant_department_salary) \
    / int(departments_number)

# 3.Добавьте аннотации типов
weight: float = 15.6
district_name: str = "Moskovsky"
is_compiled: bool = True
staff_number: int = 123
rating: float = 1 + 5 + (2*4.6)
count: int = 3//8


# 4. Запишите в переменную long_partition 100500 прочерков

short_partition = "-"

long_partition: str = short_partition * 100500

#(extra)5. Напишите последнее выражение, удовлетворяющее следующему условию
# Если пользователь админ, то ему разрешается
# Если пользователь активен, и у него есть разрешение, то ему разрешается
# Если пользователь заблокирован, то ему ничего не разрешается, даже если он админ или у него есть пермишен
is_active = True
is_admin = False
has_permission = True
is_blocked = True

is_allowed: bool = ((is_active and has_permission) or is_admin)\
 and not is_blocked
