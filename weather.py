import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_WEATHER_KEY")

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(lat, lon):
    try:
        params = {
            "lat": lat,
            "lon": lon,
            "appid": API_KEY,
            "units": "metric",  # °C au lieu de Kelvin
            "lang": "fr"        # météo en français
        }
        response = requests.get(BASE_URL, params=params)
        data = response.json()
        
        if response.status_code == 200:
            weather = {
                "ville": data["name"],
                "temp": data["main"]["temp"],
                "meteo": data["weather"][0]["description"],
                "humidite": data["main"]["humidity"],
                "vent": round(data["wind"]["speed"] * 3.6, 1)
            }
            return weather
        else:
            print("Erreur API météo :", data)
            return None
    except Exception as e:
        print("Erreur :", e)
        return None


if __name__ == "__main__":
    # Exemple : Paris CDG
    latitude, longitude = 49.0097, 2.5479  
    meteo = get_weather(latitude, longitude)

    if meteo:
        print(f"Météo à {meteo['ville']} : {meteo['meteo']} ")
        print(f"Température : {meteo['temp']}°C")
        print(f"Humidité : {meteo['humidite']}%")
        print(f"Vent : {meteo['vent']} m/s")
