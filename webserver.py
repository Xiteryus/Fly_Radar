import os
from dotenv import load_dotenv
from flask import Flask, render_template, redirect, url_for
from flight_radar import *  
from datetime import datetime
from weather import get_weather
from localisation import get_localisation

#----------------------------------------------------------------------
# .env
load_dotenv()
lat = float(os.getenv("LATITUDE"))
long = float(os.getenv("LONGITUDE"))
#get localisation avec l'IP 
loc = get_localisation()
if loc:
    print(f"Latitude: {loc[0]}, Longitude: {loc[1]}")
lat1= loc[0]
long1= loc[1]

#----------------------------------------------------------------------

app = Flask(__name__)

@app.route('/')
def home():
    data = plane()
    heure = datetime.now().strftime("%H:%M:%S")
    date = datetime.now().strftime("%d/%m/%Y")
    # recup avec .env ou IP 
    weather = get_weather(lat1,long1)
    plane_detected  = detectplane() # Renvoie True ou Flase 
    best_plane  = choseplane() # Renvoie ID avion 
    info = flightinfo(best_plane) # Info sur l'avion 
    return render_template("index.html", flights=data, heure=heure, date=date, weather=weather, detectplane=plane_detected, choseplane=best_plane, flightinfo = info)

if __name__ == "__main__":
    app.run(debug=True)
