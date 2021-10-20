# WAP to interchange first and last element in a list

Lst = list(input('enter the list : ').split(','))


def interchange(L):
    temp = L[0]
    L[0] = L[-1]
    L[-1] = temp
    print('the list after interchanging the first and last elements is : ', L)


interchange(Lst)
