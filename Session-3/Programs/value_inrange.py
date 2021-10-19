# WAP to test value of a dictionary in a given range

d = dict()
n = int(input('enter the length of the dictionary : '))
for i in range(0, n):
    key = input('enter the key : ')
    value = int(input('enter the value : '))
    d[key] = value

r_beg = int(input('enter the beginning of the range : '))
r_end = int(input('enter the end of the range : '))

result = list([k for k in d.keys() if (r_beg <= d[k] <= r_end)])
print('\nthe keys in the given range are', result)
