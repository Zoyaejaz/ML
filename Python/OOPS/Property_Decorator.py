# Property Decorator
# Use a Property decorator in the Car class to make the model attribute read-only



class Car:
    total_Car=0

    def __init__(self,brand,model):
        self.__brand=brand
        self.__model=model
        Car.total_Car+=1

    def full_name(self):
        return f"{self.__brand} {self.__model}"

    def get_brand(self):
        return self.__brand+" !"
    
    @staticmethod  #on writing this, the given method will work for the another new object as well as this main class Car
    def general_desc():
        return "Cars are means of transport"

    @property  #this is used, when we want to hide some property which can't be accessed by everyone, and the other reason is we can't override the given variable
    def model(self):
        return self.__model

class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)   
        self.battery_size=battery_size
my_tesla=ElectricCar("Tesla","Model S","85kWh")
#my_tesla.model="City"  # now it will not work as we have used @property above the model method and make the model attribute private as well
print(my_tesla.model)  



    

    
