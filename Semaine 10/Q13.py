import csv
from typing import List, Optional


class Machine:
    """
    Représente une machine avec un identifiant, un nom et une adresse IP.
    """

    def __init__(self, id: int, nom: str, adresse_ip: str) -> None:
        self.id: int = id
        self.nom: str = nom
        self.adresse_ip: str = adresse_ip

    def __str__(self) -> str:
        return f"Machine(id={self.id}, nom='{self.nom}', adresse_ip='{self.adresse_ip}')"


def lire_machines(fichier: str) -> List[Machine]:
    """
    Lit un fichier CSV et retourne une liste d'objets Machine.
    """
    machines: List[Machine] = []

    with open(fichier, newline="", encoding="utf-8") as f:
        lecteur = csv.DictReader(f)

        for ligne in lecteur:
            machine = Machine(
                id=int(ligne["ID"]),
                nom=ligne["Nom"],
                adresse_ip=ligne["Adresse_IP"]
            )
            machines.append(machine)

    return machines


def rechercher_par_ip(machines: List[Machine], ip: str) -> Optional[Machine]:
    """
    Recherche une machine par son adresse IP.
    """
    for machine in machines:
        if machine.adresse_ip == ip:
            return machine
    return None


def main():
    machines = lire_machines("machines.csv")

    ip_recherchee = input("Entrez une adresse IP à rechercher : ")

    resultat = rechercher_par_ip(machines, ip_recherchee)

    if resultat:
        print("Machine trouvée :", resultat)
    else:
        print("Aucune machine trouvée.")


if __name__ == "__main__":
    main()