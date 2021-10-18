#For loop
count=0
while(count<2):
    count += 1
    print("hello world")
print('\n')

#while loop
# iterating over a list
L = ['this','is','a','while','loop','example']
for i in L:
    print(i,end=' ')
print('\n')

#while-else loop

j=0
while j<4:
    j += 4
    print(j)
else:
    print("no break")
print('\n')

j=0
while j<4:
    j += 4
    print(j)
    break
else:
    #not executed bcs break is used
    print("break")
print('\n')

#Continue
for letter in 'justanexample':
    if letter in 'aeiou':
        continue
    print('current letter: ',letter)
print('\n')

#Break
for letter in 'complexword':
    if letter in 'aeiou':
        break
    print('current letter: ', letter)
print('\n')

#Pass
for letter in 'justanexample':
    pass
print('last word:',letter)
print('\n')

#If statement
i = 15
if i>10:
    print('i is the greater than 10')
print('\n')

#if-else
i = 20
if (i < 15):
    print("i is smaller than 15")
else:
    print("i is greater than 15")
print('\n')

#if-elif-else
i = 20
if (i == 10):
    print("i is 10")
elif (i == 15):
    print("i is 15")
elif (i == 20):
    print("i is 20")
else:
    print("i is unknown")
print('\n')

#shorthand if and if-else
i = 10
if i<12: print('i is less than 12')
print('\n')

print(True) if i>12 else print(False)
print('\n')