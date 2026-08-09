f=open("File_Input_Output/first.py")  #the iter() object is by default in file that's why we don't have to call iter() function to create an iter object for the file as we have done in the case of list and string
print(iter(f) is f) #this will return true because the file object itself is an iterator
print(iter(f) is f.__iter__()) #this will also return true because the file object itself is an iterator and it will return itself when we call __iter__() method on it
print(f.readline())
#once it will read the first line then it will move to the next line so if we again call readline() it will read the second line and once it read all the line then at end it will return empty string

#but when we write
f.__next__()
#it will read the next line and it will return the line and it will move to the next line so if we again call __next__() it will read the next line and once it read all the line then at end it will raise StopIteration error

#we can also read the file by using for loop
for line in open ("File_Input_Output/first.py"):
    print(line)
    #this will automatically read the file line by line and it will print the line and once it read all the line then it will stop the loop

#by using while loop
f=open("File_Input_Output/first.py")
while True:
    line=f.readline()
    if not line:
        break
    print(line)