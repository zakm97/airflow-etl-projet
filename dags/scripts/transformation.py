import pandas as pd

def transformer_utilisateurs():
    print("🔧 Transformation des utilisateurs")
    df = pd.read_csv("/tmp/utilisateurs.csv")

    # On garde juste name, email, address.city
    df_transforme = df[["name", "email", "address.city"]]
    df_transforme.rename(columns={"address.city": "ville"}, inplace=True)

