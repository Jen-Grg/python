#function is a block of code which can be reused again and again. to define a function we use def keyword
#defining the function
# 4

# student('Hari','Python', 'HTML') how to handle such cases when only two positional arguments can be taken,
#  it can be done through using *args which is arbitary arguments where we can pass unlimited value
# def students(*args):
#     print("The student name is {0} and the student's chosen subject is {1}".format(args[0],args[1]))

# students('Pan','Full Stack','HTML','CSS','React')

# def number(*args):
#     sum = 0
#     for i in args:
#         sum += i
#         print(sum)
# #if i have no use for the current function but m using it for future reference, us the keyword pass
# number(1,2,3,4,5,6,7,8,9)
def lists():
    lst =[]
    x = int(input("Enter the length of list: "))
    while x!=0:
        for x in range(1,x+1):
            element = int(input("Enter the elements in list: "))
            lst.append(element)
        if lst != []:
            print("The sum of {0} and {1} is {2}".format(lst[0],lst[-1],lst[0]+lst[-1]))
            break
    print("A value needs to be provided otherwise the first and last index's sum cannot be found as the list is null")
lists()
#**kwargs => keyword arbitary arguments which can pass unlimited data in key: value pair
# def std(**kwargs):
#     print("The student name is ",kwargs['name'],"The student has chosen the subject",kwargs['subject4'])
# std(name='Ram', subject1='HTML',subject2='CSS', subject3='Java',subject4='Python')
    
#scope of variable: global variable and local variable
# l = int(input("Enter length: "))#global variable
# b = int(input('Enter breadth: '))
# def area():
#     return f"The area of object is={l*b}"
# def volume():
#     h = int(input('Enter height: ')) #local variable which can only be accessed inside the defined class
#     return f"The volume of object is={l*b*h}"
# print(area())
# print(volume())
#lambda function- a function created for instance use by using lambda keyword

a = lambda a,b:a+b
print("The addition of two number is", a(2,5))
#recursive function =>a function which is called inside itself
def factorial(num):
    if num==0:
        return 1
    else:
        return num*factorial(num-1)
fact = factorial(int(input("Enter a number for factorial: ")))
print("The factorial of given number is", fact)
#map
def addition(n):
    return n + n
numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))
#filter
#reduce
#high order function: a function which uses another function as a parameter
