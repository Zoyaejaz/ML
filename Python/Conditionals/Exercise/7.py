#Grade calculator
marks=int(input("Enter your marks: "))
if(marks>100 or marks<0):
    print("Invalid marks entered")
    exit()  #this will stop the execution of the program if the marks entered are invalid and will not check the other conditions
if(marks>=90 and marks<=100):
    print("Grade: A")
elif marks>=80: # the above if condition already checks whether the marks are less than or equal to 100 so we can write only elif marks>=80
    print("Grade: B")
elif marks>=70:
    print("Grade: C")
elif marks>=60:
    print("Grade: D")
else:
    print("Grade: F")