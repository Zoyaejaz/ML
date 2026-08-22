#Polymorphism
#It is defined as The same method name can behave differently depending on the object using it.

# Demonstrate polymorphism by definig a method fuel_type in both Car and ElectricCar classes,but with different behaiours.

class Car:
    total_car=0
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
        Car.total_car += 1

    def full_name(self):    #this is called method
        return f"{self.brand} {self.model}"

    def fuel_type(self):
        return "Petrol or Diesal"

class ElecticCar(Car):
    def __init__(self, brand,model,battery_size):
        super().__init__(brand,model)   #super() helps me to get the access of the upper class
        self.battery_size=battery_size
    def fuel_type(self):
        return "Electric charge"

my_tesla=ElecticCar("Tesla","Model S","85kWh")
#print(my_tesla.__brand) --> we get the error in this bcz it becomes private 
print(my_tesla.fuel_type())
safari=Car("Tata","Safari")
print(safari.fuel_type())
print(Car.total_car)