#----------error
#print("Hello world) -> Syntax Error

# num1 = int(input("Enter a number: "))
# num2 = int(input("Enter another number: "))
# sum = num1 - num2  # This represents logical error
# print(f"Sum = {sum}")


#Exception

'''
try:


except:
.......
.......
.......
else:



finally:


'''




# try : 
#     x = int(input("Enter a number: "))
#     print(f"number = {x}")   
# except ValueError : 
#     print("Please Enter an integer")



# try : 
#     x = int(input("Enter a number: "))
# except ValueError : 
#     print("Please Enter an integer")    
# else:    
#     print(f"number = {x}")


# while True:
#     try: 
#         x = int(input("Enter a number: "))
#     except ValueError:
#         # print("Please Enter an Integer!!")
#         pass
#     else:
#         break
# print(f"The entered number is: {x}")

        
# Division By zero Error
# Task -> Program -> Takes a number -> divides 10 by the entered number
while True:
    try: 
        x = int(input("enter a number: "))
        result = 10/x
    except ValueError:
        print("Please Enter an integer")
    except ZeroDivisionError:
        print("The Divisor cannot be zero")
    else:
        break
print(f"Result = {result}")
