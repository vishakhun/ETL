from pyspark.sql import SparkSession
from google.cloud import bigquery
import pyspark.sql.functions as F

def read_from_gcs(bucket_name: str, file_name: str) -> str:
    """Generate a GCS path for Spark to read."""
    return f"gs://{bucket_name}/{file_name}"

def save_to_bigquery(df, table_id: str) -> None:
    """Save a DataFrame to a BigQuery table."""
    client = bigquery.Client()
    pandas_df = df.toPandas()  # Convert to Pandas DataFrame for BigQuery upload
    client.load_table_from_dataframe(pandas_df, table_id).result()

if __name__ == "__main__":
    BUCKET_NAME = "your-bucket-name"  # GCS bucket name
    FILE_NAME = "mars_weather.json"  # File path in GCS
    TABLE_ID = "your-project.your_dataset.your_table_name"  # BigQuery table ID

    spark = SparkSession.builder.appName("MarsWeatherETL").getOrCreate()
    
    # Read data from GCS
    gcs_path = read_from_gcs(BUCKET_NAME, FILE_NAME)
    df = spark.read.json(gcs_path)
    
    # Process data (example: calculate average temperature)
    # Replace 'AT' with the actual key from the JSON structure
    df_transformed = df.withColumn("avg_temp", F.avg("AT.av"))

    # Save to BigQuery
    save_to_bigquery(df_transformed, TABLE_ID)
