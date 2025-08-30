from flask import Flask, render_template, redirect, url_for
from flight_radar import *  # importe ta fonction
from datetime import datetime
from weather import get_weather

latitude, longitude = 48.7803222, 2.3092621  


app = Flask(__name__)

@app.route('/')
def home():
    data = plane()
    heure = datetime.now().strftime("%H:%M:%S")
    date = datetime.now().strftime("%d/%m/%Y")
    weather = get_weather(latitude,longitude)
    plane_detected  = detectplane()
    best_plane  = choseplane()
    info = flightinfo(best_plane)
    return render_template("index.html", flights=data, heure=heure, date=date, weather=weather, detectplane=plane_detected, choseplane=best_plane, flightinfo = info)

if __name__ == "__main__":
    app.run(debug=True)
