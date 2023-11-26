from datetime import datetime
from airflow import DAG
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 1, 1),
}

dag = DAG(
    'spark_submit_job',
    default_args=default_args,
    schedule_interval='@daily',  # Or your preferred interval
)

spark_task = SparkSubmitOperator(
    task_id='submit_job',
    application='/path/to/your-spark-job.py',  # Path to your Spark application
    conn_id='your_spark_connection',  # Define your Spark connection in Airflow
    dag=dag,
)