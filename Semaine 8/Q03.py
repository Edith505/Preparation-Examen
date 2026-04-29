# ce script permet de recopier une chaine en l'inversant
# on declare la chaine
mots = "eddy"

#declarer la variable final
resultat = ""

# itiration avec for pour chaque lettre
for lettre in mots:
    #ajouter les lettres en ajoutants dans resulats
    resultat = lettre + resultat
print(resultat)

#Genere par AI 
resultat = mots[::-1]
print(resultat)



