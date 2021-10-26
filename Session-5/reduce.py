"""
The reduce() function is defined in the functools module.
the reduce() function receives three arguments where third is optional.
However, it doesn't return another iterable, instead it returns a single value.
reduce() is useful when you need to apply a function to an iterable and reduce it to a single cumulative value

Syntax :
    functools.reduce(function, iterable, initializer)
"""

from functools import reduce

# to find the factorial of a number

num = int(input('enter the number to find its factorial : '))
fact = reduce(lambda x, y: x * y, range(2, num+1))
print('Factorial of {}: '.format(num), fact)
print('\n')

"""
we can also pass the third parameter which is the initializer.
below is the program to find he number greater than given number if present in the list
"""

lst = [10, 30, 40, 20, 20]
num = 50
res = reduce(lambda a, b: a if a > b else b, lst, num)
print(res)
print('\n')

"""
we can also pass filter or map into the reducer function and vice versa
below is th function to find sum of all the even numbers in a list
"""

lst = [1, 3, 4, 8, 2, 7, 9, 11, 12, 15]
res = reduce(lambda x, y: x + y, filter(lambda x: x % 2 == 0, lst))
print('the sum of all the evn numbers in the list is ', res)
