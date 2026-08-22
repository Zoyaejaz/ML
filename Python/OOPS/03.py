# Class Inheritance and ininsance() Fucntion
# Problem: Demonstrate the use of instance() to check if my_tesla is an instance of Car and ElectricCar

#isinstance() is used to check whether an object belongs to a particular class (or its child class).

class Car:
    def __init__(self,model,brand):
        self.model=model
        self.brand=brand

my_car=Car("tesla","unity")
print(isinstance(my_car,Car))