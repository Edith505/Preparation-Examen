def print_hi(name = ''):
    print(f'Bonjour, {name}')

# la variable __name__ est une variable spéciale qui indique
# si le script est exécuté directement (valeur "__main__")
# ou s'il est importé comme module dans un autre script (valeur du nom du module)

if __name__ == '__main__':
    print_hi('Eddy')

# python .\Exercice` 1\Q01.py ou python ".\Exercice 1\Q01.py"