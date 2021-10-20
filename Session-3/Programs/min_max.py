# WAP to find minimum and maximum element n a list
import math
Lst = list(map(int, (input('enter the list : ').split(','))))


def min_max(L):
    # using min and max methods of list
    # print(min(L),max(L))

    # finding min and max by iterating through the list
    min_ele = math.inf
    max_ele = -math.inf
    for i in L:
        if i < min_ele:
            min_ele = i
        if i > max_ele:
            max_ele = i
    print('the minimum number in the list is ', min_ele)
    print('the maximum number in the list is ', max_ele)


min_max(Lst)
