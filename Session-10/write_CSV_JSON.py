"""
We will be using the to_csv() method to save a DataFrame as a csv file.
To save the DataFrame with tab separators, we have to pass “\t” as the sep parameter in the to_csv() method.

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
print(df.to_string())
df.to_csv("students.csv", index_label='No.')
df.to_csv("students2.csv", index=False, sep='\t')
print('\n')

"""
to write t a json file we use to_json() method
"""

df.to_json('students.json')
json = df.to_json()
print(type(json), "\n")
print('default orient as column = ', json, "\n")
"""
There are 6 orients in json to save to
‘split’, ‘records’, ‘index’, ‘columns’, ‘values’, ‘table’
by default to_json() saves series in "index" orient and dataframes in "column" orient
    
"""
json_split = df.to_json(orient='split')
print("json_split = ", json_split, "\n")

json_records = df.to_json(orient='records')
print("json_records = ", json_records, "\n")

json_index = df.to_json(orient='index')
print("json_index = ", json_index, "\n")

json_columns = df.to_json(orient='columns')
print("json_columns = ", json_columns, "\n")

json_values = df.to_json(orient='values')
print("json_values = ", json_values, "\n")

json_table = df.to_json(orient='table')
print("json_table = ", json_table, "\n")
