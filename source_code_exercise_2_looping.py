#python source code

unlock = 1
while (True):
    password = 'APC'
    user_password = str(input("Enter your Password: "))
    if (user_password.__eq__(password) and unlock == 3):
        any_number = int(input("Enter any number: "))
        if (any_number > 0):
            print(f"Number({any_number}): Positive Number")
        if (any_number == 0):
            print(f"Number({any_number}): Neutral")
        if (any_number < 0):
            print(f"Number({any_number}): Negative Number")
        print("Thank you again!")
        break

    elif (user_password.__eq__(password) and unlock < 3):
        numbers = []
        for x in range(1, 11):
            if (x == 1):
                range_number = int(input(f"Enter {x}st Number: "))
            if (x == 2):
                range_number = int(input(f"Enter {x}nd Number: "))
            if (x == 3):
                range_number = int(input(f"Enter {x}rd Number: "))
            if (x > 3):
                range_number = int(input(f"Enter {x}th Number: "))
            numbers.append(range_number)
        print(f"Lowest Number: {min(numbers)}")
        print(f"Highest Number: {max(numbers)}")
        break
    
    elif (user_password != password and unlock >= 3):
        print(f"{unlock}/3 Tries Have Been Used")
        try_again = str(input("Try another [Y/N]: ")).upper()
        if (try_again == 'Y'):
            unlock -= 2
            continue
        elif (try_again == 'N'):
            print("This Will End The Looping Exercise!")
            break
        else:
            print("Invalid Input")
            break

    elif (user_password != password and unlock < 3):
        unlock += 1

    else:
        print('Program Terminated!')
        break