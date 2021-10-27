"""
Iterator in python is an object that is used to iterate over iterable objects like lists, tuples, dicts,
and sets.
The iterator object is initialized using the iter() method. It uses the next() method for iteration.

__iter(iterable)__ method that is called for the initialization of an iterator.
This returns an iterator object

next ( __next__ in Python 3) The next method returns the next value for the iterable.

When we use a for loop to traverse any iterable object, internally it uses the iter() method to get an
iterator object which further uses next() method to iterate over.

This method raises a StopIteration to signal the end of the iteration.
"""

iterable_value = 'tibil'
iterable_obj = iter(iterable_value)

while True:
    try:
        item = next(iterable_obj)
        print(item)
    except StopIteration:
        break
print('\n')

"""
Example of a custom iterator
"""


class Test:

    def __init__(self, limit):
        self.limit = limit

    def __iter__(self):
        self.x = 10
        return self

    def __next__(self):
        x = self.x

        if x > self.limit:
            raise StopIteration

        self.x = x + 1
        return x


obj1 = Test(15)
obj2 = Test(5)
for i in obj1:
    print(i)

for i in obj2:
    print(i)
print('\n')
