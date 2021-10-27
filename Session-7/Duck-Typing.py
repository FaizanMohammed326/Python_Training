"""
Duck Typing is a type system used in dynamic languages like python, javascript, PHP, Ruby, etc
Here the type or the class of an object is less important than the method it defines.

Using Duck Typing, we do not check types at all.
Instead, we check for the presence of a given method or attribute.


"""


class Bird:
    def fly(self):
        print("fly with wings")


class Airplane:
    def fly(self):
        print("fly with fuel")


class Rocket:
    def fly(self):
        print("fly with rich-fuel")


"""
class Fish:
    def swim(self):
        print("fish swim in sea")
"""


def fun(obj):
    obj.fly()


bird1 = Bird()
airplane1 = Airplane()
rocket1 = Rocket()
fun(bird1)
fun(airplane1)
fun(rocket1)


"""
Duck-typing emphasis what the object can really do, rather than what the object is.
"""
