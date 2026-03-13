#Arrays
import numpy as np

arr = np.array([10, 20, 30, 40, 50])
print(arr)

#Creating Simple Arrays
import numpy as np

arr = np.array([5, 10, 15, 20])

print(arr)

#Creating a 2D array:
arr2 = np.array([[1,2,3],[4,5,6]])
print(arr2)

#Array Attributes 
# Shape
import numpy as np

arr = np.array([[1,2,3],[4,5,6]])
print(arr.shape)

#Size
print(arr.size)

#Data Type
print(arr.dtype)

#Performance Comparison (Arrays vs Lists)
import numpy as np
import time

# List
list_data = list(range(1000000))
start = time.time()
result = [x * 2 for x in list_data]
print("List time:", time.time() - start)

# Array
array_data = np.array(range(1000000))
start = time.time()
result = array_data * 2
print("Array time:", time.time() - start)

