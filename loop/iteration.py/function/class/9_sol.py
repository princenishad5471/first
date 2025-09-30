class Car:
    total_car=0
    def __init__(self,brand,model):
        self.__model=model
        self.__brand=brand
        Car.total_car += 1
    
    def full_name(self):
        return f"{self.__brand} {self.__model}" 
 
    
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    @staticmethod
    def general_description():
        return "Cars are means of transport"
    
    @property
    def model(self):
        return self.__model

class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size=battery_size

    def fuel_type(self):
        return "Electric Charge"



class Battery:
    def battery_info(self):
        return "this is Battery"

class Engine:
    def engine_info(self):
        return "this is engine"

class ElectricCarTwo(Battery,Engine,Car):
    pass
    

my_new_tesla=ElectricCarTwo("Tesla","Model S")
print(my_new_tesla.engine_info())
print(my_new_tesla.battery_info())




