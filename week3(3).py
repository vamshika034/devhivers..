# Day 3: Pandas Indexing & Filtering

import pandas as pd

print("----- CREATE SAMPLE DATA -----")

# Sample Data (Students)
data = {
    'Name': ['Ravi', 'Sita', 'Arjun', 'Meena', 'Kiran'],
    'Marks': [85, 90, 78, 92, 67],
    'Age': [20, 21, 19, 22, 20],
    'City': ['Bangalore', 'Mysore', 'Mangalore', 'Delhi', 'Bangalore']
}

df = pd.DataFrame(data)
print("\nOriginal DataFrame:")
print(df)

# -------------------------------
print("\n----- USING loc[] (LABEL BASED) -----")

# Select rows 0 to 2
print("\nRows 0 to 2:")
print(df.loc[0:2])

# Select specific columns
print("\nName and Marks columns:")
print(df.loc[:, ['Name', 'Marks']])

# -------------------------------
print("\n----- USING iloc[] (POSITION BASED) -----")

# Select first 3 rows
print("\nFirst 3 rows:")
print(df.iloc[0:3])

# Select specific rows & columns
print("\nRows 1 to 3 and first 2 columns:")
print(df.iloc[1:4, 0:2])

# -------------------------------
print("\n----- CONDITIONAL FILTERING -----")

# Students with Marks > 80
print("\nMarks > 80:")
print(df[df['Marks'] > 80])

# Students from Bangalore
print("\nCity = Bangalore:")
print(df[df['City'] == 'Bangalore'])

# -------------------------------
print("\n----- BOOLEAN INDEXING (MULTIPLE CONDITIONS) -----")

# Marks > 80 AND Age < 22
print("\nMarks > 80 AND Age < 22:")
print(df[(df['Marks'] > 80) & (df['Age'] < 22)])

# Marks > 80 OR City = Delhi
print("\nMarks > 80 OR City = Delhi:")
print(df[(df['Marks'] > 80) | (df['City'] == 'Delhi')])

# -------------------------------
print("\n----- SLICING DATAFRAME -----")

# Slice rows 1 to 3
print("\nRows 1 to 3:")
print(df[1:4])

# Slice specific columns
print("\nOnly Name and City:")
print(df[['Name', 'City']])

# -------------------------------
print("\n----- PRACTICE TASKS -----")

# Task 1: Marks > 75
print("\nTask 1 - Marks > 75:")
print(df[df['Marks'] > 75])

# Task 2: Age < 21
print("\nTask 2 - Age < 21:")
print(df[df['Age'] < 21])

# Task 3: Bangalore students with Marks > 80
print("\nTask 3 - Bangalore & Marks > 80:")
print(df[(df['City'] == 'Bangalore') & (df['Marks'] > 80)])

# Task 4: Select Name & Age using loc
print("\nTask 4 - Name & Age:")
print(df.loc[:, ['Name', 'Age']])

# Task 5: Select first 2 rows using iloc
print("\nTask 5 - First 2 rows:")
print(df.iloc[0:2])

# -------------------------------
print("\n----- TITANIC-LIKE EXAMPLE -----")

# Sample Titanic Data
titanic = {
    'Name': ['A', 'B', 'C', 'D', 'E'],
    'Age': [22, 38, 26, 35, 28],
    'Class': ['1st', '3rd', '2nd', '1st', '3rd'],
    'Survived': [1, 0, 1, 1, 0]
}

df_titanic = pd.DataFrame(titanic)
print("\nTitanic Data:")
print(df_titanic)

# Filter passengers Age > 30
print("\nAge > 30:")
print(df_titanic[df_titanic['Age'] > 30])

# Filter survived passengers
print("\nSurvived = 1:")
print(df_titanic[df_titanic['Survived'] == 1])

# Filter 1st class passengers
print("\nClass = 1st:")
print(df_titanic[df_titanic['Class'] == '1st'])