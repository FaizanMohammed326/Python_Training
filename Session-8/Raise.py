"""
Sometimes, you may want to deal with a situation by raising a certain exception
The raise statement allows the programmer to force a specific exception to occur.
This must be either an exception instance or an exception class
"""

"""a, b = int(input('enter 1st number : ')), int(input('enter 2nd number : '))
if b == 0:
    raise ZeroDivisionError
else:
    print(a/b)
print('\n')"""

"""
now if put this in a try-except block
"""
try:
    if b == 0:
        raise ZeroDivisionError
    print(a / b)
except:
    print("You divided by 0")
print('\n')

"""
It is possible to use the raise keyword without specifying what exception to raise.
Then, it raises the exception that occurred.
"""

"""try:
    print(1+'2')
except:
    raise
print('\n')"""

"""
Raise With an Argument:
"""

try:
    print(1+'2')
except:
    raise TypeError("cannot add two operand with different type")
print('\n')

