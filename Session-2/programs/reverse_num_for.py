temp = num = int(input('enter the number:'))
size = 0
rev_num = 0
while temp>0:
    temp//=10
    size+=1

for i in range(0,size):
    rev_num = rev_num*10 + num%10
    num //= 10

print('the reversed number is {}'.format(rev_num))