from flask import Flask, render_template, redirect, url_for
from flight_radar import plane  # importe ta fonction
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
    return render_template("index.html", flights=data, heure=heure, date=date, weather=weather)

if __name__ == "__main__":
    app.run(debug=True)
