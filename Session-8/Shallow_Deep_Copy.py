"""
Shallow Copy:
    A shallow copy constructs a new compound object and then (to the extent possible) inserts references
into it to the objects found in the original.

Deep Copy:
    A deep copy constructs a new compound object and then, recursively,inserts copies into it
of the objects found in the original.

Both are imported from the module copy.

Shallow Copy stores the copy of the original object and points the references to the objects.
Where as Deep copy stores the copy of the original object and recursively copies the objects as well.
"""

from copy import copy, deepcopy

lst = [[1, 2, 3], (2, 3, 4), 'random', [7, 8, [9, 10]]]
lst1 = copy(lst)
lst2 = deepcopy(lst)


# Python id() function returns an identity of an object. This function takes an argument an object and
# returns a unique integer number which represents identity.
print(lst, id(lst))
print(lst1, id(lst1))
print(lst2, id(lst2))
print('\n')

print(id(lst[3]))
print(id(lst1[3]))
print(id(lst2[3]))
print('\n')

"""
Shallow Copy reflects changes made to the new/copied object in the original object.
Where as Deep copy doesn’t reflect changes made to the new/copied object in the original object.
"""
# changing original list content will change lst1 but not lst2

lst1[0][2] = 9
print(lst)
print(lst1)
print(lst2)
print('\n')

# same as before changing the lst1 content will change original list but not lst2

lst1[0][2] = 9
print(lst)
print(lst1)
print(lst2)
print('\n')

# where as changing lst 2 wont effect other lists.

lst2[0][2] = 10
print(lst)
print(lst1)
print(lst2)
