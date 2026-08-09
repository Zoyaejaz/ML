#Function which converts inches to cms
def convert(inches):
    cms = inches * 2.54
    return cms
print(convert(10))

#Function to print first n lines of the following pattern
def pattern(n):
    for i in range(1,n+1):
        for j in range(i):
            print("*",end=" ")
    print()
pattern(4)

#Function to remove a given word from a string and strip it at the same time
def remove_and_strip(string, word):
    new_string = string.replace(word, "")
    return new_string.strip()
print(remove_and_strip("   Hello World   ", "World"))

#Function to print the multiplication table of a given number
def table(n):
    for i in range(1,11):
        print(f'{n} X {i} = {n*i}')
table(5)