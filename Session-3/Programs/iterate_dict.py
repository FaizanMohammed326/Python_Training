# WAP to iterate over a dictionary

d = dict()
n = int(input('enter the length of the dictionary : '))
for i in range(0, n):
    key = input('enter the key : ')
    value = input('enter the value : ')
    d[key] = value

print('\n the given dicionary is :\n')
for key, value in d.items():
    print('key : {} , value : {}'.format(key, value))
