def afficher_menu():
    print("\n--- GESTIONNAIRE DE TÂCHES ---")
    print("0. Vider la liste.")
    print("1. Ajouter une tâche.")
    print("2. Afficher les tâches.")
    print("3. Supprimer une tâche.")
    print("4. Quitter.\n")

def choix_utilisateur():
    try:
        return int(input("Choix (1 - 4): "))
    except ValueError:
        return 0

def ajouter_tache(liste):
    add_tache = str(input("Tâche à ajouter: "))
    liste.append(add_tache)
    print("Tâche ajoutée !")

def afficher_tache(liste):
    print("Liste de tes tâches: ")
    for clé, valeur in enumerate(liste):
        print(f"{clé}. {valeur}")

def supprimer_tache(liste):
    try:
        remove_tache = str(input("Tâche à supprimer: "))
        liste.remove(remove_tache)
        print("Tâche supprimée !")
    except ValueError:
        print("Cette tâche n'est pas dans votre liste !")

def vider_liste(liste):
    if len(liste) == 0:
        print("La liste est déjà vide !")
    else:
        liste.clear()
        print("\nListe vidée !")

def charger_tache():
    try:
        with open("tache.txt", "r") as f:
            return [ligne.strip() for ligne in f.readlines()]
    except Exception:
        return []

def sauvegarder_tache(liste):
    with open("tache.txt", "w") as f:
        for tache in liste:
            f.write(tache + "\n")
    print("Liste sauvegardée !")


# --- MAIN ---
ma_liste = charger_tache()

if ma_liste:
    print("\nListe chargée : ", ma_liste)
else:
    print("\nListe vide !")

while True:

    afficher_menu()
    choix = choix_utilisateur()

    if choix == 0:
        vider_liste(ma_liste)
    elif choix == 1:
        ajouter_tache(ma_liste)
    elif choix == 2:
        afficher_tache(ma_liste)
    elif choix == 3:
        supprimer_tache(ma_liste)
    elif choix == 4:
        sauvegarder_tache(ma_liste)
        print("Bye !")
        break
    else:
        print("Choix invalide !")
