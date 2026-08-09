#Validate input
while True:
    n=int(input("Enter the number: "))
    if(1<=n<=10):
        print(n)
        break
    else:
        print("Invalid input. Please enter a number between 1 and 10.")