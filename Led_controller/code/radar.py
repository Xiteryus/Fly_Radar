#!/usr/bin/env python3
import os
import time
from dotenv import load_dotenv
from samplebase import SampleBase
from rgbmatrix import graphics
from FlightRadar24 import FlightRadar24API

# Charger config
load_dotenv()
lat1 = float(os.getenv("LATITUDE"))
long1 = float(os.getenv("LONGITUDE"))

# API
fr_api = FlightRadar24API()

class Radar(SampleBase):
    def __init__(self, *args, **kwargs):
        super(Radar, self).__init__(*args, **kwargs)

    def plane(self, latitude=lat1, longitude=long1, radius=5000):
        bounds = fr_api.get_bounds_by_point(latitude, longitude, radius)
        flights = fr_api.get_flights(bounds=bounds)

        p = []
        for flight in flights:
            p.append({
                'aircraft_code': flight.aircraft_code,
                'registration': flight.registration,
                'altitude': flight.altitude,
                'callsign': flight.callsign,
                'origin': flight.origin_airport_iata,
                'destination': flight.destination_airport_iata,
            })
        return p

    def detectplane(self, latitude=lat1, longitude=long1, radius=5000):
        bounds = fr_api.get_bounds_by_point(latitude, longitude, radius)
        flights = fr_api.get_flights(bounds=bounds)
        return len(flights) > 0

    def choseplane(self, latitude=lat1, longitude=long1, radius=5000):
        bounds = fr_api.get_bounds_by_point(latitude, longitude, radius)
        flights = fr_api.get_flights(bounds=bounds)

        chosen = None
        max_alt = 0
        for flight in flights:
            if flight.altitude and flight.altitude > max_alt:
                max_alt = flight.altitude
                chosen = flight
        return chosen

    def flightinfo(self, id, latitude=lat1, longitude=long1, radius=5000):
        bounds = fr_api.get_bounds_by_point(latitude, longitude, radius)
        flights = fr_api.get_flights(bounds=bounds)

        for flight in flights:
            if flight.aircraft_code == id:
                return {
                    'aircraft_code': flight.aircraft_code,
                    'registration': flight.registration,
                    'altitude': flight.altitude,
                    'callsign': flight.callsign,
                    'origin': flight.origin_airport_iata,
                    'destination': flight.destination_airport_iata,
                }

    def run(self):
        offscreen_canvas = self.matrix.CreateFrameCanvas()
        #chargement fonction

        choisen = self.choseplane()
        if not choisen:
            return "No plane detected"  
        p = self.flightinfo(choisen.aircraft_code)
        # police
        font = graphics.Font()
        font.LoadFont("../fonts/6x13.bdf")  
        textColor = graphics.Color(255, 255, 0)  
        #position
        pos_x = 38
        pos_y = 12
        #origin
        pos_o_x = 2
        pos_o_y = 12

        try:
            while True:

                #graphics.DrawText(offscreen_canvas, font, pos_x, pos_y, textColor, f"{p['aircraft_code']}")
                graphics.DrawText(offscreen_canvas, font, pos_o_x, pos_o_y, textColor, f"{p['origin']} ->")
                graphics.DrawText(offscreen_canvas, font, pos_x, pos_y, textColor, f" {p['destination']}")


                offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)

                time.sleep(1)
        except KeyboardInterrupt:
            print("Arrêt de l’horloge.")

if __name__ == "__main__":
    radar = Radar()

    if not radar.process():
        radar.print_help()

    """
    print("Avion détecté :", radar.detectplane())

    chosen = radar.choseplane()
    if chosen:
        print(f"Avion choisi : {chosen.aircraft_code}")
        p = radar.flightinfo(chosen.aircraft_code)
        if p:
            print(f"{p['aircraft_code']} | {p['registration']} | {p['altitude']} | "
                  f"{p['callsign']} | {p['origin']} -> {p['destination']}")"""
