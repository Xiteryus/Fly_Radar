from localisation import get_localisation
from FlightRadar24 import FlightRadar24API


fr_api = FlightRadar24API()
loc = get_localisation()
if loc:
    print(f"Latitude: {loc[0]}, Longitude: {loc[1]}")


# coordinate 
# home : 48.7803222, 2.3092621
# CDG : 49.0097, 2.5479


def plane(latitude =48.7803222 , longitude = 2.3092621, radius = 5000): 
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



if __name__=="__main__":
    p = plane()

    for flight in p:
        print(f"{flight['aircraft_code']} | {flight['registration']} | {flight['altitude']} | "f"{flight['callsign']} | {flight['origin']} → {flight['destination']}")
