"""
Inheritance is the capability of one class to derive or inherit the properties from another class.
The class that derives properties is called the derived class or base class and
the class from which the properties are being derived is called the base class or parent class.

The benefits of inheritance are:
    It provides the re-usability of a code. We don’t have to write the same code again and again.
Also, it allows us to add more features to a class without modifying it.
    It is transitive in nature, which means that if class B inherits from another class A,
then all the subclasses of B would automatically inherit from class A.

Inheritance example s shown below:
"""


class Person:

    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber

    def display(self):
        print(self.name)
        print(self.idnumber)

    def details(self):
        print("My name is {}".format(self.name))
        print("IdNumber: {}".format(self.idnumber))


# child class
class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post
        Person.__init__(self, name, idnumber)

    def details(self):
        super().details()
        print("Post: {}".format(self.post))


a = Employee('Rahul', 886012, 200000, "Intern")

a.display()
a.details()
print('\n')

"""
Types of Inheritance depends upon the number of child and parent classes involved.
There are five types of inheritance in Python:

1. Single Inheritance:
    Single inheritance enables a derived class to inherit properties from a single parent class
"""


class Parent:
    def func1(self):
        print("This function is in parent class.")


class Child(Parent):
    def func2(self):
        print("This function is in child class.")


obj1 = Child()
obj1.func1()
obj1.func2()
print('\n')

"""
2. Multiple Inheritance:
    When a class can be derived from more than one base class this type of inheritance is called multiple inheritance.
In multiple inheritance, all the features of the base classes are inherited into the derived class. 
"""


class Length:
    length = 0

    def mother(self):
        print(self.length)


class Breadth:
    breadth = 0

    def father(self):
        print(self.breadth)


class Rectangle(Length, Breadth):
    def area(self):
        print("Length :", self.length)
        print("Breadth :", self.breadth)
        print("Area : ", self.length * self.breadth)


s1 = Rectangle()
s1.length = 8
s1.breadth = 5
s1.area()
print('\n')

"""
3. Multilevel Inheritance:
    In multilevel inheritance, features of the base class and the derived class are further inherited into the new
derived class.
This is similar to a relationship representing a child and grandfather.
"""


class Family_Member:
    def show_family(self):
        print("These are the family members :")


class Father(Family_Member):
    father_name = ""

    def show_father(self):
        print(self.father_name)


# Mother class inherited from Family
class Mother(Family_Member):
    mother_name = ""

    def show_mother(self):
        print(self.mother_name)


# Son class inherited from Father and Mother classes
class Son(Father, Mother):
    def show_parent(self):
        print("Father :", self.father_name)
        print("Mother :", self.mother_name)


s1 = Son()
s1.father_name = "Mark"
s1.mother_name = "Sonia"
s1.show_family()
s1.show_parent()

"""
4. Hierarchical Inheritance:
    When more than one derived classes are created from a single base this type of inheritance is called
hierarchical inheritance.
In this program, we have a parent (base) class and two child (derived) classes.
"""


class Parent:
    def func1(self):
        print("This function is in parent class.")


class Child1(Parent):
    def func2(self):
        print("This function is in child 1.")


class Child2(Parent):
    def func3(self):
        print("This function is in child 2.")


object1 = Child1()
object2 = Child2()
object1.func1()
object1.func2()
object2.func1()
object2.func3()
print('\n')
"""
5.Hybrid Inheritance:
    Inheritance consisting of multiple types of inheritance is called hybrid inheritance.
"""


class University:

    def __init__(self):
        self.univ = "MIT"

    def display(self):
        print(f"The University name is: {self.univ}")


class Course(University):
    def __init__(self):
        super().__init__()
        self.course = "CSE"

    def display(self):
        print(f"The Course name is: {self.course}")


class Branch(University):
    def __init__(self):
        super().__init__()
        self.branch = "Data Science"

    def display(self):
        print(f"The Branch name is: {self.branch}")


class Student(Course, Branch):
    def __init__(self):
        self.name = "Tonny"
        Branch.__init__(self)
        Course.__init__(self)

    def display(self):
        print(f"The Name of the student is: {self.name}")
        super(Branch, self).display()
        super(Course, self).display()
        super().display()
        # University.display(self)
        # Branch.display(self)
        # Course.display(self)


ob = Student()
ob.display()
B = Branch()
print(Student.__mro__)
# The method resolution order (or MRO) tells Python how to search for inherited methods.
# print(Student.__mro__)
