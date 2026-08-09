l=[1,7,8]
for item in l:
    print(item)
else:
    print("Done")

#ex: using range() function
for i in range(0,7):
    print(i)  

#using break statement
for i in range(0,80):
    print(i)
    if i==3:
        break

#using continue statement
for i in range(4):
    print("printing")
    if i==2:
        continue
    print(i)

#pass statement --> it is a null statement in python. It instructs to "Do nothing" 
l=[1,7,8]
for item in l:
    pass