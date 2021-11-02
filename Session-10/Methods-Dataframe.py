"""
.replace()
    Pandas dataframe.replace() function is used to replace a string, regex, list, dictionary, series, number etc. from a dataframe.
This is a very rich function as it has many variations.

Syntax: DataFrame.replace(to_replace=None, value=None, inplace=False, limit=None, regex=False, method=’pad’,
axis=None)


"""
import pandas as pd

students = {'Student': ['Rahul', 'Andrew',
                        'Arjun', 'Dave'],
            'RollNumber': [1, 5, 10, 15],
            'Grade': ['A', 'C', 'D', 'S']}
df = pd.DataFrame(students,
                  index=[i for i in range(1, 5)],
                  columns=['Student', 'RollNumber',
                           'Grade'])
print(df, "\n")

df.replace('C', 'B', inplace=True)
df.replace('A.+', 'Name starting with A', regex=True, inplace=True)
print(df, "\n")

"""
mask()

dataframe.mask() function return an object of same shape as self and whose corresponding entries
are from self where cond is False and otherwise are from other object.

"""

df['RollNumber'] = df['RollNumber'].mask(df['RollNumber'] >= 10, 'more than 10', errors="ignore")
print(df, '\n')


def even(x):
    if x % 2 == 0:
        return True
    else:
        return False


"""
insert()

Syntax:
    DataFrameName.insert(loc, column, value, allow_duplicates = False)
"""
df.insert(2, 'Hometown', 'unknown')
print(df.to_string(), "\n")


"""
loc[]
    Pandas DataFrame.loc attribute access a group of rows and columns by label(s)
also we can use it to add new rows into the data frame
"""
print(df.loc[2])
print(df.loc[:, 'Grade'])
print(df.loc[1:2, ['RollNumber', 'Grade']])


df.loc[5] = ['Rahul', 1, 'Bangalore', 'A']
print(df.to_string(), "\n")

"""
iloc[]
    Dataframe.iloc[] method is used when the index label of a data frame is something other than numeric series
of 0, 1, 2, 3….n or in case the user doesn’t know the index label.
But we cannot add new entries to new indices but can alter the rows of existing indices
"""
print(df.iloc[2])
print(df.loc[2, 'Grade'], '\n')

df.iloc[0] = ['Rahul', 1, 'Bangalore', 'A']


"""
drop_duplicates()
    used to drop all the duplicate rows from the dataframe
"""


