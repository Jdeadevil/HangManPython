import random
import time
import numpy as np

print("Hi! Welcome to my little Hangman game, made for the demonstration of my Python skills!", end="")
print(" I hope you'll enjoy your time here.")
print("")
forename = input("Firstly, what's your name? ")
print("")
if forename:
    print(f"Hello {forename}! Let's begin with choosing a difficulty....")
else:
    print("Invalid, for some reason.")

def game():
    difficulty = input(
        '''
Super Easy (2-3 letter words"
Easy (4-5 letter words)
Normal (6-7 letter words)
Hard (8-9 letter words)
Super Hard (10-11 letter words)
    
''').lower()

    file = np.genfromtxt("hangman-words.txt", dtype=str)
    file_filter = []

    if difficulty == "super easy":
        difficulty = 3
    elif difficulty == "easy":
        difficulty = 5
    elif difficulty == "normal":
        difficulty = 7
    elif difficulty == "hard":
        difficulty = 9
    elif difficulty == "super hard":
        difficulty = 11
    else:
        print("Invalid! Let's try that again.")
        game()

    for i in range(len(file)):
        if len(file[i]) < difficulty:
            file_filter.append(file[i])

    guess = ""
    wrong_guesses = []
    target_word = random.choice(file_filter)
    length = len(target_word)
    guesses = 10
    correct_guesses = 0
    name_display = []
    for i in range(length):
        name_display.append("_")

    while name_display.count("_") > 0:
        if guesses == 0:
            print(f"You lose! The answer was {target_word}")
            repeat = input("Play again? (Y/N) ").lower()
            if repeat == "y":
                game()
            else:
                print("No worries, see you later.")
                break
        else:
            print(f"I'm thinking of a {length} letter word.")
            print(name_display)
            print(f"Guesses: {guesses}")
            print(f"Incorrect Guesses: {wrong_guesses}")
            guess = input("Letter: ").upper()
            print("")
            if guess in wrong_guesses:
                print(f"You've already guessed {guess.upper()}!")
            elif guess in target_word:
                correct_guesses += 1
                location = target_word.find(guess)
                name_display[location] = guess
            else:
                wrong_guesses.append(guess)
                guesses -= 1
    else:
        print("You did it! Well done. Now please hire me. :)")
        repeat = input("Play again? (Y/N) ").lower()
        if repeat == "y":
            game()
        else:
            print("No worries, see you later.")

game()