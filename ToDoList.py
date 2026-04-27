"""
Programme To-Do List
"""

ma_liste = []

while True:
    print("\n--- GESTIONNAIRE DE TÂCHES ---")
    print("1. Ajouter une tâche.")
    print("2. Afficher les tâches.")
    print("3. Supprimer une tâche.")
    print("4. Quitter.\n")

    choix = int(input("Choix (1 - 4): "))

    if choix == 1:
        add_tache = str(input("Tâche à ajouter: "))
        ma_liste.append(add_tache)
        print("Tâche ajoutée !")

    elif choix == 2:
        print("Liste de tes tâches: ")
        for clé, valeur in enumerate(ma_liste):
            print(f"{clé}. {valeur}")

    elif choix == 3: 
        remove_tache = str(input("Tâche à supprimer: "))
        ma_liste.remove(remove_tache)
        print("Tâche supprimée !")    

    elif choix == 4:
        break

