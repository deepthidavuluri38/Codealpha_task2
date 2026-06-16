import pandas as pd

# Sample Sales Dataset
data = {
    'Product': ['Laptop', 'Mobile', 'Tablet', 'Laptop', 'Mobile'],
    'Sales': [50000, 30000, 20000, 55000, 35000],
    'Quantity': [5, 10, 4, 6, 12],
    'Region': ['North', 'South', 'East', 'West', 'North']
}

df = pd.DataFrame(data)

# Dataset Overview
print("First 5 Rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nStatistical Summary:")
print(df.describe())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Business Questions
print("\nTotal Sales:", df['Sales'].sum())
print("Average Sales:", df['Sales'].mean())
print("Maximum Sales:", df['Sales'].max())
print("Minimum Sales:", df['Sales'].min())
