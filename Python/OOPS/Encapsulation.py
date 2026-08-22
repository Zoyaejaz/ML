# Encapsulation
#it is defined as Bundling data and the methods that work on that data together inside a class, while controlling access to the data.


# Problem: Modify the Car class to encapsulate the brand attribute, making it private, and provide a getter method for it.

class Car:
    def __init__(self,brand,model):
        self.__brand=brand  #when we write any attribute with double underscore, then it becomes proivate. so any class cannot access that variable. another class has to use getter to access this attribute
        self.model=model

    def get_brand(self):    #this is getter method
        return self.__brand + " !"

    def full_name(Self):
        return f"{self.__brand} {self.model}"

class ElecticCar(Car):
    def __init__(self, brand,model,battery_size):
        super().__init__(brand,model)   
        self.battery_size=battery_size

my_tesla=ElecticCar("Tesla","Model S","85kWh")
#print(my_tesla.__brand) --> we get the error in this bcz it becomes private 
print(my_tesla.get_brand())