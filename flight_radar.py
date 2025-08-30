from localisation import get_localisation
from FlightRadar24 import FlightRadar24API


fr_api = FlightRadar24API()
loc = get_localisation()
if loc:
    print(f"Latitude: {loc[0]}, Longitude: {loc[1]}")


# coordinate 
# home : 48.7803222, 2.3092621
# CDG : 49.0097, 2.5479


def plane(latitude =49.0097 , longitude = 2.5479, radius = 10000): 
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

def detectplane(latitude =49.0097 , longitude = 2.5479, radius = 10000):
    bounds = fr_api.get_bounds_by_point(latitude, longitude, radius)  # 10 km autour de CDG

    flights = fr_api.get_flights(bounds = bounds)
    p =[]
    for flight in flights:
        p.append({
            'aircraft_code': flight.aircraft_code,
        })
    
    return len(p)>0

def choseplane(latitude =49.0097 , longitude = 2.5479, radius = 10000):
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

def flightinfo(id, latitude =49.0097 , longitude = 2.5479, radius = 10000):
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