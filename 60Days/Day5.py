#--------- Data Structure ---------#

'''
List: A collection of items that are ordered and changeable. Allows duplicate members.
Set: A collection of items that is unordered and unchangeable. No duplicate members.
tuples: A collectio of items that is ordered and unchangeable. Allows duplicate members.
Dictionary: A collection of key-value pairs that is ordered and changeable. No duplicate members.
'''

#List -> mutable data structure

#tuple -> immutable data structure

#set -> unique values unordered

#dictionary -> key value pairs
# "name" : "ram",
# "ph_no" : 999999999


#---------------- Lists ----------------#
# List = [1, 2, 4, "Sailesh", True, 3.14]
# emty_list = []

l1 = [0, 2, "Ram", "Thapa", False, 1.2]
print(l1)
print(type(l1))

el = []
print(el)
print(type(el))

# indexing -> accessing elements of a list using their index
l2 = ["Sailesh", "Gita", 26, True, False]

'''
index = [0, 1, 2, 3, 4, ............]
if we have n elements in a list then 
the range of index : 0 to (n-1)

for example if we have 10 elements then 
range: 0 to 9
'''
print(l2[0]) # "Sailesh"
print(type(l2[0])) # <class 'str'>

# negative indexing -> accessing elements of a list from the end using negative index
# -1 index gives the last element of the list
# similarly -2 gives the second last element and so on
print(l2[-1]) # False
print(type(l2[-1])) # <class 'bool'>

x_list = [1, 2, 3, 4, 5]
sq_x = [a ** 2 for a in x_list]
print(x_list) # [1, 2, 3, 4, 5]
print(sq_x) # [1, 4, 9, 16, 25]


# len() -> gives the number of elements in a list
# slicing -> accessing a range of elements from a list using their index
# syntax: list_name[start_index : end_index]

l3 = ["Ram", "Sita", 12, True, False, 3.14, 12.3, "Gita", "Hari", "Red"]
'''
the last element => print(l3[-1]) # "Red"
the second last element => print(l3[-2]) # "Hari"
the fifth element => print(l3[4]) # False
'''
print(l3[0 : 5]) # ['Ram', 'Sita', 12, True, False]
print(l3[-4:]) # [12.3, 'Gita', 'Hari', 'Red']

# List function 
# append() 
l3.append("Banana")
print(l3) #  ["Ram", "Sita", 12, True, False, 3.14, 12.3, "Gita", "Hari", "Red", "Banana"]

# insert(index, "Value")
l3.insert(0, "ABC")
print(l3) # ["ABC", "Ram", "Sita", 12, True, False, 3.14, 12.3, "Gita", "Hari", "Red", "Banana"]

# sort
my_list = [33, 65, 78, 99, 100, 43, 11, 0, 1, 3]
my_list.sort()
print(my_list) # [0, 1, 3, 11, 33, 43, 65, 78, 99, 100]

my_list.sort(reverse = True) # or my_list.reverse() => descending order
print(my_list) # [100, 99, 78, 65, 43, 33, 11, 3, 1, 0]

#pop
myList = [1,2,3,4,5,6]
print(myList.pop()) # result => 6
print(myList) # [1, 2, 3, 4, 5]

#remove

#clear


#----------- Tuples -> immutable, indexing and slicing same as list ------------#

my_tuple = (3, 4, 5, 6, "Ram", 4.2, True, 3, 3, 3)
print(my_tuple)
print(type(my_tuple))
number = my_tuple.count(3)
print(number) # 4

tuple1 = (1,1,5,6,4,2,True,1,1,1)
number1 = tuple1.count(1)
print(number1) # 6 => True is also counted as 1

#----------------------- set --------------------------#
my_set = {1, 2, 3, 4, 2, 3}
print(my_set) # {1, 2, 3, 4}
print(type(my_set)) # <class 'set'>
my_set.add(5)
print(my_set) # {1, 2, 3, 4, 5}
my_set.remove(2)
print(my_set) # {1, 3, 4, 5}
my_set.add(-1)
print(my_set) # {1, 3, 4, 5, -1}

set1 = set() # defines empty set


#----------------------- Dictionary --------------------------#

'''
syntax:
my_dict = {
        "Key" : "Value",
        ...............
        ...............
        ...............
        "Key_n" : "Value_n"
    }

the key must be unique and immutable
'''


my_dict = {
    "Name" : "Sailesh",
    "Age" : 20,
    "Ph_no" : 999999999
}
print(my_dict)
print(type(my_dict))
print(my_dict.keys())
print(my_dict.values())
