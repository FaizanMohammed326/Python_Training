#WAP to print smallest of the 3 numbers given

'''a=int(input())
b=int(input())
c=int(input())'''

x,y,z = (int(x) for x in input('enter three numbers \n').split(','))

if(x<y & x<z):
    print('{} is the smallest number'.format(x))
elif(y<z):
    print('{} is the smallest number'.format(y))
else:
    print('{} is the smallest number'.format(z))