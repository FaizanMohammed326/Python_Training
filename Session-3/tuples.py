"""
A Tuple is a collection of Python objects separated by commas.
In someways a tuple is similar to a list in terms of indexing,
nested objects and repetition but a tuple is immutable unlike lists which are mutable.
1.creating a tuple: In Python, tuples are created by placing a sequence of values separated by ‘comma’
"""

Tuple1 = ('example', 'for', 'tuple')
print(Tuple1)

list1 = [1, 2, 4, 5, 6]
print(tuple(list1))
print('\n')

"""
2.assignment
"""

m = ['have', 'fun']

"""
3.concatenation
    Concatenation is done by the use of ‘+’ operator.
Concatenation of tuples is done always from the end of the original tuple.
"""

Tuple1 = (0, 1, 2, 3)
Tuple2 = ('example', 'for', 'tuple')

Tuple3 = Tuple1 + Tuple2
print(Tuple3)
print('\n')

"""
4.methods in tuples:
count() -
    The count() method of Tuple returns the number of times the given element appears in the tuple.
index() -
    The Index() method returns the first occurrence of the given element from the tuple.
    Syntax - tuple.index(element, start, end)
len() - to find the length of the tuple
max(),min() -  to find max and min
sum() - to find sum of the elements of the tuple
"""

Tuple1 = (0, 1, 2, 3, 2, 3, 1, 3, 2)
Tuple2 = (1, 3, 5, 6, 7, 3)
res = Tuple1.count(3)
print('Count of 3 in Tuple1 is:', res)
print('\n')

print(len(Tuple1), min(Tuple1), max(Tuple1), sum(Tuple1,))


"""
5. Comprehension:
    Comprehension works by looping or iterating over items and assigning them into a container,
a Tuple is unable to receive assignments.

6.indexing an slicing:
    similar to lists in python
slicing Syntax:
    Lst[ Initial : End : IndexJump ]
"""

tuple1 = ('a', 'b', 'c', 'd')
print(tuple1[1])
print(tuple1[-3])
print('\n')

print(tuple1[1:3:1])
