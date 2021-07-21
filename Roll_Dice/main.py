import random

min=1
max=6
#count="0"


def roll():
    count = 0
    while count < 3:
        print("Rolling Dice .....!!")
        print(random.randint(min, max))
        print(random.randint(min, max))
        count = count+1

print(roll())
