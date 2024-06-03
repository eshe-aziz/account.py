# Instance Variables

class Car:
    def __init__(self, model, make, color, year, speed):
        self.model = model
        self.make = make
        self.color = color
        self.year = year
        self.speed = speed


# OUTPUT
# >>> from car import Car
# >>> car1 = Car(model = "Audi", make = "R8", color = "white", year = 2024, speed = "303 kph")
# >>> car1.make
# 'R8'


# >>> car2 = Car(model = "Mazda", make = "CX-3", color = "maroon", year = 2024, speed = "100 kph")
# >>> car2.model
# 'Mazda'