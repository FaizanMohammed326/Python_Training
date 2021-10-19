"""
Dictionary in Python is an unordered collection of data values, used to store data
 values like a map, Dictionary holds key:value pair

 1.Creation
A Dictionary can be created by placing a sequence of elements within curly {} braces, separated by ‘comma’.
"""

import copy
fruits = {1: 'apple', 2: 'orange', 3: 'bannana'}
print(fruits)
print('\n')

"""
2. assignment
"""
fruits[4]='grapes'

"""
3. Concatenation:
we can concatenate a dict using update()
"""
fruits = {1: 'apple', 2: 'orange', 3: 'bannana'}
vegetables = {1: 'tomato',2: 'onion'}
fruits.update(vegetables)


print('concatenation : ',fruits)
print('\n')

"""
4.methods
update() -Updating an existing value in a Dictionary can be done by using the built-in update() method
get() is used in accessing the element from a dictionary.
"""

marks = {'Physics':67, 'Maths':87}
internal_marks = {'Practical':48}

marks.update(internal_marks)
print(marks)

print(marks.get(3))

del marks['Maths']
print(marks)

print('\n')
"""
Pop() method is used to return and delete the value of the key specified.
popitem() returns and removes an arbitrary element (key, value) pair from the dictionary.
All the items from a dictionary can be deleted at once by using clear() method.
"""
fruits = {1: 'apple', 2: 'orange', 3: 'bannana'}
pop_ele1 = fruits.pop(1)
pop_ele2 = fruits.popitem()
print(pop_ele1,pop_ele2)
fruits = {1: 'apple', 2: 'orange', 3: 'bannana'}
fruits.clear()
print(fruits)
print('\n')


"""
keys(): Returns list of dictionary dict’s keys
values(): Returns list of dictionary dict’s values
items(): Returns a list of dict’s (key, value) tuple pairs
len() :- It returns the count of key entities of the dictionary elements.
type() :- This function returns the data type of the argument.
copy() :- This function creates the shallow copy of the dictionary into other dictionary.
"""
fruits = {1: 'apple', 2: 'orange', 3: 'bannana'}
print(fruits.keys(),fruits.values(),fruits.items())
print(type(fruits),len(fruits))
fruits_new = fruits.copy()
print('\n')

"""
5.A dictionary comprehension takes the form {key: value for (key, value) in iterable}
"""

new_dict = {x: x**3 for x in range(10) if x**3 % 4 == 0}
print(new_dict)
print('\n')

"""
6.traversing in a dictionary
"""
fruits = {1: 'apple', 2: 'orange', 3: 'bannana'}

for key, value in fruits.items():
    print('key : {} , value : {}'.format(key, value))
