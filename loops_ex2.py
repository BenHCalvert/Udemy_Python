#Game to have user guess a random color
import random

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'white', 'black']
guess = input("I'm thinking of color. Can you guess it? ").lower()
session = True

while session == True:
    if guess == colors[random.randint(0,len(colors)-1)]:
        break
    else: guess = input("Nope. Try again: ")
print("You guessed it. The color was",guess, "! ")
session = False

if (session == False):
    play_again = input("Do you want to play again? (Y/N)").lower()
    if (play_again == 'y'):
        session == True
        print("---------------------------------")
        guess = input("I'm thinking of color. Can you guess it? ").lower()
    else:
        print("See you next time. ")