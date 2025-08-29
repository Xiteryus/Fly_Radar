import time
from datetime import datetime

def afficher_date():
    try:
        while True:
            # Récupère la date et l'heure actuelles
            maintenant = datetime.now()
            # Format : Jour/Mois/Année Heure:Minute:Seconde
            date_str = maintenant.strftime("%d/%m/%Y %H:%M:%S")
            print(date_str, end="\r")  # \r permet d'écraser la ligne
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nArrêt du programme.")

# Appel de la fonction
afficher_date()