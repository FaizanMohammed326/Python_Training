#WAP to checck whether given number is armstrong or not

'''
num = str(input())
arr = []
sum = 0
for i in num:
    arr.append(int(i))
for j in arr:
    sum = sum + j**3
if(int(num))==sum:
    print('{} is an armstrong number'.format(int(num)))
else:
    print('{} is not an armstrong number'.format(int(num)))
'''

temp1 = temp2 = num = int(input('enter the number:'))
order=0
while temp1>0:
    order+=1
    temp1//=10
sum = 0
while temp2>0:
    sum += (temp2%10)**order
    temp2 = temp2 // 10
if(num==sum):
    print('{} is an armstrong number'.format(num))
else:
    print('{} is not an armstrong number'.format(num))