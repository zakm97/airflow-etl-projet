from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def dire_bonjour():
    print("Bonjour 👋")

def dire_mon_nom():
    print("Je m'appelle Zakaria 😎")

def dire_aurevoir():
    print("Au revoir 👋")

with DAG(
    dag_id="mon_deuxieme_dag",
    start_date=datetime(2023, 1, 1),
 #  schedule="@daily",
    schedule=None,
    catchup=False,
    tags=["exemple"],
) as dag:

    task1 = PythonOperator(
        task_id="dire_bonjour",
        python_callable=dire_bonjour
    )

    task2 = PythonOperator(
        task_id="dire_mon_nom",
        python_callable=dire_mon_nom
    )

    task3 = PythonOperator(
        task_id="dire_aurevoir",
        python_callable=dire_aurevoir
    )

    # Définir l'ordre d'exécution
    task1 >> task2 >> task3
