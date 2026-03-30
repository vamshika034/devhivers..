#Convert Columns Using .astype()
import pandas as pd

data = {'Salary': ['10000', '20000', '30000']}
df = pd.DataFrame(data)

df['Salary'] = df['Salary'].astype(int)
print(df.dtypes)

#. Numeric → String Conversion
df['Salary'] = df['Salary'].astype(str)

#df['Salary'] = df['Salary'].astype(str)
df['Salary'] = pd.to_numeric(df['Salary'], errors='coerce')

#Parse Dates into Datetime
data = {'Birthdate': ['2001-05-10', '2000-11-21', '1999-01-15']}
df = pd.DataFrame(data)

df['Birthdate'] = pd.to_datetime(df['Birthdate'])
print(df.dtypes)

#Detect Mixed-Type Columns
print(df.dtypes)

#Complete Example (Real Practice)
import pandas as pd

data = {
    'Name': ['A', 'B', 'C'],
    'Salary': ['10000', '20000', '30000'],
    'Birthdate': ['2001-01-01', '2000-05-02', '1999-03-03']
}

df = pd.DataFrame(data)

# Convert salary to integer
df['Salary'] = df['Salary'].astype(int)

# Convert birthdate to datetime
df['Birthdate'] = pd.to_datetime(df['Birthdate'])

print(df)
print(df.dtypes)

