# Day 2: Pandas Import/Export (CSV & Excel)

import pandas as pd

print("----- CREATE SAMPLE DATA -----")

# Create sample DataFrame (Student Data)
data = {
    'Name': ['Ravi', 'Sita', 'Arjun', 'Meena'],
    'Marks': [85, 90, 78, 92],
    'City': ['Bangalore', 'Mysore', 'Mangalore', 'Delhi']
}

df = pd.DataFrame(data)
print("\nOriginal DataFrame:")
print(df)

# -------------------------------
print("\n----- EXPORT DATA -----")

# Export to CSV
df.to_csv("students.csv", index=False)
print("CSV file 'students.csv' created")

# Export to Excel
df.to_excel("students.xlsx", index=False)
print("Excel file 'students.xlsx' created")

# -------------------------------
print("\n----- IMPORT DATA -----")

# Import CSV
df_csv = pd.read_csv("students.csv")
print("\nImported from CSV:")
print(df_csv)

# Import Excel
df_excel = pd.read_excel("students.xlsx")
print("\nImported from Excel:")
print(df_excel)

# -------------------------------
print("\n----- USING PARAMETERS -----")

# CSV with custom separator
df.to_csv("students_pipe.csv", sep='|', index=False)
print("CSV with '|' separator created")

# Read CSV with separator
df_pipe = pd.read_csv("students_pipe.csv", sep='|')
print("\nRead CSV with custom separator:")
print(df_pipe)

# Using index column
df.to_csv("students_index.csv")
df_index = pd.read_csv("students_index.csv", index_col=0)
print("\nCSV with index column:")
print(df_index)

# Using header
df.to_csv("students_no_header.csv", index=False, header=False)
df_no_header = pd.read_csv("students_no_header.csv", header=None)
print("\nCSV without header:")
print(df_no_header)

# -------------------------------
print("\n----- TASK EXAMPLES -----")

# Task 1: Sales Data
sales = {
    'Product': ['Pen', 'Book', 'Pencil'],
    'Price': [10, 50, 5],
    'Quantity': [100, 40, 200]
}
df_sales = pd.DataFrame(sales)
df_sales.to_csv("sales.csv", index=False)
print("\nSales CSV created")

# Task 2: Read Sales Data
df_sales_read = pd.read_csv("sales.csv")
print("\nSales Data:")
print(df_sales_read)

# Task 3: Export Sales to Excel
df_sales_read.to_excel("sales.xlsx", index=False)
print("Sales Excel created") 