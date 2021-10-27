"""
Overloading a constructor allows for a class to be instantiated with a different number
of parameters per instance.

This can be achieved using two methods:
1. Using Default arguments to overload a constructor.
"""


class Fruits:
    def __init__(self, required_param, optional_param1=None, optional_param2=None):
        self.required_param = required_param
        self.optional_param1 = optional_param1
        self.optional_param2 = optional_param2


fruit1 = Fruits('apple')
fruit2 = Fruits('apple', 'banana')
fruit3 = Fruits('apple', 'banana', 'orange')
print(fruit1.__dict__)
print(fruit2.__dict__)
print(fruit3.__dict__)
print('\n')

"""
every object in python has an attribute which is denoted by __dict__.
obj.__dict__ returns all the attributes of that object stored in a dictionary in the format
attribute name as keys and attribute value as values.
"""

"""
2. Using variable length arguments (starred and key word arguments) to overload a constructor
"""


class Vegetables:
    def __init__(self, *args, **kwargs):
        self.required_param = args[0]
        self.optional_param1 = kwargs.get('optional_param1', None)
        self.optional_param2 = kwargs.get('optional_param2', None)


veg1 = Vegetables('tomato')
veg2 = Vegetables('tomato', optional_param1='onion')
veg3 = Vegetables('tomato', optional_param1='onion', optional_param2='potato')
print(veg1.__dict__)
print(veg2.__dict__)
print(veg3.__dict__)
print('\n')
