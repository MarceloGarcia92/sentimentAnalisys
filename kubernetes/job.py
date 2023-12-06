from pyspark.sql import SparkSession

def main():
    spark = SparkSession.builder.appName("example-job").getOrCreate()
    print(spark)
    # Your Spark job logic here

if __name__ == "__main__":
    main()