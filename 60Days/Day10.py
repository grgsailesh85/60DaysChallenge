#----------------------------- Exception(Part 2) -----------------------------------#

# Division By zero Error
# Task -> Program -> Takes a number -> divides 10 by the entered number
# while True:
#     try: 
#         x = int(input("enter a number: "))
#         result = 10/x
#     except (ValueError, ZeroDivisionError):
#         pass
#     else:
#         print(f"Result = {result}")
#         break

# Division By zero Error
# Task -> Program -> Takes a number -> divides 10 by the entered number
# while True:
#     try: 
#         x = int(input("enter a number: "))
#         result = 10/x
#     except ValueError:
#         print(ValueError)
#     except ZeroDivisionError:
#         print(ZeroDivisionError)
#     else:
#         break
# print(f"Result = {result}")


# def main():
#     x = get_int()
#     print(f"Number  = {x}")
    
# def get_int():
#     while True:
#         try:
#             x = int(input("Enter a Number: "))
#         except ValueError:
#             pass
#         else: 
#             return x 
# main()


#Program = take three number as input -> sum, product and operation=>(num1+num2)/num3 by using functional programming
# Functions

# Functions

def calculate_sum(a, b, c):
    return a + b + c

def calculate_product(a, b, c):
    return a * b * c

def calculate_operation(a, b, c):
    return (a + b) / c


# Input num1
while True:
    try:
        num1 = int(input("Enter first number: "))
        break
    except ValueError:
        print("Please enter a valid integer.")


# Input num2
while True:
    try:
        num2 = int(input("Enter second number: "))
        break
    except ValueError:
        print("Please enter a valid integer.")


# Input num3 (must be an integer and not zero)
while True:
    try:
        num3 = int(input("Enter third number: "))
        operation_result = calculate_operation(num1, num2, num3)
        break
    except ValueError:
        print("Please enter a valid integer.")
    except ZeroDivisionError:
        print("The divisor cannot be zero.")


# Output
print("\nResults")
print("Sum =", calculate_sum(num1, num2, num3))
print("Product =", calculate_product(num1, num2, num3))
print("(num1 + num2) / num3 =", operation_result)