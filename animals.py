#####POLYMORPHISM

class Animal:
    def make_sound(self):
        pass

    def move(self):
        pass

    def produce(self):
        pass

    def eat(self):
        pass

class Bird(Animal):
        def make_sound(self):
            print("Chirp")

        def move(self):
            print("The bird is flying")

        def produce(self):
            print("Eggs")

        def eat(self):
            print("Grains")

class Fish(Animal):
        def make_sound(self):
            print("Click")

        def move(self):
            print("Swimming")

        def produce(self):
            print("Fish")

        def eat(self):
            print("Hybranith")

class Dog(Animal):
        def make_sound(self):
            print("Barks")

        def move(self):
            print("Running")

        def produce(self):
            print("Puppies")

        def eat(self):
            print("Bones")

class Human(Animal):
        def make_sound(self):
            print("Talks")

        def move(self):
            print("Walks")

        def produce(self):
            print("Children")

        def eat(self):
            print("Food")

# >>> from animals import Bird,Fish,Human
# >>> b = Bird()
# >>> b.make_sound()
# Chirp






            
                 