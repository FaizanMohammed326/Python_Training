"""
Pandas DataFrames:
    A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array,
or a table with rows and columns.

1.Creating a Dataframe
"""
import pandas as pd

lst = ['example', 'for', 'dataframe', 'using', 'lists']

df1 = pd.DataFrame(lst)
print(df1)
print('\n')

"""
Creating DataFrame from dict of 2D array/lists

To create DataFrame from dict of 2D array/list, all the 2D array must be of same length.
If index is passed then the length index should be equal to the length of arrays.

If no index is passed, then by default, index will be range(n) where n is the array length.
"""

data = {'Name': ['Rahul', 'Ajay', 'Jack', 'Tom'],
        'Age': [20, 21, 19, 18]}

df2 = pd.DataFrame(data)
print(df2)
print('\n')

"""
Dealing with Rows and Columns
    We can perform basic operations on rows/columns like selecting, deleting, adding, and renaming.
Column Selection: In Order to select a column in Pandas DataFrame,
we can access the columns by calling them by their columns name.
"""

data1 = {'Name': ['Rahul', 'Ajay', 'Jack', 'Tom'],
         'Age': [20, 21, 19, 18],
         'Qualification': ['MCA', 'B-Tech', 'M-Tech', 'Phd']}
df3 = pd.DataFrame(data1)
print(df3[['Name', 'Qualification']])
print('\n')

"""
Row Selection: Pandas provide a unique method to retrieve rows from a Data frame.
DataFrame.loc[] method is used to retrieve rows from Pandas DataFrame.
Rows can also be selected by passing integer location to an iloc[] function.

"""
df4 = pd.DataFrame(data1, index=['a', 'b', 'c', 'd'])
ser_1 = df4.loc["c"]
ser_2 = df4.iloc[1]
print(ser_1, "\n\n", ser_2, '\n')


"""
selecting few rows and few column 
"""

# df4 = pd.DataFrame(data1, index=['a', 'b', 'c', 'd'])
ser_3 = df4[['Name', 'Qualification']][0:2]
print(ser_3)

