"""
Python Functions is a block of related statements designed to perform a computational,
logical, or evaluative task.
Functions can be both built-in or user-defined.
We can create a  Python function using the def keyword.
Syntax: 
def function_name(parameters):
    statement(s)
    return expression
"""
print('\n')


def fun():
    print("Welcome to function introduction in python")


"""
After creating a function we can call it by using the name of the function 
followed by parenthesis containing parameters of that particular function.
"""

fun()
print('\n')
"""
The function return statement is used to exit from a function and go back to the function caller
and return the specified value or data item to the caller.
Syntax: return [expression_list]
"""


def sqr_num(num):
    return num ** 2


print(sqr_num(2), sqr_num(-4))
print('\n')

"""
according to the return value and arguments present in a function,
They can be divided into 4 categories:

1.Function with no arguments and no return value
Ex.
"""


def fun_print():
    print("inside the fun_print")


fun_print()
print('\n')

"""
2.Function with no arguments and with return value
"""


def create_list():
    li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return li


new_list = create_list()

"""
3.Function with arguments but no return statement
"""


def print_dict(d):
    for key in d:
        print('{} - {}'.format(key, d[key]))


animals = {1: 'cat', 2: 'dog', 3: 'horse'}
print_dict(animals)
print('\n')

"""
4.Function with both arguments and return statement
"""


def reverse_list(li):
    rev_list = list(reversed(li))
    return rev_list


list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
rev_list_1 = reverse_list(list_1)
print(rev_list_1)
print('\n')

"""
Functions further can be divided into several types based on the arguments passed.
Python supports various types of arguments that can be passed at the time of the function call.
1.Default Arguments:
    A default argument is a parameter that assumes a default value if a value is not provided
     in the function call for that argument.
"""


def print_x_y(x, y=50):
    print("x: ", x)
    print("y: ", y)


print_x_y(10)
print('\n')

"""
2.Keyword Arguments:
    It allow the caller to specify the argument name with values so that 
    caller does not need to remember the order of parameters.
"""


def player(firstname, lastname):
    print(firstname, lastname)


player(firstname='Lionel', lastname='Messi')
player(lastname='Jr', firstname='Neymar')
print('\n')

"""
3.Variable Length Arguments:
    In Python, we can pass a variable number of arguments to a function using special symbols.
    There are two special symbols:
    1. *args (non-keyword arguments)
    2. *kwargs (keyword arguments)
"""


def print_args(*args):
    for arg in args:
        print(arg)


print_args('Example', 'For', 'variable-length', 'non-keyword', 'arguments')
print('\n')


def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print("{} == {}".format(key, value))


print_kwargs(first='example for', mid='variable-length', last='keyword arguments')
print('\n')

"""
Function Pass by Reference or pass by value:
    In Python every variable name is a reference.
When we pass a variable to a function, a new reference to the object is created.
"""


def fun1(x):
    x[0] = 20


lst = [10, 11, 12, 13, 14, 15]
fun1(lst)
print(lst)
print('\n')

"""
When we pass a reference and change the received reference to something else,
the connection between the passed and received parameter is broken
"""


def fun2(x):
    x = [20, 30, 40]


lst = [10, 11, 12, 13, 14, 15]
fun2(lst)
print(lst)
print('\n')

"""
Recursive Functions:
    In Python, it’s also possible for a function to call itself
A function that calls itself is said to be recursive function.

Uses:
1.Recursive functions make the code look clean
2.A complex task can be broken down into simpler sub-problems using recursion.
3.Sequence generation is easier with recursion than using some nested iteration.

"""


def sum_num(n):
    if n > 0:
        return n + sum_num(n - 1)
    return 0


result = sum_num(7)
print(result)
