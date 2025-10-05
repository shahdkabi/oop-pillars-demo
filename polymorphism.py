# Polymorphism: Ability to use the same interface for different data types.
class Bird:
    def fly(self):
        print("Bird is flying.")

class Airplane:
    def fly(self):
        print("Airplane is flying.")

def make_it_fly(thing):  # Polymorphic function
    thing.fly()  # Calls different implementations

# Usage
bird = Bird()
plane = Airplane()
make_it_fly(bird)  # Bird flies
make_it_fly(plane)  # Airplane flies