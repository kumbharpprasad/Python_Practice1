turns=10
failed=0
guesses=[]
word="secrete"
done=False

while not done:
    for letter in word:
        if letter in guesses:
            print(letter, end=" ")
        else:
            print("-", end=" ")

    guess=input(f"You have {turns} left, Enter the next guess: ")
    guesses.append(guess)

    if guess not in word:
        turns -= 1
        if turns == 0:
            break

    done = True
    for letter in word:
        if letter not in guesses:
            done= False

if done:
    print(f"You have found the word!, it was {word}")
else:
    print(f"Sorry Game Over!!, The word was {word}")






