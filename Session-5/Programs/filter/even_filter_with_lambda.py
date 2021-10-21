# WAP to filter even numbers from a list using filter() with lambda expression

lst = [int(x) for x in input('enter the list to be filtered : ').split(',')]
res = list(filter(lambda x: x % 2 == 0, lst))
print('even numbers in the list after the filter : ', res)
