#----- Basic Linear Transformation -------#
import numpy as np
# #define transformation matrix
# A = np.array([
#     [1, 3],
#     [3, 4]
# ])
# # define vector x
# x = np.array([1, 2])
# #apply linear transformation T(x)
# Tx = A @ x
# print(f"T(x) = {Tx}")


# Scaling...........................
# kx, ky = 2, 3

# A = np.array([
#     [kx, 0],
#     [0, ky]
# ])
# x = np.array([4, 5])
# Tx = A @ x
# print(f"Original Vector = {x}")
# print(f"Scaled vector = {Tx}")


#Rotational........................
# # anti clockwise rotational
# theta = np.pi / 2 # 90 Degree, divide by 4 for 45 degree
# A = np.array([
#     [np.cos(theta), -np.sin(theta)],
#     [np.sin(theta), np.cos(theta)]
# ])
# x = np.array([3, 2]) # -> original vector
# rotated_vector = A @ x
# print(f"Original Vector = {x}")
# print(f"Rotated Vector = {rotated_vector}")


# # clockwise rotational
# theta = np.pi / 4 # 45 Degree, divide by 2 for 90 degree
# A = np.array([
#     [np.cos(-theta), -np.sin(-theta)],
#     [np.sin(-theta), np.cos(-theta)]
# ])
# x = np.array([3, 2]) # -> original vector
# rotated_vector = A @ x
# print(f"Original Vector = {x}")
# print(f"Rotated Vector = {rotated_vector}")

# Reflection................
# Ax = np.array([
#     [1, 0],
#     [0, -1] # -> For reflection along X axis
# ])
# Ay = np.array([
#     [-1, 0],
#     [0, 1] # -> For reflection along Y axis
# ])
# x = np.array([4, 5])
# reflected_vectorx = Ax @ x
# reflected_vectory = Ay @ x

# print(f"Original vector = {x}")
# print(f"Reflection along x-axis = {reflected_vectorx}")
# print(f"Reflection along y-axis = {reflected_vectory}")

# composition of linear transformation
A = np.array([
    [1, 2],
    [3, 4]
])
B = np.array([
    [0, 1],
    [1, 0]
])
x = np.array([1, 2])
result1 = B @ (A @ x)
intermediate_matrix = B @ A  # B @ (A @ x) = (B @ A) @ x
result2 = intermediate_matrix @ x

print(result1)
print(result2)