number = input("Entrer un nombre entre 1 et 10: ")

while True :
    if (number.isdigit() and int(number) > 0 and int(number) < 11) :
        print(f"Le nombre {number} est valide.")
        break
    else :
        number = input("Entrer un nombre entre 1 et 10: ")