from car import Car

class ElectricCar(Car):
    def __init__(self, brand, model, batteryCapacity):
        super().__init__(brand, model)
        self.battery_capacity = batteryCapacity
        self.batteryLevel = 100

    def accelerate(self, speedIncrease):
        self.topSpeed += speedIncrease
        self.batteryLevel -= speedIncrease * 0.1
        if self.batteryLevel < 0:
            self.batteryLevel = 0
            self.topSpeed = 0
        return f"{self.brand} {self.model} is at {self.topSpeed} km/h, Battery: {self.batteryLevel}%"

    def charge(self, charge_amount):
        self.batteryLevel += charge_amount
        if self.batteryLevel > 100:
            self.batteryLevel = 100
        return f"{self.brand} {self.model} charged to {self.batteryLevel}%"