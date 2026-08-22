# here we will know the use of *args in the function

#args means arguments
#*args is used in a Python function when you want the function to accept any number of positional arguments.


def sum_all(*args):
    return sum(args)
print(sum_all(1,2,3,4,5))
print(sum_all(1,4,2))
print(sum_all(1))
print(sum_all(1,5))

# *args = "I don't know how many positional arguments I'll receive, so collect them all into a tuple."

