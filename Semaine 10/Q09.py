import shutil
from pathlib import Path


def sauvegarder_projets():
    source = Path("projets")
    copie = Path("sauvegarde_projets")
    archive = "sauvegarde_projets"

    # Vérifier que le dossier source existe
    if not source.exists() or not source.is_dir():
        raise FileNotFoundError("Le dossier 'projets' n'existe pas.")

    # Supprimer la copie si elle existe déjà
    if copie.exists():
        shutil.rmtree(copie)

    # Copier récursivement
    shutil.copytree(source, copie)

    # Compresser en ZIP
    shutil.make_archive(archive, "zip", copie)

    # Supprimer le dossier copié
    shutil.rmtree(copie)

    print("Sauvegarde terminée : sauvegarde_projets.zip créé.")


if __name__ == "__main__":
    sauvegarder_projets()