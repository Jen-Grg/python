#object oriented programming=> deal with real  world object and entities
#instance of an object
#oop(Object Oriented Program) => we deal with real world project and entities

#blueprint of an object
class Room():
    l = int(input("Enter a length ="))
    w = int(input("Enter a width ="))
    h = int(input("Enter a height ="))

    def area(self):
        return self.l*self.w

    def volume(self):
        return self.l*self.w*self.h

room = Room() #object
print("The area of room is",room.area())
print("The volume of room is",room.volume())


class Calculator():
    def __init__(self, num, num1):
        self.num = num
        self.num1 = num1
        print(self.num)

    def add(self, *args):
        total = 0
        for i in args:
            total+=i
        return total
    
    def divide(self, num1, num2):
        return num1/num2
    
    def multiply(self, num1, num2):
        return num1*num2

calculator = Calculator(2,3)
print(calculator.add(1,2,3,4,5))
print(calculator.divide(1/0))
print(calculator.multiply(1/0))