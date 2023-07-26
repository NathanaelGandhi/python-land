# Creating a Python class
class Car:
    speed = 0
    started = False
    def start(self):
        self.started = True
        print("Car started, let's ride!")
    def increase_speed(self, delta):
        if self.started:
            self.speed = self.speed + delta
            print('Vrooooom!')
        else:
            print("You need to start the car first")
    def stop(self):
        self.speed = 0
        print('Halting')

print('Hello world')

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
