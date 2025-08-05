from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd

# Fonction 1 : Lire et afficher le fichier
def lire_et_afficher_csv():
    df = pd.read_csv("/opt/airflow/dags/data_test.csv")
    print("📄 Contenu du fichier CSV :")
    print(df)

# Fonction 2 : Compter les lignes
def compter_lignes():
    df = pd.read_csv("/opt/airflow/dags/data_test.csv")
    nb_lignes = len(df)
    print(f"✅ Le fichier contient {nb_lignes} lignes.")

# DAG
with DAG(
    dag_id="dag_lire_csv",
    start_date=datetime(2023, 1, 1),
   # schedule="@daily",
    schedule= None,
    catchup=False,
    tags=["csv", "exemple"],
) as dag:

    lire_csv = PythonOperator(
        task_id="lire_et_afficher_csv",
        python_callable=lire_et_afficher_csv
    )

    compter = PythonOperator(
        task_id="compter_lignes_csv",
        python_callable=compter_lignes
    )

    lire_csv >> compter
