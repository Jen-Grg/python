#create a simple function that takes a number and check if its digits contain no.5 ot not

#list comprehension=>List comprehension is an easy to read, compact, and elegant way of creating a list from any existing iterable object. List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

#dictionary comprehension bring definitions
# Dictionary comprehension in Python is a concise way to create dictionaries. It allows you to generate a dictionary from an iterable in a single line of code using a similar syntax to list comprehensions.
# Creating a dictionary with squares of numbers
squares = {x: x**2 for x in range(5)}
print(squares) 

#map
def addition(n):
    return n + n
numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))
#filter
def check(x):
    if x < 18:
        return False
    else:
        return True
age = [13,18,2,19,20]
adults = filter(check, age)
for x in adults:
    print(x)

#reduce
from functools import reduce
def product(a,b):
    return a*b
num = [1,2,3,4,5]
ans = reduce(product,num)
print(ans)

print("Please use a positive digit")
def check(number):
    count = 0
    while number>0:
        number //= 10 #floor division
        count+=1
    for number in range(1, count+1):
        number%=10
        if(number==5):
            print("The digits contain the number 5")
        else:
            continue
    # for num in str(number):
    #     if(num =='5'):
    #         print("Yes")
check(int(input("Enter your digit: ")))

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