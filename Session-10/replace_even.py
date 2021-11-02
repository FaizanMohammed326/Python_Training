# WAP to replace even numbers with a name using dataframes inn pandas.


import pandas as pd

tables = {5: [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],
          6: [6, 12, 18, 24, 30, 36, 42, 48, 54, 60],
          7: [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]}

df = pd.DataFrame(tables, index=[i for i in range(1, 11)])
df.to_csv('tables.csv', index_label='x', sep='\t')

# to replace even numbers with key word "even"

df1 = pd.read_csv('tables.csv', sep='\t')
df1.set_index('x', inplace=True)
print(df1.to_string(), "\n")

# using mask()
df1 = df1.mask(df1 % 2 == 0, 'even')
print(df1, "\n")

"""col = list(df1.columns)
for i in col:
    for j in df1.index:
        print(int(df1[i][j]))"""
