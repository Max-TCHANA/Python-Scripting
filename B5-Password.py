"""
This short program shows how to manage password.
Verify the password provided by the user
Give access when the password provides is correct
"""
import hashlib
import os
from getpass import getpass

chaine_mot_de_passe = b"azerty" #to convert the text into bytes
mot_de_passe_chiffre = hashlib.sha1(chaine_mot_de_passe).hexdigest()

verrouille = True
while verrouille:
    entre = getpass("Tapez le mot de passe : ") # azerty
    # On encode la saisie pour avoir un type bytes
    entre = entre.encode()
    
    entre_chiffre = hashlib.sha1(entre).hexdigest()
    if entre_chiffre == mot_de_passe_chiffre:
        verrouille = False
    else:
        print("Mot de passe incorrect")

print("Mot de passe accepté...")

os.system("pause")
