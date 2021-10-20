# WAP to test value of a dictionary in a given range

dct = dict()
n = int(input('enter the length of the dictionary : '))
for i in range(0, n):
    key = input('enter the key : ')
    value = int(input('enter the value : '))
    dct[key] = value

r_beg = int(input('enter the beginning of the range : '))
r_end = int(input('enter the end of the range : '))


def in_range(d, beg, end):
    result = list([k for k in d.keys() if (beg <= d[k] <= end)])
    print('\nthe keys in the given range are', result)


in_range(dct, r_beg, r_end)
