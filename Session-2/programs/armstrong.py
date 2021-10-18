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

temp = num = int(input())
sum = 0
while(temp>0):
    sum += (temp%10)**3
    temp = temp // 10
if(num==sum):
    print('{} is an armstrong number'.format(num))
else:
    print('{} is not an armstrong number'.format(num))