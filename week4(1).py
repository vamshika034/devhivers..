#Identify Missing Values
import pandas as pd

data = {
    'Name': ['A', 'B', 'C', 'D'],
    'Marks': [90, None, 85, None]
}

df = pd.DataFrame(data)

print(df.isnull())
#Count missing values:
df.isnull().sum()
#Check non-missing:
df.notnull()

#Drop Missing Values
df.dropna()
#Remove columns with missing values:
df.dropna(axis=1)
#Drop only if all values missing:
df.dropna(how='all')
#Fill Missing Values
#Fill with Mean
df['Marks'].fillna(df['Marks'].mean(), inplace=True)
#Fill with Median
df['Marks'].fillna(df['Marks'].median(), inplace=True)
#Fill with Mode
df['Marks'].fillna(df['Marks'].mode()[0], inplace=True)
#Fill with Custom Value
df['Marks'].fillna(0, inplace=True)

#Forward Fill (ffill)
#Copies previous value ⬇
df.fillna(method='ffill', inplace=True)

#Backward Fill (bfill)
#Copies next value ⬆
df.fillna(method='bfill', inplace=True)

#Complete Example: Student Marks Cleaning
import pandas as pd

data = {
    'Name': ['A', 'B', 'C', 'D'],
    'Marks': [90, None, 85, None]
}

df = pd.DataFrame(data)

# Identify missing
print(df.isnull().sum())

# Fill with mean
df['Marks'].fillna(df['Marks'].mean(), inplace=True)

print(df)



