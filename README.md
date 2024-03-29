# Mars Weather Data Aggregation Pipeline

## Project Overview
This project demonstrates an ETL pipeline that utilizes NASA's InSight lander API to fetch Mars weather data, processes the data using Apache Spark, saves it to Google Cloud Storage (GCS), processes the stored data, and then stores the results in BigQuery. Apache Airflow orchestrates the pipeline, scheduling and automating the data fetching and processing tasks.

## Objectives
- Fetch Mars weather data from NASA's InSight API.
- Store the fetched data in Google Cloud Storage (GCS).
- Process and aggregate the data using Apache Spark.
- Store the processed data in BigQuery for further analysis.
- Automate and schedule the ETL process using Apache Airflow.

## Technology Stack
- **Python**: The core programming language used for scripting.
- **Requests**: A Python library used for HTTP requests to fetch data from the NASA API.
- **Apache Spark**: For data processing and aggregation.
- **Google Cloud Storage (GCS)**: To store the raw and processed data.
- **BigQuery**: For storing and querying the processed data.
- **Apache Airflow**: For orchestrating and scheduling the ETL pipeline.

## Project Structure
- `data_fetching/fetch_data.py`: Script to fetch data from the NASA API and save it to GCS.
- `data_processing/process_data.py`: Script to process data from GCS using Apache Spark and save it to BigQuery.
- `airflow_dags/mars_weather_dag.py`: Airflow DAG script for scheduling and automating the ETL tasks.
- `requirements.txt`: Lists all the Python dependencies.

## Setup Instructions
Ensure you have Python, Apache Spark, Apache Airflow, and the necessary GCP credentials configured before proceeding.

## Disclaimer

- **API Key**: The NASA API key in `fetch_data.py` is a placeholder. Replace `"YOUR_API_KEY"` with your actual API key.
- **GCP Credentials**: Ensure that you configure your Google Cloud credentials correctly. The scripts assume that your environment is authenticated with GCP.
- **Bucket Name**: Replace `"your-bucket-name"` in the scripts with the name of your actual GCS bucket.
- **BigQuery Table ID**: Replace `"your-project.your_dataset.your_table_name"` in `process_data.py` with your actual BigQuery table ID.
- **File Paths**: Adjust file paths in the Airflow DAG script as necessary to match your environment.
