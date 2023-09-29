from numpy import asarray

from src.spark.conn import spark_conn
from src.spark.parameters.connection_param import jdbc_url, connection_properties


def load_from_spark(table: str):
    spark = spark_conn('PostgreSQL')
    df = spark.read.jdbc(url=jdbc_url, table=table, properties=connection_properties)

    x = asarray(df.select('sent_text_review').toPandas()['sent_text_review'])
    y = asarray(df.select('sent_bool_sentiment').toPandas()['sent_bool_sentiment'])
    
    max_words = max([len(t.split()) for t in x])
    type_words = len({w for word_list in [word.split(' ') for word in x] for w in word_list})

    return x, y, max_words, type_words