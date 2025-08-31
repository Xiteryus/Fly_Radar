import os
from dotenv import load_dotenv
from localisation import get_localisation
from FlightRadar24 import FlightRadar24API

load_dotenv()
lat = float(os.getenv("LATITUDE"))
long = float(os.getenv("LONGITUDE"))


fr_api = FlightRadar24API()
loc = get_localisation()
if loc:
    print(f"Latitude: {loc[0]}, Longitude: {loc[1]}")



def plane(latitude = lat , longitude = long , radius = 10000): 
    bounds = fr_api.get_bounds_by_point(latitude, longitude, radius)  # 10 km autour de CDG

    flights = fr_api.get_flights(bounds = bounds)
    
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

def detectplane(latitude = lat , longitude = long , radius = 10000):
    bounds = fr_api.get_bounds_by_point(latitude, longitude, radius)  # 10 km autour de CDG

    flights = fr_api.get_flights(bounds = bounds)
    p =[]
    for flight in flights:
        p.append({
            'aircraft_code': flight.aircraft_code,
        })
    
    return len(p)>0

def choseplane(latitude = lat , longitude = long, radius = 10000):
    bounds = fr_api.get_bounds_by_point(latitude, longitude, radius)  # 10 km autour de CDG

    flights = fr_api.get_flights(bounds = bounds)

    p=[]
    for flight in flights:
        p.append({
            'aircraft_code': flight.aircraft_code,
            'registration': flight.registration,
            'altitude': flight.altitude,
            'callsign': flight.callsign,
            'origin': flight.origin_airport_iata,
            'destination': flight.destination_airport_iata,
        })
    max = 0
    id = None
    for flight in p:
        if flight['altitude'] > max:
            max = flight['altitude']
            id = flight['aircraft_code']

    return id

def flightinfo(id, latitude = lat , longitude = long, radius = 10000):
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


if __name__=="__main__":
    print(detectplane())
    print(choseplane())
    
    p = flightinfo(choseplane())
    if p:
        print(f"{p['aircraft_code']} | {p['registration']} | {p['altitude']} | "
            f"{p['callsign']} | {p['origin']} -> {p['destination']}")