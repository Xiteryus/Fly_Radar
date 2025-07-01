use fly_radar;

-- Table des avions
CREATE TABLE Plane(
   registration VARCHAR(50) PRIMARY KEY,
   aircraft_code VARCHAR(50),
   age VARCHAR(50),
   airline VARCHAR(50)
);

-- Table des vols
CREATE TABLE Flight(
   id VARCHAR(50) PRIMARY KEY,
   callsign VARCHAR(50),
   origin_airport_iata VARCHAR(50),
   destination_airport_iata VARCHAR(50),
   status VARCHAR(50),
   plane_registration VARCHAR(50),
   FOREIGN KEY (plane_registration) REFERENCES Plane(registration)
);

-- Table des positions surveillées
CREATE TABLE Position_(
   Id_position VARCHAR(50) PRIMARY KEY,
   Name_position VARCHAR(50),
   Longitude VARCHAR(50),
   Latitude VARCHAR(50),
   Radius VARCHAR(50)
);

-- Table des survols de positions par des vols
CREATE TABLE Flights_over_position(
   id_overflight VARCHAR(50) PRIMARY KEY,
   flight_id VARCHAR(50),
   position_id VARCHAR(50),
   time_ DATETIME,
   altitude INT,
   speed INT,
   FOREIGN KEY (flight_id) REFERENCES Flight(id),
   FOREIGN KEY (position_id) REFERENCES Position_(Id_position)
);

select * from Position_
