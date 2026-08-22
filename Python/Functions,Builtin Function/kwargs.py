#Function with **kwargs
#create a function that accepts any number of keyword arguments and prints them in the format key:value


# kwargs means keyword argments 
# **kwargs is used in a Python function when you want the function to accept any number of positional arguments.

def print_n(**kwargs):
    for key,value in kwargs.items():
      print(f"{key}: {value}")

print_n(name="shaktiman",power="lazer")
print_n(name="shaktiman")
print_n(name="spiderman",power="web",enemy="shaktiman")





