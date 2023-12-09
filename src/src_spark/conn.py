from pyspark.sql import SparkSession

def spark_conn(name:str):
    spark = SparkSession.builder \
    .appName(name) \
    .config('spark.jars', '/opt/spark/src/src/spark/app/postgresql-42.2.27.jre7.jar') \
    .getOrCreate()
    return spark




