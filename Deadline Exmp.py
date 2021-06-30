import datetime


# Program to find out the time left deadline from todays date.





user_input = input("Please enter the goal & deadline in DD.MM.YYYY format, seperated by ':' =  ")
list_input = user_input.split(":")
goal = list_input[0]
deadline = list_input[1]
d_date = datetime.datetime.strptime(deadline, "%d.%m.%Y")
t_date = datetime.datetime.today()
t_deadline = d_date - t_date
print(f"{t_deadline} days are left to complete the {goal}")

