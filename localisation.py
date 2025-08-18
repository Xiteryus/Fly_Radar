import requests

def get_localisation():
    try:
        # On interroge une API de géolocalisation par IP
        response = requests.get("http://ip-api.com/json/")
        data = response.json()
        
        if data["status"] == "success":
            latitude = data["lat"]
            longitude = data["lon"]
            return latitude, longitude
        else:
            return None
    except Exception as e:
        print("Erreur :", e)
        return None

