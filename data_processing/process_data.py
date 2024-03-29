from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg

def process_weather_data(input_path: str, output_path: str) -> None:
    """
    Processes Mars weather data using Apache Spark to calculate average temperatures.

    Parameters:
    input_path (str): Path to the input JSON file containing Mars weather data.
    output_path (str): Path to save the processed data.

    Returns:
    None
    """
    spark = SparkSession.builder.appName("MarsWeatherAnalysis").getOrCreate()
    df = spark.read.json(input_path)

    # Example transformation: calculate the average temperature
    # This is a placeholder; actual computation depends on the data structure
    df_transformed = df.withColumn("avg_temp", avg(col("AT.av")))
    
    df_transformed.write.format("parquet").save(output_path)
    spark.stop()
    print("Data processed and saved successfully.")

if __name__ == "__main__":
    process_weather_data('mars_weather.json', 'processed_mars_weather.parquet')
