# Inheritance
# It is defined as A child class can reuse properties and methods of a parent class.


#Problem: Create an ElectricCar class that inherits from the Car class and has an additional attribute battery_size

class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def full_name(self):    #this is called method
        return f"{self.brand} {self.model}"

class ElecticCar(Car):
    def __init__(self, brand,model,battery_size):
        super().__init__(brand,model)   #super() helps me to get the access of the upper class
        self.battery_size=battery_size

my_tesla=ElecticCar("Tesla","Model S","85kWh")
print(my_tesla.full_name())