x = 50  # int
x = 60.5  # float
x = "Hello World"  # string
x = ["geeks", "for", "geeks"]  # list 
x = ("geeks", "for", "geeks")  # tuple

#Numeric types
a = 5  
print(type(a))  #Type checking
b = 5.0
print(type(b))
c = 2 + 4j
print(type(c))
print(float(40))
print(int(23.5))
x="10"
y=int(x)
print(type(y))
print(2**1000) #Python3 can easily handle this. it give the full value while when we run this line in python 2, it will give number with l in last telling its a long number. and does not give the full number 

#Basic operation
a=5
b=2
print(a+b)
print(a-b)
print(a/b)

#String
s = 'Welcome to the Geeks World'
print(s)
# check data type 
print(type(s))
# access string with index
print(s[1])
print(s[2])
print(s[-1])

#Boolean
valid=True
is_done=False
print(type(valid))
print(1<2)
# x<y<z 
#x<y and y<z -->this statement and the above statement both are same here we just use the and operator and in the above we use the shortcut  
#example
print(1==2<3)
print(1==2 and 2<3)

print('hello')
str('hello')
repr('hello')
print(True==1)
print(True is 1)  
print(True+4)  #as True is 1 therefore it will result 5(1+4)

