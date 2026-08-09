#Find greatest of 3 numbers
def greatest(n1,n2,n3):
    if(n1>n2 and n2>n3):
        print(f'{n1} is greatest')
    elif(n2>n1 and n1>n3):
        print(f'{n2} is greatest')
    else:
        print(f'{n3} is greatest')
greatest(5,7,4)

#Convert celsius to farenheit
def convert(celsius):
    return ((celsius*9)/5)+32
ans=convert(32)
print(ans)

#Sum of first n natural number
def sum(n):
    if n==1:
        return 1
    return n+sum(n-1)
print(sum(3))

#prevent a python print() function to print a new line at the end
print("Hello",end="")  #use the end statement 
print("world")
