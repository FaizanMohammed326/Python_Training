"""
map() function returns a map object(which is an iterator) of the results after applying the given function
 to each item of a given iterable (list, tuple etc.)
The returned value from map() (map object) then can be passed to functions like list() (to create a list),
   set() (to create a set)
"""


def double(n):
    return n + n


numbers = (1, 2, 3, 4)
result = list(map(double, numbers))
print('results without using lambda in map : ', result)
print('\n')

"""
We can also use lambda expressions with map to achieve above result.
"""

results_lambda = list(map(lambda x: x + x, numbers))
print('results after using lambda in map : ', results_lambda)
print('\n')

"""
we can also pass more than one iterable to a map function
"""

numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]

result = map(lambda x, y: x + y, numbers1, numbers2)
print(list(result))
# print(list(result))
