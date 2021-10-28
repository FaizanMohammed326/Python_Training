import math

""""
There are two types of error in python:
1. Syntax error:
    When the proper syntax of the language is not followed then a syntax error is thrown.
Errors are the problems in a program due to which the program will stop the execution.
2. Logical error (Exception):
    When in the runtime an error that occurs after passing the syntax test is called exception or logical type.
exceptions are raised when some internal events occur which changes the normal flow of the program.
Some of the common errors in python:

IndexError	            When the wrong index of a list is retrieved.
AttributeError	        It occurs when an attribute assignment is failed.
ImportError	            It occurs when an imported module is not found.
KeyError	            It occurs when the key of the dictionary is not found.
NameError	            It occurs when the variable is not defined.
MemoryError	            It occurs when a program runs out of memory.
TypeError	            It occurs when a function and operation are applied in an incorrect type.
ValueError              It occurs when a a function receives an argument of the correct type but an
                        inappropriate value.

Error/Exception Handling:
    When an error and an exception are raised then we handle that with the help of the Handling method.
We can handle errors by the Try/Except/Finally method. we write unsafe code in the try,
if an error occurs then it goes into except block, after executing except final code in finally is executed.

Error Handling is important because:
    Exception handling allows you to separate error-handling code from normal code.
    It clarifies the code and enhances readability.
    Raising an exception helps you to break the current code execution and returns the exception back
to execution until it is handled.
    An exception is a convenient method for handling error messages.
"""

try:
    print("code start")
    lst = [1, 2, 3]
    # print(lst[0])
    print([lst[4]])
except:
    print("an error occurs")

finally:
    print("final code")
print('\n')

"""
Catching Specific Exception:
    
"""

x = int(input('Please enter a positive number:\n'))

try:
    print(f'Square Root of {x} is {math.sqrt(x)}')
except ValueError as ve:
    print(f'You entered {x}, which is not a positive number.')
print('\n')

"""
Try with multiple except blocks:
    A try statement can have more than one except clause, to specify handlers for different exceptions.
But at most one handler will be executed.
"""
# a, b = 1, 0
a, b = 4, 2
try:
    print(a / b)
    print('10' + 10)

except TypeError:
    print("You added values of incompatible types")

except ZeroDivisionError:
    print("You divided by 0")

print('\n')

"""
multiple exceptions in one except:
    the above example can be written as follows
"""
try:
    print('10' + 10)
    print(1 / 0)

except (TypeError, ZeroDivisionError):
    print("Invalid input")

print('\n')

"""
Try with Else Clause
    We can also use the else clause on the try-except block which must be present after all the except clauses.
The code enters the else block only if the try clause does not raise an exception.
"""

try:
    age = int(input('Enter your age: '))
except:
    print('You have entered an invalid value.')
else:
    if age <= 18:
        print('You are not allowed to enter, you are too young.')
    else:
        print('Welcome, you are old enough.')
