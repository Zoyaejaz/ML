# Multiple Inheritance
# Problem: Create two classes Battery and Engine, and let the ElectricCar class inherit from both, demonstrating multiple inheritance

class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

class Battery:
    def bat_info(self):
        return "this is battery"

class Engine:
    def eng_info(self):
        return "this is engine"

class ElectricCar(Battery,Engine,Car):
    pass

my_car=ElectricCar("Tesla","Model S")
print(my_car.eng_info())
print(my_car.bat_info())