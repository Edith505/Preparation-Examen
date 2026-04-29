nombre = input("Entrez des nombres séparés par des espaces : ")

tab = []
for x in nombre.split():
    tab.append(int(x))

somme = 0
max = tab[0]
min = tab[0]

for n in tab:
    somme += n

    if n > max:
        max = n
    if n < min:
        min = n

moyenne = somme / len(tab)

print(f"Somme : {somme}")
print(f"Moyenne : {moyenne}")
print(f"Maximum : {max}")
print(f"Minimum : {min}")