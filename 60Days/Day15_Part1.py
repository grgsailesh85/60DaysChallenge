import numpy as np

# #Array Reshaping -> allows to change the shape of an array without altering the data
# arr = np.arange(12) #creates an array with 12 elements
# reshaped_arr = arr.reshape(3, 4) # reshape it into a 3 * 4 matrix
# print("Original Array", arr)
# print("Reshaped Array: \n", reshaped_arr) 

# # -1 automatically infer one dimension
# auto_reshaped = arr.reshape(4, -1) #numpy automatically calculates the missing dimension
# print(auto_reshaped.shape) #output -> (4, 3)
# print("Auto Reshaped Array \n", auto_reshaped) 

# Array Iteration
#Iteration over 1D Array
# arr_1D = np.array([10, 20, 30, 40])
# print("1D Array Iteration") 
# for num in arr_1D:
#     print(num)
    
    
# #Iteration over a 2D Array
# arr_2D = np.array([
#         [1, 2, 3], 
#         [4, 5, 6]
#     ])
# print("2D Array Iteration")
# for ls in np.nditer(arr_2D) :
#     print(ls)



#Creating two numpy arrays
# a = np.array([1, 2, 3, 4])
# b = np.array([5, 6, 7, 8])
# #elements wise arithmetic operations
# print("Addition:", a + b)
# print("Subtraction: ", a - b)
# print("Multiplication: ", a * b)
# print("Division: ", a / b)
# print("Exponentiation: ", a ** 2)  #square each element of array->a
# print("Modulus: ", b % a)  # remainder



#Universal function
#creating a sample array
arr = np.array([1, 2, 3, 4, 5])
#applying universal functions
print("Square root: ",np.sqrt(arr))
print()
print("Exponential (e^x): ", np.exp(arr))
print()
print("Natural logarithm (ln): ", np.log(arr))
print()
print("Bas-10 logarithm (log10): ", np.log(arr))
print()
print("Sine: ", np.sin(arr))
print()
print("Cosine: ", np.cos(arr))
print()
print("Tangent: ", np.tan(arr))
