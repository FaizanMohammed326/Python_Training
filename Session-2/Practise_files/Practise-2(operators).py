# Arithmetic Operators
print('examples of arithmetic operators')
a = 10
b = 3

add = a + b

sub = a - b

mul = a * b

div1 = a / b

div2 = a // b

mod = a % b

p = a ** b

print(add)
print(sub)
print(mul)
print(div1)
print(div2)
print(mod)
print(p)
print('\n')

#Comparison Operator

print('examples of comparison Operators')
a = 10
b = 29

print(a > b)
print(a < b)
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)
print('\n')

#Logical Operators
print('examples of Logical Operator')
a = False
b = True

print(a and b)
print(a or b)
print(not a)
print(0 or 30 or 23 or 0)
print(10 or 12)
print(20 and 40 and 50 and 0)
print(10 and 2 and 8)
print(0 or 40 and 0)
print(10 or 20 and 40 and 19)
print(10 or (20 and (40 and 19)))
print(((10 or 20) and 40) and 19)
print('\n')

#Bitwise operators

print('examples of Bitwise operators')
a = 20
b = 19

print(a & b)
print(a | b)
print(~a)
print(a ^ b)
print(a >> 2)
print(a << 2)
print('\n')

#assignment operator

print('examples of assignment operators')
a=10
b=20
c=b
x=3
print(a,b,c)
a+=4
b-=6
c/=2
c*=4
a<<=3
b>>=x
print('\n')

#Identity operator

print('examples of identity operators')
a=10
b=20
c=a

print(a is b)
print(a is not b)
print(a is c)
print(b is c)
print('\n')

#membership operator

print('examples of membership operator')

x=20
y=18
a=[10,20,30,40,50]
b='just an example'
l='x'
m='z'

if x in a:
    print('x is present in a')
else:
    print('x is not present in a')

if y not in a:
    print('y is not present in a')
else:
    print('y is present in a')

if l in b:
    print('{} is present in the string'.format(l))
else:
    print('{} is not present in the string'.format(l))

if m not in b:
    print('{} is not present in the string'.format(m))
else:
    print('{} is present in the string'.format(m))

