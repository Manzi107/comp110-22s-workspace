"""Ex02 - One-Shot Wordle - Another amateur & cute step towards worldle"""

_author_ = "730489734"

#The most crucial part of the program aka seting up variables

secret_word: str = "python"
user_winput: str = input(f"What is your {len(secret_word)}-letter guess?")
i: int = 0

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

boxes: str = ""

#The Following line is setting up an important and a reoccuring message

while len(user_winput) != len(secret_word):
    user_winput = input (f"That was not {len(secret_word)} letters! Try again: ")

#About to kickstart the while loop as the basis of what the user will see after their input

while i < len(secret_word):
    if user_winput[i] == secret_word[i]:
        boxes += GREEN_BOX
        i += 1
    else:
        found_anywhere: bool = False
        alternate_i: int = 0
        while alternate_i < len(secret_word):
            if user_winput[i] == secret_word[alternate_i]:
                found_anywhere = True 
                alternate_i = len(secret_word)
            else:
                alternate_i += 1
        if found_anywhere:
                boxes += YELLOW_BOX
        else:
            boxes += WHITE_BOX
        i += 1
print (boxes)

#Next lines dictate what the user sees when they make a correct or wrong guess

if len (user_winput) == len(secret_word) :
    if user_winput == secret_word:
        print ("Woo! You got it!")
    else:
        print ("Not quite. Play again soon!")