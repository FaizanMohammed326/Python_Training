#WAP to find minimum and maximum element n a list
import math
L = list(map(int,(input('enter the list : ').split(','))))

# using min and max methods of list
# print(min(L),max(L))

# finding min and max by iterating through the list
min = math.inf
max = -math.inf
for i in L:
    if i<min:
        min = i
    if i>max:
        max = i
print('the minimum number in the list is ',min)
print('the maximum number in the list is ',max)
