import numpy as np

# 1D Array -> a simple list of numbers
# 2D Array -> a matrix (rows and columns)
# 3D Array -> a collection of 2D arrays

#Creating a 3D Numpy array
# arr_3d = np.array([[[2, 3, 5], [6, 8, 9]],[[3, 4, 7], [4, 7, 8]]])
# print(arr_3d)

#creating an array of zeros
# zeros_arr = np.zeros((3, 3))  # creates 3 * 3 matrix filled with zeros
# print(f"Zeros Array:\n{zeros_arr}")

#creating an array of ones
# ones_arr = np.ones((2, 5))  # creates 2 * 5 matrix filled with one
# print(f"Ones Array:\n{ones_arr}")

#creating an identity matrix
# identity_matrix = np.eye(4)  # creates 4 * 4 identity matrix
# print(f"Identity Matrix:\n{identity_matrix}")


#creating an array with a range of values
# range_arr = np.arange(1, 11, 2) # -> creates an array with values from 1 to 10 with a step of 2
# print(f"Range Array: \n{range_arr}")

#creating an array with evenly spaced values
# linspace_arr = np.linspace(0, 1, 5) #creates 5 evenly spaced values between 0 and 1
# print("Linspace Array:", linspace_arr)

#creating a random array
# random_arr = np.random.rand(3, 3) #generates a 3 * 3 array of random values between 0 and 1
# print("Random Array: \n", random_arr)

# random_arr1 = np.random.randint(1, 11, size = (3, 3))
# print("Random Array1: \n", random_arr1) #generates a 3 * 3 array of random values between 1 and 10

#Array Attributes
#creating  a sample numpy array
# arr = np.array([[10, 20, 30], [40, 50, 60]])
# print("Array: \n", arr)
# print("Shape of array:",arr.shape) # -> returns (rows, columns)
# print("Size of array: ", arr.size) # -> returns total number of elements
# print("Number of Dimensions:", arr.ndim) # -> returns 2 (for 2d array)
# print("Data type of elements: ", arr.dtype) # -> data type of elements
# print("Item size in bytes: ", arr.itemsize) # -> size of each element in bytes
# print("Total Memory consumed: ", arr.nbytes, "bytes") # -> total memory usage


# Array indexing and slicing
# accessing element in a 1D Array
arr_1d = np.array([10, 20, 30, 40, 50])
print("1D Array\n", arr_1d)
print("First Element: ", arr_1d[0]) #access first element
print("Last Element: ", arr_1d[-1]) #access last element
print("Elements from index 1 to 3:", arr_1d[1: 4]) #slicing
print("Every second element:", arr_1d[::2]) #step slicing

# accessing element in a 2D Array
arr_2d = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
print("2D Array\n", arr_2d)
print("Element at row 1 nad column 2: ", arr_2d[1, 2]) #accessing first element
print("First Row: ", arr_2d[0, :]) #accessing entire row
print("First Column: ", arr_2d[:, 0]) #accessing entire column
print("Second Row: ", arr_2d[1, :]) #accessing entire row
print("Second Column: ", arr_2d[:, 1]) #accessing entire column
