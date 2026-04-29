import subprocess
import platform


def obtenir_ip_windows() -> tuple[str, str]:
    sortie = subprocess.check_output("ipconfig", encoding="utf-8", errors="ignore")

    ip = None
    masque = None

    lignes = sortie.splitlines()

    for i, ligne in enumerate(lignes):
        # Adapter selon la carte (Ethernet)
        if "Ethernet" in ligne:
            for j in range(i, i + 15):
                if j < len(lignes):
                    l = lignes[j].strip()

                    if "IPv4" in l:
                        ip = l.split(":")[-1].strip()

                    if "Masque" in l or "Subnet Mask" in l:
                        masque = l.split(":")[-1].strip()

                if ip and masque:
                    return ip, masque

    return ip, masque


def obtenir_ip_linux() -> tuple[str, str]:
    sortie = subprocess.check_output(["ifconfig"], encoding="utf-8", errors="ignore")

    ip = None
    masque = None

    lignes = sortie.splitlines()

    for ligne in lignes:
        ligne = ligne.strip()

        if "inet " in ligne and "127.0.0.1" not in ligne:
            parties = ligne.split()

            for i, p in enumerate(parties):
                if p == "inet":
                    ip = parties[i + 1]

                if p in ("netmask", "Mask:"):
                    masque = parties[i + 1]

            if ip and masque:
                return ip, masque

    return ip, masque


def main():
    systeme = platform.system()

    if systeme == "Windows":
        ip, masque = obtenir_ip_windows()

    elif systeme == "Linux":
        ip, masque = obtenir_ip_linux()

    else:
        raise OSError("Système non supporté")

    if ip and masque:
        print(f"IP : {ip} / {masque}")
    else:
        print("Impossible de récupérer l'adresse IP.")


if __name__ == "__main__":
    main()