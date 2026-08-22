
x=99
def f1():
    x=88  #if we don't write x here then we get 99 only on printing x
    def f2():
        print(x)
    return f2
result=f1()
result()

#In the first example, x = 99 is in the global scope, but inside f1() you create another x = 88. Then f2() is defined inside f1() and tries to print x. Python first looks inside f2() but doesn't find x, so it looks in the enclosing function f1(), where it finds x = 88, and therefore prints 88. When you do result = f1(), result stores the f2 function itself, and when you call result(), f2() still remembers the x = 88 from f1(). This remembering of the outer variable is called a closure.



def code(num):
    def actual(x):
        return x**num
    return actual

f=code(2)
g=code(3)
print(f)
print(g)
print(f(3))
print(g(2))

#In the second example, code(num) is a function that creates another function. When you do f = code(2), the inner actual(x) function remembers num = 2, so f(3) means 3², giving 9. Similarly, when you do g = code(3), another actual(x) function is created that remembers num = 3, so g(2) means 2³, giving 8. In simple words, code(2) creates a function for squaring, while code(3) creates a function for cubing. This is also an example of a closure because the inner function remembers the value of num.