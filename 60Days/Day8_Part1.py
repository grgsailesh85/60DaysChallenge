#-----------------------User Defined Function-------------------------------#

#program to write a program that greets the user using function

# def greet(name) :
#     print(f"Welcome {name}") 


# name = input("Enter Your Name: ")
# greet(name)


# Program to calculate temperature converter celsius to farenheit

# def celsius_to_farenheite(celsius) : 
#     farenheite = (celsius * 9 / 5) + 32
#     return farenheite

# def main(): 
#     celsius = int(input("Enter Temperature in celsius: "))
#     feren = celsius_to_farenheite(celsius)
#     print(f"Temperature in farenheit = {feren:.2f} degree farenheit")

# main()

# Program to find the maximum among 3 numbers

def max_three_no(num1, num2, num3) :
    if (num1 >= num2) and (num1 >= num3) :
        return num1
    if (num2 >= num1) and (num2 >= num3) :
        return num2
    else : 
        return num3

def main() :
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    num3 = int(input("Enter third number: "))
    greatest = max_three_no(num1, num2, num3)
    print(f"The greatest number among {num1}, {num2} and {num3} is {greatest}")

main()
