#A student is passed r not according to total perentage and each subject percentage
marks1=int(input("Enter the marks of subject1: "))
marks2=int(input("Enter the marks of subject2: "))
marks3=int(input("Enter the marks of subject3: "))
sub1=(marks1/100)*100
sub2=(marks2/100)*100
sub3=(marks3/100)*100
total=(int)((marks1+marks2+marks3)/3)*100
if(total>=40 and sub1>=33 and sub2>=33 and sub3>=33):  #we use and if we want to compare both side are truthy or falsy value. and we use & if we want to comapare each and every bit like math
    print("Student has passed in the exam.")
else:
    print("Student has failed in the exam.")