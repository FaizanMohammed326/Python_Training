"""
Assertion:
    It takes an expression as an argument and raises a python exception
if the expression has a False Boolean value.
if the expression is true it performs no operation.

the exception it raises is AssertionError

We can use assertions to check for valid input and output to functions.
"""

assert True

# assert False

try:
    print(1)
    assert 2 + 2 == 4
    print(2)
    assert 1 + 2 == 4
    print(3)
except AssertionError:
    print("An assert failed.")
finally:
    print("Done")

"""
Second Argument to assert
    You may optionally provide a second argument to give out some extra information about the problem.
"""

assert (2/3 == 2//3), "the operators are different"
