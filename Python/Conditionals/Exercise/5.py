#Age Group categorization
age=int(input("Enter your age: "))
if(age<13):
    print("The person is child")
elif(age>=13 and age<19):  #here we can write only elif age<19 because the ageis less than 13 is already checked in the first if statement
    print("The person is a teenager")
elif(age>=20 and age<59):
    print("The person is an adult")
else:
    print("The person is a senior")