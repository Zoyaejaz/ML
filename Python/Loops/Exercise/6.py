str=input("Enter the string: ")
output=str[::-1]
print(output)

#Or we can also do it by using for loop
output="Python"
reverse=""
for char in output:
    reverse=char+reverse
print(reverse)