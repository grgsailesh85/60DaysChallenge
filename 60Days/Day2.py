#This is the day two of AI/ML class
print("This is the day two of AI/ML class")

#This @ is @ the @ day @ two @ of @ AI/ML @ class
print("This is the day two of AI/ML class", sep=" @ ")

#This @ is @ the @ day # two # of # AI/ML # class
print("This", "is", "the", "day", sep = " @ ", end=" # ")
print("one", "of", "AI/ML", "class", sep = " # ")

#F string
num = 10
print("The number is: ", num)
print(f"The number is: {num}")

name = "Sailesh"
print(f"My name is {name}")


#The number is 4.123
num1 = 4.123124
print(f"The number is {num1:.3f}")

num2 = float(input("Enter a number: "))
num3 = float(input("Enter another number: "))
sum = num2 + num3
diff = num2 - num3
pro = num2 * num3
print(f"The sum of {num2} , {num3} is {sum}")
print(f"The differenece of the two numbers {diff}")
print(f"The product of the two numbers {pro:.2f}")
