# Inheritance: Child classes inherit properties/methods from parent.
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

class Dog(Animal):  # Inherits from Animal
    def speak(self):
        print(f"{self.name} barks: Woof!")

class Cat(Animal):  # Inherits from Animal
    def speak(self):
        print(f"{self.name} meows: Meow!")

# Usage
dog = Dog("Buddy")
dog.speak()  # Overrides parent's speak
cat = Cat("Whiskers")
cat.speak()