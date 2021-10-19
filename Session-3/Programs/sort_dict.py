# WAP to sort dictionary in ascending and descending order of the values

d = dict()
n = int(input('enter the length of the dictionary : '))
for i in range(0, n):
    key = input('enter the key : ')
    value = int(input('enter the value : '))
    d[key] = value


def return_value(k):
    return k[1]


sort_asc = sorted(d.items(), key=return_value)
sort_desc = sorted(d.items(), key=return_value, reverse=True)

print('the dictionary sorted in ascending order is : ',sort_asc)
print('the dictionary sorted in descending order is : ',sort_desc)

