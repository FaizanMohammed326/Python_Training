#WAP to print multiplication table to a given range

num = int(input('beginning of the range:'))
r = int(input('end of the range:'))

for i in range(num,r+1):
    for j in range(1,11):
        print('{} * {} = {}'.format(i,j,i*j))

