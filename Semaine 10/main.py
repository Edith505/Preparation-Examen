#============================== Exercice 1 — Recherche de motif ==============================
def trouver_motif(chemin_fichier, motif):
    try:
        with open(chemin_fichier, "r", encoding="utf-8") as f:
            for index_ligne, ligne in enumerate(f):
                index_colonne = ligne.find(motif)
                if index_colonne != -1:
                    return (index_ligne, index_colonne)
    except FileNotFoundError:
        print(f"Erreur : fichier '{chemin_fichier}' introuvable.")
    except PermissionError:
        print(f"Erreur : accès refusé au fichier '{chemin_fichier}'.")
    return None

# Test
resultat = trouver_motif("mon_fichier.txt", "bonjour")
if resultat:
    print(f"Motif trouvé à la ligne {resultat[0]}, colonne {resultat[1]}")
else:
    print("Motif non trouvé.")


#============================== Exercice 2 — Journal en attente ============================== 
import time

def surveiller_fichier(chemin_fichier):
    print(f"Surveillance de : {chemin_fichier} (Ctrl+C pour arrêter)")
    with open(chemin_fichier, "r", encoding="utf-8") as f:
        f.seek(0, 2)  # Se place à la fin du fichier
        while True:
            ligne = f.readline()
            if ligne:
                print(ligne, end="")
            else:
                time.sleep(0.5)  # Attendre avant de réessayer
# Utilisation
surveiller_fichier("mon_log.txt")
# Sur Linux : surveiller_fichier("/var/log/syslog")

# ============================== Exercice 3 — Lister les fichiers PDF ==============================
from pathlib import Path

# Choisir le dossier de départ (dossier personnel de l'utilisateur)
dossier = Path.home()

print(f"Recherche de fichiers PDF dans : {dossier}\n")

for fichier in dossier.rglob("*.pdf"):
    print(f"Chemin absolu  : {fichier}")
    print(f"Chemin relatif : {fichier.relative_to(dossier)}")
    print()

# ============================== Exercice 4 — Analyse de code ==============================
# Clé API lue depuis une variable d'environnement (plus codée en dur)
# reponse.save_to_disk() remplacée par open() + write() (méthode qui existe vraiment)
import requests
import os

def telecharger_donnees():
    # CORRECTION 1 : ne jamais écrire la clé directement dans le code.
    # Elle doit être définie dans l'environnement :
    #   Windows : set API_KEY=ma-vraie-cle
    #   Linux   : export API_KEY=ma-vraie-cle
    cle_api = os.environ.get("API_KEY")

    if not cle_api:
        print("Erreur : la variable d'environnement API_KEY n'est pas définie.")
        return

    url = "https://api.systeme.interne/v1/export"
    en_tetes = {"Authorization": "Bearer " + cle_api}

    reponse = requests.get(url, headers=en_tetes)

    # CORRECTION 2 : save_to_disk() n'existe pas dans requests.
    # On écrit le contenu de la réponse dans un fichier normalement.
    with open("/var/backups/export.json", "w", encoding="utf-8") as f:
        f.write(reponse.text)

    print("Exportation terminée.")

if __name__ == "__main__":
    telecharger_donnees()
    

# ============================== Exercice 5 — Gestion de stockage ==============================
import argparse
from pathlib import Path

# Récupérer le chemin en argument
parser = argparse.ArgumentParser()
parser.add_argument("dossier", help="Dossier à analyser")
args = parser.parse_args()

dossier = Path(args.dossier)

taille_totale = 0
nb_fichiers = 0
plus_gros_fichier = None
taille_max = 0

for fichier in dossier.rglob("*"):
    if fichier.is_file():
        taille = fichier.stat().st_size
        taille_totale += taille
        nb_fichiers += 1
        if taille > taille_max:
            taille_max = taille
            plus_gros_fichier = fichier

print(f"Nombre de fichiers : {nb_fichiers}")
print(f"Taille totale      : {taille_totale / 1024:.2f} Ko")
if plus_gros_fichier:
    print(f"Plus gros fichier  : {plus_gros_fichier.name} ({taille_max / 1024:.2f} Ko)")


#============================== Exercice 6 — Gestion d'exceptions (division) ==============================
while True:
    try:
        a = float(input("Entrez le premier nombre  : "))
        b = float(input("Entrez le deuxième nombre : "))
        resultat = a / b
        print(f"Résultat : {a} / {b} = {resultat}")
        break  # Tout s'est bien passé, on sort de la boucle
    except ValueError:
        print("Erreur : veuillez entrer des nombres valides.\n")
    except ZeroDivisionError:
        print("Erreur : impossible de diviser par zéro.\n")


#============================== Exercice 7 — Analyse de code : nettoyage de logs =============================


#============================== Exercice 8 — Quelle heure est-il ? ==============================
from datetime import datetime

while True:
    try:
        saisie = input("Entrez une date future (AAAA-MM-JJ HH:MM) : ")
        date_future = datetime.strptime(saisie, "%Y-%m-%d %H:%M")
        break  # Format valide, on sort de la boucle
    except ValueError:
        print("Format invalide. Exemple : 2025-12-31 23:59\n")

maintenant = datetime.now()
difference = date_future - maintenant

if difference.total_seconds() <= 0:
    print("Ce moment est déjà passé !")
