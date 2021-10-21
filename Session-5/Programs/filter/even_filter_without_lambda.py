# WAP to filter even numbers from a list using filter but without using lambda expression


lst = [int(x) for x in input('enter the list to be filtered : ').split(',')]


def even(x):
    if x % 2 == 0:
        return True
    else:
        return False


res = list(filter(even, lst))
print('even numbers in the list after the filter : ', res)
