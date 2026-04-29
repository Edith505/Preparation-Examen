resultat = 0
for i in range(1, 101):
    if i % 2 == 0:
        resultat += i
print(resultat)

# Genere par AI 
resultat = sum(i for i in range(1, 101) if i % 2 == 0) ; print(resultat)