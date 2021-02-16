
class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.name
    def run(self):
    	return self.mileage 
    def car(self):
    	return self.capacity	   
  
class Bus(Vehicle):
    

School_bus = Bus("School Volvo", 12, 50)
print("bus name", School_bus.fare())
print("total mileage is:",School_bus.run())
print("total capacity:",School_bus.car())
