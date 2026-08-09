# List is an ordered data type, it is a mutable data type 
# Empty list
a = []
# list with int values
a = [1, 2, 3]
print(a)
print(a[1:1]) # it will give us empty list as we are slicing from index 1 to 1
#to add the element in list we can use append() method
a.append(4)
print(a)
#to remove the last element from the list we use pop()
a.pop()
print(a)  #to delete any other element from the list we can use remove() method
# list with mixed values int and String
b = ["Geeks", "For", "Geeks", 4, 5]
print(b)
#Accessing elements from list
c = ["Geeks", "For", "Geeks","Programming","DSA","Learning"]
print("Accessing element from the list")
print(c[0])
print(c[2])
print(c[-2])
print(c[0:3])
numbers = [1, 2, 4, 3]
c[2]="Python" # we can change the value of list as it is mutable data type
print(c)
c[3:4]="goal" # we can also change the value of list by slicing
print(c[3])
c[4:5]=["Lemon"] #on slicing we have to assign the value in list format as it is a list
print(c[4])
print(c)


#List methods
numbers.sort()  #it sort the elements of list in an ascending order
print(numbers)

numbers.reverse() #it updates the ist in from last to first element
print(numbers)

numbers.append(8) #it adds the element at the end of the list
print(numbers)

numbers.insert(3,7) # it will add 7 at the index 3
print(numbers)

numbers.pop(2) #it will delete element at index 2 and return its value
print(numbers)

numbers.remove(7) #it will remove 7 from list
print(numbers)

#using random library in list to shuffle the list and many more 
import random
l1=['lemon','masala','ginger','mint']
print(random.choice(l1))  #it will randomly choose any element from l1
print(random.choice(l1))
print(random.choice(l1))
random.shuffle(l1)  #it will shuffle the elements of the list
print(l1)


#List comprehension
#List comprehension is a concise way to create new list by iterating over an existing iterable(like a list,tuple, or range) and optionally applying a condition.
squares=[x**2 for x in range(5)]
print(squares)


