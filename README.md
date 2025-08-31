# Fly_Radar

**Fly_Radar** est un tableau d’informations en temps réel qui combine :

* L’affichage de l’heure
* La météo locale (température, humidité, vent)
* Le suivi des avions passant au-dessus de votre tête avec leurs informations (vol, altitude, vitesse…)

---

## Fonctionnalités

1. **Horloge en temps réel**

   * Affichage de l’heure centrale
   * La date affichée en haut à gauche
   * Mise à jour automatique toutes les secondes

2. **Météo locale**

   * Température en °C
   * Description météo en français
   * Humidité et vent (en km/h)

3. **Suivi des avions**

   * Informations sur les vols passant au-dessus de votre position
   * Affichage du vol, altitude, vitesse et autres détails

4. **Interface graphique WEB**

   * Affichage clair et centré
   * Mise à jour automatique via JavaScript

5. **Interface physique**

    * Affichage sur un ecran LED 
    * Carte raspberry pi

---

## Technologies utilisées

* **Backend** : Python, Flask
* **Frontend** : HTML, CSS, JavaScript
* **API météo** : OpenWeatherMap
* **API vols** : FlightRadar 

---


## Installation

1. Cloner le projet :

```bash
git clone https://github.com/Xiteryus/Fly_Radar.git
cd Fly_Radar
```

2. Installer les dépendances :

```bash
pip install flask, python-dotenv
```

3. Configurer la base de données et variables d'environnement

Dans la racine du projet, créez un fichier .env comme suit :

```
LATITUDE=votrelatitude
LONGITUDE=votrelongitude
```

Vous pouvez récupérer vos coordonnées GPS sur ce site : https://www.coordonnees-gps.fr/


3. Configurer votre clé API OpenWeatherMap dans `weather_module.py` :

```python
API_KEY = "VOTRE_CLE_API"
```

4. Lancer l’application Flask :

```bash
python app.py
```

5. Ouvrir votre navigateur à l’adresse :

```
http://127.0.0.1:5000/
```


