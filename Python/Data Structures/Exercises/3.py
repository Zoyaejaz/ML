#print type of s={}  -->dict
s={}
print(type(s))

#length of set
s1=set()
s1.add(20)
s1.add(20.0)
s1.add("20")
print(s1)
print(len(s1))
 
#can we have a set with 18(int) and "18(str)" as values in it? ----> Yes
s2={18,"18"}
print(type(s2))
print(s2)

#program to input eighth numbers from the user and display all the unique numbers(once).
n1=int(input("Enter first number: "))
n2=int(input("Enter second number: "))
n3=int(input("Enter third number: "))
n4=int(input("Enter fourth number: "))
n5=int(input("Enter fifth number: "))
n6=int(input("Enter sixth number: "))
n7=int(input("Enter seventh number: "))
n8=int(input("Enter eighth number: "))
s3=set()
s3.add(n1)
s3.add(n2)
s3.add(n3)
s3.add(n4)
s3.add(n5)
s3.add(n6)
s3.add(n7)
s3.add(n8)
print(s3)

#Can we change the alues inside a list which is contained in set s
s={8,7,12,"Hash",[1,2]}
s[3]="Zoya"
print(s)
#It will result in TypeError because set cannot contain lists , and sets element cannot be changed as it is immutable
