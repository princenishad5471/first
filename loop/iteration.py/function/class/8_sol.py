class Car:
    total_car=0
    def __init__(self,brand,model):
        self.model=model
        self.brand=brand
        Car.total_car += 1
    
    def full_name(self):
        return f"{self.brand} {self.model}" 

    
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    @staticmethod
    def general_description():
        return "Cars are means of transport"

class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size=battery_size

    def fuel_type(self):
        return "Electric Charge"

my_Tesla=ElectricCar("Tesla","model S","85kwh")

print(isinstance(my_Tesla,Car))
print(isinstance(my_Tesla,ElectricCar))

#print(my_Tesla.fuel_type())

my_car=Car("Tata","safari")
Car("Tata","Nexon")
print(Car.total_car)

#print(my_car.general_description())
print(Car.general_description())

#my_car=Car("toyota","corollo")
#print(my_car.brand)
#print(my_car.model)