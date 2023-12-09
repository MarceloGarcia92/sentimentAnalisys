from airflow import DAG
from airflow.contrib.operators.spark_submit_operator import SparkSubmitOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2021, 1, 1),
    'email': ['your-email@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG('spark_submit_job', default_args=default_args, schedule_interval=timedelta(1))

t1 = SparkSubmitOperator(
    task_id='spark_submit_job',
    conn_id='spark_default',
    application='/src/spark_job.py',
    total_executor_cores='1',
    executor_cores='1',
    executor_memory='2g',
    num_executors='1',
    name='spark-job',
    verbose=False,
    driver_memory='1g',
    conf={'master':'spark://spark-master:7077'},
    dag=dag)