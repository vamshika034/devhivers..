# Day 4: Pandas Grouping & Aggregation

import pandas as pd

print("----- CREATE SAMPLE DATA -----")

# Sample Student Data
data = {
    'Name': ['Ravi', 'Sita', 'Arjun', 'Meena', 'Kiran', 'Anita'],
    'Subject': ['Math', 'Science', 'Math', 'Science', 'Math', 'Science'],
    'Marks': [85, 90, 78, 92, 67, 88],
    'Gender': ['M', 'F', 'M', 'F', 'M', 'F']
}

df = pd.DataFrame(data)
print("\nOriginal DataFrame:")
print(df)

# -------------------------------
print("\n----- GROUP BY SUBJECT -----")

# Average marks by subject
print("\nAverage Marks by Subject:")
print(df.groupby('Subject')['Marks'].mean())

# Total marks by subject
print("\nTotal Marks by Subject:")
print(df.groupby('Subject')['Marks'].sum())

# Count of students per subject
print("\nCount by Subject:")
print(df.groupby('Subject')['Marks'].count())

# -------------------------------
print("\n----- GROUP BY GENDER -----")

# Average marks by gender
print("\nAverage Marks by Gender:")
print(df.groupby('Gender')['Marks'].mean())

# -------------------------------
print("\n----- MULTIPLE AGGREGATIONS -----")

# Using agg()
print("\nMultiple Aggregations (Subject):")
print(df.groupby('Subject')['Marks'].agg(['mean', 'sum', 'count', 'max', 'min']))

# -------------------------------
print("\n----- GROUP BY MULTIPLE COLUMNS -----")

# Group by Subject and Gender
print("\nSubject & Gender Analysis:")
print(df.groupby(['Subject', 'Gender'])['Marks'].mean())

# -------------------------------
print("\n----- PRACTICE TASKS -----")

# Task 1: Average marks by Gender
print("\nTask 1 - Avg Marks by Gender:")
print(df.groupby('Gender')['Marks'].mean())

# Task 2: Total marks by Subject
print("\nTask 2 - Total Marks by Subject:")
print(df.groupby('Subject')['Marks'].sum())

# Task 3: Count students by Gender
print("\nTask 3 - Count by Gender:")
print(df.groupby('Gender')['Name'].count())

# Task 4: Multiple aggregation
print("\nTask 4 - Multiple Aggregation:")
print(df.groupby('Gender')['Marks'].agg(['mean', 'max', 'min']))

# Task 5: Group by Subject & Gender
print("\nTask 5 - Subject & Gender Mean:")
print(df.groupby(['Subject', 'Gender'])['Marks'].mean())

# -------------------------------
print("\n----- TITANIC-LIKE EXAMPLE -----")

# Sample Titanic Data
titanic = {
    'Class': ['1st', '3rd', '2nd', '1st', '3rd', '2nd'],
    'Survived': [1, 0, 1, 1, 0, 1],
    'Fare': [100, 20, 50, 120, 15, 60]
}

df_titanic = pd.DataFrame(titanic)
print("\nTitanic Data:")
print(df_titanic)

# Survival rate by class
print("\nSurvival Rate by Class:")
print(df_titanic.groupby('Class')['Survived'].mean())

# Average fare by class
print("\nAverage Fare by Class:")
print(df_titanic.groupby('Class')['Fare'].mean())

# Multiple aggregation
print("\nFare Analysis:")
print(df_titanic.groupby('Class')['Fare'].agg(['mean', 'max', 'min']))