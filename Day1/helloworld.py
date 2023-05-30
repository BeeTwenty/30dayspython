import math
# excercuse level 1

# Addition(+)
print(3+5)
# subtraction
print(6-4)
# Multiplication
print(3*5)
# Modulus
print(4%3)
# division
print(8/4)
# exponential
print(3**4)
# floor divition
print(7//3)

# ny name
print('Sindre')
# Family Name
print('Berge')
# Country
print('Norway')
# string
print('I am enjoying 30 days of python')

# data type of:
# 10
print(type(10))
# 9.8
print(type(9.8))
# 3.14
print(type(3.14))
# 4-4j
print(type(4-4j))
# ['ABC', 'CDE', 'EFG']
print(type(['ABC', 'CDE', 'EFG']))
# Sindre
print(type('Sindre'))
# berge
print(type('Berge'))
# Norway
print(type('Norway'))

# Bool
is_true = True
print(is_true)
print(type(is_true))
# tuple
tuple_list = (3.4, 2.54, 4.4)
print(tuple_list)
print(type(tuple_list))
# set
set_list = {1, 2, 3, 4}
print(set_list)
print(type(set_list))
# dict
dict_list = {
    'name':'Sindre',
    'Family':'Berge',
    'Country':'Norway',
}
print(dict_list)
print(type(dict_list))

# Euclidian Distance between (2, 3) and (10, 9)
p = 2, 3
q = 10, 9
result = math.dist( p, q)
print(result)