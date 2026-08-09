#Movie ticket pricing
age=int(input("Enter your age:"))
day=input("Enter the day of the week:")
if(age>=18):
    if(day=="Wednesday"):
        print("The ticket is of $10 price")
    else:
        print("The ticket is of $12 price")
else:
    if(day=="Wednesday"):
        print("The ticket is of $6 price")
    else:
        print("The ticket is of $8 price")


#we can write this above code in a short form also 
age=int(input("Enter your age:"))
day=input("Enter the day of the week:")
price=12 if age>=18 else 8
if day=="wednesday":
    price-=2
print("The ticket price is $",price)