"""
A Set is an unordered collection data type that is iterable, mutable and has no duplicate elements.
1.Sets can be created by using the built-in set() function with an iterable object or a sequence by placing the sequence
 inside curly braces, separated by ‘comma’.
"""
li = [1,2,3,4]
set1 = set(li)
print(set1,type(set1))

set2 = {2, 3, 4, 5}
print(set2,type(set2))
print('\n')

"""
2. new elements can be assign using add() or update() functions
"""

set1.add(8)
set1.add(9)
set1.add((6, 7))
print(set1)
print('\n')

set1.update([10, 11])
print(set1)
print('\n')


"""
3.Concatenation:
    for concatenation we use '|' operator , update() function and union() function
"""
seta = {1,2,3}
setb = {4,5,6}
setc = {7,8}
setd = {9,10}

print(seta)
seta |= setb
print(seta)
seta.update(setc)
print(seta)
print(seta.union(setd))
print('\n')

"""
4..methods in sets
add() :
    Only one element at a time can be added to the set by using add() method
update() :
    For addition of two or more elements Update() method is used.
The update() method accepts lists, strings, tuples as well as other sets as its arguments
union() :
    values are accessed and traversed with merge operation perform on them to combine the elements,
at the same time duplicates are removed.
intersection() - To find intersection between 2 sets.
difference() - To find difference in between sets.
pop() - to remove a random element and return that element
remove() - to remove a specified element from a set


"""
set1 = {1,2,3,4,5}
set2 = {3,4,5,6,7}
set3 = set1.intersection(set2)
print('intersection : ',set3)

set4 = set1-set2
print('difference : ',set4)

fruits = {"apple", "banana", "cherry"}
x = fruits.pop()
print(x)

fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
print(fruits)
print('\n')
"""
5.comprehension in sets:
    similar to lists and dictionaries we have comprehension in sets in python
Syntax :
    [expr for val in collection if condition]
"""

squares = {i**2 for i in range(1, 11)}
print(squares)
print('\n')

"""
6.since sets are unordered and immutable they do not have indices and cannot be sliced
"""