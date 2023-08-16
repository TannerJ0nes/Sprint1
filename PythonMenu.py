

# Def fizz function which auto runs with no input from
# user other then menu selection
# Author: Tanner Jones
# Date: February 20th 2023
global MenuUse
MenuUse = 1

# list of functions for menu options
def fizz():

    # 101 used to run loop 100 times
    for num in range(1, 101):
        string = ""
        if num % 3 == 0:
            string = string + "Fizz"
        if num % 4 == 0:
            string = string + "Buzz"
        if num % 4 != 0 and num % 3 != 0:
            string = string + str(num)
        print(string)
    input("Press any key to continue")


# a program to get your employee identification number and  daily access code for super secret chocolate lab

# author: Ryan Crowley
# date : February 19 2023

def StringFun():
    # imports
    import datetime

    #inputs for employee information
    firstName = input("Enter employee's first name: ").upper()
    lastName = input("Enter employee's last name: ").upper()
    phoneNum = input("Enter employee's phone number (###-###-####): ")
    startDate = input("Enter employee's start date: (YYYY-MM-DD): ")
    birthDate = input("Enter employee's date of birth (YYYY-MM-DD): ")
    curDate = datetime.datetime.now()

    def IDnumber(firstName, lastName, phoneNum, startDate, birthDate):
        partA = firstName[:2]
        partB = lastName[:2]
        partC = startDate[2:4]
        partD = birthDate[-2:]
        partE = phoneNum[-4:]
        identification = partA + partB +"-"+ partC + partD + "-" + partE
        return (identification)

    def DailySecertCode (curDate, firstName, lastName,):
        nameCodeA = len(firstName)
        nameCodeB = len(lastName)
        timeCodeA = datetime.datetime.strftime(curDate, "%Y")
        timeCodeA = int(timeCodeA)
        timeCodeB = datetime.datetime.strftime(curDate, "%f")
        timeCodeB = timeCodeB[-4:]
        passCodeA = timeCodeA//nameCodeA
        passCodeA = str(passCodeA)
        passCodeB = timeCodeA//nameCodeB
        passCodeB = str(passCodeB)
        passCode = passCodeA + "-" + passCodeB + "-" + timeCodeB
        return(passCode)

    print("WELCOME" , IDnumber(firstName, lastName, phoneNum, startDate, birthDate))
    print("HERE IS YOUR DAILY TEMPORARY PASS CODE TO ENTER THE SUPER SECRET CHOCOLATE R&D DEPARTMENT")
    print("*"*91)
    print(DailySecertCode (curDate, firstName, lastName,))
    input("Press any key to continue ...")


# Program to determine the travel expenses that employees must claim

# Author: Ryan Crowley
# Date: February 18th 2023

