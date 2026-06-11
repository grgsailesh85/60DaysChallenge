import numpy as np # numpy -> np
import scipy.linalg as la

# #vector 
# v = np.array([1, 2, 3])
# print(v)
# print("\n")

# #matrix
# A = np.array( [ [1, 2], [3, 4] ] )
# '''
# 1 2
# 3 4
# ->(2 x 2) matrix
# '''
# print(A)
# print("\n")


# #Scalar multiplication
# v_scaled = 10 * v  # 10 -> Scalar
# print(v_scaled)
# print("\n")


# #matrix Multiplication
# C = np.array( [ [1, 2], [3, 4] ] )
# B = np.array( [ [5, 6], [7, 8] ] )
# '''
# C * B != B * C -> They are not equal
# mul = C @ B -> Does Matrix Multiplication
# '''
# D = C @ B  # -> Matrix multiplication
# Mul = C * B  # -> Element wise multiplication
# print("multiplication")
# print(D)
# print("\n")
# print(Mul)

# #matrix Addition
# print("Addition")
# add_v = C + B
# print(add_v)

# #matrix transpose
# A_Transpose = A.T
# print("Transpose")
# print(A_Transpose)



# '''
# 2x + 3y = 8, 5x + 4y = 13
# b =[8, 13]
# A = 2  3
#     5  4
# '''
# A = np.array([[2, 3], [5, 4]])
# b = np.array([8, 13])
# x = np.linalg.solve(A, b)  # linalg -> linear algebra
# print(f"Solution = {x}")


#LU Decomposition
A = np.array([
    [2, 4, 5],
    [1, 3, 2],
    [4, 2, 1]
])

P, L, U = la.lu(A) #[P_value, L_Value, U_Value]

print(f"P = {P}")
print(f"L = {L}")
print(f"U = {U}")

