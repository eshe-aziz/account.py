#######INHERITANCE


class Vehicle:
    def __init__(self, make, model, color):
        self.make = make
        self.model = model
        self.color = color

    def move(self):
        print("Starts moving")

    def hoot(self):
        print("Honk honk")

class Bus(Vehicle):
    def __init__(self, make, model, color, capacity):
        super().__init__(make, model, color)
        self.capacity = capacity

    def start_boarding(self):
        print("The bus is now boarding")

class Lorry(Vehicle):
    def __init__(self, make, model, color, max_load):
        super().__init__(make, model, color)
        self.max_load = max_load

    def load(self):
        print("Started loading")

# >>> from vehicle import Bus,Lorry
# >>> b = Bus(make = "Isuzu", model = "Xyz", color = "Blue", capacity = 3000)
# >>> l = Lorry(make = "Tata", model = "Abc", color = "White", max_load = 10000)
# >>> b.hoot()
# Honk honk
# >>> b.start_boarding()
# The bus is now boarding











    