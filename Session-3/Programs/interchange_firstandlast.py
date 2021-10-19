#WAP to interchange first and last element in a list

L = list(input('enter the list : ').split(','))
temp = L[0]
L[0] = L[-1]
L[-1] = temp
print('the list after interchanging the first and last elements is : ',L)