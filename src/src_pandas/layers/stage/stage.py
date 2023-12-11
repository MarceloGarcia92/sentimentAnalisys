import pandas as pd
from src_spark.parameters.data_param import *


def create_tbl():
    #Read file, with header and specific delimiter, from parameters PATH
    df = pd.read_csv(PATH, delimiter=',', header=True)
    #Write the table in postgresql, check connections params in spark, parameters
    df.to_parquet('data/stage/sentiment-analysis.parquet')