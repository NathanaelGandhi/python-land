# Creating a module
import mymodule

# Importing specific parts of a Python module
from mymodule import my_function


# Python inheritance example
class Vehicle:
    def __init__(self, started=False, speed=0):
        self.started = started
        self.speed = speed

    def start(self):
        self.started = True
        print("Started, let's ride!")

    def stop(self):
        self.speed = 0

    def increase_speed(self, delta):
        if self.started:
            self.speed = self.speed + delta
            print("Vrooooom!")
        else:
            print("You need to start me first")


# Creating a Python class
# Modified into Creating your own Python constructor
# Modified into Python inheritance example
class Car(Vehicle):
    trunk_open = False

    def open_trunk(self):
        self.trunk_open = True

    def close_trunk(self):
        self.trunk_open = False


# Overriding Python methods
# Modified into Overriding other methods
class Motorcycle(Vehicle):
    def __init__(self, center_stand_out=False):
        self.center_stand_out = center_stand_out
        super().__init__()

    def start(self):
        print("Sorry, out of fuel!")


# Hello World
# Modified into Creating a module
mymodule.my_function()

# Importing specific parts of a Python module
my_function()

# Create a Python object
car = Car()
car.increase_speed(10)
car.start()
car.increase_speed(40)

# Creating Multiple Python Objects
car1 = Car()
car2 = Car()
print(id(car1))
print(id(car2))
car1.start()
car1.increase_speed(10)
print(car1.speed)
print(car2.speed)

# Creating your own Python constructor
c1 = Car()
c2 = Car(True)
c3 = Car(True, 50)
c4 = Car(started=True, speed=40)
