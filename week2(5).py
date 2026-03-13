#Element-Wise Operations
#Aim: Perform addition, subtraction, and multiplication on arrays.
import numpy as np

a = np.array([10, 20, 30])
b = np.array([5, 4, 3])

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)

#Basic Statistical Calculations
#aim: Calculate sum, mean, maximum, and minimum values.
import numpy as np

data = np.array([12, 18, 25, 30, 45])

print("Sum:", np.sum(data))
print("Mean:", np.mean(data))
print("Maximum:", np.max(data))
print("Minimum:", np.min(data))

#Median and Standard Deviation
#Aim: Find median and standard deviation.
import numpy as np

numbers = np.array([10, 15, 20, 25, 30])

print("Median:", np.median(numbers))
print("Standard Deviation:", np.std(numbers))

#Aggregate Functions on Matrix
#Aim: Calculate row and column sums and means.
import numpy as np

matrix = np.array([[10,20,30],
                   [40,50,60],
                   [70,80,90]])

print("Row Sum:", np.sum(matrix, axis=1))
print("Column Sum:", np.sum(matrix, axis=0))

print("Row Mean:", np.mean(matrix, axis=1))
print("Column Mean:", np.mean(matrix, axis=0))


#Statistical Analysis of Exam Scores
#Aim: Apply statistical functions to exam scores.
import numpy as np

scores = np.array([78, 85, 90, 88, 76, 95, 89])

print("Average Score:", np.mean(scores))
print("Highest Score:", np.max(scores))
print("Lowest Score:", np.min(scores))
print("Median Score:", np.median(scores))
print("Standard Deviation:", np.std(scores))
