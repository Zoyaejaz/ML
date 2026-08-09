#Program whether the given name is in the list or not
selected=["zoya","ariba","misbah","shiba","fahad"]
name="zoya"
if(name in selected):
    print("the name is in the list.")
else:
    print("the name is not in the list.")

#calculate the grade
marks=int(input("Enter  the marks: "))
if(marks>90 and marks<=100):
    print("Excellent")
elif (marks>80 and marks<=90):
    print("A")
elif (marks>70 and marks<=80):
    print("B")
elif (marks>60 and marks<=70):
    print("C")
elif (marks>50 and marks<=60):
    print("D")
else:
    print("F")