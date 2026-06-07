#---------------- Looping or Iterative Statements -----------------#

# for loop...........................
# fruits = ["Apple", "Banana", "Kiwi", "Mango", "Watermelon"]
# for fruit in fruits : 
#     print(fruit)

# #my_list = range(starting value, ending value, step->1)

# my_List = list(range(1, 11))
# print(my_List)

# my_List1 = list(range(1, 11,2))
# print(my_List1)

#program to print the number from 1 to 20
# for i in range(1,21) :
#     print(i, end = " ")

#program to print odd numbers from 1 to 20
print("The Odd Number:")
for i in range(1,21) :
    if i % 2 != 0:
        print(i, end=" ")


print()
print("The Even Number:")
#program to print even numbers from 1 to 20
for j in range(1,21) :
    if j % 2 == 0:
        print(j, end=" ")



#While..............................#
'''
while condition => true
    runs
'''

count = 0 
while count <= 10:
    print("Sailesh Gurung")
    count += 1 #count = count + 1


# break -> When a particular condition occurs, break the loop
print()
for k in range(1, 10):
    if k == 6:
        break
    print(k, end=" ")  # 1 2 3 4 5 


# continue => When a particular condition occurs, skip the iteration

print()
for l in range(1, 10):
    if l == 6:
        continue
    print(l, end = " ") # 1 2 3 4 5 7 8 9 