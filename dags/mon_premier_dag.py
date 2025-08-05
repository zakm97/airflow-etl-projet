from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def dire_bonjour():
    print("Hello Zakaria, ton DAG fonctionne ! 🎉")

with DAG(
    dag_id="mon_premier_dag",
    start_date=datetime(2025, 8, 5),
    #schedule="@daily",  # <<== ici, on utilise "schedule" et non "schedule_interval"
    schedule=None,  
    catchup=False,
    tags=["demo"],
) as dag:

    tache_hello = PythonOperator(
        task_id="dire_bonjour",
        python_callable=dire_bonjour,
    )

    tache_hello




