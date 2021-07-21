
import time
name = input("What is your name?  ")
print (f"Hello {name}, Time to play hangman!!!")
print (" ")
time.sleep(1)      #wait for 1 second
print("Start guessing......")
time.sleep(0.5)

word = "secret"    #here we set the secret
guesses =[]    #creates an variable with an empty value

# Create a while loop #check if the turns are more than zero
turns = 10
while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:       # see if the character is in the players guess
            print(char, end="")
        else:
            print("_", end="")
            failed = failed+1
        if failed == 0:
            print(" You won")
            exit(0)

        guess = input("guess a character: ")
        guesses += guess  # set the players guess to guesses

        if guess not in word:               # if the guess is not found in the secret word
            turns -= 1                      # turns counter decreases with 1 (now 9)
            print("Wrong")
            print(f"You have {turns}, more guesses")
            if turns == 0:
                print("You Lose")