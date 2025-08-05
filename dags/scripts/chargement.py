import pandas as pd

def charger_utilisateurs():
    print("💾 Chargement des utilisateurs")
    df = pd.read_csv("/tmp/utilisateurs_transformes.csv")
    print(df)
