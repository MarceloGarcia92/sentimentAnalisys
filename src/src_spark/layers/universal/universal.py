from pyspark.sql.functions import regexp_replace, col, when, current_date
from pyspark.sql.types import FloatType, StringType, BooleanType, DateType

from src.spark.conn import spark_conn
from src.spark.parameters.connection_param import jdbc_url, connection_properties
from src.models.sentiment.parametros import *


def create_sat():
    spark = spark_conn('PostgreSQL')

    df = spark.read.jdbc(url=jdbc_url, table="tbl_sentiment_analysis", properties=connection_properties)
    #Transformation
    df = df.withColumn('sent_bool_sentiment', when(col(" Sentiment") == " Positive", True).otherwise(False))
    df = df.withColumn('sent_text_review', regexp_replace(col("Text"), '"', ''))
    df = df.withColumn('sent_num_score', regexp_replace(col(" Confidence Score"), '"', ''))
    df = df.withColumn('periodo_mes', current_date())
    #Columns type definition
    df = df.withColumn('sent_bool_sentiment', col('sent_bool_sentiment').cast(BooleanType()))
    df = df.withColumn('sent_text_review', col('sent_text_review').cast(StringType())) 
    df = df.withColumn('sent_num_score', col('sent_num_score').cast(FloatType()))
    df = df.withColumn('sent_date_review', col(' Date/Time').cast(DateType())) 
    #Select columns
    df = df.select('sent_text_review', 'sent_num_score', 'sent_bool_sentiment')
    #Save table
    df.write.jdbc(url=jdbc_url, table="sat_sentiment_analysis", mode="overwrite", properties=connection_properties)