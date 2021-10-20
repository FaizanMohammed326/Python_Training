# WAP to find factorial of a number without using recursion


def fact(n):
    res = 1
    for i in range(2,n+1):
        res = res * i
    return res


num = int(input('enter the number : '))
if num < 0:
    print('invalid number')
else:
    print('the factorial of the number is :', fact(num))
