from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

from scripts.extraction import extraire_utilisateurs
from scripts.transformation import transformer_utilisateurs
from scripts.chargement import charger_utilisateurs

with DAG(
    dag_id="etl_utilisateurs",
    start_date=datetime(2023, 1, 1),
    schedule=None,
    catchup=False,
    tags=["api", "etl"]
) as dag:

    t1 = PythonOperator(
        task_id="extraction",
        python_callable=extraire_utilisateurs
    )

    t2 = PythonOperator(
        task_id="transformation",
        python_callable=transformer_utilisateurs
    )

    t3 = PythonOperator(
        task_id="chargement",
        python_callable=charger_utilisateurs
    )

    t1 >> t2 >> t3
