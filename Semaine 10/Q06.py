while True:
    try:
        a = float(input("Entrez le premier nombre : "))
        b = float(input("Entrez le second nombre : "))

        resultat = a / b

    except ValueError:
        print("Erreur : veuillez entrer des nombres valides.")
        continue

    except ZeroDivisionError:
        print("Erreur : division par zéro impossible.")
        continue

    else:
        print(f"Résultat : {resultat}")
        break
    