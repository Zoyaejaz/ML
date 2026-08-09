import math #math is a library in the python
print(math.floor(3.5)) #floor gives the closest value below value.That's why in this it will give 3 and not 4 bcz the closest is 3 and it is below the value. it gives the bottom value. if we give 3.9 also it will give 3
print(math.floor(-3.5)) #here we get -4 bcz -4 is lower than -3
print(math.floor(3.6)) 
print(math.floor(3.2))

print(math.trunc(2.8)) #trunc takes you near the zero . ye zero ke paas le jaata hai
print(math.trunc(-2.8)) #here we get -2 bcz -2 is closer to 0 as compared to -3

#to write octal value
print(0o20)
#to print hexadecimal 
print(0xFF)
#to print binary number
print(0b100)

#we can convert the one data type to other
print(oct(64))
print(hex(64))
print(bin(64))

#we cann also use the int() method for the above process
print(int(64))
print(int('64',8)) #8 will tell we want the octal value of the number 64 
print(int('64',16))  #here 8,16 and others tell about the base in which we want to convert 
print(int('100001',2))

