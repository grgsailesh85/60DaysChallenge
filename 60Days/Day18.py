import numpy as np
# Vector space => A vector space is a set of vectors that is closed under vector addition and scalar multiplication and contains the zero vector.
# v1 = np.array([1, 2])
# v2 = np.array([2, 3])
# v_sum = v1 + v2
# print(v_sum)
# print()
# s = 3
# new_v = s * v1
# print(new_v)
# print()
# d = np.dot(v1, v2)
# print(d)

# v = np.array([1, 2, 3, 4, 5, 5, 8, 90, 100])
# # Norm is a way to measure the length, size, or magnitude of a vector.
# n_v = np.linalg.norm(v)
# print(n_v)
# print()

# v1 = np.array([1, 2, 3, 4])
# v2 =-np.array([2, 3, 4, 7])
# is_ortho = (np.dot(v1, v2) == 0)
# print(is_ortho)
# print()
# v3 = np.array([1, -1])
# v4 =-np.array([2, 2])
# is_ortho = (np.dot(v3, v4) == 0)
# print(is_ortho)







# projection -> Projection means casting one vector onto another vector.
# v1 = np.array([1, -1, 3])
# v2 = np.array([2, 2, 2])
# proj = (np.dot(v1, v2) / np.dot(v2, v2) * v2 )
# print(proj)


# Matrix = np.array([
#     [1, 2, 3], 
#     [3, 4, 4], 
#     [5, 6, 1]
# ])
# c1 , c2 = 1.5, 2
# linear_combination = c1 * Matrix[0] + c2 * Matrix[2]
# print(linear_combination)


# v1 = np.array([1, 2, 3])
# v2 = np.array([3, 6, 9])
# M = np.stack([v1, v2], axis = 1)
# r = np.linalg.matrix_rank(M)
# # print(r)
# is_independent = (r == M.shape[1])
# if is_independent :
#     print("The Vectors are independent")
# else: 
#     print("The Vectors are Dependent")



# dimensionality reduction: example with PCA
from sklearn.decomposition import PCA
x = np.random.rand(5, 3) # generate a matrix of 5 * 3 (R^3)
p = PCA(n_components = 2)
reduced = p.fit_transform(x)
print(x)
print()
print(reduced)


