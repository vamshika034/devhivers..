# Day 1: Pandas Series & DataFrames - Single Program

import pandas as pd

print("----- PANDAS SERIES -----")

# Create Series from list
fruits = ['apple', 'banana', 'mango', 'orange']
series_fruits = pd.Series(fruits)
print("\nFruits Series:")
print(series_fruits)

# Series with custom index
scores = [85, 90, 78, 92]
series_scores = pd.Series(scores, index=['A', 'B', 'C', 'D'])
print("\nScores Series with custom index:")
print(series_scores)

print("\n----- PANDAS DATAFRAME -----")

# Create DataFrame from dictionary
data = {
    'Name': ['Ravi', 'Sita', 'Arjun', 'Meena'],
    'Age': [20, 21, 19, 22],
    'Grade': ['A', 'B', 'A', 'C']
}

df = pd.DataFrame(data)
print("\nStudent DataFrame:")
print(df)

print("\n----- BASIC EXPLORATION -----")

# Head
print("\nFirst 5 rows:")
print(df.head())

# Tail
print("\nLast 5 rows:")
print(df.tail())

# Describe
print("\nSummary Statistics:")
print(df.describe())

# Data types
print("\nData Types:")
print(df.dtypes)

print("\n----- PRACTICE TASKS -----")

# Task 1: Series
marks = [70, 85, 90, 60]
student_marks = pd.Series(marks)
print("\nStudent Marks Series:")
print(student_marks)

# Task 2: DataFrame
students = {
    'Name': ['Rahul', 'Anita', 'Kiran'],
    'Marks': [88, 76, 95],
    'City': ['Bangalore', 'Mysore', 'Mangalore']
}

df_students = pd.DataFrame(students)
print("\nStudents DataFrame:")
print(df_students)

# Task 3: Exploration
print("\nStudents DataFrame Head:")
print(df_students.head())

print("\nStudents DataFrame Tail:")
print(df_students.tail())

print("\nStudents DataFrame Summary:")
print(df_students.describe())

print("\nStudents DataFrame Data Types:")
print(df_students.dtypes)