#if else, if elif, nesting
# age = int(input("Enter a age: "))
# if (age >= 18):
#     print("You are eligible for citizenship.")
# else:
#     print("You are not eligible fro citizenship")
#atm machine
user = int(input("Enter your pin: ")) 
if(user == 0000):
    user1 = int(input("Would you like to deposit, display or withdraw money from the bank(1/2/3): "))
    if(user1 == 1):
        deposit= int(input("How much money should be deposited: "))
        print(deposit , " amount is deposited.")
    elif(user1 == 2):
        print('10000 is stored in your account.')
    elif(user1 == 3): 
        withdraw= int(input("How much money should be withdrawn: "))
        if(withdraw<10000):
            print(withdraw , " amount is withdrawn.")
        else:
            print("The amount to be withdrawn is invalid. ")
    else:
        print('The option is invalid.')
else:
    print('The pin number is incorrect')
