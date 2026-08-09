#Multiplication Table printer
n=int(input("Enter the number: "))
for i in range(1,11):
    if(i==5):
        continue
    print(f"{n} X {i} ={n*i}")