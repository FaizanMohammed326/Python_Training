# WAP to find factorial of a number using recursion


def fact(n):
    if n == 0:
        return 1
    else:
        return n*fact(n-1)


num = int(input('enter the number : '))
if num<0:
    print('invalid number')
else:
    res = fact(num)
    print('the factorial of the number is :', res)