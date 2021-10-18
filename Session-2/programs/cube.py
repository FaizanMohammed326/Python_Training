#WAP to write cube of numbers from 1 to a given number

num = int(input('enter the number:'))
for i in range(1,num+1):
    print('cube of {} is {}'.format(i,i**3))
