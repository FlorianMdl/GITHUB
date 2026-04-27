"""
Juste prix (Mode difficile)
"""

import random

variable_secrete = random.randint(1, 20)
nombre_essais_max = 7
gagne = False 

print("\n-- Jeu du juste prix (Difficile) --")
print(f"Devine le nombre entre 1 et 20 en {nombre_essais_max} essais.\n")

for i in range(nombre_essais_max):
    try:
        choix_utilisateur = int(input(f"Essai n°{i+1} - Votre choix : "))
    except ValueError:
        print("Erreur ! Tu dois taper un nombre entier.")
        continue 

    if choix_utilisateur < variable_secrete: 
        print("C'est plus !")
    elif choix_utilisateur > variable_secrete:
        print("C'est moins !")
    else:
        print(f"Bravo, vous avez gagné en {i+1} coups !")
        gagne = True
        break

if not gagne:
    print(f"\nDommage ! Le nombre secret était {variable_secrete}.")

        