# No. 1

## a) Duck Typing is a type of programming style where an object's suitability is determined by the methods and attributes it has, not theits class or inheritance hierarchy.
## b) It needed a speak function to be implemented in the car class which enabled it to work in the same loop as classes Dog and cat without inheriting from Animal superclass.
#No.2
class Car:
  def move(self):
    print("The car drives on the road.")
class Boat:
  def move(self):
    print("The boat sails on water.")
class Drone:
  def move(self):
    print("The drone flies in the sky.")

def start_trip(vehicle):
  vehicle.move()

Vehicles = [Car(), Boat(), Drone()]
for vehicle in Vehicles:
  start_trip(vehicle)

# No. 3
## The code demonstrated polymorphism the printed output of the move() function from each class were different from each other, which all resulted fro the start_trip() method.