import json

data = json.load(open("data.json"))

def close_matec(i):
    if i in data:
        print(data[i])
    else:
        print(f"{i} not found in dictionary")


user_data = input("Please Enter Here = ")

if len(user_data) > 1:
    list = user_data.split(" ")
    for i in list:
        if not i:
            print("Please enter some input")
        elif i.isalpha():
            result = close_matec(i)
            print(f"==> {i} = {result}")
        else:
            print("Please enter the alphabet")