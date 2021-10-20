# WAP to reverse a given list

lst = list(input('enter the list to be reversed : ').split(','))


def rev(li):
    i = 0
    j = len(li) - 1
    while i < j:
        li[i], li[j] = li[j], li[i]
        i += 1
        j -= 1
    print('the reversed list is : ', li)


rev(lst)