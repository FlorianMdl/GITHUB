'''
Recuperation des informations de bases sur l'utilisateur.
'''


nom = str(input("Nom: "))
prenom = str(input("Prénom: "))
age = int(input("Age: "))
sexe = str(input("Sexe: "))

print(f"Enchanté {nom} {prenom}. Tu as {age} ans et tu es un {sexe}.")

if age >= 18:
    print("Tu es majeur. Accès autorisé.")
elif 13 < age < 18:
    print("Tu es ado. Accès restreint.")
else: 
    print("Tu es trop jeune. Accès refusé.")
