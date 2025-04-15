class Car:
    brand = "Volvo"
    


car1 = Car()
print(car1.brand)    



class Vehicle:
    def __init__ (self, brand, doors, wheels=4):
        self.brand = brand
        self.doors = doors
        self.wheels = wheels
    def car_greeting(self, localGreeting="Hello"):
        print(f'{localGreeting} from {self.brand} car, that has {self.doors} doors and {self.wheels} wheels')    


veh1 = Vehicle("Toyota",2,3)
veh2 = Vehicle("Honda", 4)

veh1.car_greeting('Sho ')
