#Pet recommendation
pet=input("Enter the type of pet you have: ")
age=int(input("Enter the age of your pet: "))
if(pet=="dog"):
    if(age<2):
        print("Give puppy food")
    else:
        print("Give adult dog food")
elif(pet=="cat"):
    if(age>5):
        print("Give senior cat food")
    else:
        print("Give regular cat food")