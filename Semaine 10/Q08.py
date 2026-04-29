from datetime import datetime

def demander_date():
    while True:
        try:
            saisie = input("Entrez une date future (AAAA-MM-JJ HH:MM) : ")
            date_future = datetime.strptime(saisie, "%Y-%m-%d %H:%M")
            return date_future
        except ValueError:
            print("Format invalide. Réessayez.")

def calculer_temps_restant(date_future):
    maintenant = datetime.now()
    difference = date_future - maintenant

    if difference.total_seconds() <= 0:
        print("Le moment est déjà passé.")
        return

    total_secondes = int(difference.total_seconds())

    jours = total_secondes // 86400
    reste = total_secondes % 86400

    heures = reste // 3600
    reste = reste % 3600

    minutes = reste // 60
    secondes = reste % 60

    print(f"Temps restant : {jours} jours, {heures} heures, {minutes} minutes, {secondes} secondes")

def main():
    date_future = demander_date()
    calculer_temps_restant(date_future)

if __name__ == "__main__":
    main()