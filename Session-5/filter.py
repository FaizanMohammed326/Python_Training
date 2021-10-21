"""
The filter() method filters the given sequence with the help of a function that tests each element in the sequence
to be true or not.
Syntax :
    filter(function, sequence)
here function should return true or false
sequence can be any iterable or a sequence containing iterators like map() object
"""


def fun(variable):
    vowels = ['a', 'e', 'i', 'o', 'u']
    if variable in vowels:
        return True
    else:
        return False


lst = list(input('enter the string : '))
filtered = list(filter(fun, lst))
print('The filtered letters are:', filtered)


"""
The above code can be written using lambda expressions in filter 
"""
vowel = ['a', 'e', 'i', 'o', 'u']

filtered = list(filter(lambda x: x in vowel, lst))
print('The filtered letters after using lambda expression :', filtered)
print('\n')

"""
map object can also be passed on filter and vice versa
"""

lst = ['2', 't', 'a', '4', 'fa', 'g', '5', 'd']
res = list(map(lambda x: int(x)**2, filter(lambda x: x.isdigit(), lst)))

print('squares of the digits in the list are : ', res)
