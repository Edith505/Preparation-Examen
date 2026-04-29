import argparse
from pathlib import Path

def analyser_dossier(chemin):
    dossier = Path(chemin)

    if not dossier.exists() or not dossier.is_dir():
        raise ValueError("Le chemin fourni n'est pas un dossier valide.")

    taille_totale = 0
    nombre_fichiers = 0
    plus_gros_fichier = None
    taille_max = 0

    # parcours récursif
    for element in dossier.rglob("*"):
        if element.is_file():
            taille = element.stat().st_size

            taille_totale += taille
            nombre_fichiers += 1

            if taille > taille_max:
                taille_max = taille
                plus_gros_fichier = element

    # conversion en kilo-octets
    taille_ko = taille_totale / 1024

    print(f"Taille totale : {taille_totale} octets ({taille_ko:.2f} KO)")
    print(f"Nombre total de fichiers : {nombre_fichiers}")

    if plus_gros_fichier:
        print(
            f"Plus gros fichier : {plus_gros_fichier.name} "
            f"({taille_max} octets)"
        )
    else:
        print("Aucun fichier trouvé.")


def main():
    parser = argparse.ArgumentParser(
        description="Analyse de stockage d'un dossier"
    )
    parser.add_argument(
        "chemin",
        type=str,
        help="Chemin du dossier à analyser"
    )

    args = parser.parse_args()

    analyser_dossier(args.chemin)


if __name__ == "__main__":
    main()


# ================================= Analyse du script ============================================
from pathlib import Path

"""
Question reformulée :

Écrire un script Python qui :

- Prend comme constante le chemin d’un dossier à analyser.
- Parcourt récursivement tous les fichiers et sous-dossiers de ce dossier.
- Calcule et affiche :
    le nombre total de fichiers
    la taille totale de tous les fichiers en kilo-octets (Ko)
    le plus gros fichier avec son nom et sa taille en Ko

"""

chemin = Path("C:/Users/2433177/Documents")

taille_totale = 0
nb_fichiers = 0
fichier_max = ""
taille_max = 0

for racine, dossiers, fichiers in chemin.walk():
    for nom in fichiers:
        fichier = racine / nom
        taille = fichier.stat().st_size / 1024
        
        taille_totale += taille
        nb_fichiers += 1

        if taille > taille_max:
            taille_max = taille
            fichier_max = fichier

print(f"Nombre total de fichiers : {nb_fichiers}")

print(f"Taille totale : {taille_totale:.2f} Ko")

print(f"Fichier le plus gros : {fichier_max} ({taille_max:.2f} Ko)")