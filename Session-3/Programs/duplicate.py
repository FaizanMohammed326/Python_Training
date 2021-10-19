# WAP to find duplicates in a list
# from collections import Counter

li = list(input('enter the list : ').split(','))
d = {}
for i in li:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1

'''
d = Counter(l)
'''
new_list = list([ele for ele in d if d[ele] > 1])  # list comprehension used
print(new_list)
