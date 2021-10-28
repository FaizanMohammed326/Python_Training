"""
users can define custom exceptions by creating a new class. This exception class has to be derived,
either directly or indirectly, from the built-in Exception class.
Most of the built-in exceptions are also derived from this class.

similar to the naming of the standard exceptions in python, we can follow the convention where we name
the exception class ending with "Error"

"""

"""
 Most implementations declare a custom base class and derive others exception classes from this base class.
This is the standard way to define user-defined exceptions in Python programming,
but you are not limited to this way only.

This example just inherits from exception class but doesnt override its methods.
"""


class Error(Exception):
    pass


class ValueTooSmallError(Error):
    pass


class ValueTooLargeError(Error):
    pass


number = 10
while True:
    try:
        i_num = int(input("Enter a number: "))
        if i_num < number:
            raise ValueTooSmallError
        elif i_num > number:
            raise ValueTooLargeError
        break

    except ValueTooSmallError:
        print("This value is too small, try again!", end='\n\n')

    except ValueTooLargeError:
        print("This value is too large, try again!", end='\n\n')

print("Congratulations! You guessed it correctly.")
print('\n')

"""
Customizing Exception Classes:
    We can further customize this class to accept other arguments as per our needs.
Let's look at one example:
"""


class SalaryNotInRangeError(Exception):
    def __init__(self, salary, message="Salary is not in (5000, 15000) range"):
        self.salary = salary
        self.message = message
        super().__init__(self.message)

    # __str__ return the value/message given in the exception as a message
    def __str__(self):
        return f'{self.salary} -> {self.message}'


Mysalary = int(input("Enter salary amount: "))

if not 5000 < Mysalary < 15000:
    raise SalaryNotInRangeError(Mysalary)

try:
    if not 5000 < Mysalary < 15000:
        raise SalaryNotInRangeError(Mysalary, message="salary not in range")

except SalaryNotInRangeError:
    print("salary not in range")

else:
    Mysalary -= 5000
    print('salary is in the given range')

