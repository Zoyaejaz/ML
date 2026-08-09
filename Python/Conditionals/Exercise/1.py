#print yes if age is greater than or equal to 18
age=int(input("Enter your age: "))
if(age>=18):
    print("yes")
else:
    print("no")


#Write a program to find greatest of four numbers entered by the user
n1=int(input("Enter your first number: "))
n2=int(input("Enter your second number: "))
n3=int(input("Enter your third number: "))
n4=int(input("Enter your fourth number: "))
if(n1>n2 & n2>n3 & n3>n4):
    print("n1 is greatest: ",n1)
elif(n2>n1 & n1>n3 & n3>n4):
    print("n2 is greatest: ",n2)
elif(n3>n1 & n3>n2 & n3>n4):
    print("n3 is greatest: ",n3)
else:
    print("n4 is greatest: ",n4)