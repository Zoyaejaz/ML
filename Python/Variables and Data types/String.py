#String slicing
s1="zoya"
print(s1[0])
print(s1[0:2]) #this is called slicing
s2="amazing"
print(s2[1:6:2]) #slicing with skip value
print(s2[:7])
print(s2[0:])

#String functions
print(len(s1))  #len()
print(s1.upper())  #upper()
print(s2.endswith("r"))  #endswith()
print(s2.count("a"))     #count()
print(s1.capitalize())   #capitalize()
print(s2.find("n"))      #find()-->It will return index no.
print(s2.replace("a","l"))  #replace(oldword,newword)
print(s2) # this shows that the original string is not changed as strings are immutable in python. if we want to change the original string then we have to assign the new string to the original variable, by using any method like repace() or upper() etc. it does not change the original string


s4="Lemon, Ginger, Masala, Mint"
print(s4.split())
print(s4.split(", "))


s3="  hello"
print(s3.strip())  #it will remove the spaces from the start and end of the string
#to remove only the spaces at end, we use rstrip() and to remove only the spaces at start we use lstrip()

#To print something which contains both string and integer value we can use f-string
print(f"The age of isabel is {28/7} years") 
#on calculating the value of 28/7 it will give us 4.0 but if we want to print only 4 then we can use :0.0f in the f-string
print(f"The age of isabel is {28/7:.0f} years")
# the :.0f part tells Python to display the result of 28/7 without any decimal places. You don’t need to worry too much about the details, but the f in :.0f indicates that the number is a floating-point number and should be formatted accordingly. This means it will be rounded to the nearest whole number and displayed without any decimal part. So, in this case, it will display 4 instead of 4.0.
#to display one deciaml place we can use :.1f
print(f"The house was a good size: 1200 square feet, or {1200 * 0.092903:.1f} meters sq")
#or we can use placeholder for the value and then use format() method to replace the placeholder with the value
quantity=1200
type="Masala"
order="I want to order {} grams of {}"
print(order.format(quantity,type))



#To print multiple lines of string we can use triple quotes
print(f"""
    Most countries use the metric system for recipe measurement, 
    but American bakers use a different system. For example, they use 
    fluid ounces to measure liquids instead of milliliters (ml).
    
    So you need to convert recipe units to your local measuring system!
    
    For example, 8 fluid ounces of milk is {8 * 29.5735} ml.
    And 100ml of water is {100 / 29.5735} fluid ounces.
""")


#to convert list to string we can use join() method
my_list=["apple","banana","cherry"]

my_string=", ".join(my_list)
print(my_string)

my_string=" ".join(my_list)
print(my_string)

my_string="-".join(my_list)
print(my_string)

my_string="".join(my_list)
print(my_string)


#to include double string in the sentence
print("He said, \"Hello World\"")  #we can use backslash to include double quotes in the string
#to print word on the new line we can use \n
print("Hello\nWorld")

#to print any directives in the string we use raw string by adding r before the string
print(r"c:\user\pwd")
#if we want to print the above statement without raw, will give error
#we can write it by using double backslash
print("c:\\user\\pwd")
print(r"Hello\nWorld")  

