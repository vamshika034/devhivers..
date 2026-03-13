#Import NumPy
import numpy as np

#Matrix Addition
A = np.array([[1,2,3],
              [4,5,6]])

B = np.array([[6,5,4],
              [3,2,1]])

result = A + B

print("Matrix A:\n", A)
print("Matrix B:\n", B)
print("Addition Result:\n", result)


#Matrix Subtraction
result = A - B

print("Subtraction Result:\n", result)

#Matrix Multiplication
A = np.array([[1,2],
              [3,4]])

B = np.array([[5,6],
              [7,8]])

result = np.dot(A, B)

print("Matrix Multiplication:\n", result)

#Generate Random Numbers
random_numbers = np.random.rand(5)

print("Random Numbers:", random_numbers)

#Generate Random Matrix
random_matrix = np.random.randint(1, 10, (3,3))

print("Random Matrix:\n", random_matrix)

#Dice Roll Simulation
dice_rolls = np.random.randint(1, 7, 10)

print("Dice Rolls:", dice_rolls)


#Random Sampling from Dataset
students = np.array([101,102,103,104,105,106,107])

sample = np.random.choice(students, 3)

print("Random Sample:", sample)

#Small Practice Exercise
A = np.random.randint(1,10,(2,2))
B = np.random.randint(1,10,(2,2))

print("Matrix A:\n", A)
print("Matrix B:\n", B)

print("Addition:\n", A+B)
print("Subtraction:\n", A-B)
print("Multiplication:\n", np.dot(A,B))

