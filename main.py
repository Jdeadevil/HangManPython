import random
import time

target_word = "PYTHON"
length = len(target_word)
guesses = 10
correct_guesses = 0
name_display = []
for i in range(length):
    name_display.append("_")

print("Hi! Welcome to my little Hangman game, made for the demonstration of my Python skills!", end="")
print(" I hope you'll enjoy your time here.")
print("")
forename = input("Firstly, what's your name? ")
print("")
if forename:
    print(f"Hello {forename}! Let's begin with choosing a difficulty....")
else:
    print("Invalid, for some reason.")

difficulty = input(
    '''
Super Easy (2-3 letter words"
Easy (4-5 letter words)
Normal (5-6 letter words)
Hard (7-8 letter words)
Super Hard (9-10 letter words)

''')

while correct_guesses < length:
    print(f"I'm thinking of a {length} letter word.")
    print(name_display)
    print(f"Guesses: {guesses}")
    guess = input("Letter: ").upper()
    print("")
    if guess in target_word:
        correct_guesses += 1
        location = target_word.find(guess)
        name_display[location] = guess
    else:
        guesses -= 1
else:
    print("You did it! Well done. Now please hire me. :)")