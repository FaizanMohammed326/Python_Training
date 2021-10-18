#WAP to reverse a number using for loop


num = int(input('enter the number to be reversed:'))
rev_num=0
while(num>0):
    rev_num = rev_num*10 + num%10;
    num = num // 10
print('reversed number is {}'.format(rev_num))

