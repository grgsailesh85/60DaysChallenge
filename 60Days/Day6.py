#----------Conditional Statement---------------#

'''
if
if else
if elif......else
nested
match case statements
'''

'''
if condition : 
    statement(s)
'''

# a = 6
# if a > 0 :
#     print("The Number is Positive")


# num = -9
# if num > 0 :
#     print("The Number is Positive")
# else :
#     print("The Number is negative")


# num = int(input("Enter a Number: "))
# if num > 0:
#     print(f"The number {num} is Positive")
# else:
#     print(f"The number {num} is Negative")


#---------------------------- [ if -> else if (elif)..... -> else ] -------------------------#

'''
if condition :
    statement(s)
elif condition :
    ........
    statement(s):
    ........
    ........
else:
    statement(s)

'''

#Program to check if the number is positive or negative
# number = int(input("Enter a Number:"))
# if number > 0 :
#     print(f"The Number {number} is Positive")
# elif number < 0 :
#     print(f"The Number {number} is Negative")
# else : 
#     print(f"The number {number} is Zero")


# Write a program to check whether the entered number is odd or even
# num1 = int(input("Enter a Number: "))
# if num1 == 0 :
#     print("The number is Zero")
# elif num1 % 2 ==0 : 
#     print("The number is Even")
# else :
#     print("The number is Odd")



'''
if condition : 
    if condition :
        statement(s)
    else :
        statement(s)
else: 
    if condition :
        statement(s)
    else :
        statement(s)
'''

# program to find the greatest among three number
Num1 = int(input("Enter first number: "))
Num2 = int(input("Enter second number: "))
Num3 = int(input("Enter third number: "))

if Num1 > Num2 :
    if Num1 > Num3 :
        print(f"The Greatest number is {Num1}")
    else : 
        print(f"The Greatest number is {Num3}")
else : 
    if Num2 > Num3 :
        print(f"The greatest number is {Num2}")
    else :
        print(f"The greatest number is {Num3}")
        