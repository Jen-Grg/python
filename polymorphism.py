#polymorphism=> having different forms
class Vehicle:
    def gear(self):
        print("Every vehicle has a gear system")
    def max_speed(self):
        print("Every vehicle has their own max speed")

class Car(Vehicle):
    def gear(self):
        print("the car has 5 gear system")
    def max_speed(self):
        print("Car has a max speed of 200km/hr")
class Bike(Vehicle):
    def gear(self):
        print("Bike has 5 gear system")
    def max_speed(self):
        print("The max speed of a bike is 150km/hr")

car = Car()
car.gear()
car.max_speed()
bike = Bike()
bike.gear()
bike.max_speed()
import math
#another example
class Shape:
    def area(self):
        return NotImplementedError("It's sub-class is not implement the parent method")
class Square(Shape):
    def area(self,length):
        self.length = length
        return self.length * self.length
class Circle(Shape):
    def area(self,radius):
        self.radius = radius
        return math.pi * radius*radius
    def show(self):
        print("Circle")
class Rectangle(Shape):
    def area(self,length,width):
        self.length = length
        self.width = width
        return self.length * self.width
square = Square()
print(square.area(6))
circle = Circle()
circle.show()
print(circle.area(6))
rectangle = Rectangle()
print(rectangle.area(5,7))