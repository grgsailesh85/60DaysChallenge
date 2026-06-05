Text = " $$ Sailesh ** % (+977)9811234567"
# first_name = Sailesh
# ph_no = 9811234567

clean_text = Text.strip(" $").replace(" ** % ", " ") # result = "Sailesh (+977)9811234567"

first_name, nonclean_ph = clean_text.split() # result => first_name = "Sailesh" and ph_no = "(+977)9811234567"

ph_no = nonclean_ph.replace("(+977)", "") # result = "98112334567"

print(first_name) # result = "Sailesh"
print(ph_no) # result = "9811234567"