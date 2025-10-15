class cng:
    def fuel_type(self):
        return "CNG fuel"

class petrol:
    def fuel_type(self):
        return "Petrol fuel"

class Car(cng, petrol):
    def show_fuel(self):
        print(self.fuel_type())   

car = Car()
car.show_fuel()  
