#Calculate the factorial of a given number(ex:5) using for loop
fact=1
for i in range(1,5):
    fact=fact*i
print(fact)

#find the sum of first 10 natural number using while loop
sum=0
i=1
while(i<11):
    sum=sum+i
    i=i+1
print(sum)

#check whether the given number is prime or not
n=11
i=1
count=0
while(i<=n):
    if(n%i==0):
        count=count+1
    i=i+1
if(count>2):
    print(f'{n} is not a prime number')
else:
    print(f'{n} is a prime number')

#program to greet all the person names stored in a list and whose name starts with s
l1=["Harry","Sohan","Sachin","Rahul"]
for item in l1:
    if(item.startswith("S")):
        print(f'Good Morning {item}')