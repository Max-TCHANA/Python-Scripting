"""This file contains the hangman game.

It relies on files:
- data.py
- functions.py """

import os
from data import *
from functions import *

# We retrieve the scores of the game
scores = recup_scores()

# We get a username
utilisateur = recup_nom_utilisateur()

# If the user does not yet have a score, we add him
if utilisateur not in scores.keys():
    scores[utilisateur] = 0 # 0 point to start

# Our variable to know when to stop the game
continuer_partie = 'o'

while continuer_partie != 'n':
    print("Player {0}: {1} point (s)".format(utilisateur, scores[utilisateur]))
    mot_a_trouver = choisir_mot()
    lettres_trouvees = []
    mot_trouve = recup_mot_masque(mot_a_trouver, lettres_trouvees)
    nb_chances = nb_coups
    while mot_a_trouver!=mot_trouve and nb_chances>0:
        print("Word to find {0} (still {1} chances)".format(mot_trouve, nb_chances))
        lettre = recup_lettre()
        if lettre in lettres_trouvees: # The letter has already been chosen
            print("You have already chosen this letter.")
        elif lettre in mot_a_trouver: # The letter is in the word to find
            lettres_trouvees.append(lettre)
            print("Well played")
        else:
            nb_chances -= 1
            print("... no, this letter is not in the word ...")
        mot_trouve = recup_mot_masque(mot_a_trouver, lettres_trouvees)

    # Have we found the word or are our chances exhausted ?
    if mot_a_trouver==mot_trouve:
        print("Congratulations ! You have found the word {0}.".format(mot_a_trouver))
    else:
        print("HANGED !!! You lost.")

    # We update the user's score
    scores[utilisateur] += nb_chances

    continuer_partie = input("Would you like to continue the game (Y / N) ?")
    continuer_partie = continuer_partie.lower()

# The game is over, we record the scores
enregistrer_scores(scores)

# On affiche les scores de l'utilisateur
print("You end the game with {0} points.".format(scores[utilisateur]))

os.system("pause")