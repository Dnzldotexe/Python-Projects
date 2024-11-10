# ask user their hourly pay rate
# if the rate can't be converted to float
    # ask user to try again
# if the rate can be converted to float
    # display "your hourly rate is", x
# the program should not finish until user has entered a value that can be converted to float


while True:
    try:
        rate = round(float(input("What is your hourly rate? ")), 2)
    except:
        print("Try again.")
        continue
    print("Your hourly rate is", rate)
    break