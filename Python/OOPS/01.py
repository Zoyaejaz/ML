# Basic Class and Object
# Create a Car class with attributes like brand and model. Then Create an instance of this class.


class Car:
    def __init__(self,userbrand,usermodel):   #this __init__ method is called a Constructor
        self.brand=userbrand
        self.model=usermodel

my_car=Car("Toyota","Corolla")
print(my_car.brand)
print(my_car.model)

new_car=Car("Maruti","Thar")
print(new_car.brand)
print(new_car.model)