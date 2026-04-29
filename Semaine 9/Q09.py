fichier = input("Entrez le nom du fichier : ")

with open(fichier, "r") as f:
    lignes = f.readlines()

for i, ligne in enumerate(lignes, start=1):
    mots = ligne.split()
    nb_mots = len(mots)
    print(f"Ligne {i} : {nb_mots} mots")