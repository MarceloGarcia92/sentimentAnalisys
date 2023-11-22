from airflow import DAG
from airflow.contrib.operators.spark_submit_operator import SparkSubmitOperator
#from airflow.operators.postgres_operator import PostgresOperator
from datetime import datetime, timedelta

from src.spark.layers.stage.stage import create_tbl
from src.spark.layers.universal.universal import create_sat


default_args = {
    'owner':'Marcelo Garcia',
    'start_date':datetime(2023, 1, 1),
    'depends_on_past':False,
    'retries':1,
    'email': ['marcelo.garcia.c92@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': False,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG('data_ingestion', default_args=default_args, schedule_interval=timedelta(1))


extract_task = SparkSubmitOperator(
    task_id='stage_create_tbl',
    application='/path/to/your/spark-job.py',
    total_executor_cores='1',
    executor_cores='1',
    executor_memory='2g',
    driver_memory='1g',
    name='spark_submit_job',
    verbose=False,
    dag=dag)


split_task = SparkSubmitOperator(
    task_id='universal_create_sat',
    application='/path/to/your/spark-job.py',
    total_executor_cores='1',
    executor_cores='1',
    executor_memory='2g',
    driver_memory='1g',
    name='spark_submit_job',
    verbose=False,
    dag=dag)

extract_task >> split_task