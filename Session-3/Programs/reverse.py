#WAP to reverse a given list

l = list(input('enter the list to be reversed : ').split(','))
i=0
j=len(l)-1
while i<j:
    l[i],l[j] = l[j],l[i]
    i+=1
    j-=1
print('the reversed list is : ',l)