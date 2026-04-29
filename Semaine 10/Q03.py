from pathlib import Path
import os

CHEMIN_ON_DRIVE = "U:/SESSION 4/420-4Q5-LI Automatisation des tâches/Semaine 10"
chemin = Path(CHEMIN_ON_DRIVE)

for racine, dossiers, fichiers in os.walk(chemin):
    for fichier in fichiers:
        chemin_fichier = Path(racine) / fichier

        if chemin_fichier.suffix == ".pdf":
            print("--------------------------------------------------------")
            print(f"Chemin absolu : {chemin_fichier.resolve()}")
            print(f"Chemin relatif : {chemin_fichier.relative_to(chemin)}")
           