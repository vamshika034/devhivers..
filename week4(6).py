#Project: Customer Records Data Cleaning
#Step 1 — Import Libraries
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

#Step 2 — Create Messy Dataset (Example)
data = {
    'Name': ['A', 'B', 'C', 'D', 'E'],
    'Age': ['25', '30', None, '45', '100'],  # string + missing + outlier
    'Salary': ['20000', '30000', '40000', None, '900000'],  # string + missing + outlier
    'Department': ['HR', 'IT', 'HR', 'Sales', None],  # missing category
    'JoinDate': ['2020-01-01', '2019-05-20', '2021-07-15', None, '2018-02-10']
}

df = pd.DataFrame(data)
print(df)

#Step 3 — Handle Missing Values
# Age & Salary numeric conversion first
df['Age'] = pd.to_numeric(df['Age'], errors='coerce')
df['Salary'] = pd.to_numeric(df['Salary'], errors='coerce')

# Fill numeric missing with mean
df['Age'].fillna(df['Age'].mean(), inplace=True)
df['Salary'].fillna(df['Salary'].mean(), inplace=True)

# Fill categorical missing
df['Department'].fillna('Unknown', inplace=True)

#Step 4 — Convert Data Types
df['JoinDate'] = pd.to_datetime(df['JoinDate'])
#Check types:
print(df.dtypes)


#Step 5 — Detect & Handle Outliers (IQR)
Q1 = df['Salary'].quantile(0.25)
Q3 = df['Salary'].quantile(0.75)
IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

# Cap outliers
df['Salary'] = df['Salary'].clip(lower, upper)

#Step 6 — Feature Scaling (Standardization)
scaler = StandardScaler()
df[['Age', 'Salary']] = scaler.fit_transform(df[['Age', 'Salary']])

#Step 7 — Encode Categorical Variables
df = pd.get_dummies(df, columns=['Department'])

#Step 8 — Final Cleaned Dataset
print(df)
