import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def close_matec(w):
    if word in data:
        print(data[word])
    else:
        print(f"{word} not found in dictionary")


'''def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.upper() in data:
        return data[w.upper()]
    elif w.title() in data:
        return data[w.title()]
    elif len(get_close_matches(w,data.keys())) > 0:
        out = input("Did You mean %s if Yes then press Y else N: " % get_close_matches(w,data.keys())[0] )
        if out == "Y":
            return get_close_matches(w,data.keys())[0]
        elif out == "N":
            return "Match not Found Try again..."
    else:
        return "Not Found"

word = input("Enter Any word: ")
output = translate(word)
if type(output) == list:
    for iteam in output:
        print("=>",iteam)
else:
    print("=>",output)'''

close = ' '


while close != 'exit':
    user_input = input("Please Enter The Word = ")
    word = user_input.lower()
    try:
        if not word:
            print("Please enter some input")
        elif word.isalpha():
            result = close_matec(word)
            print(result)
            close = input("Enter 'exit' to close the program OR Press Enter to continue")

        else:
            print("Please enter the alphabet")
    except:
        print(f"Input {word} is not ideal input, try again. \n !!!!!Exiting Program!!!!!")