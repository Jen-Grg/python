#exception handling => to maintain the normal flow of code
# try:
#     a = int(input("Enter a number: "))
#     b = int(input("Enter a second number: "))
#     c = a+b
# except:
#     print("The value must be an integer")
# else:
#     print("The addition of two number is", c)
#     print("Successfully done.")
# print("Welcome to dursikhsya")
# try:
#     a = int(input("Enter a first number: "))
#     b = int(input("Enter a second number: "))
#     c = a/b
# except ValueError:
#     print("The value must be an integer")
# except ZeroDivisionError:
#     print("Values cannot be divided by 0")
# else:
#     print("The division of two number is", c)

#raise => u can only raise defined errors!!!!
def login():
    try:
        username = 'Jen'
        pin = 1234
        r_username = int("Enter your username: ")
        r_pin = int(input("Enter your pin: "))
        if(username != r_username):
            raise ValueError
        if(pin != r_pin):
            raise ZeroDivisionError
    except ValueError:
        print("Username is incorrect")
        login()
    except ZeroDivisionError:
        print("The pin number is invalid")
        login()
    else:
        print("Welcome to user dashboard")
    finally:
        print("Hello") #prints regardless of which error or else runs, so it can be printed multiple times if other errors are raised
login()
