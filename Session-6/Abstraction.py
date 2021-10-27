"""
Abstraction in python is defined as a process of handling complexity by hiding unnecessary information
from the user.
In Python, abstraction can be achieved by having/using abstract classes and methods in our programs.

An abstract method in a base class identifies the functionality that should be implemented by all
its subclasses. However, since the implementation of an abstract method would differ from one subclass
to another, often the method body comprises just a pass statement.
Every subclass of the base class will ride this method with its implementation.

A class which contains one or more abstract methods is called an abstract class.
An abstract method is a method that has a declaration but does not have an implementation.

By default, Python does not provide abstract classes. Python comes with a module that provides the base for defining
Abstract Base classes(ABC) and that module name is ABC.
A method becomes abstract when decorated with the keyword @abstractmethod.
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def move(self):
        pass


class Human(Animal):
    def move(self):
        print("I can walk and run")


class Snake(Animal):
    def move(self):
        print("I can crawl")


class Dog(Animal):
    def move(self):
        print("I can bark")


class Lion(Animal):
    def move(self):
        print("I can roar")


R = Human()
R.move()

K = Snake()
K.move()

R = Dog()
R.move()

K = Lion()
K.move()
print('\n')

"""
Implementation Through Subclassing : 
    By subclassing directly from the base, we can avoid the need to register the class explicitly.
But A side-effect of using direct subclassing is, it is possible to find all the implementations of your plugin
by asking the base class for the list of known classes derived from it.
"""


class parent:
    def geeks(self):
        pass


class child(parent):
    def geeks(self):
        print("child class")


print(issubclass(child, parent))
print(isinstance(child(), parent))