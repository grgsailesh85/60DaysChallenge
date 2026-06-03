#-------Data Cleaning-------#

'''
lstrip() - removes leading characters (left side)
rstrip() - removes trailing characters (right side)
strip() - removes both leading and trailing characters (left and right side)
replace() - replaces a specified phrase with another specified phrase
'''

# name = " ---- My --- name is Sailesh 1 2 3 __ "  -> present data
# name = "My name is Sailesh"

'''
name = "   Sailesh"
newname = name.lstrip()  # removes leading spaces
print(newname)  # "Sailesh"

name1 = "Sailesh  "
newname1 = name1.rstrip() #removes trailing spaces
print(newname1)  # "Sailesh"

name2 = "  Sailesh  "
newname2 = name2.lstrip().rstrip() #removes leading and trailing spaces
print(newname2)  # "Sailesh"

name3 = "Sailesh ** Gurung"
newname3 = name3.replace(" ** ", " ") #replaces ** with space
print(newname3)  # "Sailesh Gurung"

name4 = "__Sailesh"
newname4 = name4.lstrip("__") #removes leading __  or 
#name4.replace("__", "") -> replaces __ with empty string 
print(newname4)  # "Sailesh"
'''

name = "  Sailesh  "
newname = name.strip() #removes leading and trailing spaces
print(newname)  # "Sailesh"

name1 = " ---- My --- name is Sailesh 1 2 3 __ "
# step 1 -> clear the front and rear part 
# step 2 -> clear the middle part by using replace

newname1 = name1.strip(" -123_") 
print(newname1) # "My --- name is Sailesh"
newnamefinal1 = newname1.replace(" --- " , " ")
print(newnamefinal1) # "My name is Sailesh"


name2 = " --- I am a ___ Computer 123 Science Student --- "

newname2 = name2.strip(" - ") 
print(newname2) # "I am a ___ Computer 123 Science Student"
newnamefinal2 = newname2.replace(" ___ " , " ").replace(" 123 ", " ")
print(newnamefinal2) # "I am a Computer Science Student"