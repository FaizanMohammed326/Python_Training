"""


instance variable are basically a class variable without a static modifier and is usually shared by all class instances.
Across different objects, these variables can have different values.
the contents of an instance variable are totally independent of one object instance to others.

There are two ways to access and create the instance variable of class:
1.Within the class by using self and object reference inside a constructor.
"""


class student:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno

    def display(self):
        print("hello my name is:", self.name)
        print("my roll number is:", self.rollno)


s = student('HARRY', 1001)
s.display()
print(s.name)
print('\n')

"""
2. using . operator on the object
"""
s.section = 'D'
print("my section is ", s.section)
print('\n')

"""
3.Using getattr() and setattr() method
"""


class emp:
    name = 'Harsh'
    salary = '25000'

    def show(self):
        print(self.name)
        print(self.salary)


e1 = emp()
print(getattr(e1, 'name'))
setattr(e1, 'height', 152)
print(getattr(e1, 'height'))
delattr(emp, 'salary')
print('\n')
"""
Scope of the variable:
    Instance variables are private to an instance and can only be modified by that instance.
    
Instance attributes are those attributes that are not shared by objects.
Every object has its own copy of the instance attribute and methods.
An instance method can access and even modify the value of attributes of an instance.

so similar to instance variables, instances methods have the same scope as variables.
"""


class shape:

    def __init__(self, edge, color):
        self.edge = edge
        self.color = color

    def finEdges(self):
        return self.edge

    def modifyEdges(self, newedge):
        self.edge = newedge


circle = shape(0, 'red')
square = shape(4, 'blue')

print("No. of edges for circle: " + str(circle.finEdges()))
square.modifyEdges(6)
print("No. of edges for square: " + str(square.finEdges()))
print('\n')
