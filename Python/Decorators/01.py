#Timing function execution
#problem: Write a decorator that measures the time a function takes to execute

import time

def timer(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        result=func(*args,**kwargs)
        end=time.time()
        print(f"{func.__name__} ran in {end-start} time")
        return result
    return wrapper

@timer               #here we are using the decorator 
def example_fun(n):
    time.sleep(n)

example_fun(2)