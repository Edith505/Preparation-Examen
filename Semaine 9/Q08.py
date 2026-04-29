import argparse

parser = argparse.ArgumentParser()

parser.add_argument("fichier", help="Chemin du fichier")

parser.add_argument("--lignes", action="store_true")
parser.add_argument("--mots", action="store_true")
parser.add_argument("--caracteres", action="store_true")

args = parser.parse_args()

with open(args.fichier, "r") as f:
    contenu = f.read()

if args.lignes:
    if contenu:
        nb_lignes = contenu.count("\n") + 1
    else:
        nb_lignes = 0
    print(f"Nombre de lignes : {nb_lignes}")

if args.mots:
    nb_mots = len(contenu.split())
    print(f"Nombre de mots : {nb_mots}")

if args.caracteres:
    nb_caracteres = len(contenu)
    print(f"Nombre de caractères : {nb_caracteres}" )

if not (args.lignes or args.mots or args.caracteres):
    print("Veuillez spécifier au moins une option : --lignes, --mots ou --caracteres")