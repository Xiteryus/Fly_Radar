import requests

API_KEY = "ffc439b2ebf216a792c0bb2c619b7574"  
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
                "vent": data["wind"]["speed"]
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
        print(f"Météo à {meteo['ville']} : {meteo['meteo']} 🌦️")
        print(f"Température : {meteo['temp']}°C")
        print(f"Humidité : {meteo['humidite']}%")
        print(f"Vent : {meteo['vent']} m/s")
