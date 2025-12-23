import pandas as pd
import numpy as np
import re

emp_dataframe2 = {
    'emp_id': ['E001', 'E002', 'E003', 'E004', 'E005', None, 'E007'],
    'name': ['John-Doe', 'Jane Smith', 'Bob Johnson', 'Alice-Wong', 
             'Charlie Brown', 'David Lee', 'Eva_Green'],
    'depart': ['IT', 'Sales', 'IT', 'HR', 'Sales', 'IT', 'Marketing'],
    'salary': ['50000', '60000', '55000', '48000', '62000', '53000', '58000'],
    'join_date': ['2020-01-15', '2019-03-22', 'invalid', '2021-11-30',
                  '2018-06-14', '2022-02-28', '2020-09-15'],
    'contract_end': ['2023-12-31', '2022-12-31', '2023-06-30', '2024-05-31',
                     '2022-11-30', '2023-08-31', '2024-01-15'],
    'designation_type': ['Full-Time', 'Part-Time', 'Remote', 'Internee',
                         'Full-Time', 'Full-Time', 'Internee'],
    'performance_score': [85, 92, 78, 88, 90, 76, 95]
}

df2 = pd.DataFrame(emp_dataframe2)
print("Original Dataframe: \n", df2)

# Q1. Identify missing indices and fill missing 'emp_id'
missing_mask = df2['emp_id'].isna()

# 2. Logic: Get the ID immediately preceding the missing value
# We use shift(1) to look at the previous row's ID
prev_id = df2['emp_id'].shift(1).iloc[df2[missing_mask].index[0]]

# 3. Extract number from the previous ID (E005 -> 5), add 1, and format back to E006
prev_id_number = int(re.findall(r'\d+', prev_id)[0])
new_id = f'E{(prev_id_number + 1):03d}'

# 4. Fill the missing value
df2['emp_id'] = df2['emp_id'].fillna(new_id)
print("\nDataframe after filling missing 'emp_id' with sequential logic: \n", df2)


# Q2: Using multiple replace operations to clean 'name' column clean names with (-) and (_)

# modern Pandas requires you to explicitly set regex=False if you are replacing simple characters!
# Use a regex [-_] to catch both characters at once
df2['name_cleaned'] = df2['name'].str.replace(r'[-_]', ' ', regex=True)
print("Before cleaning vs After cleaning:")
for idx, row in df2.iterrows():
    print(f"{row['name']:15} -> {row['name_cleaned']}")

# Correctly replaced 'name' column with 'name_cleaned column' in df2
df2['name'] = df2['name_cleaned']
df2.drop(columns=['name_cleaned'], inplace=True)    # deleted this new column
print("Employee data after replacing names correctly:\n", df2)

# 5. Convert join_date to datetime, invalid dates become NaT
print("5. Join Date Conversion:")
print("Before conversion:")
print(df2[['emp_id', 'join_date']])

df2['join_date'] = pd.to_datetime(df2['join_date'], errors='coerce', format='%Y-%m-%d')
print("\nAfter conversion:")
print(df2[['emp_id', 'join_date']])
print(f"\nData types after conversion: {df2['join_date'].dtype}")


#Q3. Calculating experience of every employee

# 1. Ensure dates are in datetime format (handles 'invalid' as NaT)
df2['join_date'] = pd.to_datetime(df2['join_date'], errors='coerce')
df2['contract_end'] = pd.to_datetime(df2['contract_end'], errors='coerce')

# 2. Calculate experience in years
# We divide the difference in days by 365.25 for accuracy
df2['experience_years'] = (df2['contract_end'] - df2['join_date']).dt.days / 365.25

# 3. Round the result for readability (optional)
df2['experience_years'] = df2['experience_years'].round(2)
print("\n Calculating employees experience:")
# Show only the new column with name for context
print(df2[['name', 'experience_years']])

