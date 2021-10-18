#WAP to remove all characters other than integers from a string

string = str(input('enter the input string:'))
digits = ['0','1','2','3','4','5','6','7','8','9']
for i in string:
    if i not in digits:
        string = string.replace(i,'')
print('the resulting string is {}'.format(string))
