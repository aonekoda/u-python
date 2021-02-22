class MotorVehicle:
    def __init__(self, range):
        self.range = range
        self.tank = range
    def travel(self, distance):
        if distance > self.tank:
            print(f"Not enough in the tank. Only traveled {self.tank} kilometers.")
            self.tank = 0
        else:
            print(f"VOOOM! Traveled {self.distance} kilometers.")
            self.tank -= distance
    def refuel(self):
        print("Refueling...")
        self.tank = self.range
    def __str__(self):
        print(f"Vehicle(range={self.range}, tank={self.tank})")

class Car(MotorVehicle):
    def __init__(self, range, wheels, color):
        super().__init__(range)
        self.wheels = wheels
        self.color = color
'''
mv = MotorVehicle(100)
print(mv)  # Vehicle(range=100, tank=100)
mv.travel(50)  # VOOOM! Traveled 50 kilometers.
mv.travel(30)  # VOOOM! Traveled 30 kilometers.
mv.travel(20)  # Not enough in the tank. Only traveled 20 kilometers.
print(mv)  # Vehicle(range=100, tank=0)
mv.refuel()  # Refueling...
print(mv)  # Vehicle(range=100, tank=100)
'''

'''
c = Car(500, 4, 'red')
print(c.range)  # 500
print(c.tank)  # 500
print(c.wheels)  # 4
print(c.color)  # 'red'
print(c.__dict__)  # {'range': 500, 'tank': 500, 'wheels': 4, 'color': 'red'}
c.travel(50)  # VOOOM! Traveled 50 kilometers.
c.travel(100)  # VOOOM! Traveled 100 kilometers.
c.refuel()  # Refueling...
print(c)  # Vehicle(range=500, tank=500)
'''
