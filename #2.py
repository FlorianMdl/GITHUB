"""
Jeu du juste prix 
"""

variable_secrete = 13
choix_utilisateur = 0

print("Jeu du juste prix -- Tu dois deviner le nombre secret (entre 1 et 20)\n")

while choix_utilisateur != variable_secrete: 
    choix_utilisateur = int(input("Votre choix: "))
    if choix_utilisateur < variable_secrete: 
        print("C'est plus !")
    elif choix_utilisateur > variable_secrete:
        print("C'est moins !")

print("Bravo, vous avez gagné !")

        