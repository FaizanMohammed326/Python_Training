"""
Encapsulation is one of the fundamental concepts in object-oriented programming (OOP).
It describes the idea of wrapping data and the methods that work on data within one unit.
This puts restrictions on accessing variables and methods directly and can prevent the accidental
modification of data.

A class is an example of encapsulation as it encapsulates all the data that is member functions and variables.

Protected members:
    Protected members are those members of the class that cannot be accessed outside the class but
can be accessed from within the class and its subclasses.
To accomplish this in Python, just follow the convention by prefixing the name of the member
by a single underscore “_”.
"""


class Base1:
    def __init__(self):
        self._a = 2


class Derived1(Base1):
    def __init__(self):
        Base1.__init__(self)
        print(self._a)


obj2 = Derived1()
obj1 = Base1()
# print(obj2.a)
print('\n')

"""
To prevent accidental change, an object’s variable can only be changed by an object’s method.
Those types of variables are known as private variable.
Private members are similar to protected members, the difference is that the class members declared private should
neither be accessed outside the class nor by any base class
In Python, there is no existence of Private instance variables that cannot be accessed except inside a class.
However, to define a private member prefix the member name with double underscore “__”.
"""


class Base2:
    def __init__(self):
        self.a = "Variable-a"
        self.__c = "Variable-c"
        print(self.__c)


class Derived2(Base2):
    def __init__(self):
        Base2.__init__(self)
        print("Calling private member of base class: ")
        print(self.__c)


obj3 = Base2()
print(obj3.a)
# print(obj3.__c)
# obj4 = Derived2()
print('\n')

"""
You are not able to access the private variables directly in Python.
That's why we implemented the getter and setter method.
"""


class SampleClass:

    def __init__(self, a):
        self.__a = a

    def get_a(self):
        return self.__a

    def set_a(self, a):
        self.__a = a


obj = SampleClass(10)
print(obj.get_a())
obj.set_a(45)

print(obj.get_a())
print('\n')
"""
@property is used to get the value of a private attribute without using any getter methods.
We have to put a line @property in front of the method where we return the private variable.

To set the value of the private variable,
we use @method_name.setter in front of the method. We have to use it as a setter.
"""


class Property:

    def __init__(self, var):
        self.__a = var

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, value):
        self.__a = value


obj = Property(23)
print(obj.a)
print('\n')
"""
Another way to use property is as follows
"""


class FinalClass:

    def __init__(self, var):
        self.__set_a(var)

    def __get_a(self):
        return self.__a

    def __set_a(self, var):
        self.__a = var

    a = property(__get_a, __set_a)


obj = FinalClass(12)
#  print(obj.__get_a())
print(obj.a)
print('\n')
