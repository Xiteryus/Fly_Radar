#!/usr/bin/env python3
import time
from datetime import datetime
#--
import requests
import os
from dotenv import load_dotenv
#--
from samplebase import SampleBase
from rgbmatrix import graphics

load_dotenv()
API_KEY = os.getenv("API_WEATHER_KEY")

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

class Clock(SampleBase):
    def __init__(self, *args, **kwargs):
        super(Clock, self).__init__(*args, **kwargs)

    def weather(self,lat,lon):
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


    def run(self):
        offscreen_canvas = self.matrix.CreateFrameCanvas()
        #heure
        font = graphics.Font()
        font.LoadFont("../fonts/7x13.bdf")  # police fournie avec la lib
        #date
        fontdate = graphics.Font()
        fontdate.LoadFont("../fonts/5x7.bdf")  # police fournie avec la lib
        textColor = graphics.Color(255, 255, 255)  
        #weather
        latitude, longitude = 49.0097, 2.5479  
        meteo = self.weather(latitude,longitude)
        # heure
        pos_h_x = 4 
        pos_h_y = 15
        # date 
        pos_d_x = 8 
        pos_d_y = 23
        # temp 
        pos_temp_x = 2
        pos_temp_y =30

        try:
            while True:
                # Date et heure actuelles
                maintenant = datetime.now()
                heure = maintenant.strftime("%H:%M:%S")
                date = maintenant.strftime("%d/%m/%Y")
                offscreen_canvas.Clear()

                # Dessine le texte
                graphics.DrawText(offscreen_canvas, font, pos_h_x, pos_h_y, textColor, heure)
                graphics.DrawText(offscreen_canvas, fontdate, pos_d_x, pos_d_y, textColor, date)
                graphics.DrawText(offscreen_canvas, fontdate, pos_temp_x, pos_temp_y, textColor, f"{meteo['temp']}°C")


                # Bascule l’image
                offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)

                time.sleep(1)
        except KeyboardInterrupt:
            print("Arrêt de l’horloge.")


# Point d’entrée
if __name__ == "__main__":
    clock = Clock()
    if not clock.process():
        clock.print_help()
