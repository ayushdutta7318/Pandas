# Rows and Columns Operations:
import pandas as pd

data = {
    "Employee_Name": ["ayush", "ramesh", "suresh", "sarah", "emily", "casandra"],
    "ID": [1001, 1002, 1003, 1004, 1005, 1006],
    "Salary": [7000000, 68000, 50000, 600000, 780000, 950000],
}
df = pd.DataFrame(data)
print(df)

# add new column
df["Team"] = ["CEO", "HR", "CTO", "DA", "Marketing", "Engineering"]
print(df)

df["Bonus"] = df["Salary"] * 0.2
print(df)

# add new row
df.loc[len(df)] = ["ABC", 1007, 75000, "IT", 2000]
print(df)

# update value using index:
df.loc[1, "Salary"] = 60000
print(df)

# update value using filter:
df.loc[df.Employee_Name == "ramesh", "Salary"] = 63000
print(df)

# delete rows and coln:
df.drop(df[df.Employee_Name == "ABC"].index, inplace=True)
print(df)

# delete coln:
df.drop('Bonus', axis=1, inplace = True);
print(df);

# delete multiple coln:
# df.drop(['Bonus', 'Team'], axis = 1, inplace = True);

# sorting:
df.sort_values('Salary', inplace=True);
print(df);

df.sort_values('Salary', ascending=False, inplace=True);
print(df);

# Working with date:
df['DOJ'] = ['2021-01-01', '2025-05-04', '2024-12-31', '2020-05-06', '2023-06-08', '2022-02-28'];
print(df);
print(df['DOJ'].dtype);

df['DOJ'] = pd.to_datetime(df['DOJ']);
print(df['DOJ'].dtype);

df2 = df;
df2['DOJ2'] = ['1-1-2021', '31-12-2020', '15-3-2026', '9-8-2024', '6-12-2022', '7-11-2023'];
print(df2['DOJ2'].dtype);

df2["DOJ2"] = pd.to_datetime(df2["DOJ2"], format= '%d-%m-%Y');
print(df2);

# extract day, date, month, year
print(df2["DOJ2"].dt.date)
print(df2["DOJ2"].dt.day)
print(df2["DOJ2"].dt.month)
print(df2["DOJ2"].dt.year)

df2['Year'] = df2["DOJ2"].dt.year;
print(df2);


# If we wanna add something to the row:
print(df);
df['DOJ'] = df["DOJ"] + pd.Timedelta(days=90);
print(df);

# Handling null values: used in real world when there are missing values in dataset.
import numpy as np;
df.loc[df.Employee_Name == "ramesh", "Salary"] = np.nan;
print(df);
print(df.isnull());
# to find total null val:
print(df.isnull().sum());

# to fill null value:
df.fillna(0, inplace=True);
print(df);

df.loc[df.Employee_Name == "ramesh", 'Salary'] = 63000;
print(df);

# Aggregation and Group by:
print(df['Year'].value_counts());#counts frequency of value in each coln
print(df[df['Year']==1].value_counts());

# grouping
print(df.groupby("Year")["Salary"].mean());#aggregation based on group
print(df.groupby('Year').agg({'Salary': 'mean', 'Employee_Name': 'count'}));

###################################################################################
# Concat Operation:

df1 = pd.DataFrame({'ID':[1,2,3], 'Name': ['A', 'B', 'C']});
print(df1);

df2 = pd.DataFrame({'ID':[4,5,6,7], 'Score': [78,95,165,24]});
print(df2);

print(pd.concat([df1, df2], axis = 0));
print(pd.concat([df1, df2], axis = 1));

# Merge:
print(pd.merge(df1, df2, how='inner', on='ID'));
print(pd.merge(df1, df2, how='right', on='ID'));
print(pd.merge(df1, df2, how='left', on='ID'));
print(pd.merge(df1, df2, how='inner', left_on='ID', right_on='ID'));

#AI and ChatGPT: for the given dataframe, create a filter for the employee who joined in january and has salary greater than 70000.
print(df);

filtered_df = df[
    (df['DOJ'].dt.month == 4) &
    (df['Salary'] > 70000)
]

print(filtered_df);