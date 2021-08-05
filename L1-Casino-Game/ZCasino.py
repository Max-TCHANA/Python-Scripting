# This file houses the code for ZCasino, a suitable roulette game

import os
from random import randrange
from math import ceil

# Declaration of the starting variables
argent = 1000 # We have $ 1000 at the start of the game
continuer_partie = True # Boolean which is true as long as we have to
                        # continue the game

print("You sit at the roulette table with", argent, "$.")

while continuer_partie: # As long as we have to continue the game
    # the user is asked to enter the number on
    # which one he will bet
    nombre_mise = -1
    while nombre_mise < 0 or nombre_mise > 49:
        nombre_mise = input("Type the number you want to bet on (between 0 and 49): ")
        # We convert the number bet
        try:
            nombre_mise = int(nombre_mise)
        except ValueError:
            print("You did not enter a number")
            nombre_mise = -1
            continue
        if nombre_mise < 0:
            print("This number is negative")
        if nombre_mise > 49:
            print("This number is greater than 49")

    # Now we select the amount to bet on the number
    mise = 0
    while mise <= 0 or mise > argent:
        mise = input("Enter the amount of your bet: ")
        # On convertit la mise
        try:
            mise = int(mise)
        except ValueError:
            print("Vous n'avez pas saisi de nombre")
            mise = -1
            continue
        if mise <= 0:
            print("The bet entered is negative or zero.")
        if mise > argent:
            print("You cannot bet that much, you only have", argent, "$")

    # The bet number and the stake have been selected by
    # the user, we spin the wheel
    numero_gagnant = randrange(50)
    print("The roulette wheel spins ... ... and stops on the number", numero_gagnant)

    # We establish the player's gain
    if numero_gagnant == nombre_mise:
        print("Congratulation ! You obtain", mise * 3, "$ !")
        argent += mise * 3
    elif numero_gagnant % 2 == nombre_mise % 2: # they are the same color
        mise = ceil(mise * 0.5)
        print("You bet on the right color. You obtain", mise, "$")
        argent += mise
    else:
        print("Sorry friend, it's not for this time. You lose your stake.")
        argent -= mise

    # The game is interrupted if the player is ruined
    if argent <= 0:
        print("You are ruined! It's the end of the game.")
        continuer_partie = False
    else:
        # We display the player's money
        print("You now have", argent, "$")
        quitter = input("Would you like to leave the casino (y / n)? ")
        if quitter == "y" or quitter == "Y":
            print("You leave the casino with your winnings.")
            continuer_partie = False

# We pause the system (Windows)
os.system("pause")