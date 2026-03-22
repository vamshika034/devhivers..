# Titanic Dataset Practice - Full Analysis

import pandas as pd
import matplotlib.pyplot as plt

print("----- LOAD DATASET -----")

# Load dataset (make sure titanic.csv is in same folder)
df = pd.read_csv("titanic.csv")

print("\nFirst 5 Rows:")
print(df.head())

# -------------------------------
print("\n----- BASIC EXPLORATION -----")

print("\nColumns:")
print(df.columns)

print("\nData Info:")
print(df.info())

print("\nSummary Statistics:")
print(df.describe())

print("\nMissing Values:")
print(df.isnull().sum())

# -------------------------------
print("\n----- INDEXING & FILTERING -----")

# Passengers age > 30
print("\nAge > 30:")
print(df[df['Age'] > 30].head())

# Female passengers
print("\nFemale Passengers:")
print(df[df['Sex'] == 'female'].head())

# Survived passengers
print("\nSurvived Passengers:")
print(df[df['Survived'] == 1].head())

# -------------------------------
print("\n----- GROUPING & AGGREGATION -----")

# Survival rate by gender
print("\nSurvival Rate by Gender:")
print(df.groupby('Sex')['Survived'].mean())

# Survival rate by class
print("\nSurvival Rate by Class:")
print(df.groupby('Pclass')['Survived'].mean())

# Average age by class
print("\nAverage Age by Class:")
print(df.groupby('Pclass')['Age'].mean())

# -------------------------------
print("\n----- ADVANCED FILTERING -----")

# Female survivors
female_survivors = df[(df['Sex'] == 'female') & (df['Survived'] == 1)]
print("\nFemale Survivors:")
print(female_survivors.head())

# First class passengers who survived
first_class_survived = df[(df['Pclass'] == 1) & (df['Survived'] == 1)]
print("\n1st Class Survivors:")
print(first_class_survived.head())

# -------------------------------
print("\n----- MERGING (SIMULATION) -----")

# Create small extra dataset (Cabin info)
extra = df[['PassengerId', 'Cabin']]

# Merge back (example)
merged_df = pd.merge(df, extra, on='PassengerId', how='left')
print("\nMerged Data (with Cabin):")
print(merged_df.head())

# -------------------------------
print("\n----- SMALL ANALYSIS -----")

# Overall survival rate
survival_rate = df['Survived'].mean()
print("\nOverall Survival Rate:", survival_rate)

# Average age of survivors
avg_age_survivors = df[df['Survived'] == 1]['Age'].mean()
print("Average Age of Survivors:", avg_age_survivors)

# -------------------------------
print("\n----- VISUALIZATION -----")

# Survival count plot
df['Survived'].value_counts().plot(kind='bar')
plt.title("Survival Count")
plt.xlabel("Survived (0 = No, 1 = Yes)")
plt.ylabel("Count")
plt.show()

# Survival by gender plot
df.groupby('Sex')['Survived'].mean().plot(kind='bar')
plt.title("Survival Rate by Gender")
plt.show()

# -------------------------------
print("\n----- COMPLETED TITANIC ANALYSIS -----")