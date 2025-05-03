from soundEffect import playCarAccelerationSound

class Car:
    totalCars = 0
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.topSpeed = 0
        Car.totalCars += 1

    def accelerate(self, speed_increase):
        self.topSpeed += speed_increase
        playCarAccelerationSound()
        return f"{self.brand} {self.model} is now at {self.topSpeed} km/h"

    def getInfo(self):
        return f"Car: {self.brand} {self.model}, Speed: {self.topSpeed} km/h"

