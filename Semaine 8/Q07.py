nombres = input("Entrer une liste de nombres séparés par des espaces: ")
nombres_list = nombres.split(" ")

list = []

for nombre in nombres_list :
    if nombre.isdigit() :
        list.append(int(nombre))
    else :
        print(f"{nombre} sera ignoré.")

list.sort()
print(list)
