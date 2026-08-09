#transportation mode selection
distance=float(input("Enter the distance: "))
if(distance<3):
    print("You can walk")
elif distance<=15:
    print("Take a Bike")
else:
    print("Take a Car")