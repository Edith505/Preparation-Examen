import os

def nettoyer_fichiers_log(dossier_cible):
    print("Analyse du dossier : " + dossier_cible)
    
    # Mauvaise pratique :
    # Aucun contrôle si le dossier existe → risque d'exception (FileNotFoundError)
    elements = os.listdir(dossier_cible)
    
    for element in elements:
        chemin_absolu = os.path.join(dossier_cible, element)
        
        # Erreur possible avec le nom des dossiers :
        # On teste seulement le nom (.log) sans vérifier si c'est un fichier.
        # Si un dossier se termine par ".log", os.remove va provoquer une erreur.
        if element.endswith(".log"):
            os.remove(chemin_absolu)
            print("Fichier supprimé : " + chemin_absolu)


if __name__ == "__main__":
    nettoyer_fichiers_log("./serveur_logs")


# ==================================== Correction proposée ====================================

def nettoyer_fichiers_log_corrige(dossier_cible):
    if not os.path.exists(dossier_cible):
        raise FileNotFoundError("Le dossier n'existe pas.")

    print("Analyse du dossier : " + dossier_cible)
    
    for element in os.listdir(dossier_cible):
        chemin_absolu = os.path.join(dossier_cible, element)
        
        # Vérifier que c'est bien un fichier
        if os.path.isfile(chemin_absolu) and element.endswith(".log"):
            os.remove(chemin_absolu)
            print("Fichier supprimé : " + chemin_absolu)