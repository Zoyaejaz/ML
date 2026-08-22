#Debugging Function calls
#problem: Create a decorator that print the function name and the values of its arguments every time the function is called.

def debug(func):
    def wrapper(*args,**kwargs):
        args_val=', '.join(str(arg) for arg in args)
        kwargs_val=', '.join(f"{k}={v}" for k,v in kwargs.items())
        print(f"calling: {func.__name__} with args {args_val} and kwargs {kwargs_val}")
        return func(*args,**kwargs)
    return wrapper


@debug
def greet(name,greeting="hello"):
    print(f"{greeting},{name}")

greet("Zoya")
greet("saira","hi")