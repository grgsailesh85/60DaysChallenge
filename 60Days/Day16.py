import numpy as np

# #Statistical functions
# #Creating a dataset
# data = np.array([10, 20, 30, 40, 50])
# #calculating key statistics
# print("Mean (Average): ", np.mean(data))
# print("Median (Middle value): ", np.median(data))
# print("Standard Deviation: ", np.std(data))  # measures data spread
# print("Variance: ", np.var(data))  # square of standard deviation
# print("Minimum Value: ", np.min(data)) #smallest value
# print("Maximum value: ", np.max(data)) #largest value
# print("Index of Minimum Value: ", np.argmin(data)) # index of smallest value
# print("index of Maximum Value: ", np.argmax(data)) # index of largest value


# #Determinant of matrxi
# A = np.array([[1, 2], [3, 4]]) # 2 x 2
# B = np.array([[5, 6], [7, 8]])
# dit1 = np.linalg.det(A)
# dit2 = np.linalg.det(B)
# print(f"Determinant of matrix A : \n {dit1}")
# print()
# print(f"Determinant of matrix B : \n {dit2}")
# print() 
# #Inverse of matrix
# inv1 = np.linalg.inv(A)
# inv2 = np.linalg.inv(B)
# print(f"Inverse of matrix A : \n {inv1}")
# print()
# print(f"Inverse of matrix B : \n {inv2}")







# #advance mathematical function
# # Summation and Cumulative Sum
# arr = np.array([1, 2, 3, 4])
# print("Array =>", arr)
# print("Sum of elements: ", np.sum(arr))
# print("Cumulative Sum: ", np.cumsum(arr))
# print()

# #finding unique elements and counting occurrences
# arr1 = np.array([1, 2, 3, 1, 2, 3, 4, 4, 4, 4, 2])
# print("Array =>", arr1)
# unique_elements, count = np.unique(arr1, return_counts = True)
# print("Unique Elements:" , unique_elements)
# print("Counts: ", count)
# print()

# #sorting an array
# arr2 = ([3, 1, 4, 1, 5, 9])
# print("Array => ", arr2)
# print("Sorted Ascending Array: ", np.sort(arr2))  #ascending order
# print("Indices of Sorted elements: ", np.argsort(arr2))
# print("Sorted Descending Array: ", np.sort(arr2)[::-1])  #ascending order




# finding percentiles and quantiles
data = np.array([10, 20, 30, 40, 50])
print("25th Percentile: ", np.percentile(data, 25))
print("50th Percentile (median): ", np.percentile(data, 50))
print("75th Percentile: ", np.percentile(data, 75))
