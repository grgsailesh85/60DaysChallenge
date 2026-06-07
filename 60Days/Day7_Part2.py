my_dict = {
    "1" : "Apple",
    "2" : "Banana",
    "3" : "Mango"
}

for k in my_dict :
    print(f"{k} : {my_dict[k]}")



fruits = ["Red", "Blue", "White"]
count = 0
for fruit in fruits :
    count = count + 1
    print(f"{count} : {fruit}")  



#Task my_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
skipped = []
for i in range(1,16) : # [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    if i in [5, 6, 7] :
        skipped.append(i)
        continue
    print(i, end = " ")
print()
print(f"Skipped value = {skipped}")