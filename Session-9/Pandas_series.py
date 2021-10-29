"""
Pandas is an open source Python package that is most widely used for data science/data analysis and
machine learning tasks. It is built on top of another package named Numpy,which provides support for
multi-dimensional arrays.

It has functions for analyzing, cleaning, exploring, and manipulating data.

Panda Series:
    Panda Series is like a column in a table
It is a one dimensional array holding the data of any type.
Pandas Series is nothing but a column in an excel sheet.
The object supports both integer and label-based indexing and provides a host of methods
for performing operations involving the index.

To create a panda series:
"""
import pandas as pd

data1 = ['e', 'x', 'a', 'm', 'p', 'l', 'e']
ser1 = pd.Series(data1)
print(ser1)
print('\n')

"""
If nothing else is specified, the values are labeled with their index number.
First value has index 0, second value has index 1 etc.
This label can be used to access a specified value.
"""

print(ser1[0])
print('\n')

"""
With the index argument, you can name your own labels.
"""

lst2 = [10, 12, 35, 28]
ser3 = pd.Series(lst2, index=['a', 'b', 'c', 'd'])
print(ser3)
print(ser3['b'])
print('\n')

"""
storing key value objects from dictionary to series
"""
w_hours = {'day1': 7, 'day2': 9, 'day3': 8}
w_ser = pd.Series(w_hours)
print(w_ser)
print('\n')

"""
To select only some of the items in the dictionary, use the index argument and specify only the items 
you want to include in the Series.
"""

w_ser1 = pd.Series(w_hours, index=['day1', 'day2'])
print(w_ser1)
