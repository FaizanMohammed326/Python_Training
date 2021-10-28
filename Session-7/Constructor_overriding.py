"""
Constructor overriding is nothing but method overriding but here the method is a constructor method.
When we inherit a class from a base class we can inherit the constructor and add few more statements to it.
when we instantiate the new derived class to an object the new constructor is even though it has the same name
as its base class's constructor.

"""


class Parent:
    def __init__(self, name):
        self.name = name

    def func1(self):
        print("My name is ", self.name)


class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def func2(self):
        print(f"My name is {self.name} and my age is {self.age}")


obj1 = Parent('Dhoni')
obj2 = Child('Kohli', 32)
print('Parent`s Name: ', obj1.name)
print(f'Child`s Name: {obj2.name}, Age: {obj2.age}')
