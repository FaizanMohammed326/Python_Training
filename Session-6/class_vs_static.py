"""
Class Method:
    A class method is a method that is bound to the class and not the object of the class.
A class method receives the class as an implicit first argument,
just like an instance method receives the instance
It can modify a class state that would apply across all the instances of the class.
For example, it can modify a class variable that will be applicable to all the instances.

We use @classmethod decorator in python to create a class method

Static Method:
    A static method does not receive an implicit first argument.
A static method is also a method that is bound to the class and not the object of the class.
A static method can’t access or modify the class state. i.e class variables

we use @staticmethod decorator to create a static method in python.
"""

from datetime import date


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # a class method to create a Person object by birth year.
    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year)

    # a static method to check if a Person is adult or not.
    @staticmethod
    def isAdult(age):
        return age > 18


person1 = Person('faizan', 23)
person2 = Person.fromBirthYear('faizan', 1998)

print(person1.age)
print(person2.age)
print(Person.isAdult(22))
