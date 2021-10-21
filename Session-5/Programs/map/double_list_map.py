# WAP to double all values in a list with map (without lambda expression)


def double(x):
    return x + x


lst = [int(x) for x in input('enter the list : ').split(',')]
res = list(map(double, lst))
print('list after doubling its elements : ', res)
