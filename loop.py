# pseudocode
'''

'''


# python source code
# initializing variables
# ask the user for inputs


unlock = 0
while (True):
    if (unlock == 3):
        any_number = int(input("Enter any number: "))
        if (any_number > 0):
            print("Number: Positive Number")
        if (any_number == 0):
            print("Number: Zero")
        if (any_number < 0):
            print("Number: Negative Number")

    if (unlock == 10):
        break
    
    else:
        password = 'APC'
        user_password = str(input("Enter your Password: ")).upper()
        if (user_password.__eq__(password)):
            print('if first')
            break

        elif (user_password != password):
            try_again = str(input("Try another [Y/N]: ")).upper()
            if (try_again == 'Y'):
                unlock += 1
                print(f"You Have Tried {unlock}/10 Time/s")
            elif (try_again == 'N'):
                print("This Will End The Looping Exercise!")
                break
            else:
                print("Invalid Input")
                break
        
        else:
            print('Program Terminated')
            break