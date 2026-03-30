#Normalization (Min-Max Scaling)
import pandas as pd

data = {'Marks': [40, 60, 80, 100]}
df = pd.DataFrame(data)

df['Normalized'] = (df['Marks'] - df['Marks'].min()) / \
                   (df['Marks'].max() - df['Marks'].min())

print(df)

#Standardization (Z-Score Scaling)
df['Standardized'] = (df['Marks'] - df['Marks'].mean()) / df['Marks'].std()
print(df)
#Using Scikit-Learn (Recommended)
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
df['Marks_norm'] = scaler.fit_transform(df[['Marks']])

#Standardization
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
df['Marks_std'] = scaler.fit_transform(df[['Marks']])

#Example: Normalize Student Marks
data = {'Math': [40, 80, 60],
        'Science': [30, 90, 50]}

df = pd.DataFrame(data)

from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
df_scaled = scaler.fit_transform(df)

print(df_scaled)

#Example: Standardize Salary
data = {'Salary': [20000, 30000, 40000, 100000]}
df = pd.DataFrame(data)

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
df['Salary_std'] = scaler.fit_transform(df[['Salary']])

print(df)

