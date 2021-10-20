# WAP to iterate over a dictionary

n = int(input('enter the length of the dictionary : '))
d = dict()
for i in range(0, n):
    key = input('enter the key : ')
    value = input('enter the value : ')
    d[key] = value


def iterate(dct):
    print('\n the given dictionary is :\n')
    for k, v in dct.items():
        print('key : {} , value : {}'.format(k, v))


iterate(d)
