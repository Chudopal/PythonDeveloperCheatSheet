# 1.Возведите 2 в 1024 степень

res: int = ...

# 2.Сделайте так, чтобы код работал, не меняя объявление переменных и расставьте скобки, чтобы вычислялась средняя зарплата всех отделов:

developer_department_salary = 1700
qa_department_salary = 1400
accountant_department_salary = 1500
departments_number = "3"

avg_salary = developer_department_salary + qa_department_salary + accountant_department_salary / departments_number

# 3.Добавьте аннотации типов
weight = 15.6
district_name = "Moskovsky"
is_compiled = True
staff_number = 123
rating = 1 + 5 + (2*4.6)
count = 3//8


# 4. Запишите в переменную long_partition 100500 прочерков

short_partition = "-"

long_partition: str = ...

#(extra)5. Напишите последнее выражение, удовлетворяющее следующему условию
# Если пользователь админ, то ему разрешается
# Если пользователь акивен, и у него есть разрешение, то ему так же разрешается
# Если пользователь заблокирован, то ему ничего не разрешается, даже если он админ или у него есть пермишен
is_active = True
is_admin = False
has_permission = True
is_blocked = True

is_allowed: bool = ...