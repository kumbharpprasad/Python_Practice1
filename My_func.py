# function to take the input from user, number of days and convert it into second, minute and hours.

# input_validation() > to validate the input is correct (nox text, non 0, integer value) and store it in "days" variable.
# day_to_units() > Will convert the user input days into asked units, i.e seconds, hours, minutes!

from main import *

"""def input_validation():
    if user_input.isdigit():
        days = int(user_input)
        if days == 0:
            print ("Please enter non 0 value")
        elif days > 0:
            days_to_units(days)
        else:
            print("Enter the the positive input")
    else:
        print("User Input is not digit, exiting!!!")


def days_to_units(days):
        Units = input("Please Enter the units in: minutes, hours, seconds = ")  # local variable
        if Units == "minutes":
            result = days * 24 * 60
            print(f"Total number of {Units} in {days} days is {result} \n")
        elif Units == "hours":
            result = days * 24
            print(f"Total number of {Units} in {days} days is {result} \n")
        elif Units == "seconds":
            result = days * 24 * 60 * 60
            print(f"Total number of {Units} in {days} days is {result} \n")
        else:
            print("Please enter correct unit value & try again")

########################################################################################
#individual functions to convert days into hours, minutes & seconds.

def days_to_hours(days):
    result = days * 24
    print(f"Total number of hours in {days} days are {result} \n")

def days_to_minutes(days):
        result = days * 24 * 60
        print(f"Total number of minutes in {days} days are {result} \n")

def days_to_seconds(days):
    result = days * 24*60*60
    print(f"Total number of seconds in {days} days are {result} \n")

###################################################################################################
#with try/except; try will control the program error & termination & will print the message that we want to print.
#Below it is covering all errors related to ValueError; for all errors just remove ValueError & left the field blank.

def input_validation_try():
    try:
        days = int(user_input)
        if days == 0:
            print("Please enter non 0 value")
        elif days > 0:
            days_to_units(days)
        else:
            print("Enter the the positive input")

    except ValueError:
        print("Please enter integer value!!!!")

def input_validation_try_for():
    try:
        days = int(num_of_days)
        if days == 0:
            print("Please enter non 0 value")
        elif days > 0:
            days_to_hours(days)
        else:
            print("Enter the the positive input")

    except ValueError:
        print("Please enter integer value!!!!")"""


#################Dictionary func#########################################################


def input_validation_try1():
    try:
        days = int(days_units_dict["day"])  # assigning dict key to variable
        unit1 = (days_units_dict["unit"])  # assigning dict key to variable
        if days == 0:
            print("Please enter non 0 value")
        elif days > 0:
            day_to_unit(days, unit1)
        else:
            print("Enter the the positive values for days")

    except ValueError:
        print("Please enter integer value in days field!!!!")


def input_validation_2():
    days = int(days_units_dict["day"])
    unit1 = (days_units_dict["unit"])  # assigning dict key to variable
    if days == 0:
        print("Please enter non 0 value")
    elif days > 0:
        day_to_unit(days, unit1)
    else:
        print("Enter the the positive values for days")


def day_to_unit(days, unit1):
    if unit1 == "Hours":
        result = days * 24
        print(f"Total number of hours in {days} is {result}")
    elif unit1 == "Minutes":
        result = days * 24 * 60
        print(f"Total number of minutes in {days} is {result}")

    elif unit1 == "Seconds":
        result = days * 24 * 60 * 60
        print(f"Total number of seconds in {days} is {result}")

    else:
        print("Unsupported unit entered")

#################func#########################################################
