#for i in range(1,4):
 #   for j in range(i):
  #      print("*",end=" ")
   # print()  

n=3
for i in range(n):
    for j in range(n):
        if(i==0 or j==0 or i==n-1 or j==n-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


for i in range(1,n+1):
    print(" "*(n-i),end="")
    print("*" *(2*i-1))