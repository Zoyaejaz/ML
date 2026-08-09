#Find the first non-repeated character in a string
input=input("Enter the string: ")
for char in input:
    if(input.count(char)==1):
        print(char)
    else:
        continue
        