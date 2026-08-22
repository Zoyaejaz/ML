def func():
    global x
    x=12
func()     #we have executed function that's why we get the value of x otherwise we get the error of x is not defined.
print(x)

#this type of cases is mostly avoided by developers, to escape from the error of overriding