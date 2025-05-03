from car import Car
from electricCar import ElectricCar

Car1=Car("Dodge","Challenger")
Car2=Car("Toyota","Supra")
Car3=Car("Ford","GT Mustang")

eCar1=ElectricCar("Tesla","Model S",100)
eCar2=ElectricCar("Xiaomi","SU7",210)

print(eCar1.charge(20))
print (Car1.accelerate(20))
print(eCar2.model)