#WAP to print multiplication table to a given range

num = int(input('enter the number:'))
r = int(input('enter the range:'))

for i in range(1,r+1):
    print('{} * {} = {}'.format(num,i,num*i))
