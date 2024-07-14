# anonymize_data_spark.py

from pyspark.sql import SparkSession
from pyspark.sql.functions import sha2, concat_ws, col

def anonymize_csv_spark(input_file, output_file):
    spark = SparkSession.builder.appName('AnonymizeCSV').getOrCreate()
    df = spark.read.csv(input_file, header=True)

    df = df.withColumn('first_name', sha2(col('first_name'), 256))
    df = df.withColumn('last_name', sha2(col('last_name'), 256))
    df = df.withColumn('address', sha2(col('address'), 256))

    df.write.csv(output_file, header=True)
    spark.stop()

# Example usage
anonymize_csv_spark('sample.csv', 'anonymized_sample_spark')
