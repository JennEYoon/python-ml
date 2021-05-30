quantity = 3
item = 'widgets'
price = 4995.345
myorder = "I want {} pieces of {} for ${:,.2f}."
print(myorder.format(quantity, item, price)) 
>>>I want 3 pieces of widgets for $4,995.35.

# : is for formatting codes 
# $ is outside of {} 
# ,.2f means comma thousand separator, 2 decimal float16 number
# String has to be ' ' quotes in definition, input  

# Can be in all one line with ".format()" call to function.  
print("User {} is {} years old.".format("Tom", 17))
>>>User Tom is 17 years old.  
