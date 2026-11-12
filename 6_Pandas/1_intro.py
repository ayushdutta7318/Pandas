# Pandas Introduction:
import pandas as pd

print(f"Pandas Version: {pd.__version__}")

"""
What is a DataFrame in Pandas?
Simple Explanation

A DataFrame is the most important data structure in Pandas.

Think of it as an Excel spreadsheet inside Python.

It has:

Rows (records)
Columns (fields/attributes)
Data organized in a table format

Example:

Employee_ID	Name	Salary
101	John	50000
102	Sarah	60000
103	Mike	55000
"""

# Create DataFrame:
df = pd.DataFrame([37, 45, 189])
print(df)

# togive column name in above:
df = pd.DataFrame([37, 45, 189], columns=["Column_Name"])
print(df)

# Create DataFrame using Dictionary:
data = {"names": ["ayush", "ramesh", "suresh"], "id": [145, 45, 39]}

df_1 = pd.DataFrame(data)
print(df_1)
print(type(df_1))

# head: gives raw data
print(df_1.head(3))
print(df_1.tail(3))
print(df_1.columns)

# column rename
df_1 = df_1.rename(columns={"names": "n"})
print(df_1)

df_1.rename(columns={"n": "employee"}, inplace=True);#inplace = true, you dont have to write df_1 = df_1.rename().
print(df_1);

# info()
print(df_1.info());

# describe:
print(df_1.describe());