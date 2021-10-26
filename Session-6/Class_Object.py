"""
In Python, object-oriented Programming (OOPs) is a programming paradigm that uses
objects and classes in programming.
 It aims to implement real-world entities like inheritance, polymorphisms, encapsulation, etc.

A class is a user-defined blueprint or prototype from which objects are created.
Creating a new class creates a new type of object, allowing new instances of that type to be made.

An Object is an instance of a Class. A class is like a blueprint while an instance is a copy of the class
with actual values.

A class attribute is a Python variable that belongs to a class rather than a particular object.
It is shared between all the objects of this class
Behaviors are actions that can occur on an object.
The behaviors that can be performed on a specific class of object are called methods.

An object consists of :

State : Each class instance(Object) can have attributes attached to it for maintaining its state.
Behaviour : Class instances(Object) can also have methods (defined by their class) for modifying their state.
Identity: It gives a unique name to an object and enables one object to interact with other objects.

Class Definition Syntax:

class ClassName:
    # Statement-1
    .
    .
    .
    # Statement-N

class attributes and methods can be accessed using . operator after the class name
"""


class Dog:
    attr1 = "mammal"
    attr2 = "dog"

    def fun(self):
        print("I'm a", self.attr1)
        print("I'm a", self.attr2)


# Object instantiation
Rodger = Dog()

print(Rodger.attr1)
Rodger.fun()
print('\n')

"""
Constructors:
    Constructors are used to initializing the object’s state.
Constructor also contains a collection of statements that are executed at the time of object creation.
It runs as soon as an object of a class is instantiated.
Syntax of he constructor:
    def __init__(self):
    # body of the constructor

uses of a constructor:
    This method(constructor) is useful to do any initialization you want to do with your object.
    
Types of constructors : 
    1.default constructor:  The default constructor is a simple constructor which doesnt accept any arguments.
Its definition has only one argument which is a (self)reference to the instance being constructed.

    2.parameterized constructor: constructor with parameters is known as parameterized constructor.
The parameterized constructor takes its first argument as a reference to the instance being constructed
known as self and the rest of the arguments are provided by the programmer.

self:
    The self parameter is a reference to the current instance of the class,
and is used to access variables that belongs to the class.
It does not have to be named self , you can call it whatever you like,
but it has to be the first parameter of any function in the class:
"""


class DConstructor:

    def __init__(self):
        self.type = 'default'

    def my_type(self):
        print('my type is {} constructor'.format(self.type))


p = DConstructor()
p.my_type()
print('\n')


class PConstructor:

    def __init__(self, parameterized):
        self.type = parameterized

    def my_type(self):
        print('my type is {} constructor'.format(self.type))


p = PConstructor('parameterized')
p.my_type()
print('\n')
