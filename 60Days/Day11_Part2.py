import numpy as np # numpy -> np
import scipy.linalg as la

# QR Decomposition................

A = np.array([
    [1, 2, 3],
    [3, 4, 5]
])
Q, R = np.linalg.qr(A)

print(f"Q = \n{Q}")
print(f"R = \n{R}") 
 