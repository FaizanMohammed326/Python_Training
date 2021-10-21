# WAP to find the sum of all the elements in the given list

from functools import reduce

lst = [int(x) for x in input('enter the list : ').split(',')]
lst_sum = reduce(lambda x, y: x + y, lst)
print('the sum of all the elements in the list is ', lst_sum)
