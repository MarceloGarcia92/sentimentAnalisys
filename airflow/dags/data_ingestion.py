from airflow import DAG
from airflow.operators.python import PythonOperator
#from airflow.operators.postgres_operator import PostgresOperator
from datetime import datetime

from src.spark.layers.stage.stage import create_tbl
from src.spark.layers.universal.universal import create_sat


default_args = {
    'owner':'Marcelo Garcia',
    'start_date':datetime(2023, 1, 1),
    'depends_on_past':False,
    'retries':1,
}

dag = DAG('data_ingestion', default_args=default_args, schedule_interval=None)


extract_task = PythonOperator(
    task_id='stage_create_tbl',
    python_callable=create_tbl,
    dag=dag,
)

split_task = PythonOperator(
    task_id='universal_create_sat',
    python_callable=create_sat,
    dag=dag,
)

extract_task >> split_task