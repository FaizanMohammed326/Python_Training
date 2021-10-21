# WAP to double the elements in a list using map with lambda expressions

lst = [int(x) for x in input('enter the list : ').split(',')]
res = list(map(lambda x: x + x, lst))
print('list after doubling its elements : ', res)

