lettres = input("Entrer un texte: ")
compteur = 0

for lettre in lettres :
    if lettre in "aeiouAEIOU" :
        compteur += 1

print(f"Le texte contient {compteur} voyelles.")