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
        font.LoadFont("../fonts/6x13.bdf")  
        textColor = graphics.Color(255, 255, 0)  
        #date
        fontdate = graphics.Font()
        fontdate.LoadFont("../fonts/5x7.bdf")  
        #weather police 
        fontweather = graphics.Font()
        fontweather.LoadFont("../fonts/6x9.bdf")  
        #meteo
        fontmeteo = graphics.Font()
        fontmeteo.LoadFont("../fonts/5x8.bdf") 

        #weather
        latitude, longitude = 49.0097, 2.5479  
        meteo = self.weather(latitude,longitude)
        # heure x=8 y=10
        pos_h_x = 8 
        pos_h_y = 19
        # date x=8 y=19
        pos_d_x = 1 
        pos_d_y = 6
        # uni
        pos_x = 2 
        pos_y = 30
        """
        # temp 
        pos_temp_x = 2
        pos_temp_y =30
        # humidity
        pos_hum_x = 2
        pos_hum_y = 30
        #vent 
        pos_v_x = 2
        pos_v_y = 30
        #meteo 
        pos_m_x = 2 
        pos_m_y = 30 """

        
        try:
            start_time = time.time()
            afficher_1 = True
            afficher_2 = False
            afficher_3 = False

            while True:
                # Date et heure actuelles
                maintenant = datetime.now()
                heure = maintenant.strftime("%H:%M:%S")
                date = maintenant.strftime("%d/%m/%Y")
                offscreen_canvas.Clear()

                # Dessine le texte
                graphics.DrawText(offscreen_canvas, font, pos_h_x, pos_h_y, textColor, heure)
                graphics.DrawText(offscreen_canvas, fontdate, pos_d_x, pos_d_y, textColor, date)

                if afficher_1 : 
                    graphics.DrawText(offscreen_canvas, fontweather, pos_x, pos_y, textColor, f"{int(meteo['temp'])}°C")
                elif afficher_2:
                    graphics.DrawText(offscreen_canvas, fontweather, pos_x, pos_y, textColor, f"{meteo['humidite']}%")
                elif afficher_3 : 
                    graphics.DrawText(offscreen_canvas, fontweather, pos_x, pos_y, textColor, f"{int(meteo['vent'])}m/s")
                else:
                    graphics.DrawText(offscreen_canvas, fontmeteo, pos_x, pos_y, textColor, f"{meteo['meteo']}")

                offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)

                if time.time() - start_time >= 0:
                    afficher_1 = True
                if time.time() - start_time >= 5:
                    afficher_1 = False
                    afficher_2 = True
                    afficher_3 = False
                if time.time() - start_time >= 10:
                    afficher_2 = False
                    afficher_3 = True
                if time.time() - start_time >= 15:
                    afficher_3 = False
                if time.time() - start_time >=20:
                    start_time = time.time()

                time.sleep(1)
        except KeyboardInterrupt:
            print("Arrêt de l’horloge.")


# Point d’entrée
if __name__ == "__main__":
    clock = Clock()
    if not clock.process():
        clock.print_help()
