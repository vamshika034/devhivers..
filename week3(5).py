# Day 5: Pandas Merging & Joining

import pandas as pd

print("----- CREATE SAMPLE DATA -----")

# Student Info
students = {
    'ID': [1, 2, 3, 4],
    'Name': ['Ravi', 'Sita', 'Arjun', 'Meena'],
    'Age': [20, 21, 19, 22]
}
df_students = pd.DataFrame(students)

# Exam Scores
scores = {
    'ID': [1, 2, 3, 5],
    'Marks': [85, 90, 78, 88]
}
df_scores = pd.DataFrame(scores)

print("\nStudents Data:")
print(df_students)

print("\nScores Data:")
print(df_scores)

# -------------------------------
print("\n----- MERGE (INNER JOIN) -----")

inner_merge = pd.merge(df_students, df_scores, on='ID', how='inner')
print("\nInner Join:")
print(inner_merge)

# -------------------------------
print("\n----- LEFT JOIN -----")

left_merge = pd.merge(df_students, df_scores, on='ID', how='left')
print("\nLeft Join:")
print(left_merge)

# -------------------------------
print("\n----- RIGHT JOIN -----")

right_merge = pd.merge(df_students, df_scores, on='ID', how='right')
print("\nRight Join:")
print(right_merge)

# -------------------------------
print("\n----- OUTER JOIN -----")

outer_merge = pd.merge(df_students, df_scores, on='ID', how='outer')
print("\nOuter Join:")
print(outer_merge)

# -------------------------------
print("\n----- HANDLE OVERLAPPING COLUMNS -----")

# Create another dataset with overlapping column
extra = {
    'ID': [1, 2, 3, 4],
    'Marks': [80, 85, 75, 95]
}
df_extra = pd.DataFrame(extra)

merge_overlap = pd.merge(df_scores, df_extra, on='ID', suffixes=('_exam', '_extra'))
print("\nHandling overlapping columns:")
print(merge_overlap)

# -------------------------------
print("\n----- CONCAT (VERTICAL) -----")

df1 = pd.DataFrame({'Name': ['A', 'B'], 'Marks': [70, 80]})
df2 = pd.DataFrame({'Name': ['C', 'D'], 'Marks': [90, 85]})

concat_vertical = pd.concat([df1, df2], axis=0)
print("\nVertical Concatenation:")
print(concat_vertical)

# -------------------------------
print("\n----- CONCAT (HORIZONTAL) -----")

concat_horizontal = pd.concat([df1, df2], axis=1)
print("\nHorizontal Concatenation:")
print(concat_horizontal)

# -------------------------------
print("\n----- PRACTICE TASKS -----")

# Task 1: Inner join
print("\nTask 1 - Inner Join:")
print(pd.merge(df_students, df_scores, on='ID', how='inner'))

# Task 2: Left join
print("\nTask 2 - Left Join:")
print(pd.merge(df_students, df_scores, on='ID', how='left'))

# Task 3: Outer join
print("\nTask 3 - Outer Join:")
print(pd.merge(df_students, df_scores, on='ID', how='outer'))

# Task 4: Vertical concat
print("\nTask 4 - Vertical Concat:")
print(pd.concat([df1, df2]))

# Task 5: Horizontal concat
print("\nTask 5 - Horizontal Concat:")
print(pd.concat([df1, df2], axis=1))

# -------------------------------
print("\n----- TITANIC-LIKE EXAMPLE -----")

# Passenger data
passengers = {
    'PassengerId': [1, 2, 3],
    'Name': ['A', 'B', 'C'],
    'Class': ['1st', '2nd', '3rd']
}
df_passengers = pd.DataFrame(passengers)

# Cabin data
cabin = {
    'PassengerId': [1, 2, 4],
    'Cabin': ['C85', 'E46', 'B28']
}
df_cabin = pd.DataFrame(cabin)

print("\nPassengers Data:")
print(df_passengers)

print("\nCabin Data:")
print(df_cabin)

# Merge passenger & cabin
merged_titanic = pd.merge(df_passengers, df_cabin, on='PassengerId', how='left')
print("\nMerged Titanic Data:")
print(merged_titanic)