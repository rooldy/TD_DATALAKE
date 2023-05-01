import os

# Chemin du répertoire contenant les scripts à exécuter
scripts_path = "C:\TD_DATALAKE\TD_DATALAKE\DVLP"

# Dictionnaire des choix possibles
choix_possibles = {
    "1": ("2_LANDING_ZONE", "TESTScript.py"),
    "2": ("2_CURATED_ZONE\EMP", "ScriptEmp.py"),
    "3": ("2_CURATED_ZONE\AVIS", "ScriptAvis.py"),
    "4": ("2_CURATED_ZONE\LOCALISATION", "ScriptLocalisation.py"),
    "5": ("2_CURATED_ZONE\SOC", "ScriptSoc.py"),
}

# Boucle principale
while True:
    # Afficher les choix possibles
    print("Choisissez un emplacement de destination pour les données :")
    for choix, info in choix_possibles.items():
        print(f"{choix}. {info[0]}")

    print("0. Quitter")

    # Demander le choix de l'utilisateur
    choix = input("Entrez le numéro de votre choix : ")
    if choix == "0":
        print("Fin du programme.")
        break

    # Vérifier si le choix est valide
    if choix in choix_possibles:
        dossier_destination, script_a_executer = choix_possibles[choix]
        # Exécuter le script correspondant au choix de l'utilisateur
        os.system(f"python {scripts_path}/{script_a_executer} {dossier_destination}")
    else:
        print("Choix invalide.")
