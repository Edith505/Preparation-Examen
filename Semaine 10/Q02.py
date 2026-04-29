import time
from pathlib import Path

def suivre_fichier(fichier):
    chemin = Path(fichier)
    try:
        with chemin.open('r') as f:

            f.seek(0, 2)

            while True:
                ligne = f.readline()
                
                if not ligne:
                    time.sleep(0.5) 
                    continue
                
                print(ligne, end="")
    except FileNotFoundError:
        print("fichier introuvable")
    
    except PermissionError:
        print("permission refusée")
    
    except Exception as e:
        print(f"erreur : {e}")
    
  
