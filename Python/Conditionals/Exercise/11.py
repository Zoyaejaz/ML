#coffee customization
order_size=input("Enter the size of your coffee (small, medium, large): ")
extra_shot=True
if(extra_shot):
    if(order_size=="small"):
        print("The coffee size is small with an extra shot")
    elif(order_size=="medium"):
        print("The coffee size is medium with an extra shot")
    elif(order_size=="large"):
        print("The coffee size is large with an extra shot")
else:   
    if(order_size=="small"):
        print("The coffee size is small")   
    elif(order_size=="medium"):
        print("The coffee size is medium")
    elif(order_size=="large"):
        print("The coffee size is large")
