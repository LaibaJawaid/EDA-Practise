import pandas as pd
import numpy as np

dataframe1 = {
    'storeId': [1, 2, 3, 4, 5, 6, 7, 8],
    'date': ['2024-01-01', '2024-01-02', '2024-01-06', '2024-01-02', 
             '2024-01-01', '2024-01-03', '2024-01-01', '2024-01-02'],
    'product_Cat': ['Electronics', 'Clothing', 'Food', 'Clothing',
                    'Electronics', 'Clothing', 'Electronics', 'Clothing'],
    'revenue': [1500, 800, 2200, 600, 1800, 900, 1200, 750],
    'unitsSold': [15, 40, 22, 30, 18, 45, 12, 38],
}

df= pd.DataFrame(dataframe1)
print("Original Dataframe: \n", df)

# Add new column based on Revenue per unit
df['revenue_per_unit'] = df['revenue'] / df['unitsSold']
print("\nDataframe after adding 'revenue_per_unit' column: \n", df)

# Find total revenue per product category
total_revenue = df.groupby('product_Cat')['revenue'].sum().reset_index()
print("\nTotal revenue per product category: \n", total_revenue)

# Highest revenue day
highest_revenue_day = df.loc[df['revenue'].idxmax()]
print("\nHighest revenue day: \n", highest_revenue_day)

# Create pivot for total units sold per store per product category
pivot_table = df.pivot_table(values='unitsSold', index='storeId', 
            columns='product_Cat', aggfunc='sum', fill_value=0)
print("\nPivot table of total units sold per store per product category: \n", pivot_table)

