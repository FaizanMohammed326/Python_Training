"""
There are two terms involved when we discuss generators.

1. Generator Function:
    A generator-function is defined like a normal function, but whenever it needs to generate a value,
it does so with the yield keyword rather than return.
If the body of a def contains yield, the function automatically becomes a generator function.

2. Generator-Object : Generator functions return a generator object. Generator objects are used either by
calling the next method on the generator object or using the generator object in a “for in” loop.
yield :
    The yield statement suspends function’s execution and sends a value back to the caller,
but retains enough state to enable function to resume where it is left off.
When resumed, the function continues execution immediately after the last yield run.
"""


def GeneratorFun():
    yield 1
    yield 2
    yield 3


obj1 = GeneratorFun()
for value in obj1:
    print(value)
print('\n')

obj2 = GeneratorFun()
print(next(obj2))
print(next(obj2))
print(next(obj2))
# print(next(obj2))
print('\n')
"""
Return sends a specified value back to its caller whereas Yield can produce a sequence of values.
We should use yield when we want to iterate over a sequence, but don’t want to store the entire sequence
in memory.
"""


def fib(limit):
    a, b = 0, 1

    for j in range(0, limit):
        yield a
        a, b = b, a + b


obj_fib = fib(10)
for i in obj_fib:
    print(i)
