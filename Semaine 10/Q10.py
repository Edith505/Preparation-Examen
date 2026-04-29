import shutil
from pathlib import Path


class GestionnaireStockage:
    """
    Classe responsable de la gestion de la sauvegarde de dossiers.
    
    Elle permet de :
    - Copier un dossier source
    - Compresser la copie en archive ZIP
    - Supprimer la copie après compression
    """

    def __init__(self, source: str, destination: str) -> None:
        """
        Initialise le gestionnaire avec les chemins source et destination.

        Args:
            source (str): chemin du dossier à sauvegarder
            destination (str): nom du dossier de copie
        """
        self.source: Path = Path(source)
        self.destination: Path = Path(destination)

    def verifier_source(self) -> None:
        """
        Vérifie que le dossier source existe.

        Raises:
            FileNotFoundError: si le dossier source est introuvable
        """
        if not self.source.exists() or not self.source.is_dir():
            raise FileNotFoundError("Le dossier source n'existe pas.")

    def nettoyer_destination(self) -> None:
        """
        Supprime le dossier de destination s'il existe déjà.
        """
        if self.destination.exists():
            shutil.rmtree(self.destination)

    def copier_dossier(self) -> None:
        """
        Copie récursivement le dossier source vers la destination.
        """
        shutil.copytree(self.source, self.destination)

    def compresser(self) -> None:
        """
        Compresse le dossier de destination en archive ZIP.
        """
        shutil.make_archive(self.destination.name, "zip", self.destination)

    def supprimer_copie(self) -> None:
        """
        Supprime le dossier de destination après compression.
        """
        if self.destination.exists():
            shutil.rmtree(self.destination)

    def sauvegarder(self) -> None:
        """
        Exécute toutes les étapes de sauvegarde :
        vérification, copie, compression et suppression.
        """
        self.verifier_source()
        self.nettoyer_destination()
        self.copier_dossier()
        self.compresser()
        self.supprimer_copie()

        print("Sauvegarde terminée.")


# Exemple d'utilisation
if __name__ == "__main__":
    gestionnaire = GestionnaireStockage("projets", "sauvegarde_projets")
    gestionnaire.sauvegarder()