from src.spark.conn import spark_conn
from src.spark.parameters.connection_param import jdbc_url, connection_properties
from src.models.sentiment.parametros import *


def create_tbl():
    #Connection to the postgresql database
    spark = spark_conn('PostgreSQL')
    #Read file, with header and specific delimiter, from parameters PATH
    df = spark.read.options(delimiter=',', header=True).csv(PATH)
    #Write the table in postgresql, check connections params in spark, parameters
    df.write.jdbc(url=jdbc_url, table="tbl_sentiment_analysis", mode="overwrite", properties=connection_properties)