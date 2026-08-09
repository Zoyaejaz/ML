import random

print(random.random()) #it will give the random number between 0 and 1 always

#we can get the random integer, to get the random integer between 1 and 100
print(random.randint(1,10)) #it will give the random integer between 1 and 10 where 1 is inclusive and 10 is exclusive


#we get some problem on working with decimal
print((0.1+0.1+0.1)-0.3)  #it will give you the result which will be very different to the result when you calculte it by yourself.

#so to handle decimal values,we will import libraries. similarly to work with fractions. we import Fraction from fractions
from decimal import Decimal
print(Decimal('0.1') + Decimal('0.1') + Decimal('0.1') -Decimal('0.3')) #it will give the correct value as we have calculated
