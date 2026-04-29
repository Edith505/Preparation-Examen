"""
    Mise en situation
    Un technicien veut automatiser la copie de tous les fichiers d'un dossier source vers un dossier de destination, sans avoir à le faire à la main un par un.
    Ce que le script doit faire
        - Accepter deux arguments en ligne de commande : le dossier source et le dossier destination.
        - Vérifier que le dossier source existe. Afficher un message d'erreur clair et quitter si ce n'est pas le cas.
        - Créer automatiquement le dossier destination s'il n'existe pas encore.
        - Copier tous les fichiers du dossier source vers le dossier destination (pas les sous-dossiers, seulement les fichiers directs).
        - Afficher le nom de chaque fichier copié au fur et à mesure.
        - Afficher un résumé final : nombre de fichiers copiés.
    Gestion d'erreurs à prévoir
        ✦ Le dossier source n'existe pas → message d'erreur + arrêt du script.
        ✦ Un fichier ne peut pas être copié (permissions) → afficher l'erreur et continuer avec les autres fichiers.
    Exemple d'utilisation
    python script.py documents/ sauvegarde/

    Copie en cours...
        ✔ rapport.pdf
        ✔ notes.txt
        ✔ photo.png
        ✗ secret.log → Permission refusée

    Terminé : 3 fichier(s) copié(s) sur 4.
    Indices
        → argparse pour lire les arguments en ligne de commande.
        → Path.exists() pour vérifier si un dossier existe.
        → Path.mkdir(exist_ok=True) pour créer le dossier destination.
        → Path.iterdir() pour parcourir le contenu d'un dossier.
        → fichier.is_file() pour ignorer les sous-dossiers.
        → shutil.copy2(src, dst) pour copier un fichier.
        → Entourer la copie d'un bloc try / except PermissionError.

"""

import argparse
import shutil
from pathlib import Path


# --- Arguments en ligne de commande ---
parser = argparse.ArgumentParser(description="Copie tous les fichiers d'un dossier vers un autre.")
parser.add_argument("source", help="Dossier source")
parser.add_argument("destination", help="Dossier destination")
args = parser.parse_args()

source = Path(args.source)
destination = Path(args.destination)

# --- Vérification du dossier source ---
if not source.exists():
    print(f"Erreur : le dossier source '{source}' n'existe pas.")
    exit()

# --- Création du dossier destination si nécessaire ---
destination.mkdir(parents=True, exist_ok=True)

# --- Copie des fichiers ---
print("Copie en cours...\n")

nb_copies = 0
nb_total  = 0

for fichier in source.iterdir():
    if fichier.is_file():          # On ignore les sous-dossiers
        nb_total += 1
        try:
            shutil.copy2(fichier, destination / fichier.name)
            print(f"  ✔ {fichier.name}")
            nb_copies += 1
        except PermissionError:
            print(f"  ✗ {fichier.name} → Permission refusée")


# --- Résumé ---
print(f"\nTerminé : {nb_copies} fichier(s) copié(s) sur {nb_total}.")
