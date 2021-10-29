"""
A simple way to store big data sets is to use CSV files
CSV files contains plain text and is a well know format that can be read by everyone including Pandas.
read_csv() is used to read a csv file into a data frame.

By default, when you print a DataFrame, you will only get the first 5 rows, and the last 5 rows:
"""

import pandas as pd

df = pd.read_csv('data.csv')
print(df)  # By default, when you print a DataFrame, you will only get the first 5 rows, and the last 5 rows:
print(df.to_string())
print('\n')

"""
Big data sets are often stored, or extracted as JSON.
JSON is plain text, but has the format of an object, and is well known in the world of programming,
including Pandas.

"""
df1 = pd.read_json('data.json')
print(df1.to_string())
