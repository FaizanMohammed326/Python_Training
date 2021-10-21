"""
Python Lambda Functions are anonymous function means that the function is without a name
the lambda keyword is used to define an anonymous function in Python.
Syntax :  lambda arguments: expression
This function can have any number of arguments but only one expression, which is evaluated and returned.
"""


def cube(y):
    return y * y * y


lambda_cube = lambda y: y * y * y


print(cube(5))
print(lambda_cube(5))
print('\n')

max_ = lambda a, b: a if (a > b) else b
print(max_(5, 2))
print('\n')

"""
Uses of lambda function:
We use lambda functions when we require a nameless function for a short period of time.
In Python, we generally use it as an argument to a higher-order function
(a function that takes in other functions as arguments).
Lambda functions are used along with built-in functions like filter(), map(),reduce() etc
"""

"""
tables = [(lambda x: x * 10)(x) for x in range(1,11)]
print(tables)

tables2 = [lambda x=x: x*10 for x in range(1,11)]
for table in tables2:
    print(table())
"""