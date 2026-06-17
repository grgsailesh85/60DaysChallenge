import numpy as np

# Broadcasting -> Broadcasting automatically expands the smaller array to match the shape of the larger array.
# arr = np.array([1, 2, 3])
# result = arr + 10
# print(result)
# print()
# NumPy automatically treats 10 as:[10 10 10]

# A = np.array([
#     [1, 2, 3],
#     [4, 5, 6]
# ])
# B = np.array([10, 20, 30])
# print(A + B)
# NumPy automatically expands B. Internally, it behaves like: [[1 2 3],[4 5 6]] + [[10 20 30],[10 20 30]]

# 1D Array Sorting
# A = np.array([1, 5, 99, 8, 3, 50])
# print(np.sort(A)[::-1])

# 2D Array Sorting
# m = np.array([
#     [6, 4, 9],
#     [2, 1, 8],
#     [7, 9, 1]
# ])
# # This line sorts each row of the 2D array m independently
# new_m = np.sort(m, axis = 1)
# print("Original Array: \n", m)
# print("Row wise Sorted array \n",new_m)
# print()
# new_m1 = np.sort(m, axis = 0)
# # This line sorts each column of the 2D array m independently
# print("Column wise Sorted array \n",new_m1)



mat = np.array([
    [1, 2, 3],
    [2, 3, 6]
])
new_row1 = np.array([[2, 5, 7]])
new_row2 = np.array([[8, 1, 2]])
new_mat1 = np.append(mat, new_row1, axis = 0)
new_mat2 = np.append(new_mat1, new_row2, axis = 0)
print("Original matrix\n", mat)
print()
print("New appended matrix\n", new_mat1)
print()
print("New appended matrix\n", new_mat2)
