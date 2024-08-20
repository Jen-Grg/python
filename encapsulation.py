#encapsulation is the process of binding data and method in a single unit. It is used to hide the data
# data hiding in encapsulation
#public=> we can access data from anywhere
#protected => data can be accessed within its class and subclass
#private=> the data can be accessed within only defined class
class Person:
    def __init__(self):
        self.name = "Ram"#.name is private
        self._age = 18#._ is protected
        self.__address = "Ktm" #.__ is private  (double underscore)
person = Person()
print(person.name)
print(person._age)
print(person)