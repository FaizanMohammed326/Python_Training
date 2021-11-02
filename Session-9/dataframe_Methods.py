"""
drop():
    Pandas provide data analysts a way to delete and filter data frame using .drop() method.
Rows or columns can be removed using index label or column name using this method.
Syntax:
    DataFrame.drop(labels=None, axis=0, index=None, columns=None, level=None, inplace=False, errors=’raise’)

labels: String or list of strings referring row or column name.
axis: int or string value, 0 ‘index’ for Rows and 1 ‘columns’ for Columns.
index or columns: Single label or list. index or columns are an alternative to axis and cannot be used
    together.
level: Used to specify level in case data frame is having multiple level index.
inplace: Makes changes in original Data Frame if True.
errors: Ignores error if any value from the list doesn’t exists and drops rest of the values when
    errors = ‘ignore’
Return type: Dataframe with dropped values
"""
import pandas as pd

df = pd.read_csv('data.csv')
df.drop(['Duration'], axis=1, inplace=True)
print(df.to_string())
print('\n')
df2 = df.drop(df.index[0:40])
print(df2.to_string())
print('\n')

"""
.to_string():
    Use DataFrame.to_string() function to render the given DataFrame to a console-friendly tabular output.
"""

"""
.index()
    returns the index of the rows in dataframe 
"""

print(df.index[0:10])

"""
head(n):
    return top n rows from a dataframe
tail(n):
    return bottom n rows from a dataframe
"""
print(df.head(20).to_string())
print('\n')
print(df.tail(20).to_string())