else:
    total_secondes = int(difference.total_seconds())
    jours    = total_secondes // 86400
    reste    = total_secondes % 86400
    heures   = reste // 3600
    reste    = reste % 3600
    minutes  = reste // 60
    secondes = reste % 60

    print(f"Temps restant : {jours}j {heures}h {minutes}min {secondes}s")

#============================== Exercice 9 — Sauvegarde avec shutil ==============================
import shutil

source = "projets"
copie  = "sauvegarde_projets"

# Étape 1 : copier le dossier
shutil.copytree(source, copie)
print(f"Dossier copié : {copie}")

# Étape 2 : compresser en .zip
shutil.make_archive(copie, "zip", copie)
print(f"Archive créée : {copie}.zip")

# Étape 3 : supprimer la copie
shutil.rmtree(copie)
print(f"Dossier temporaire supprimé : {copie}")

#============================== Exercice 10 — Refactorisation orientée objet ==============================
import shutil


class GestionnaireStockage:
    """Gère la sauvegarde et la compression d'un dossier."""

    def __init__(self, source: str, destination: str) -> None:
        """
        Initialise le gestionnaire avec les chemins source et destination.

        Args:
            source: Chemin du dossier à sauvegarder.
            destination: Nom du dossier de sauvegarde (sans extension).
        """
        self.source = source
        self.destination = destination

    def copier(self) -> None:
        """Copie récursivement le dossier source vers la destination."""
        shutil.copytree(self.source, self.destination)
        print(f"Dossier copié : {self.destination}")

    def compresser(self) -> None:
        """Compresse le dossier destination en archive .zip."""
        shutil.make_archive(self.destination, "zip", self.destination)
        print(f"Archive créée : {self.destination}.zip")

    def nettoyer(self) -> None:
        """Supprime le dossier de copie temporaire."""
        shutil.rmtree(self.destination)
        print(f"Dossier temporaire supprimé : {self.destination}")

    def sauvegarder(self) -> None:
        """Exécute les trois étapes dans l'ordre : copie, compression, nettoyage."""
        self.copier()
        self.compresser()
        self.nettoyer()


# Utilisation
gestionnaire = GestionnaireStockage("projets", "sauvegarde_projets")
gestionnaire.sauvegarder()

#============================== Exercice 11 — Subprocess : config IP ==============================
import subprocess
import platform
import re

systeme = platform.system()

if systeme == "Windows":
    resultat = subprocess.run(["ipconfig"], capture_output=True, text=True, encoding="cp850")
    sortie = resultat.stdout

    adresse_ip = None
    masque = None

    for ligne in sortie.splitlines():
        if "Adresse IPv4" in ligne:
            adresse_ip = ligne.split(":")[-1].strip()
        if "Masque de sous-réseau" in ligne:
            masque = ligne.split(":")[-1].strip()

else:  # Linux / Mac
    resultat = subprocess.run(["ifconfig"], capture_output=True, text=True)
    sortie = resultat.stdout

    adresse_ip = None
    masque = None

    for ligne in sortie.splitlines():
        if "inet " in ligne and "127.0.0.1" not in ligne:
            parties = ligne.split()
            adresse_ip = parties[1]
            # Le masque est en notation CIDR ou après "netmask"
            if "netmask" in parties:
                masque = parties[parties.index("netmask") + 1]
            break

if adresse_ip and masque:
    print(f"IP : {adresse_ip} / {masque}")
else:
    print("Impossible de trouver l'adresse IP.")

## Exercice 12 — Surveillance système avec psutil
# Documentation officielle vérifiée :
# https://psutil.readthedocs.io/en/latest/#psutil.cpu_percent
# https://psutil.readthedocs.io/en/latest/#psutil.virtual_memory

# Installation : pip install psutil

import psutil
import time

print("Surveillance CPU et RAM (Ctrl+C pour arrêter)\n")

while True:
    cpu = psutil.cpu_percent(interval=1)   # % CPU sur 1 seconde
    ram = psutil.virtual_memory().percent  # % RAM utilisée

    print(f"CPU : {cpu:5.1f}%   RAM : {ram:5.1f}%", end="\r")
    time.sleep(1)


# ============================== Exercice 13 — La classe Machine (CSV) ==============================
import csv


class Machine:
    def __init__(self, id: int, nom: str, adresse_ip: str) -> None:
        self.id = id
        self.nom = nom
        self.adresse_ip = adresse_ip

    def __repr__(self) -> str:
        return f"Machine(id={self.id}, nom={self.nom}, ip={self.adresse_ip})"


# Lire le fichier CSV et créer les objets
machines = []

with open("machines.csv", newline="", encoding="utf-8") as f:
    lecteur = csv.DictReader(f)
    for ligne in lecteur:
        machine = Machine(
            id=int(ligne["ID"]),
            nom=ligne["Nom"],
            adresse_ip=ligne["Adresse_IP"]
        )
        machines.append(machine)

# Afficher toutes les machines
print("Machines chargées :")
for m in machines:
    print(m)

# Recherche par adresse IP
def trouver_par_ip(liste: list, ip: str):
    for machine in liste:
        if machine.adresse_ip == ip:
            return machine
    return None

ip_recherchee = "192.168.1.20"
resultat = trouver_par_ip(machines, ip_recherchee)

if resultat:
    print(f"\nMachine trouvée pour {ip_recherchee} : {resultat}")
else:
    print(f"\nAucune machine avec l'IP {ip_recherchee}")

