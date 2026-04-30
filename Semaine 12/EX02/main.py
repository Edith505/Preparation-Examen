import requests
import time
from datetime import datetime
 
LATITUDE = 48.8566
LONGITUDE = 2.3522
URL = "https://api.open-meteo.com/v1/forecast"
 
PARAMS = {
    "latitude": LATITUDE,
    "longitude": LONGITUDE,
    "current": ["temperature_2m", "relative_humidity_2m", "wind_speed_10m"],
    "timezone": "auto"
}
 
def fetch_weather():
    try:
        response = requests.get(URL, params=PARAMS)
        response.raise_for_status()
        data = response.json()
       
        current = data["current"]
        temp = current["temperature_2m"]
        humidity = current["relative_humidity_2m"]
        wind = current["wind_speed_10m"]
        timestamp = datetime.now().strftime("%H:%M:%S")
 
        print(f"[{timestamp}] Temp: {temp}°C | Humidité: {humidity}% | Vent: {wind} km/h", flush=True)
       
    except requests.exceptions.RequestException as e:
        print(f"Erreur de connexion : {e}")
    except KeyError:
        print("Erreur : Format de données API inattendu.")
 
if __name__ == "__main__":
    print(f"Démarrage du suivi météo (toutes les 10s) pour Lat:{LATITUDE}, Lon:{LONGITUDE}")
 
    while True:
        fetch_weather()
        time.sleep(10)