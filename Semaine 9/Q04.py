tab = []
try:
    with open("Exercice 9/config.txt", 'r') as conf:
        for ligne in conf:
            tab.append(ligne.strip())
        print(f"tab : {tab}")

    for item in tab:
        serveur, ip, statut = item.split(',')

        if statut == "ON":
            print(f"Serveur {serveur} ({ip}) est actif")

except FileNotFoundError:
    print("Erreur : Le fichier n'existe pas")