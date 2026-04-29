# le probleme ici est que la variable x est modifiée à l'intérieur de la fonction increment, mais cette modification n'affecte pas la variable x à l'extérieur de la fonction.En
# correction proposer est de mettre un parametre dans la focntion increment pour retourner la valeur modifiée de x, et ensuite assigner cette valeur à une variable à l'extérieur de la fonction.
def increment(x):
    x = x + 1
    return x

print(increment(5))

# Le probleme ici est que si on utilise  = ,la comparaison des entiers en python utilise l'opérateur ==
# Si on utilise different de, l'opérateur de comparaison est !=
number = 10
if number % 2 != 0:
    print("Le nombre est impair")
else:
    print("Le nombre est pair")


# le probleme ici est que la boucle while ne s'arrête jamais car la condition counter < 5 est toujours vraie. 
# Pour corriger cela, il faut incrémenter la variable counter à chaque itération de la boucle.
counter = 0
while counter < 5:
    print(f"Counter: {counter}")
    counter += 1

