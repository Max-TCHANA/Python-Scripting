"""This file defines useful functions for the hangman program.

We use the program data contained in data.py"""

import os
import pickle
from random import choice

from data import *

# score management

def recup_scores():
    """This function retrieves the recorded scores if the file exists.
     In all cases, we return a dictionary,
     either the unpickled object,
     or an empty dictionary.

     We rely on nom_fichier_scores defined in data.py """
    
    if os.path.exists(nom_fichier_scores): # The file exists
        # We retrieve it
        fichier_scores = open(nom_fichier_scores, "rb")
        mon_depickler = pickle.Unpickler(fichier_scores)
        scores = mon_depickler.load()
        fichier_scores.close()
    else: # The file does not exist
        scores = {}
    return scores

def enregistrer_scores(scores):
    """This function is responsible for recording the scores in the file
     nom_fichier_scores. It receives the scores dictionary as a parameter
     to save"""

    fichier_scores = open(nom_fichier_scores, "wb") # we erase the old scores
    mon_pickler = pickle.Pickler(fichier_scores)
    mon_pickler.dump(scores)
    fichier_scores.close()

# Functions managing the elements entered by the user

def recup_nom_utilisateur():
    """Function responsible for retrieving the name of the user.
     The user's name must be at least 4 characters long,
     numbers and letters exclusively.

     If this name is not valid, we recursively call the function
     to get a new one """

    nom_utilisateur = input("Type your name: ")
    # We put the first letter in upper case and the others in lower case
    nom_utilisateur = nom_utilisateur.capitalize()
    if not nom_utilisateur.isalnum() or len(nom_utilisateur)<4:
        print("This name is invalid.")
        # We call the function again to have another name
        return recup_nom_utilisateur()
    else:
        return nom_utilisateur

def recup_lettre():
    """This function retrieves a letter entered by
     the user. If the retrieved string is not a letter,
     we recursively call the function until we get a letter """

    lettre = input("Type a letter: ")
    lettre = lettre.lower()
    if len(lettre)>1 or not lettre.isalpha():
        print("You did not enter a valid letter.")
        return recup_lettre()
    else:
        return lettre

# Hangman game functions

def choisir_mot():
    """This function returns the word chosen in the word list
     liste_mots.

     We use the choice function of the random module (see help). """
    
    return choice(liste_mots)

def recup_mot_masque(mot_complet, lettres_trouvees):
    """This function returns a hidden word in whole or in part, depending on:
     - the original word (type str)
     - letters already found (type list)

     We return the original word with * replacing the letters we
     has not yet found. """
    
    mot_masque = ""
    for lettre in mot_complet:
        if lettre in lettres_trouvees:
            mot_masque += lettre
        else:
            mot_masque += "*"
    return mot_masque