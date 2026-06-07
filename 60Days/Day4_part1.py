#---------- DATA CLEANING (PART 2) ----------#

# name = "   ---sailesh @@ gurung 1 2 3 __   "  -> Present Data
# result = "Sailesh Gurung" -> Desired Data

'''
split() -> It will split the string into a list of words based on whitespace by default.
capatalize() -> It will convert the first character of the string to uppercase and the rest to lowercase.
title() -> It will convert the first character of each word to uppercase and the rest to the lowercase.
'''



'''
name = "   ---sailesh @@ gurung 1 2 3 __   "
new_name = name.strip(" -123_") # result = "sailesh @@ gurung"
print(new_name)
new_name1 = new_name.replace(" @@ ", " ") # result = "sailesh gurung"
print(new_name1)
new_name_final = new_name1.title() # result = "Sailesh Gurung"
print(new_name_final) # result = "Sailesh Gurung"
'''



# first_name = Sailesh and last_name = Gurung
'''
after breaking the string into a list of words,
first part => first_name
second part => last_name
'''



'''
first_name, last_name = new_name_final.split() 
print(first_name) # result = "Sailesh"
print(last_name) # result = "Gurung"

name1 = "Ram#Bahadur#Thapa" 
first, middle, last = name1.split("#")
print(first) # result = "Ram"
print(middle) # result = "Bahadur"
print(last) # result = "Thapa"

name2 = "sailesh gurung" 
new_name2 = name2.capitalize() # result = "Sailesh gurung"
print(new_name2) 
'''



'''
Name = "  __-- firoj ##&& karki 123 @@"
First_name = Firoj
Last_name = Karki
'''

Name = "  __-- firoj ##&& karki 123 @@"
data = Name.strip(" _-123@").replace(" ##&& ", " ").title()
First_name , Last_name = data.split()
print(First_name)
print(Last_name)


ph_no = "(+977)9811012191"
ph_no1 = ph_no.replace("(+977)", "")
print(ph_no1) # result = "9811012191"
ph_no2 = "(+977)" + ph_no1
print(ph_no2) # result = "(+977)9811012191"


