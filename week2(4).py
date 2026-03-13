#. Indexing and Slicing Arrays
import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print(arr[0])   # first element
print(arr[3])   # fourth element

#Slicing
print(arr[1:4])

#Extract Rows, Columns, and Sub-Arrays from Matrices
import numpy as np

matrix = np.array([[1,2,3],
                   [4,5,6],
                   [7,8,9]])

#Extract a Row
print(matrix[1])

#Extract a Column
print(matrix[:,1])

#Extract Sub-Array
print(matrix[0:2, 1:3])

#Reshape Arrays (1D → 2D → 3D)
import numpy as np

arr = np.array([1,2,3,4,5,6])

#Convert to 2D
arr2 = arr.reshape(2,3)
print(arr2)

#Convert to 3D 
arr3 = arr.reshape(1,2,3)
print(arr3)

#Combine Arrays (Stacking & Concatenation)
import numpy as np

a = np.array([1,2,3])
b = np.array([4,5,6])

c = np.concatenate((a,b))
print(c)

#Vertical Stacking
a = np.array([1,2,3])
b = np.array([4,5,6])

v = np.vstack((a,b))
print(v)

#Horizontal Stacking
h = np.hstack((a,b))
print(h)


