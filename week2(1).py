#Examples Using Everyday Items
fruits = ["apple", "banana", "mango", "apple"]

print(fruits)


#Tuple Example (Numbers)
numbers = (10, 20, 30, 40)

print(numbers)

#Set Example (Unique Items)
fruits_set = {"apple", "banana", "mango", "apple"}

print(fruits_set)


#Dictionary Example (Student Information)
student = {
    "name": "Rahul",
    "age": 20,
    "course": "BCA"
}

print(student)


#Converting Between Data Structures
#List → Set

numbers = [1, 2, 3, 3, 4, 4]

numbers_set = set(numbers)

print(numbers_set)

#Tuple → List
numbers = (10, 20, 30)

numbers_list = list(numbers)

print(numbers_list)

#List → Tuple
fruits = ["apple", "banana", "mango"]

fruits_tuple = tuple(fruits)

print(fruits_tuple)


#Dictionary Example (Student Grades)
grades = {
    "Rahul": 85,
    "Priya": 90,
    "Amit": 78
}

print(grades)


#Get specific grade:
print(grades["Priya"])

#Add new student:

grades["Neha"] = 88
print(grades)


#Mini Practice Examples
#Example 1
fruits = ["apple", "banana", "apple", "mango"]

unique_fruits = set(fruits)

print(unique_fruits)


#Example 2
student = {
    "name": "Ravi",
    "age": 21,
    "marks": 92
}

print(student["name"])


#Example 3
numbers = (5, 10, 15)

numbers_list = list(numbers)

print(numbers_list)