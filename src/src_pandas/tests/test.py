# test_app.py

import unittest
from pyspark.sql import SparkSession
from app import add_new_column

class PySparkTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.spark = SparkSession.builder \
            .appName("PySparkTest") \
            .master("local[2]") \
            .getOrCreate()

    @classmethod
    def tearDownClass(cls):
        cls.spark.stop()

    def test_add_new_column(self):
        # Create a DataFrame
        df = self.spark.createDataFrame([(1, "foo"), (2, "bar")], ["id", "value"])

        # Apply the transformation
        new_df = add_new_column(df)

        # Check the results
        expected_columns = ['id', 'value', 'new_column']
        self.assertListEqual(new_df.columns, expected_columns)
        self.assertEqual(new_df.where(col("new_column") != 1).count(), 0)

if __name__ == '__main__':
    unittest.main()
