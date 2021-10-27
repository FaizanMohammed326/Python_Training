"""
Polymorphism:
    The word polymorphism means having many forms. In programming, polymorphism means the same function name
being used for different types.

Example of inbuilt polymorphic functions :
"""

print(len("geeks"))

print(len([10, 20, 30]))
print('\n')

"""
Examples of method-overloading using default arguments (user-defined polymorphic functions):

"""


def add(x, y, z=0):
    return x + y + z


print(add(2, 3))
print(add(2, 3, 4))
print('\n')

"""
Example of method-overloading using variable length arguments

"""


class Calculate:
    def add(self, *args):
        result = 0
        for param in args:
            result += param
        print("Result: {}".format(result))


c1 = Calculate()
c1.add(10, 20, 30)
c1.add(10, 20)
print('\n')
"""
Polymorphism with Inheritance(method-overriding): 
    Polymorphism lets us define methods in the child class that have the same name
as the methods in the parent class.
In inheritance, the child class inherits the methods from the parent class.
However, it is possible to modify a method in a child class that it has inherited from the parent class.
This process of re-implementing a method in the child class is known as Method Overriding.
"""


class Bird:

    def flight(self):
        print("Most of the birds can fly but some cannot.")


class sparrow(Bird):
    def flight(self):
        print("Sparrows can fly.")


class ostrich(Bird):
    def flight(self):
        print("Ostriches cannot fly.")


obj_bird = Bird()
obj_spr = sparrow()
obj_ost = ostrich()
obj_bird.flight()
obj_spr.flight()
obj_ost.flight()
print('\n')

"""
Polymorphism with a Function and objects: (Duck-Typing)
"""


class India:
    def capital(self):
        print("New Delhi is the capital of India.")

    def language(self):
        print("Hindi is the most widely spoken language of India.")

    def type(self):
        print("India is a developing country.")


class USA:
    def capital(self):
        print("Washington, D.C. is the capital of USA.")

    def language(self):
        print("English is the primary language of USA.")

    def type(self):
        print("USA is a developed country.")


def func(obj):
    obj.capital()
    obj.language()
    obj.type()


obj_ind = India()
obj_usa = USA()

func(obj_ind)
func(obj_usa)
