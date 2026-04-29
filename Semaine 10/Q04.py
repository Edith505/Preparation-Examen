# ================================= Analyse du script ============================================

import requests
import os

def telecharger_donnees():
    # Faille de sécurité critique :
    # La clé API est codée en dur dans le programme, ce qui peut entraîner une fuite d'information.
    cle_api = "12345-SECRET-API-KEY-67890"
    
    url = "https://api.systeme.interne/v1/export"
    
    en_tetes = {"Authorization": "Bearer " + cle_api}
    reponse = requests.get(url, headers=en_tetes)
    
    # Méthode inventée (hallucination) :
    # L'objet Response de requests ne possède pas de méthode save_to_disk.
    reponse.save_to_disk("/var/backups/export.json")
    
    print("Exportation terminée.")


if __name__ == "__main__":
    telecharger_donnees()


# ============================== Correction proposée ==========================================

def telecharger_donnees_corrige():
    # Correction sécurité : utiliser une variable d'environnement
    cle_api = os.getenv("API_KEY")
    
    url = "https://api.systeme.interne/v1/export"
    
    en_tetes = {"Authorization": "Bearer " + cle_api}
    reponse = requests.get(url, headers=en_tetes)
    
    # Correction méthode inexistante
    with open("/var/backups/export.json", "wb") as f:
        f.write(reponse.content)
    
    print("Exportation terminée.")

