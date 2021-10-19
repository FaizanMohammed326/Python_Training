"""Lists are nothing but ordered collection of data. It is also mutable
1.Creation of lists
Lists in Python can be created by just placing the sequence inside the square brackets[]"""

li = [1, 2, 3, 4, 1, 3, 4, 'a b c d', (1, 3), [2, 3]]

"""
2.assignment of an element
we can assign a variable with '=' sign variable being on the left hand side and list being on the right side
also to clone a list we can use slicing, extend(), list comprehension and list() method
"""

test_list = [21, 43, 546, 66, 87, 23]
l1 = test_list[:]
l2 = []
l2.extend(test_list)
l3 = [i for i in test_list]
l4 = list(test_list)
print(test_list, '\n', l1, '\n', l2, '\n', l3, '\n', l4, '\n')

"""
3.concatenation 
there are 6 ways to concatinate a list in python
a. using append()
b. using '+' operator
d. using extend()
e. using '*' operator
"""
l1 = [1, 3, 5]
l2 = [2, 4, 6]

# using append()

for i in li:
    l2.append(i)
print()
print('l2 : ', l2)
# using +
l3 = list(l1)
l4 = list(l2)

l3 = l3 + l4
print('l3 : ', l3)

# using list comprehension
l5 = list(l1)
l6 = list(l2)

l5 = [y for x in [l5, l6] for y in x]
print('l5 : ', l5)

# using * operator

l7 = list(l1)
l8 = list(l2)
l7 = [*l7, *l8]

print('l7 : ', l7)
"""
4.methods in lists
append(): Used for appending and adding elements to List.
It is used to add elements to the last position of List.,
extend(): Adds contents of List2 to the end of List1.
insert(): Inserts an elements at specified position.
sum(), count(), index(), min() and max()
"""
l1 = [1, 3, 1, 5]
l1.insert(10, 1)
print(l1)

print(sum(l1), l1.count(1), len(l1), l1.index(1, 2, 4), min(l1), max(l1))

"""
sort() and reverse()
sort is used to sort the elements of the list.
reverse is used to reverse the list.
"""
l2 = [2, 3, 5, 7, 1, 2, 8]
print(sorted(l2, reverse=True))
print(l2.sort())

"""
pop() is used to remove an element from end of  a list. index is optional to remoe a specific index
del() : Element to be deleted is mentioned using list name and index.
remove(): Element to be deleted is mentioned using list name and element
"""

l3 = [1,2,4,46,6,3,23,41]
l3.pop(3)
print(l3)

del l3[5]
print(l3)

l3.remove(6)
print(l3,'\n')

"""
list comprehension 
list comprehension offers a shorter syntax when you want to create a new list based on the values
 of an existing list.
Syntax :
newlist = [expression for item in iterable if condition == True]
"""
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

"""
indexing and slicing
Indexing: Indexing is used to obtain individual elements.
Slicing: Slicing is used to obtain a sequence of elements.
slicing Syntax:
    Lst[ Initial : End : IndexJump ]
"""

l3 = [1,2,4,46,6,3,23,41]
print(l3[3],l3[-5])

print(l3[2:4:1])
