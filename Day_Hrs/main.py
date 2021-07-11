from My_func import *



# print("Total number of minutes in 171 days = ", 171 * 24 * 60) > Formula*

"""time1 = 171 * 24 * 60
print("Total number of minutes in 171 days = ", time1, '\n')"""

# programs
# while loop, infinite loop.
# """ > to comment out the code.
"""while True:     
    user_input = input("Enter the days = ")
    input_validation_try()"""

# while loop, program will exit after entering the word "exit".
# need to define user_input variable with empty value because for 1st time exec of while loop there is not user_input define.

"""user_input = " "
while user_input != "exit":
    user_input = input("Enter the days = ")
    input_validation_try()"""

# For loop with List example.

# convert user_input list value to individual variable value by .split().
# Change input_validation function and use "num_of_days" value.
# also to automate the conversion, introduce 3 new functions


"""user_input = " "
while user_input != "exit":
    user_input = input("Enter the days = ")
    print(type(user_input.split()))  # to check the type of input
    for num_of_days in user_input.split():
        input_validation_try_for()"""

# For SET example
# SET is same as list but it DOES not allow duplicate values. i.e. if number 10 enter twice or more time, program will execute it once.

"""user_input = " "
while user_input != "exit":
    user_input = input("Enter the days = ")
    print(user_input.split())  # to check the list
    print(set(user_input.split()))   # to check the Set
    for num_of_days in set(user_input.split()):
        input_validation_try_for()"""

#######################


##############################################


# Dictionary : take the days and unit from user
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
        print(f"Total number of hours in {days} days are {result}")
    elif unit1 == "Minutes":
        result = days * 24 * 60
        print(f"Total number of minutes in {days} days are {result}")

    elif unit1 == "Seconds":
        result = days * 24 * 60 * 60
        print(f"Total number of seconds in {days} days are {result}")

    else:
        print("Unsupported unit entered")


#user_input = " "

user_input = "10:Seconds"
days_units = user_input.split(":")
days_units_dict = {"day": days_units[0], "unit": days_units[1]}
input_validation_2()


