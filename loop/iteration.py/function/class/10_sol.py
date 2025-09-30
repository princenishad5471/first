class Car:
    def __init__(self,brand,model):
        self.model=model
        self.brand=brand
    
    def full_name(self):
        return f"{self.brand} {self.model}" 

    
    
    def fuel_type(self):
        return "Petrol or Diesel"

class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size=battery_size

    def fuel_type(self):
        return "Electric Charge"

my_Tesla=ElectricCar("Tesla","model S","85kwh")
print(my_Tesla.fuel_type())

safari=Car("Tata","safari")
print(safari.fuel_type())


my_car=Car("toyota","corollo")
print(my_car.brand)
print(my_car.model)