# Save and Load data from csv file:
import pandas as pd

data = {"names": ["ayush", "ramesh", "suresh"], "id": [156, 789, 158]}
df = pd.DataFrame(data)
print(df)

# Save and Load data to csv:
df.to_csv("Test_Data.csv", index=False)

# Read from csv:
load_df = pd.read_csv("3_test_data.csv")
print(load_df)

# Rows - Column Selection:
# select column:
print(df[["names"]])
print(load_df[["Employee_Name"]])

# select rows:
print(load_df.loc[load_df.Employee_Name == "Sarah Johnson"])

# more conditions in loc
print(
    load_df.loc[(load_df.Employee_Name == "Sarah Johnson") & (load_df.Salary >= 50000)]
)

# selecting rows with index: iloc
print(load_df.iloc[1])
print(load_df.iloc[0:5])

# same can be done with loc:
print(load_df.loc[0:3])

# value filtering in
print(load_df[load_df["Employee_ID"] >= 1002])
print(load_df[(load_df["Employee_ID"] >= 1002) & (load_df['Salary'] >= 60000)])

# more to condition:
print(load_df.where(load_df['Salary'] >= 60000, other="N/A"));


