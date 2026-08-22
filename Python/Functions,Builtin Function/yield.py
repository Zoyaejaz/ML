# Generator function with yield
#write a generator function that yields even numbers up to a specified limit.

#yield is a Python keyword used to create a generator.


def even_generator(limit):
    for i in range(2,limit+1,2):
        yield i

for num in (even_generator(10)):
    print(num)


#return gives you the result and ends the function. yield gives you one result, pauses the function, and remembers where it stopped.
#This "pause and continue later" behavior is the main purpose of yield.


#The biggest advantage is memory efficiency.Imagine you want numbers from 1 to 1 billion.