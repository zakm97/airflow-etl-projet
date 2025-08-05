import requests
import pandas as pd

def extraire_utilisateurs():
    print("📡 Extraction des utilisateurs depuis l'API")
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    data = response.json()

    df = pd.json_normalize(data)
    print("la taille des Données extraites est bien : ",  len(df))