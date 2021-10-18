#WAP to remove all characters other than integers from a string

string = str(input('enter the input string:'))
for i in string:
    if not i.isdigit():
        string = string.replace(i,'')
print('the resulting string is {}'.format(string))