def Claim():
    # Imports and constants
    import datetime
    HST = 0.15
    DAY_RATE = 85.00
    MILE_RATE = 0.17  # for when employee uses own car
    RENT_RATE = 65.00  # for when employee uses rented car
    DAY_BONUS = 100.00  # for tips longer than 3 days
    MILE_BONUS = 0.04  # for tips in own car over 1000km
    EXEC_BONUS = 45.00
    DATE_BONUS = 50.00  # for trips that happen between Dec 15 and Dec 22

    # Inputs for the employees expenses on their trip

    while True:
        while True:
            employeeNum = input("Enter the employees number (5 numerical characters): ")
            if employeeNum == "":
                print("Employee number cannot be left blank, please re-enter.")
            elif employeeNum.isnumeric() is False:
                print("Employee number must contain only numerical values (1-9).")

            elif len(employeeNum) != 5:
                print("Employee number must be 5 digits long.")
            else:
                break

        firstName = input("Enter the employee's first name: ").title()
        lastName = input("Enter the employee's last name: ").title()
        location = input("Enter the location of employee's trip: ")

        while True:
            try:
                startDate = input("Enter the start date of employee's trip (YYYY-MM-DD):")
                startDate = datetime.datetime.strptime(startDate, "%Y-%m-%d")
            except:
                print("The start date is invalid, please re-renter in proper format.")
            else:
                break

        while True:
            try:
                endDate = input("Enter the end date of employee's trip (YYYY-MM-DD): ")
                endDate = datetime.datetime.strptime(endDate, "%Y-%m-%d")
            except:
                print("The end date is invalid, please re-renter in proper format.")
            else:
                if endDate <= startDate:
                    print("End date must be later than start date, please re-enter: ")
                elif (endDate - startDate).days > 7:
                    print("Trip cannot be longer than 7 days")
                else:
                    break
        tripLength = (endDate - startDate).days
        print("The employee's trip was", tripLength, "days long.")

        carUse = input("Did employee use their own car or a rental ('O' for own, 'R' for rental): ").upper()

        if carUse == "O":
            while True:
                try:
                    mileage = int(input("Enter kilometers travelled on trip (cannot exceed 2000): "))
                except:
                    print("The kilometers entered is not valid, please re-enter.")
                else:
                    if mileage > 2000:
                        print("Employee's trip cannot exceed 2000km, please re-enter.")
                    else:
                        break

        claimType = input("Is claim type standard or executive ('S' for standard, 'E' for executive): ").upper()

        # calculations for the per diem, mileage, and bonus for the  employee's claim amount
        # per diem
        perDiem = tripLength * DAY_RATE

        # mileage pay
        if carUse == "O":
            milePay = mileage * MILE_RATE
        else:
            rentalPay = tripLength * RENT_RATE

        # bonus pay

        bonus = 0
        if tripLength > 3:
            bonus += DAY_BONUS
        if carUse == "O" and mileage > 1000:
            bonus += (mileage * MILE_BONUS)
        if claimType == "E":
            bonus += (tripLength * EXEC_BONUS)

        bonusDate = str(startDate.month) + "-" + str(startDate.day)
        bonusDate = datetime.datetime.strptime(bonusDate, "%m-%d")
        bonusStartDate = "12-15"
        bonusStartDate = datetime.datetime.strptime(bonusStartDate, "%m-%d")
        bonusEndDate = "12-22"
        bonusEndDate = datetime.datetime.strptime(bonusEndDate, "%m-%d")

        if bonusStartDate <= bonusDate <= bonusEndDate:
            bonus += (tripLength * DATE_BONUS)

        # total claim amount
        if carUse == "O":
            claimAmount = perDiem + milePay + bonus
        else:
            claimAmount = perDiem + rentalPay + bonus
        claimHST = HST * claimAmount
        claimTotal = claimAmount + claimHST

        # outputs to show employee's information and claim
        print("*" * 40)
        print("Employee number:", employeeNum)
        print("Employee first name:", firstName)
        print("Employee last name:", lastName)
        print("Trip location:", location)
        print("Start date of trip:", startDate.date())
        print("End date of trip:", endDate.date())
        print("Length of trip in days:", tripLength)
        if carUse == "O":
            print("Employee car use: Own vehicle")
        else:
            print("Employee car use: Rented vehicle")
        if carUse == "O":
            print("Distance traveled during trip:", mileage, "km")
        if claimType == "S":
            print("Employee claim type: Standard")
        else:
            print("Employee claim type: Executive")
        print("*" * 40)
        print()

        perDiemDsp = "${:,.2f}".format(perDiem)
        print(f"Per diem:           {perDiemDsp:>9s}")

        if carUse == "O":
            milePayDsp = "${:,.2f}".format(milePay)
            print(f"Mileage pay:        {milePayDsp:>9s}")
        else:
            rentalPayDsp = "${:,.2f}".format(rentalPay)
            print(f"Rental pay:         {rentalPayDsp:>9s}")

        bonusDsp = "${:,.2f}".format(bonus)
        print(f"Bonus pay:          {bonusDsp:>9s}")

        claimAmountDsp = "${:,.2f}".format(claimAmount)
        print(f"Claim amount:       {claimAmountDsp:>9s}")

        claimHSTDsp = "${:,.2f}".format(claimHST)
        print(f"Claim HST:          {claimHSTDsp:>9s}")

        print(" " * 20 + "-" * 9)

        claimTotalDsp = "${:,.2f}".format(claimTotal)
        print(f"Total claim amount: {claimTotalDsp:>9s}")

        print("*" * 40)

        exitPro = input("Do you wish to continue with another claim (Y/N): ").upper()
        if exitPro == "N":
            break



# Comment like a pro.
# Author: Cameron Penney
# Date Written: Feb 22nd, 2023
# How to run a Function in a process.

from time import sleep
from multiprocessing import Process

# a custom function that blocks for a moment
def task(sleep_time, message):
# block for a moment
    sleep(sleep_time)
# display a message
    print(message)
    print("Waiting for the process...")
    input("Press any key to continue... ")

# entry point
    if __name__ == '__main__':
        # create a process
        process = Process(target=task, args=(1.5,))
        # run the process
        process.start()
        # wait for the process to finish
        print('Waiting for the process...')
        process.join()


# Start of the main program.
while True:
    print()
    print("NL Chocolate Company")
    print("Travel Claims Processing System")
    print()
    print(f'Times Menu Has Been Ran This Session:{MenuUse} ')
    print()
    print("1. Enter an Employee Travel Claim..")
    print("2. Fun Interview Question.")
    print("3. Cool Stuff with Strings and Dates.")
    print("4. Something Old, Something New")
    print("5. Quit")
    print()
    Choice = (input("Enter choice (1-5): "))
    MenuUse += 1
# if statements for each choice including number validation at bottom

    if Choice == "1":
         Claim()
    elif Choice == "2":
         fizz()
    elif Choice == "3":
         StringFun()
    elif Choice == "4":
         task(3, "Message displayed from another process...")
    elif Choice == "5":
         exit()
    else:
         print("invalid input try again")


