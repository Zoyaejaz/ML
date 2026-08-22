#Static method
# It is defined as a method that belongs to a class rather than an instance(object) of a class.

class Car:
    total_Car=0

    def __init__(self,brand,model):
        self.__brand=brand
        self.model=model
        Car.total_Car+=1

    def full_name(self):
        return f"{self.__brand} {self.model}"

    def get_brand(self):
        return self.__brand+" !"
    
    @staticmethod  #on writing this, the given method will work for the another new object as well as this main class Car
    def general_desc():
        return "Cars are means of transport"

class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)   
        self.battery_size=battery_size
my_tesla=ElectricCar("Tesla","Model S","85kWh")
print(my_tesla.general_desc())  #as in this, if i don't write static method, and write self inside an argument of the method, it will give me an output
print(Car.general_desc())# in this, after writing @staticmethod and removing the self in the argument, then only it  can give the output


    

    