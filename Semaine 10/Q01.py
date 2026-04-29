from pathlib import Path

def trouver_motif(chemin_fichier, motif):
    resultat = None
    chemin = Path(chemin_fichier)

    try:
        with chemin.open('r') as fichier:
            for index_ligne, ligne in enumerate(fichier):

                # la méthode find() retourne l'index ou -1
                index_colonne = ligne.find(motif)

                if index_colonne != -1:
                    resultat = (index_ligne, index_colonne)
                    break

    except FileNotFoundError:
        print("fichier introuvable")
    
    except PermissionError:
        print("permission refusée")
    
    except Exception as e:
        print(f"erreur : {e}")

    return resultat